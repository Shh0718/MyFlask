from flask_wtf import FlaskForm  # 从flask_wtf包中导入FlaskForm类
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # 导入这些类
from wtforms.validators import DataRequired

"""
存放Web表单类
"""


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # 校验 DataRequired验证器 只是简单地检查该字段不会提交为空
    password = PasswordField('Password', validators=[DataRequired()])  # 校验
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
