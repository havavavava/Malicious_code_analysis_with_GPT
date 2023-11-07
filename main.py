from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from werkzeug.utils import secure_filename
import joblib   # joblib를 추가합니다.
import pandas as pd  # pandas를 추가합니다.
import sklearn
#from aspose.cells import Workbook, SaveFormat
import requests

app = Flask(__name__)


# csv 파일 분석 후 PE 헤더 정보 출력 및 그래프로 나타내기
# def print_csv():

# 모델 로드
# pkl 파일이 있는 곳으로 경로를 변경해야 합니다
clf = joblib.load("static/model_pickle/rf_classifier.pkl")

@app.route('/')
def main():
    return render_template('upload.html')

'''
def excel_to_csv(f):
    workbook = Workbook("./static/uploads/" + secure_filename(f.filename))
    workbook.save("./static/uploads/" + secure_filename(f.filename), SaveFormat.CSV)
'''

'''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save("./static/uploads/" + secure_filename(f.filename))
        #return render_template('home.html')
    return render_template('upload.html')
'''

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/model', methods=['GET','POST'])
def model():
    if request.method == 'POST':
        f = request.files['file']
        # 파일 저장
        f.save("./static/uploads/" + secure_filename(f.filename))

        file_path = "static/uploads/" + secure_filename(f.filename)
        df = pd.read_csv(file_path)
        # 데이터프레임을 이용하여 예측 등 원하는 작업 수행
        X = df.loc[:, 'API/DLL_0':'ENTRY_49']
        predicted_label = clf.predict(X)

        # JSON 형식으로 응답을 생성하여 반환
        # response_data = {"predicted_label": predicted_label.tolist()}

        # home.html로 predicted=예측값 쿼리로 넘김
        if predicted_label.tolist() == 'normal':
            return render_template('templates/normal.html')
        else:
            return redirect(url_for('home', predicted=predicted_label.tolist()))
    return render_template('upload.html')
    #jsonify(response_data), 200



if __name__ == '__main__':
    app.run('0.0.0.0', port=80, threaded=True)
