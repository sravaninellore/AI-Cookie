from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
import os
from groq import Groq

app = Flask(__name__)
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/advice", methods=["POST"])
def advice():
    category = request.json.get("category")
    user_question = request.json.get("question", "")

    if not category:
        return jsonify({"message": "Please select a category!"})

    try:
        if category == "Fortune Cookie":
            prompt = "You are a fortune cookie. Give a short positive fortune."
        elif category == "Decision Helper":
            if not user_question:
                return jsonify({"message": "Please ask a question!"})
            prompt = f"You are a helpful advisor. Give a short practical suggestion for this question: {user_question}"
        elif category == "Daily Mentor":
            prompt = "Give a short daily tip for career, coding, health, or productivity."
        elif category == "Tech Trends":
            prompt = "Summarize a trending technology or AI tool in one sentence."
        elif category == "Positive Nudges":
            prompt = "Give a short science-backed nudge for health or wellbeing."
        else:
            prompt = "Give a fun positive message."

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content.strip()
    except Exception as e:
        print("⚠️ API failed, using fallback:", e)
        result = "Believe in yourself and all things are possible 💫"

    return jsonify({"message": result})

if __name__ == "__main__":
     # Local test on port 9500
#      app.run(host="0.0.0.0", port=9500)
    # Bind to 0.0.0.0 and pick dynamic port from environment (for Render)
     port = int(os.environ.get("PORT", 9500))  # Use 9500 if PORT not set
     app.run(host="0.0.0.0", port=port)