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

@app.route('/exo/literraire')
def literraire():
    return render_template('francais.html')

@app.route('/exo/math')
def index2():
    return render_template('math.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
