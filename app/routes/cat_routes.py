from flask import Blueprint
from app.models.cat import cats


cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.get("")
def get_all_cats():

    return [
        {"id": cat.id,
         "name": cat.name,
         "color": cat.color,
         "personality": cat.personality}
        for cat in cats]


@cats_bp.get("/<id>")
def get_cat(id):
    return
