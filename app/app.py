
#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
from models.models import DataContent
from models.database import db_session
from datetime import datetime

#Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
@app.route("/index",methods=["GET"])
def index():
    datas = DataContent.query.all()
    return render_template("index.html", datas=datas)


@app.route("/index",methods=["POST"])
def post():
    title = request.form["title"]
    body = request.form["body"]
    print(title,body)
    content = DataContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    datas = DataContent.query.all()
    return render_template("index.html", datas=datas)

@app.route("/delete",methods=["POST"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = DataContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    datas = DataContent.query.all()
    return render_template("index.html", datas=datas)

#おまじない
if __name__ == "__main__":
    app.run(debug=True)