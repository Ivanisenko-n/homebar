from flask import Blueprint, render_template, request, redirect, url_for
from db_utils.db_connection import create_alcohol_collection, create_category_collection
from bson import ObjectId

alcohol_app = Blueprint("alcohol", __name__)
alcohol_collection = create_alcohol_collection()
category_collection = create_category_collection()

# Добавление алкоголя
@alcohol_app.route("/add_alcohol", methods=["GET", "POST"])
def add_alcohol():
    category_list = list(category_collection.find({}, {"_id": 0, "name": 1}))
    if request.method == "POST":
        data = {
            "original_name": request.form["original_name"],
            "russian_name": request.form["russian_name"],
            "common_name": request.form["common_name"],
            "category": request.form["category"],
            "alcohol_content": request.form["alcohol_content"],
            "description": request.form["description"]
        }
        alcohol_collection.insert_one(data)
        return redirect(url_for("alcohol.add_alcohol"))

    return render_template("add_alcohol.html", category_list=category_list)

@app.route("/add_category", methods=["POST"])
def add_category():
    category_name = request.form.get("category")
    if category_name:
        category_collection.insert_one({"name": category_name})

    return redirect(url_for("category"))
