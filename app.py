from flask import Flask
from redis import Redis
from flask import render_template

app = Flask(__name__)
redis = Redis(host='flask-redis', port=6379)

@app.route('/hello')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/')
def index():
    return render_template('index.html', titre="LeTitre", mots=["test1","test2","test3"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
