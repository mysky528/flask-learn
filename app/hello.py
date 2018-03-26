#coding:utf-8

'''
所有Flask程序都必须创建一个程序实例。
Flask类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。
'''
from flask import Flask,render_template
app = Flask(__name__)

'''
在Flask程序中定义路由最简便的方式，是使用程序实例提供的app.route修饰器，把修饰的函数注册为路由。
index()函数称为视图函数。视图函数返回的响应可以是包含HTML的简单字符串，也可以是复杂的表单。
'''
@app.route('/')
def index():
    #return '<h1>Hello World</h1>'
    '''
    使用模版
    '''
    return render_template('index.html')


'''
包含动态路由
'''
@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello,%s!</h1>' % name
    '''
    使用模版，然后是模版接收到name的变量
    '''
    return render_template('user.html',name=name)


'''
程序实例用run方法启动Flask集成的开发Web服务器
'''
if __name__ == '__main__':
    app.run(debug=True)
