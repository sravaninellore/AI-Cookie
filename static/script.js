const categorySelect = document.getElementById("category");
const cookieIcon = document.getElementById("cookieIcon");
const getAdviceBtn = document.getElementById("getAdvice");
const resultText = document.getElementById("resultText");
const btnText = document.getElementById("btnText");
const loader = document.getElementById("loader");
const userQuestion = document.getElementById("userQuestion");

const emojis = {
    "Fortune Cookie": "🍪",
    "Decision Helper": "💡",
    "Daily Mentor": "🌅",
    "Tech Trends": "🔧",
    "Positive Nudges": "💖"
};

// Format plain text advice with simple markdown-like
function formatAdviceTextToHTML(text) {
    let html = text.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
    html = html.replace(/\n/g, '<br>');
    return html;
}

// Animate cookie crack on icon click
cookieIcon.addEventListener("click", () => {
    cookieIcon.classList.add("crack");
    setTimeout(() => cookieIcon.classList.remove("crack"), 400);
});

getAdviceBtn.addEventListener("click", async () => {
    const category = categorySelect.value;
    const question = userQuestion.value.trim();

    if (!category) {
        alert("Please select a cookie type!");
        return;
    }

    getAdviceBtn.disabled = true;
    loader.hidden = false;
    btnText.textContent = "Cracking your cookie...";
    cookieIcon.textContent = emojis[category] || "🥠";

    try {
        const res = await fetch("/advice", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category, question })
        });

        if (!res.ok) throw new Error(`HTTP error: ${res.status}`);

        const data = await res.json();
        resultText.innerHTML = formatAdviceTextToHTML(data.message);
        resultText.style.backgroundColor = "#fffae3";
        setTimeout(() => {
            resultText.style.backgroundColor = "";
        }, 300);

    } catch (e) {
        console.error("Error fetching advice:", e);
        resultText.textContent = "Something went wrong. Try again!";
    } finally {
        getAdviceBtn.disabled = false;
        loader.hidden = true;
        btnText.textContent = "Crack the Cookie!";
    }

});

// Enable or disable question input based on selected cookie type
categorySelect.addEventListener("change", () => {
    if (categorySelect.value === "Decision Helper") {
        userQuestion.placeholder = "Ask your question (e.g., Should I learn Python?)";
        userQuestion.disabled = false;
    } else {
        userQuestion.placeholder = "No question needed for this cookie";
        userQuestion.value = "";
        userQuestion.disabled = true;
    }
});

