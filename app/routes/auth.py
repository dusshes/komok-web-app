from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.models.location import City, Country
from app.models.verification_code import EmailVerificationCode
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms.register_form import RegisterForm
from app.services.email_service import send_verification_email
import random
import string
from datetime import datetime, timedelta

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
            if not user.is_verified:
                flash('Пожалуйста, подтвердите ваш Email.', 'warning')
                return redirect(url_for('auth.verify_email', email=email))
            login_user(user)
            return redirect(next_url or url_for('main.index'))
        else:
            flash('Неверный Email или пароль', 'danger')
            
    return render_template('login.html', email=email)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    countries = Country.query.all()
    cities = City.query.all()
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password_hash=generate_password_hash(form.password.data),
            city_id=form.city_id.data,
            whatsapp=form.whatsapp.data,
            telegram=form.telegram.data,
            zalo=form.zalo.data,
            max=form.max_val.data,
            preferred_contact=form.preferred_contact.data,
            payout_details=form.payout_details.data,
            is_verified=False
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Generate and save code
        code = ''.join(random.choices(string.digits, k=6))
        code_hash = generate_password_hash(code)
        new_code = EmailVerificationCode(user_id=new_user.id, code_hash=code_hash)
        db.session.add(new_code)
        db.session.commit()
        
        send_verification_email(new_user.email, code)
        
        flash('Регистрация прошла успешно! Пожалуйста, подтвердите ваш Email.', 'info')
        return redirect(url_for('auth.verify_email', email=new_user.email))
            
    return render_template('register.html', cities=cities, form=form)

@auth_bp.route('/verify-email', methods=['GET', 'POST'])
def verify_email():
    email = request.args.get('email') or request.form.get('email')
    if request.method == 'POST':
        code = request.form.get('code')
        user = User.query.filter_by(email=email).first()
        if user:
            verification = EmailVerificationCode.query.filter_by(user_id=user.id).first()
            if verification and not verification.is_expired() and check_password_hash(verification.code_hash, code):
                user.is_verified = True
                db.session.delete(verification)
                db.session.commit()
                flash('Email успешно подтвержден! Вы можете войти.', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Неверный или просроченный код.', 'danger')
        else:
            flash('Пользователь не найден.', 'danger')
            
    return render_template('verify_email.html', email=email)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

