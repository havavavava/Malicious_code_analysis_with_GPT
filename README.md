# Malicious_code_analysis_with_GPT

## AWS EC2 클라우드 서비스 접속
1. pageant.exe에 키페어 파일 올리기
2. Putty HostName에 퍼블릭 DNS 입력(Port:22)
3. login as : ec2-user
4. AWS EC2 터미널 내에서 해당 폴더로 이동 후 실행
```python
sudo python3 main.py
```
5. 주소창에 퍼블릭 DNS로 접속
   
## GitHub에서 코드 내려받기
```python
git clone https://github.com/havavavava/Malicious_code_analysis_with_GPT
```

requirements.txt로 한번에 패키지 다운로드 
```python
pip install -r requirements.txt
```


## 오류
- Pycharm IDE에서 실행 버튼 활성화 안될 시
1. Add Configuration.. 클릭 후 + 누르고 Python으로 선택 (https://csy7792.tistory.com/101 참고)
2. Script path에서 폴더의 main.py 선택 후 OK

## 참고
- Pycharm Git 연동 https://hoohaha.tistory.com/38
