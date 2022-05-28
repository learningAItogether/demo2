from flask import Flask

#5 request代表用户所有内容
from flask import request

#6 可以使用前端模板文件 html文件
from flask import render_template

#1构建Flask实例 创建服务对象
app = Flask(__name__)


#4系统默认开启HTTP Get方法。可以使用methords添加新方法
@app.route("/", methods = ["GET","POST"])
def userinfo():
    if request.method == "GET":
        return render_template("userinfo.html")

    elif request.method == "POST":
        username = request.form["username"]
        if  username == "":
            return "请填写表单！"
        else:
            return render_template("result.html",username = username, safe = False)

    
#2启动服务器
if __name__ == "__main__":
    app.run(debug = True)