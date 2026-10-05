from flask import Flask, render_template, request, jsonify
from feedback_generator import generate_student_feedback

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        name = data.get("name", "").strip()
        marks = data.get("marks", {})

        if not name:
            return jsonify({"error": "Please enter the student's name."}), 400

        if not marks:
            return jsonify({"error": "Please enter at least one subject and mark."}), 400

        converted_marks = {}

        for subject, score in marks.items():
            subject = subject.strip()

            if not subject:
                continue

            score = float(score)

            if score < 0 or score > 100:
                return jsonify(
                    {"error": f"Marks for {subject} must be between 0 and 100."}
                ), 400

            converted_marks[subject] = score

        if not converted_marks:
            return jsonify({"error": "Please enter valid subject marks."}), 400

        result = generate_student_feedback(name, converted_marks)

        return jsonify(result)

    except ValueError:
        return jsonify({"error": "Please enter valid numbers for marks."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)