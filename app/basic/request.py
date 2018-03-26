#coding:utf-8
from flask import Flask,request
app = Flask(__name__)


'''
Flask使用上下文临时把某些对象变为可访问的全局变量。
'''
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is %s</p>' % user_agent



if __name__ == '__main__':
    app.run(debug=True)
