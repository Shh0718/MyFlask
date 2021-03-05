from app import app
from flask import render_template,flash,redirect  # 从flask包中导入render_template函数
from app.forms import LoginForm


# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数

def index():
    user = {'username': 'Miguel'}  # 用户
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])  # 参数methods作用是：告诉Flask这个视图函数接受GET和POST请求方法
def login():
    form = LoginForm()  # 表单实例化对象
    # form.validate_on_submit()方法完成所有表单处理工作。当浏览器发送GET接收带有表单的网页请求时，此方法将返回False，此时函数会跳过if语句并直接在函数的最后一行呈现模板。
    # 当用户在浏览器按下提交按钮时，浏览器发送POST请求，form.validate_on_submit()将收集所有数据，运行附加到字段的所有验证器，如果一切正常，它将返回True，表明数据有效且可由应用程序处理。但如果至少有一个字段未通过验证，则函数就会返回False，接着就像上述GET请求那样。
    if form.validate_on_submit():
        # flash() 用于向用户显示消息，如让用户知道某些操作是否成功。目前为止，将使用其机制作为临时解决方案，因为暂无用户登录未真实所需的基础结构，此时只是显示一条消息用于确认应用程序已收到凭据。
        flash('Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data))
        # redirect()用于指示客户端（浏览器）自动导航到作为参数给出的其他页面（如上述代码中的/index页面，即重定向到应用程序的/index页面）
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

