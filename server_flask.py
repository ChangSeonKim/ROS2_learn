from flask import Flask
#flask 인스턴스 생성
app = Flask(__name__)
# 여기서 URL '/'는 다음 행에 정의되어 있는 hello함수와 연결된다.



@app.route("/")
def hellworld():
    str = "Hello world changseon"
    return str 

app.run(host= '0.0.0.0' , port='8000')