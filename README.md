# 🥠 AI Daily Mentor

An **interactive AI-powered "cookie-cracking" web app** that delivers daily advice, tech trends, productivity tips, and personalized decision support. Crack a virtual cookie and receive bite-sized guidance for career, coding, wellness, and more!  

---

## 🌟 Features

- 🍪 **Fortune Cookie** – Motivational messages for daily positivity.  
- 💡 **Decision Helper** – Ask a question and get a short, practical suggestion.  
- 🌅 **Daily Mentor** – Personalized daily tips for coding, productivity, or career growth.  
- 🔧 **Tech Trends** – One-line summaries of trending technologies or AI tools.  
- 💖 **Positive Nudges** – Science-backed reminders for health and well-being.  
- Interactive **cookie-cracking animations** with emojis.  
- Fallback messages in case the AI API fails.  

---

## 🎨 Demo

[![Demo GIF](link-to-demo-gif-or-screenshot)](https://github.com/user-attachments/assets/613cacf5-e8ec-4e95-9a9b-cf177cb44a25)  

Click a cookie to reveal your advice, suggestion, or tip instantly!

---

## ⚡ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI:** Groq API (`llama-3.1-8b-instant`)  
- **Environment Management:** `.env` for API keys  
- **Animations:** Cookie crack animation using CSS and JS  

---

## 📂 Folder Structure

project/
├─ templates/
│ └─ index.html
├─ static/
│ ├─ style.css
│ ├─ script.js
├─ app.py
├─ requirements.txt
└─ .env

---

## 🚀 Installation & Local Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/ai-daily-mentor.git
cd ai-daily-mentor
Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
Install dependencies

bash
pip install -r requirements.txt
Create a .env file in the root directory:

ini
GROQ_API_KEY=your_groq_api_key_here
Run the Flask app locally

bash
python app.py
Visit http://127.0.0.1:5000 in your browser.

🌐 Deployment
You can deploy the app on free platforms:
Render – Free hosting for Flask apps.
Railway – Easy deployment with free tier.
PythonAnywhere – Free hosting for small Python web apps.
Replit – Online IDE with hosting capabilities.

Note: Bind Flask to 0.0.0.0 and use the PORT environment variable for deployment.

Example for app.py:
python
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
✨ How to Use
Open the app in your browser.

Select a cookie type from the dropdown.

(Optional) Ask a question for "Decision Helper."

Click Crack the Cookie!.

View your advice, tip, or tech trend with fun emoji animation.

🤝 Contributing
Contributions are welcome!

Add new cookie categories or tips.

Improve animations or UI/UX.

Suggest new AI prompts or responses.

📄 License
This project is open-source under the MIT License.

👤 Author
Sravani – AI web projects & experimentation
