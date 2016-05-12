from wtforms import Form, BooleanField, StringField, validators
# from model.fp_flask_sql import *


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=20)])
    password = StringField('Password', [validators.Length(min=5, max=20)])


class ProfileForm(Form):
    username = StringField('Username')
    password = StringField('Password')

def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user = {'Username':form.username.data, 'Password':form.password.data}

    #return render_response('register.html', form=form)