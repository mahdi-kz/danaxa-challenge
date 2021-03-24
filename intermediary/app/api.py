from flask import Blueprint, jsonify, request
from .environment import Environment
from . import queue

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/start", methods=["POST"])
def start_service():
    if Environment.service_status in ['stopped', 'to stop']:
        Environment.service_status = 'running'
        queue.call_service()
        return jsonify(status=200, message="service started", data={}), 200
    else:
        return jsonify(status=200, message="service is running", data={}), 200


@bp.route("/stop", methods=["POST"])
def stop_service():
    if Environment.service_status in ['running', 'idle']:
        Environment.service_status = 'to stop'
        return jsonify(status=200, message="service put to stop", data={}), 200
    else:
        return jsonify(status=200, message="service is not running", data={}), 200


@bp.route("/call", methods=["POST"])
def get_call():
    if request.is_json:
        if Environment.service_status in ['stopped', 'to stop']:
            return jsonify(status=500, message="service is not running", data={}), 500

        insertion_index = queue.enqueue(request.json)
        return jsonify(status=200, message="The request is queued at index " + str(insertion_index), data={}), 200
    return jsonify(status=500, message="request is wrong.", ), 500
