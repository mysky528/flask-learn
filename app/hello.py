#coding:utf-8

'''
所有Flask程序都必须创建一个程序实例。
Flask类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。
将bootstrap从flask.ext命名空间导入。
'''
from flask_bootstrap import Bootstrap
from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

'''
在Flask程序中定义路由最简便的方式，是使用程序实例提供的app.route修饰器，把修饰的函数注册为路由。
index()函数称为视图函数。视图函数返回的响应可以是包含HTML的简单字符串，也可以是复杂的表单。
'''
@app.route('/',methods=['GET','POST'])
def index():
    #return '<h1>Hello World</h1>'
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Look like your have changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    '''
    使用模版
    '''
    return render_template('index.html',form=form,name=session.get('name'))


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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


'''
定义表单类
'''
class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

'''
定义数据模型
'''
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref = 'role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


'''
程序实例用run方法启动Flask集成的开发Web服务器
'''
if __name__ == '__main__':
    app.run(debug=True)
