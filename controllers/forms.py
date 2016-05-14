from wtforms import Form, BooleanField, StringField, validators, PasswordField
# from model.fp_flask_sql import *


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=20)])
    password = PasswordField('Password', [validators.Length(min=5, max=20), validators.DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user = {'Username':form.username.data, 'Password':form.password.data}

    #return render_response('register.html', form=form)
