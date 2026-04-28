from src.models.predict import predict_course, predict_student_gpa

GRADE_POINTS = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "D-": 0.67,
    "F": 0.0,
}


def clamp_gpa(value):
    return round(max(0.0, min(4.0, float(value))), 3)


def course_name(course):
    subject = str(course.get("subject", "")).strip().upper()
    number = str(course.get("number", "")).strip()
    return f"{subject} {number}".strip()


def grade_to_gpa(grade):
    normalized = str(grade or "").strip().upper()
    if normalized not in GRADE_POINTS:
        raise ValueError(f"Unsupported grade: {grade}")
    return GRADE_POINTS[normalized]


def gpa_to_letter(gpa):
    gpa = float(gpa)
    if gpa >= 3.85:
        return "A"
    if gpa >= 3.5:
        return "A-"
    if gpa >= 3.15:
        return "B+"
    if gpa >= 2.85:
        return "B"
    if gpa >= 2.5:
        return "B-"
    if gpa >= 2.15:
        return "C+"
    if gpa >= 1.85:
        return "C"
    if gpa >= 1.5:
        return "C-"
    if gpa >= 1.15:
        return "D+"
    if gpa >= 0.85:
        return "D"
    if gpa >= 0.5:
        return "D-"
    return "F"


def difficulty_from_gpa(gpa):
    if gpa >= 3.5:
        return "Low"
    if gpa >= 3.0:
        return "Medium"
    if gpa >= 2.5:
        return "High"
    return "Very high"


def average(values):
    clean = [float(value) for value in values if value is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def predict_course_gpa(course):
    return predict_course(
        course.get("subject", ""),
        course.get("number", ""),
        course.get("professor", ""),
    )


def calculate_past_adjustment(past_courses):
    adjustments = []
    skipped = []

    for course in past_courses:
        try:
            actual_gpa = grade_to_gpa(course.get("grade"))
        except ValueError as exc:
            skipped.append({"course": course_name(course), "reason": str(exc)})
            continue

        predicted_gpa = predict_course_gpa(course)
        if predicted_gpa is None:
            skipped.append({"course": course_name(course), "reason": "Course was not found"})
            continue

        adjustments.append(actual_gpa - predicted_gpa)

    return average(adjustments) or 0.0, skipped


def predict_future_courses(future_courses, student_adjustment):
    predictions = []

    for course in future_courses:
        class_gpa = predict_course_gpa(course)
        if class_gpa is None:
            predictions.append({
                "course": course_name(course),
                "professor": course.get("professor", ""),
                "error": "Course was not found",
            })
            continue

        adjusted_gpa = clamp_gpa(class_gpa + student_adjustment)
        predictions.append({
            "course": course_name(course),
            "professor": course.get("professor", ""),
            "class_gpa": clamp_gpa(class_gpa),
            "adjusted_gpa": adjusted_gpa,
            "predicted_grade": gpa_to_letter(adjusted_gpa),
            "difficulty": difficulty_from_gpa(class_gpa),
            "confidence": 0.72,
        })

    return predictions


def has_complete_student_profile(profile):
    required = [
        "age",
        "study_hours_per_day",
        "sleep_hours",
        "screen_time_hours",
        "attendance_percentage",
        "stress_level",
    ]
    return all(str(profile.get(key, "")).strip() != "" for key in required)


def predict_student_schedule_gpa(
    past_courses,
    future_courses,
    student_profile=None,
    class_weight=0.7,
    student_weight=0.3,
):
    student_profile = student_profile or {}
    student_adjustment, skipped_past_courses = calculate_past_adjustment(past_courses)
    course_predictions = predict_future_courses(future_courses, student_adjustment)

    future_average_class_gpa = average(
        prediction.get("class_gpa") for prediction in course_predictions
    )

    adjusted_class_projection = None
    if future_average_class_gpa is not None:
        adjusted_class_projection = clamp_gpa(future_average_class_gpa + student_adjustment)

    student_profile_projection = None
    profile_error = None
    if has_complete_student_profile(student_profile):
        try:
            student_profile_projection = clamp_gpa(predict_student_gpa(student_profile))
        except ValueError as exc:
            profile_error = str(exc)

    if adjusted_class_projection is not None and student_profile_projection is not None:
        final_projected_gpa = clamp_gpa(
            class_weight * adjusted_class_projection
            + student_weight * student_profile_projection
        )
    elif adjusted_class_projection is not None:
        final_projected_gpa = adjusted_class_projection
    else:
        final_projected_gpa = student_profile_projection

    return {
        "final_projected_gpa": final_projected_gpa,
        "final_projected_grade": (
            gpa_to_letter(final_projected_gpa)
            if final_projected_gpa is not None
            else None
        ),
        "future_average_class_gpa": (
            clamp_gpa(future_average_class_gpa)
            if future_average_class_gpa is not None
            else None
        ),
        "student_adjustment": round(float(student_adjustment), 3),
        "adjusted_class_projection": adjusted_class_projection,
        "student_profile_projection": student_profile_projection,
        "course_predictions": course_predictions,
        "skipped_past_courses": skipped_past_courses,
        "profile_error": profile_error,
        "weights": {
            "class_projection": class_weight,
            "student_profile": student_weight,
        },
    }
