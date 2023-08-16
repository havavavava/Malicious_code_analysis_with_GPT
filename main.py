from flask import Flask
app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return 'Hello, World~~!'

if __name__=='__main__':
    app.run('0.0.0.0',port=80,threaded=True)