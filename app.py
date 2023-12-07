from flask import Flask, render_template, request, redirect, url_for
from db_utils.db_connection import create_alcohol_collection, create_cocktail_collection, create_category_collection
from bson import ObjectId
from db_utils import main_page

app = Flask(__name__)
alcohol_collection = create_alcohol_collection()
cocktail_collection = create_cocktail_collection()
category_collection = create_category_collection()

# Регистрируем blueprint
app.register_blueprint(main_page, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)

# Коктейли
@app.route("/cocktails")
def cocktails():
    # Здесь вы можете добавить логику для отображения коктейлей
    return "Страница с коктейлями"

# Добавление коктейля
@app.route("/add_cocktail")
def add_cocktail():
    # Здесь вы можете добавить логику для добавления коктейля
    return "Страница для добавления коктейля"

# Добавление алкоголя
@app.route("/add_alcohol")
def add_alcohol():
    category_list = list(category_collection.find({}, {"_id": 0, "name": 1}))
    if request.method == "POST":
        data = {
            "original_name": request.form["original_name"],
            "russian_name": request.form["russian_name"],
            "common_name": request.form["common_name"],
            "type": request.form["type"],
            "alcohol_content": request.form["alcohol_content"],
            "description": request.form["description"]
        }
        alcohol_collection.insert_one(data)
        return redirect(url_for("add_alcohol"))
    return render_template("add_alcohol.html", category_list=category_list)

# Добавление категории
@app.route("/add_category", methods=["GET", "POST"])
def category():
    category_list = list(category_collection.find())
    if request.method == "POST":
        category_name = request.form.get("category")
        if category_name:
            category_collection.insert_one({"name": category_name})
            return redirect(url_for("category"))

    return render_template("add_category.html", category_list=category_list)

@app.route("/delete_category/<string:id>", methods=["POST"])
def delete_category(id):
    try:
        category_collection.delete_one({"_id": ObjectId(id)})
    except Exception as e:
        print("Error:", str(e))

    return redirect(url_for("category"))


@app.route("/add_category", methods=["POST"])
def add_category():
    category_name = request.form.get("category")
    if category_name:
        category_collection.insert_one({"name": category_name})

    return redirect(url_for("category"))

# # Главная
# @app.route("/", methods=["GET"])
# def index():
#     data_list = list(alcohol_collection.find())  # Получаем данные из коллекции "alcohol"
#     return render_template("index.html", data_list=data_list)
# Удаление
@app.route("/delete_alcohol/<string:id>", methods=["POST"])
def delete_alcohol(id):
    try:
        # Обработка удаления записи
        alcohol_collection.delete_one({"_id": ObjectId(id)})
        return "", 200  # Возвращаем HTTP 200 (OK) без тела ответа
    except Exception as e:
        print("Error:", str(e))
        return "", 500  # Возвращаем HTTP 500 (INTERNAL SERVER ERROR)


if __name__ == "__main__":
    app.run(debug=True)
