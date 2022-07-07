# an api
With resources and a datastore build by `docker-compose` via `make`, this is a modest API to pull and update some arbitrary granular data provided originally in `JSON` files.

It's designed to use `PostgreSQL` as a backend and `Redis` for caching. This will build these resources, and their containers are accessible via `docker exec` cli, but for now `Django` isn't talking to them properly. Working on a deadline and wanting to show working views, that code reads directly from the JSON files, which is not remotely ideal.

To stand it up, make sure `pipenv` is installed locally. Create a dir called `api` and clone in this repo. Run `pipenv install` to create a virtual environment -- not a necessity with `docker` but a nice-to-have for some local dev and debugging. Installing the dependencies from the `Pipfile` will give you access to `make`, which is going to make(!) the job of setting this up a bit cleaner for us.

To get started, go into the virtual environment with `pipenv shell`.

Once there, confirm `make` by running `make help` to see a list of available commands.

And then:

```bash
# grab the relevant docker images and build containers, moving data and dependencies
$ make local-build
# and to get the app up and running once that finishes:
$ make local-run
```

At this point, in a browser, you should be able to go to `localhost:8000/api/factories` and get back a bunch of JSON that would be long to dump in here, or, say, to `localhost:8000/api/fatory/1` and get back something that looks like this:

```json
factory	
chart_data	
sprocket_production_actual	
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
sprocket_production_goal	
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
time	
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

