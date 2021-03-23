from flask import Blueprint, jsonify, request
import time

bp = Blueprint("limited", __name__, url_prefix="/limited")


@bp.route("/call", methods=["POST"])
def call():
    if request.is_json:
        data = request.json
        time.sleep(2)
        print("Request --> uid = " + str(data['user_id']) + " , X = " + str(data['x']))
        return jsonify(status=200, message="PROCESSED", data={}), 200
    return jsonify(status=500, message="request is wrong.", ), 500
