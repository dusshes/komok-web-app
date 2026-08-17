from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.models.location import City, Country
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next')
    email = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.password_hash and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(next_url or url_for('main.index'))
        else:
            flash('Неверный Email или пароль')
            
    return render_template('login.html', email=email)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    countries = Country.query.all()
    cities = City.query.all()
    
    form_data = {}
    
    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'city_id': request.form.get('city_id'),
            'whatsapp': request.form.get('whatsapp'),
            'telegram': request.form.get('telegram'),
            'zalo': request.form.get('zalo'),
            'max': request.form.get('max'),
            'preferred_contact': request.form.get('preferred_contact'),
            'payout_details': request.form.get('payout_details')
        }
        password = request.form.get('password')
        
        # Валидация
        if len(password) < 6:
            flash('Пароль должен содержать не менее 6 символов')
            return render_template('register.html', cities=cities, form_data=form_data)
            
        if not any([form_data['whatsapp'], form_data['telegram'], form_data['zalo'], form_data['max']]):
            flash('Пожалуйста, укажите хотя бы один способ связи (WhatsApp, Telegram, Zalo или Max)')
            return render_template('register.html', cities=cities, form_data=form_data)
            
        if User.query.filter_by(email=form_data['email']).first():
            flash('Этот Email уже зарегистрирован в системе')
            return render_template('register.html', cities=cities, form_data=form_data)
        
        new_user = User(
            email=form_data['email'],
            name=form_data['name'],
            password_hash=generate_password_hash(password),
            city_id=form_data['city_id'],
            whatsapp=form_data['whatsapp'],
            telegram=form_data['telegram'],
            zalo=form_data['zalo'],
            max=form_data['max'],
            preferred_contact=form_data['preferred_contact'],
            payout_details=form_data['payout_details']
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('Регистрация прошла успешно! Теперь вы можете войти.')
        return redirect(url_for('auth.login'))
            
    return render_template('register.html', cities=cities, form_data=form_data)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

