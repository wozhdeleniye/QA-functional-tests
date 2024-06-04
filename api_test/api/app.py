from flask import Flask, request, abort
from solution import Solution

app = Flask(__name__)


@app.get('/')
def form():
    return '<html><body><h1>Erase Overlap Intervals</h1>' \
           '<form action="/" method="POST">' \
           '<input type="text" name="string">' \
           '<input type="submit">' \
           '<form></body></html>'


@app.post('/')
def check_inclusion():
    try:
        input = request.form['string']
        return {"result": Solution.eraseOverlapIntervals(input)}
    except TypeError:
        abort(400)
    except ValueError:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)
