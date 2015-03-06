Python Demo App
===============

A trivial Flask web app that can be used to demo performance monitoring features. The app has routes that do things like:

1. Sleep in a way that draws a pretty response time graph.
2. Raise uncaught exceptions in application code.
3. Simulate slow database calls in MySQL and PostgreSQL.
4. Make external HTTP calls.
5. Return HTTP errors (5xx and 4xx).

NOTE: To use the AppDynamics Python Agent, you must have a compatible (4.0+) AppDynamics controller in SAAS or On Premise and a license provisioned for Python agents.

## Installation

Python 2.6 or 2.7 are required. MacOS X and recent Linux distributions should have these preinstalled. Older Linux distributions (like CentOS 5) may come with a version of Python is too old, but you should be able to easily find packages for Python 2.7.

You must have `pip` and `virtualenv` installed. These may already be installed for you. If not, install `pip` with:

```
sudo easy_install pip
```

And then use `pip` to install `virtualenv`:

```
sudo pip install virtualenv
```

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

If your version of pip is older than 1.5, upgrade pip with:

```
pip install -U pip
```

Then install the agent into your virtualenv:

```
env/bin/pip install --pre appdynamics
```

Run the agent with the `pyagent` command and a configuration file (there's a sample configuration file included in this repository, `appdynamics.cfg`):

```
env/bin/pyagent run -c appdynamics.cfg - env/bin/gunicorn -w 4 -b 0.0.0.0:9000 demo.app:app
```

## Generating load

Install siege through your package manager (`yum install siege` on Red Hat, `apt-get install siege` on Debian, or `brew install siege` on Mac). Edit the siege.txt (or copy it and edit the copy) and edit the variables defined at the top to specify the exit calls you wish to make, then run:

```
siege -d 1 -f siege.txt
```

## HTTP Exit Call / Distributed Correlation Testing

The AppDynamics Python agent supports distributed correlation across tiers. The agent supports both being the originating tier and the continuing tier. To demonstrate this and test it out, you can use the `/http` endpoint to cause an HTTP exit call with a correlation header. This is useful for testing cross-tier correlation (as of 4.0.0, the Python agent does not support cross-app correlation). For example, if you have a .NET instrumented tier at 192.168.0.1, you can cause correlation by going to `http://127.0.0.1/http?url=http://192.168.0.1/`.
