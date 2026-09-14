from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from app.models.user import User
from app.models.location import City

class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message='Поле обязательно для заполнения')])
    email = StringField('Email', validators=[DataRequired(message='Поле обязательно для заполнения'), Email(message='Введите корректный Email')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Поле обязательно для заполнения'), Length(min=6, message='Пароль должен содержать не менее 6 символов')])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(message='Поле обязательно для заполнения'), EqualTo('password', message='Пароли должны совпадать')])

    city_id = SelectField('Город', coerce=int, validators=[DataRequired(message='Выберите город')])
    whatsapp = StringField('WhatsApp')
    telegram = StringField('Telegram')
    zalo = StringField('Zalo')
    max_val = StringField('Max')
    preferred_contact = SelectField('Предпочитаемый способ связи', choices=[
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('zalo', 'Zalo'),
        ('max', 'Max')
    ])
    payout_details = TextAreaField('Реквизиты для выплат')
    submit = SubmitField('Зарегистрироваться')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id.choices = [(c.id, c.name) for c in City.query.all()]

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Этот Email уже зарегистрирован в системе')

    def validate(self, extra_validators=None):
        rv = super().validate(extra_validators)
        
        if not any([self.whatsapp.data, self.telegram.data, self.zalo.data, self.max_val.data]):
            self.whatsapp.errors.append('Пожалуйста, укажите хотя бы один способ связи')
            rv = False
        
        return rv
