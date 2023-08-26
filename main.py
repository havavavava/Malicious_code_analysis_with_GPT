from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run('0.0.0.0',port=80,threaded=True)