from flask import Blueprint, render_template
from app.models.location import Country

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    countries = Country.query.all()
    return render_template('index.html', countries=countries)
