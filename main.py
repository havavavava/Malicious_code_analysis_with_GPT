from flask import Flask, render_template, request, session, url_for, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('upload.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save("./static/uploads/" + secure_filename(f.filename))
        return render_template('/home.html')
    else:
        return render_template('/upload.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run('0.0.0.0',port=80,threaded=True)