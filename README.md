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
