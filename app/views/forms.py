from wtforms import Form, StringField, PasswordField, IntegerField, SelectField, validators, EmailField


# Login Form Class
class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])


# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class AddForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=30)])
    price = IntegerField('Price')

    brand = StringField('Brand', [validators.Length(min=4, max=30)])
    model = StringField('Model', [validators.Length(min=1, max=30)])
    category = SelectField('Category',
                           choices=['Hatchback', 'Sedan', 'SUV', 'Coupe', 'Convertible', 'Wagon', 'Targa', 'Minivan',
                                    'Buggy', 'Pickup', 'Other'])
    vin = StringField('VIN number', [validators.Length(min=4, max=30)])
    year = IntegerField('Year of production')
    mileage = IntegerField('Mileage')

    engine_capacity = IntegerField('Engine capacity')
    engine_power = StringField('Engine power', [validators.Length(min=1, max=8)])
    engine_fuel = SelectField('Engine fuel', choices=['petrol', 'diesel', 'electric', 'gas'])

    transmission = SelectField('Transmission', choices=['manual', 'automat'])
    num_of_seats = IntegerField('Number of seats')
    color = StringField('Color', [validators.Length(min=1, max=30)])
    accident = SelectField('Accident', choices=['no', 'yes'])
    country = StringField('Country of origin', [validators.Length(min=2, max=30)])
    desc = StringField('Description', [validators.Length(max=1000)])


class SearchForm(Form):
    category = SelectField('Category',
                           choices=['', 'Hatchback', 'Sedan', 'SUV', 'Coupe', 'Convertible', 'Wagon', 'Targa', 'Minivan',
                                    'Buggy', 'Pickup', 'Other'])

    brand = StringField('Brand', [validators.Length(max=30)])
    model = StringField('Model', [validators.Length(max=30)])
    year_from = IntegerField('From', [validators.optional()])
    year_to = IntegerField('To', [validators.optional()])
    price_from = IntegerField('From', [validators.optional()])
    price_to = IntegerField('To', [validators.optional()])
    mileage = IntegerField('Max mileage', [validators.optional()])
    transmission = SelectField('Transmission', choices=['', 'manual', 'automat'])
    accident = SelectField('Accident', choices=['', 'no', 'yes'])
