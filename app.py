from flask import Flask, render_template
from flask.wrappers import Request 


app = Flask(__name__,template_folder='templates')

    
@app.route('/')
def func():
    return render_template('index.htm')

@app.route('/C')
def givec():
    return render_template('helloc.htm')

@app.route('/C++')
def givecpp():
    return render_template('hellocpp.htm')

@app.route('/Python')
def givepy():
    return render_template('hellopy.htm')

@app.route('/Java')
def givejava():
    return render_template('hellojava.htm')

@app.route('/Javascript')
def givejs():
    return render_template('hellojs.htm')

if __name__ == '__main__':
    app.run(debug=True)