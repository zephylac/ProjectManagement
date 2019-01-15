from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titre="LeTitre", mots="[test1,test2,test3]")

if __name__ == '__main__':
    app.run(debug=True)
