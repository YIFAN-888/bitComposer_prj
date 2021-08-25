from flask import Flask,render_template
from datetime import datetime

ima = datetime.now()

app = Flask(__name__)

@app.route('/')
def welcome():
    title = "ようこそ"
    page_t = "メインページ"
    time = ima.strftime("%Y年%m月%d日")
    return render_template('index.html',title=title,page_title=page_t,time=time)

@app.route('/main',methods=["GET","POST"])
def bc():
    title = "bit composer"
    page_t = "bit composer"
    return render_template('bc.html',title=title,page_title=page_t)

if __name__ == "__main__":
    app.run()