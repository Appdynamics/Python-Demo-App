python-web-demo-flask
=====================

A trivial Flask web app that can be used to demo performance monitoring features. The app has routes that do things like:

1. Sleep in a way that draws a pretty response time graph.
2. Raise uncaught exceptions in application code.
3. TODO: Simulate slow database calls in MySQL and PostgreSQL.
4. TODO: Make external HTTP calls.
5. TODO: Return HTTP errors (5xx and 4xx).

To install:

```
virtualenv env
env/bin/pip install -r requirements.txt
```

To run the development server:

```
env/bin/python demo/app.py
```

