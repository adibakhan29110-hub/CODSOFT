function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    if (message === "") return;

    addMessage("You: " + message, "user");
    input.value = "";

    fetch("/get-response", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => addMessage("Nova: " + data.response, "bot"));
}

function addMessage(text, type) {
    let chatBox = document.getElementById("chat-box");
    let msgDiv = document.createElement("div");
    msgDiv.className = "message " + type;
    msgDiv.innerText = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}




// DARK MODE TOGGLE
const toggleSwitch = document.getElementById("theme-toggle");

toggleSwitch.addEventListener("change", function () {
    document.body.classList.toggle("light-mode");
});
