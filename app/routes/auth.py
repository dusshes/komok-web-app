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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.password_hash and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(next_url or url_for('main.index'))
        else:
            flash('Неверный Email или пароль')
            
    return '''
        <h3>Вход</h3>
        <form method="POST">
            Email: <input type="email" name="email" required><br>
            Пароль: <input type="password" name="password" required><br>
            <button type="submit">Войти</button>
        </form>
        <p><a href="/register">Регистрация</a></p>
    '''

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    countries = Country.query.all()
    cities = City.query.all()
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        city_id = request.form.get('city_id')
        whatsapp = request.form.get('whatsapp')
        telegram = request.form.get('telegram')
        zalo = request.form.get('zalo')
        max_val = request.form.get('max')
        preferred_contact = request.form.get('preferred_contact')
        payout_details = request.form.get('payout_details')
        
        # Валидация
        if len(password) < 6:
            flash('Пароль должен содержать не менее 6 символов')
            return redirect(url_for('auth.register'))
            
        if not any([whatsapp, telegram, zalo, max_val]):
            flash('Пожалуйста, укажите хотя бы один способ связи (WhatsApp, Telegram, Zalo или Max)')
            return redirect(url_for('auth.register'))
            
        if User.query.filter_by(email=email).first():
            flash('Этот Email уже зарегистрирован в системе')
            return redirect(url_for('auth.register'))
        
        new_user = User(
            email=email,
            name=name,
            password_hash=generate_password_hash(password),
            city_id=city_id,
            whatsapp=whatsapp,
            telegram=telegram,
            zalo=zalo,
            max=max_val,
            preferred_contact=preferred_contact,
            payout_details=payout_details
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('Регистрация прошла успешно! Теперь вы можете войти.')
        return redirect(url_for('auth.login'))
            
    return f'''
        <h3>Регистрация</h3>
        <form method="POST">
            Имя: <input type="text" name="name" required><br>
            Email: <input type="email" name="email" required><br>
            Пароль: <input type="password" name="password" required><br>
            Город: <select name="city_id">{''.join([f'<option value="{c.id}">{c.name}</option>' for c in cities])}</select><br>
            WhatsApp: <input type="text" name="whatsapp"><br>
            Telegram: <input type="text" name="telegram"><br>
            Zalo: <input type="text" name="zalo"><br>
            Max: <input type="text" name="max"><br>
            Предпочитаемый способ: 
            <select name="preferred_contact">
                <option value="email">Email</option><option value="whatsapp">WhatsApp</option>
                <option value="telegram">Telegram</option><option value="zalo">Zalo</option><option value="max">Max</option>
            </select><br>
            Реквизиты для выплат: <textarea name="payout_details"></textarea><br>
            <button type="submit">Зарегистрироваться</button>
        </form>
    '''

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

