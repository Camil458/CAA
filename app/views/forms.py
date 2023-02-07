from wtforms import Form, StringField, PasswordField, IntegerField, SelectField, validators


# Login Form Class
class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class AddForm(Form):
    brand = StringField('Brand', [validators.Length(min=4, max=30)])
    model = StringField('Model', [validators.Length(min=1, max=30)])
    category = StringField('Category', [validators.Length(min=1, max=30)])
    subcategory = StringField('Subcategory', [validators.Length(min=1, max=30)])
    vin = StringField('VIN number', [validators.Length(min=4, max=30)])
    reg = StringField('Registration number', [validators.Length(min=4, max=30)])
    year = IntegerField('Year of production')
    mileage = IntegerField('Mileage')

    engine_name = StringField('Engine name', [validators.Length(min=1, max=30)])
    engine_capacity = StringField('Engine capacity', [validators.Length(min=1, max=30)])
    engine_power = StringField('Engine power', [validators.Length(min=1, max=8)])
    engine_fuel = SelectField('Engine fuel', choices=['petrol', 'diesel'])

    transmission = SelectField('Transmission', choices=['manual', 'automat'])
    num_of_seats = IntegerField('Number of seats')
    color = StringField('Color', [validators.Length(min=1, max=30)])
    accident = SelectField('Accident', choices=['no', 'yes'])
    country = StringField('Country of origin', [validators.Length(min=2, max=30)])
    desc = StringField('Description', [validators.Length(max=1000)])
