from typing import List

from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_string = request.form['string']
        try:
            result = Solution.eraseOverlapIntervals(string=input_string)
        except Exception as e:
            result = str(e)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)



