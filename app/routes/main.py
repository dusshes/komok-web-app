from flask import Blueprint, render_template, request
from app.models.item import Item
from app.models.location import City
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    city_id = request.args.get('city_id', type=int)
    search = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 12

    # Use joinedload to fetch city info efficiently
    from sqlalchemy.orm import joinedload
    query = Item.query.options(joinedload(Item.city)).filter_by(status='available')

    if city_id:
        query = query.filter_by(city_id=city_id)
    
    if search:
        query = query.filter(
            (Item.title.ilike(f'%{search}%')) | (Item.description.ilike(f'%{search}%'))
        )

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items
    cities = City.query.all()

    return render_template(
        'index.html',
        items=items,
        cities=cities,
        city_id=city_id,
        search=search,
        pagination=pagination
    )
