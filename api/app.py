from flask import Flask

#5 request代表用户所有内容
from flask import request

#6 可以使用前端模板文件 html文件
from flask import render_template

#9 引入消息闪现
from flask import flash

#10 引入重定向
from flask import redirect

#1构建Flask实例 创建服务对象
app = Flask(__name__)
#使用session需要配置密钥
app.secret_key = "2020-03-24"

@app.route("/",methods = ["GET"])
def userinfo():
    return render_template("index.html")

#4系统默认开启HTTP Get方法。可以使用methords添加新方法
@app.route("/result", methods = ["POST"])
def result():
    if request.method == "POST":
        username = request.form["username"]
        if  username == "":
            #8 使用消息闪现将错误信息传入下次请求
            flash("用户名必须填写!")
            # 9 再次回到填写信息页面
            return redirect("/")
        else:
            return render_template("result.html",username = username, safe = False)

    
#2启动服务器
if __name__ == "__main__":
    app.run(debug = True)