from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from werkzeug.utils import secure_filename
import joblib   # joblib를 추가합니다.
import pandas as pd  # pandas를 추가합니다.

app = Flask(__name__)

# 엑셀 -> csv 변환
# def excel_to_csv():

# csv 파일 분석 후 PE 헤더 정보 출력 및 그래프로 나타내기
# def print_csv():

# 모델 로드
# pkl 파일이 있는 곳으로 경로를 변경해야 합니다
clf = joblib.load("C:/Users/김현서/Documents/Malicious_code_analysis_with_GPT/rf_classifier.pkl")

@app.route('/')
def main():
    return render_template('upload.html')

@app.route('/model', methods=['POST'])
def model():
    
    # 업로드된 파일을 데이터프레임으로 읽어옵니다.
    f = request.files['file']
    file_path = "./static/uploads/" + secure_filename(f.filename)
    df = pd.read_csv(file_path)
        
    # 데이터프레임을 이용하여 예측 등 원하는 작업 수행
    X = df.loc[:, 'API/DLL_0':'ENTRY_49']
    predicted_label = clf.predict(X)

    # JSON 형식으로 응답을 생성하여 반환
    response_data = {"predicted_label": predicted_label.tolist()}
    return jsonify(response_data), 200
        

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save("./static/uploads/" + secure_filename(f.filename))
        return render_template('home.html')
    else:
        return render_template('upload.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, threaded=True)
