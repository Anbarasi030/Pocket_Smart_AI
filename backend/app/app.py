from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("Key loaded:", bool(GEMINI_API_KEY))
print("Key length:", len(GEMINI_API_KEY) if GEMINI_API_KEY else 0)
client=genai.Client(api_key=GEMINI_API_KEY)

FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../frontend")
)

app = Flask(
    __name__, 
    static_folder=FRONTEND_DIR,
     static_url_path=""
     )
CORS(app)

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/generate-home", methods=["GET", "POST"])
def generate_home():

    if request.method == "POST":
        data = request.get_json()
        budget = data.get("budget", 0)
    else:
        budget = 20000

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Create a simple and practical home interior plan
            for a budget of ₹{budget}.

            Give:
            1. Suggested items
            2. Approximate budget allocation
            3. Money-saving tips
            """
        )

        return jsonify({
            "message": response.text,
            "budget": budget
        })

    except Exception:
        return jsonify({
            "message": "Gemini is temporarily unavailable.",
            "fallback": f"Home Planner is ready for a budget of ₹{budget}. Suggested areas: furniture, lighting, curtains, decoration and storage.",
            "budget": budget
        })


@app.route("/generate-party")
def generate_party():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Create a simple party plan for a budget of ₹10,000 with 20 guests."
        )

        return jsonify({
            "message": response.text
        })

    except Exception:
        return jsonify({
            "message": "Gemini is temporarily unavailable.",
            "fallback": "Party Planner is ready! Budget: ₹10,000. Plan includes food, decorations, seating, music and return gifts."
        })

@app.route("/generate-jewelry")
def generate_jewelry():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Suggest simple jewelry options for a budget of ₹15,000 for a traditional family function."
        )

        return jsonify({
            "message": response.text
        })

    except Exception:
        return jsonify({
            "message": "Gemini is temporarily unavailable.",
            "fallback": "Jewelry Planner is ready. Budget: ₹15,000. Suggested options: simple earrings, necklace, bangles and a matching bracelet."
        })


@app.route("/test-gemini-key")
def test_gemini_key():
    if GEMINI_API_KEY:
        return "Gemini API key loaded successfully!"
    else:
        return "Gemini API key not found!"


@app.route("/test-gemini")
def test_gemini():
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Say hello to PocketSmart AI"
    )
    return response.text

if __name__ == "__main__":
    app.run(debug=True)