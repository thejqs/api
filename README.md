# a docker-compose'd api
With resources and a datastore build by `docker-compose` via `make`, this is a modest API to pull and update some arbitrary granular data provided originally in `JSON` files.

It's designed to use `PostgreSQL` as a backend and `Redis` for caching. This will build these resources, provide a method to load the data, and routes to pull it from its new home in the backend.

To stand it up, make sure `pipenv` is installed locally (`pip install pipenv`, perhaps, or on a Mac with `Homebrew`, `brew install pipenv`). Create a dir called `api`, `cd` into it and clone in this repo. Run `pipenv install` to create a virtual environment -- not a necessity with `Docker` but a nice-to-have for some local dev and debugging. Installing the dependencies from the `Pipfile` will give you access to `make`, which is going to make(!) the job of setting this up a bit cleaner for us.

To get started, go into the virtual environment with `pipenv shell`.

Once there, confirm `make` by running `make help` to see a list of available commands.

And then:

```bash
# grab the relevant docker images and build containers, moving data and dependencies
$ make local-build
# and to get the app up and running once that finishes:
$ make local-run
```

One nice touch: Even though our code is running in a container, using `py-autoreload` from `uwsgi` means changes we make locally will get autorefreshed into the container.

Before we test the endpoints, we'll need to load some data. There's a `make` target wrapped around a `Django` management command to do that for us. Run `make local-load-data`. If there are no errors in the modest output, we can keep going.

At this point, in a browser, you should be able to go to `localhost:8000/api/factories` and get back a bunch of `JSON` that would be long to dump in here, or, say, to `localhost:8000/api/factory/1` and get back something that looks like this:

```json
factory:	
    chart_data:
        sprocket_production_actual:
            0	32
            1	28
            2	31
            3	30
            4	30
            5	32
            6	29
            7	28
            8	30
            9	32
            10	32
            11	29
            12	31
            13	30
            14	31
            15	32
            16	29
            17	29
            18	33
            19	30
        sprocket_production_goal:
            0	31
            1	33
            2	29
            3	29
            4	32
            5	30
            6	30
            7	31
            8	29
            9	31
            10	31
            11	30
            12	28
            13	29
            14	32
            15	29
            16	30
            17	31
            18	28
            19	32
        time:
            0	1611204818
            1	1611204878
            2	1611204938
            3	1611204998
            4	1611205058
            5	1611205118
            6	1611205178
            7	1611205238
            8	1611205298
            9	1611205358
            10	1611205418
            11	1611205478
            12	1611205538
            13	1611205598
            14	1611205658
            15	1611205718
            16	1611205778
            17	1611205838
            18	1611205898
            19	1611205958
```

Prefer to see only that `chart_data` for a specific `factory`? Try `localhost:8000/api/factory/2/chart-data`.

There are also methods to update and create `Sprocket` instances. As defined in `config/urls.py`, a request to update a specific sprocket should look like this:
```
http://localhost:8000/api/sprocket/create/5/6/4/7/
```

Those parameters after `/create/` are, in order, a sprocket's `teeth`, `pitch_diameter`, `outside_diameter` and `pitch`.

To update an existing sprocket, we do something quite similar:
```
http://localhost:8000/api/sprocket/3/update/5/6/4/7/
```

The first numerical url parameter is the ID of the sprocket to update, and the rest is as above -- same order for the same parameters. Could we have added something more targeted to update only specific fields on the sprocket? Well sure. Who doesn't love iterating?

Now. Let's talk for a minute about workarounds. The first version of this used several, because, it turns out, `Django` was slightly misconfigured in a way that meant `docker-compose` was using the wrong top-level directory to try to network all the resources.

Not great.

But now that we've found that little hammer of a bug (and thoroughly mixed our metaphors) we no longer have to read data from a file and can use our actual database. We've squashed our biggest bug.

That doesn't mean all this code is amazing. For example, because this is a local-only example project at the moment, I haven't taken the extra step of moving, say, `Django`-y app secrets and such into private configs. The url routes to the API that should be `POST` requests don't register as `POST` requests and the views don't insist on it. Nothing requires authentication.

There is still work to be done here.

In an actual API, we'd have tokens and auth and rate-limits and more robust ways of controlling access. We'd log user agents and have methods for turning off previously-granted access and for blowing away entire accounts. We'd spend more time making sure the way we're shaping our data will scale -- as it gets bigger, as more people attempt to use it, all that fun stuff. 

Speaking of scaling. A few ways we can think about that.

There isn't much in our data to tell us how frequently to expect writes. But that seems like it will happen less frequently than reads. What I'd aimed for was, as a first line of defense, to have each successful write trigger and update of that data in the cache. And depending on how granularly someone wanted that data via the api, to keep several cache keys so it's already pre-assembled for every endpoint we provide. Validate the request, ensure the person requesting it has the right permissions (right organization? right seniority? other things?), and here's your stuff.

Turns out writes are overwhelming us as sprocket production skyrockets? We can add follower dbs and read only from those, while writing to the leader.

The path forward from here seems clear. Round out another few views (delete methods, perhaps?), maybe hash or encode the data in transit for security, better obscure the parameters and shape of the data, flesh out caching, and ensure some sort of uniqueness for the data so we can't simply keep loading the same objects over and over again. 
