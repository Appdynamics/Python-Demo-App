Python Demo App
===============

A trivial Flask web app that can be used to demo performance monitoring features. The app has routes that do things like:

1. Sleep in a way that draws a pretty response time graph.
2. Raise uncaught exceptions in application code.
3. Simulate slow database calls in MySQL and PostgreSQL.
4. Make external HTTP calls.
5. Return HTTP errors (5xx and 4xx).

## Installation

Create a virtualenv:

```
virtualenv env
env/bin/pip install -r requirements.txt
```

Install and configure MySQL and/or PostgreSQL. They both are configured in `demo/config.py` to be running on localhost with the default port, a user named `test`, with password `test`, and a database named `test`. There do not need to be any tables or anything in the `test` database.

The web server runs on port 9000.

To run the development server:

```
env/bin/python demo/app.py
```

To run in production:

```
env/bin/gunicorn -w 4 -b 0.0.0.0:9000 demo.app:app
```

## Running with the agent

Install the agent into your virtualenv with:

```
env/bin/pip install /path/to/agent/appdynamics_bindeps_linux_x64_cp27m-1.0.0-cp27-none-any.whl
env/bin/pip install /path/to/agent/appdynamics-1.0.0-py2-none-any.whl
```

Run the agent with the `pyagent` command and a configuration file (there's a sample configuration file included, `appdynamics.cfg`):

```
env/bin/pyagent run -c appdynamics.cfg - env/bin/gunicorn -w 4 -b 0.0.0.0:9000 demo.app:app
```

## Generating load

Install siege through your package manager (`yum install siege` on Red Hat, `apt-get install siege` on Debian, or `brew install siege` on Mac). Edit the siege.txt (or copy it and edit the copy) and edit the variables defined at the top to specify the exit calls you wish to make, then run:

```
siege -d 1 -f siege.txt
```

