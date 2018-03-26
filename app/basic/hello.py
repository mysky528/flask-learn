#coding:utf-8

'''
所有Flask程序都必须创建一个程序实例。
Flask类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(debug=True)
