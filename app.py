from flask import Flask
from redis import Redis
from flask import render_template
import math_custom
import francais

app = Flask(__name__)
redis = Redis(host='flask-redis', port=6379)

@app.route('/hello')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/')
def index():
    return render_template('index.html')

""" @app.route('/exo/literraire')
def literraire():
    francais.go()

@app.route('/math/easy')
def index2():
    math_custom.easy()

@app.route('/math/medium')
def index3():
    math_custom.medium()

@app.route('/math/hard')
def index4():
    math_custom.hard() """


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
