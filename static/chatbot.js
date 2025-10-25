// Toggle chat window
document.getElementById("chatbot-button").onclick = () => {
    const chatbox = document.getElementById("chatbot-box");
    const isVisible = chatbox.classList.contains("show");
    chatbox.classList.toggle("show");

    // Only show welcome message when chat becomes visible AND not shown yet
    if (!isVisible && !sessionStorage.getItem("welcomeShown")) {
        showWelcomeMessage();
    }
};

document.getElementById("chat-close").onclick = () => {
    document.getElementById("chatbot-box").classList.remove("show");
};

// Send message
document.getElementById("send-chat").onclick = sendMessage;

document.getElementById("chat-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (!message) return;

    addMessage("user", message);
    input.value = "";

    const chatBox = document.getElementById("chat-messages");
    const typingDiv = document.createElement("div");
    typingDiv.className = "typing";
    typingDiv.innerHTML = `<span></span><span></span><span></span>`;
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/chatbot/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `message=${encodeURIComponent(message)}`
    })
    .then(res => res.json())
    .then(data => {
        setTimeout(() => {
            typingDiv.remove();
            addMessage("bot", data.response || "Sorry, something went wrong.");
        }, 1000);
    })
    .catch(() => {
        typingDiv.remove();
        addMessage("bot", "Error talking to the bot.");
    });
}

function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-messages");
    const div = document.createElement("div");
    div.className = sender;
    div.innerHTML = formatMessage(text);
    div.style.animation = "fadeInBubble 0.3s ease-in-out";
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function formatMessage(text) {
    return text
        .replace(/:\)/g, "😊")
        .replace(/:D/g, "😄")
        .replace(/:\(/g, "😢")
        .replace(/<3/g, "❤️")
        .replace(/:thumbsup:/g, '<i class="fas fa-thumbs-up"></i>')
        .replace(/:smile:/g, '<i class="fas fa-smile"></i>');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
