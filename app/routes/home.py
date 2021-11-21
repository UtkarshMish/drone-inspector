from flask import Blueprint, render_template


home_route = Blueprint("home", __name__)


@home_route.get("/<path:path>")
@home_route.get("/")
def home_page(path: str = None):
    return render_template("index.html")
