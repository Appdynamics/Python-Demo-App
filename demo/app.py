from flask import Flask, render_template_string
import math
import random
import time

app = Flask(__name__)


@app.route('/wave/<whatever>')
def response_time_wave(whatever):
    angle = math.radians(time.time())
    delay = (math.sin(angle) + 1.0) / 5
    time.sleep(delay)
    return render_template_string("<!DOCTYPE html><title>Wave</title><h1>%s</h1>" % (delay,))


@app.route('/error/<when>')
def cause_error(when):
    if when == 'always' or random.randint(0, 9) == 0:
        raise random_exception()
    return render_template_string("<!DOCTYPE html><title>No Exception This Time</title><h1>OK This Time</h1>")


def random_exception():
    if random.randint(0, 3) == 0:
        my_dict = {}
        return my_dict['typo_eror']

    if random.randint(0, 3) == 0:
        my_list = [1, 2, 3, 4]
        return my_list[10]

    if random.randint(0, 3) == 0:
        assert True is False

    # Uh oh
    return int('abc')

if __name__ == '__main__':
    app.run('0.0.0.0', 9000, debug=True)
