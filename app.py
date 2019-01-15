from flask import Flask
from redis import Redis
from flask import render_template
from flask import session, redirect, url_for, escape, request
import math_custom
import francais

app = Flask(__name__)
redis = Redis(host='flask-redis', port=6379)
app.secret_key="random_secret"
sessionName=""
score=0

@app.route('/hello')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/')
def index():
    return render_template('index.html', score=score, name=sessionName)

@app.route('/exo/literraire')
def literraire():
    return render_template('francais.html')

@app.route('/exo/litteraire/easy')
def litteraire_easy():
    var1, var2, var3 = francais.qfacile()
    return render_template('francais.html',question=var1,answer=var2,reponses=var3)

@app.route('/exo/litteraire/medium')
def litteraire_medium():
    var1, var2, var3 = francais.qmoyen()
    return render_template('francais.html',question=var1,answer=var2,reponses=var3)

@app.route('/exo/litteraire/hard')
def litteraire_hard():
    var1, var2, var3 = francais.qdiff()
    return render_template('francais.html',question=var1,answer=var2,reponses=var3)

@app.route('/exo/math/')
def math():
    return render_template('math.html')

@app.route('/exo/math/easy')
def math_easy():
    var1, var2, var3 = math_custom.easy()
    return render_template('easy.html',var1=var1,var2=var2,var3=var3,score=score)

@app.route('/exo/math/medium')
def math_medium():
    var1, var2, var3 = math_custom.medium()
    return render_template('medium.html',var1=var1,var2=var2,var3=var3,score=score)

@app.route('/exo/math/hard')
def math_hard():
    var1, var2, var3 = math_custom.hard()
    return render_template('hard.html',var1=var1,var2=var2,var3=var3,score=score)

@app.route('/serious-game')
def seriousGame():
    return render_template('serious.html')

@app.route('/authorisation')
def authorise():
    session['authenticated']=True
    return render_template('auth.html',name=sessionName)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
