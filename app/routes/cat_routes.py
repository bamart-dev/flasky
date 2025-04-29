from flask import Blueprint, abort, make_response, request, Response
from app.db import db
from app.models.cat import Cat

cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@cats_bp.post("", strict_slashes=False)
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    response = {
        "id": new_cat.id,
        "name": new_cat.name,
        "color": new_cat.color,
        "personality": new_cat.personality,
    }

    return response, 201


@cats_bp.get("", strict_slashes=False)
def get_all_cats():
    query = db.select(Cat)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Cat.name == name_param)

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%"))

    query = query.order_by(Cat.id)

    cats = db.session.scalars(query)

    return [
        {
                "id": cat.id,
                "name": cat.name,
                "color": cat.color,
                "personality": cat.personality,
            }
    for cat in cats]


@cats_bp.get("/<id>")
def get_one_cat(id):
    cat = validate_cat(id)

    return {
        "id": cat.id,
        "name": cat.name,
        "color": cat.color,
        "personality": cat.personality,
    }


@cats_bp.put("/<id>")
def update_cat(id):
    cat = validate_cat(id)
    request_body = request.get_json()

    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]
    db.session.commit()

    return Response(status=204,  mimetype="application/json")


@cats_bp.delete("/<id>")
def delete_cat(id):
    cat = validate_cat(id)
    db.session.delete(cat)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

# validation function
def validate_cat(id):
    """Validates cat_id."""
    try:
        id = int(id)
    except ValueError:
        response = {"message": "Invalid input."}
        abort(make_response(response, 400))
    query = db.select(Cat).where(Cat.id == id)
    cat = db.session.scalar(query)

    if not cat:
        response = {"message": f"cat {id} not found"}
        abort(make_response(response, 404))

    return cat
