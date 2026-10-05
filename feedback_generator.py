from textblob import TextBlob


class FeedbackGenerator:

    def __init__(self):

        self.templates = {

            "excellent":
                "Excellent performance, {name}! "
                "You have demonstrated strong understanding and consistent effort.",

            "good":
                "Good performance, {name}! "
                "You are doing well and can improve further with continued practice.",

            "average":
                "Good effort, {name}! "
                "There are some areas where additional practice can help you improve.",

            "needs_improvement":
                "Keep working, {name}! "
                "Focus on the weaker areas and practice regularly to improve your performance."
        }


    def analyze_score(self, score):

        if score >= 85:
            return "excellent"

        elif score >= 70:
            return "good"

        elif score >= 50:
            return "average"

        else:
            return "needs_improvement"


    def identify_strengths(self, marks):

        strengths = []

        for subject, score in marks.items():

            if score >= 75:
                strengths.append(subject)

        return strengths


    def identify_improvements(self, marks):

        improvements = []

        for subject, score in marks.items():

            if score < 60:
                improvements.append(subject)

        return improvements


    def recommendations(self, improvements):

        recommendations = []

        for subject in improvements:

            recommendations.append(
                f"Practice {subject} regularly and revise important concepts."
            )

        if not recommendations:

            recommendations.append(
                "Continue your current study routine and challenge yourself with advanced problems."
            )

        return recommendations


    # NLP SENTIMENT ANALYSIS

    def analyze_sentiment(self, feedback):

        analysis = TextBlob(feedback)

        polarity = analysis.sentiment.polarity

        if polarity > 0:
            return "Positive"

        elif polarity < 0:
            return "Negative"

        else:
            return "Neutral"


    def generate_feedback(self, name, marks):

        scores = list(marks.values())

        average_score = sum(scores) / len(scores)


        performance_type = self.analyze_score(
            average_score
        )


        strengths = self.identify_strengths(
            marks
        )


        improvements = self.identify_improvements(
            marks
        )


        recommendations = self.recommendations(
            improvements
        )


        feedback = self.templates[
            performance_type
        ].format(name=name)


        sentiment = self.analyze_sentiment(
            feedback
        )


        return {

            "name": name,

            "average": round(
                average_score,
                2
            ),

            "performance":
                performance_type.replace(
                    "_",
                    " "
                ).title(),

            "feedback":
                feedback,

            "strengths":
                strengths,

            "improvements":
                improvements,

            "recommendations":
                recommendations,

            "sentiment":
                sentiment
        }


def generate_student_feedback(name, marks):

    generator = FeedbackGenerator()

    return generator.generate_feedback(
        name,
        marks
    )


if __name__ == "__main__":

    sample_marks = {

        "Python": 85,

        "Machine Learning": 72,

        "NLP": 58,

        "Data Science": 80
    }


    result = generate_student_feedback(
        "Pravallika",
        sample_marks
    )


    print("\nAI PERFORMANCE FEEDBACK")

    print("-----------------------")

    print(
        "Student:",
        result["name"]
    )

    print(
        "Average:",
        result["average"]
    )

    print(
        "Performance:",
        result["performance"]
    )

    print(
        "Sentiment:",
        result["sentiment"]
    )

    print("\nFeedback:")

    print(
        result["feedback"]
    )

    print("\nStrengths:")

    for item in result["strengths"]:

        print(
            "-",
            item
        )

    print(
        "\nAreas for Improvement:"
    )

    for item in result["improvements"]:

        print(
            "-",
            item
        )

    print(
        "\nRecommendations:"
    )

    for item in result["recommendations"]:

        print(
            "-",
            item
        )