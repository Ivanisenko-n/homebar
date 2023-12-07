# main_page.py
from flask import Blueprint, render_template
from db_utils.db_connection import create_alcohol_collection

main_page = Blueprint("main_page", __name__)
alcohol_collection = create_alcohol_collection()

@main_page.route("/", methods=["GET"], endpoint="index")
def index():
    data_list = list(alcohol_collection.find())
    return render_template("index.html", data_list=data_list)
