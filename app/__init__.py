from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///komok.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Импорт моделей для регистрации в SQLAlchemy
    from app import models
    
    # Регистрация роутов
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    return app
