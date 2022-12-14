from flask import Flask

from fibonacci import get_fibonacci_value_for_n

app = Flask(__name__)


@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/fibonacci/<n>')
def fib(n):
    n = int(n)
    return f'Web App with Python Flask!\n\n' \
           f'Fibonacci od {n} = {get_fibonacci_value_for_n(n)}'


app.run(host='0.0.0.0', port=5000)
