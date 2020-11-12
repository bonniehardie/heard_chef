from flask_login import login_required
from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    return render_template("orders.html")
