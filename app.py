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
    return render_template('hellocpp.cpp')

@app.route('/Python')
def givepy():
    return render_template('hellopy.py')


if __name__ == '__main__':
    app.run(debug=True)