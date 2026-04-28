from flask import Flask, jsonify, request

from src.models.schedule_pipeline import predict_student_schedule_gpa

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/predict", methods=["OPTIONS"])
def predict_options():
    return ("", 204)


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    past_courses = payload.get("past_courses") or []
    future_courses = payload.get("future_courses") or []
    student_profile = payload.get("student_profile") or {}

    if not past_courses and not future_courses and not student_profile:
        return jsonify({"error": "Provide past courses, future courses, or a student profile."}), 400

    try:
        result = predict_student_schedule_gpa(
            past_courses=past_courses,
            future_courses=future_courses,
            student_profile=student_profile,
        )
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
