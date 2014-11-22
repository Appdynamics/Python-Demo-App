import logging
import math
import random
import requests
import time

from flask import Flask, render_template, render_template_string, request

from demo import db

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


class MissingArgumentException(Exception):
    status_code = 400

    def __init__(self, message):
        super(MissingArgumentException, self).__init__()
        self.message = message


@app.errorhandler(MissingArgumentException)
def handle_missing_argument_exception(error):
    return render_template_string(
        "<!DOCTYPE html><title>Missing Required Argument</title><h1>Missing required argument: {{msg}}",
        msg=error.message)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/wave/<whatever>')
def response_time_wave(whatever):
    a = 0.2
    b = 3
    c = 1
    x = math.radians(time.time())

    try:
        c = int(whatever)
    except:
        pass

    delay = a * (math.sin(b * x + c) + 1.0)
    time.sleep(delay)
    return render_template_string("<!DOCTYPE html><title>Wave</title><h1>%s</h1>" % (delay,))


@app.route('/error/<when>')
def cause_error(when):
    if when == 'always' or random.randint(0, 9) == 0:
        raise random_exception()
    return render_template_string("<!DOCTYPE html><title>No Exception This Time</title><h1>OK This Time</h1>")


@app.route('/query/<dbtype>')
def query_db(dbtype):
    assert dbtype in ('pgsql', 'mysql')

    query_type = random.choice(('slow', 'error', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal'))
    sleep = random.randrange(1, 8) / 10.0

    if dbtype == 'pgsql':
        with db.pgsql() as cxn:
            cur = cxn.cursor()

            if query_type == 'slow':  # Be a slow query
                cur.execute("SELECT pg_sleep(%f)" % sleep)
            elif query_type == 'error':  # Be an erroneous query
                cur.execute("SELECT sql - error")
            else:
                cur.execute("SELECT 123")
    elif dbtype == 'mysql':
        with db.mysql() as cxn:
            cur = cxn.cursor()

            if query_type == 'slow':  # Be a slow query
                cur.execute("SELECT SLEEP(%f)" % sleep)
            elif query_type == 'error':  # Be an erroneous query
                cur.execute("SELECT sql - error")
            else:
                cur.execute("SELECT 123")

    return render_template_string(
        "<!DOCTYPE html><title>Query {{dbtype}}</title><h1>Ran DB Query {{type}}</h1>",
        dbtype=dbtype, type=query_type)


@app.route('/http')
def http_exit_call():
    url = request.args.get('url')

    if url is None:
        raise MissingArgumentException('required argument "url" is missing')

    lower_url = url.lower()
    if not lower_url.startswith('http://') and not lower_url.startswith('https://'):
        raise MissingArgumentException('required argument "url" must be a URL with protocol, like http://...')

    resp = requests.get(url)

    return render_template_string(
        "<!DOCTYPE html><title>HTTP Exit Call</title><h1>Response from {{url}}</h1><p>Content length {{len}}</p>",
        url=url, len=resp.headers.get('content-length', 'n/a'))


def random_exception():
    if random.randint(0, 3) == 0:
        my_dict = {}
        return my_dict['typo_eror']

    if random.randint(0, 3) == 0:
        my_list = [1, 2, 3, 4]
        return my_list[10]

    if random.randint(0, 3) == 0:
        assert True is False

    return int('abc')


if __name__ == '__main__':
    app.run('0.0.0.0', 9000, debug=True)
