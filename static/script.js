function ensureElements() {
    const requiredIds = ["fileInput", "uploadTrigger", "dropZone", "fileList", "query", "chat", "uploadStatus"];
    return requiredIds.every((id) => document.getElementById(id));
}

function removePlaceholder() {
    const placeholder = document.querySelector(".chat-placeholder");
    if (placeholder) {
        placeholder.remove();
    }
}

function addFileToSidebar(fileName) {
    const fileList = document.getElementById("fileList");
    if (!fileList) {
        return;
    }

    const item = document.createElement("li");
    item.className = "doc-item";
    item.textContent = fileName;
    fileList.prepend(item);
}

function addChatMessage(text, role) {
    const chat = document.getElementById("chat");
    if (!chat) {
        return;
    }

    removePlaceholder();

    const bubble = document.createElement("div");
    bubble.className = `chat-message ${role}`;
    bubble.textContent = text;
    chat.appendChild(bubble);
    chat.scrollTop = chat.scrollHeight;
}

async function uploadFile(file) {
    if (!file) {
        return;
    }

    const uploadStatus = document.getElementById("uploadStatus");
    uploadStatus.textContent = `Uploading ${file.name}...`;

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (!res.ok) {
            throw new Error("Upload endpoint unavailable");
        }

        uploadStatus.textContent = `${file.name} uploaded successfully`;
    } catch (error) {
        uploadStatus.textContent = `${file.name} added locally (demo mode)`;
    }

    addFileToSidebar(file.name);
}

async function sendMessage() {
    const input = document.getElementById("query");
    if (!input) {
        return;
    }

    const query = input.value.trim();
    if (!query) {
        return;
    }

    addChatMessage(query, "user");
    input.value = "";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        });

        if (!res.ok) {
            throw new Error("Chat endpoint unavailable");
        }

        const data = await res.json();
        const answer = data?.answer || "I could not generate a response.";
        addChatMessage(answer, "bot");
    } catch (error) {
        addChatMessage("Demo mode: connect /chat endpoint to get live answers.", "bot");
    }
}

function setupUpload() {
    const fileInput = document.getElementById("fileInput");
    const uploadTrigger = document.getElementById("uploadTrigger");
    const dropZone = document.getElementById("dropZone");

    uploadTrigger.addEventListener("click", () => fileInput.click());

    fileInput.addEventListener("change", async () => {
        const file = fileInput.files[0];
        await uploadFile(file);
        fileInput.value = "";
    });

    dropZone.addEventListener("dragover", (event) => {
        event.preventDefault();
        dropZone.classList.add("dragging");
    });

    dropZone.addEventListener("dragleave", () => {
        dropZone.classList.remove("dragging");
    });

    dropZone.addEventListener("drop", async (event) => {
        event.preventDefault();
        dropZone.classList.remove("dragging");
        const file = event.dataTransfer.files[0];
        await uploadFile(file);
    });
}

function setupChat() {
    const input = document.getElementById("query");
    const sendBtn = document.getElementById("sendBtn");

    if (sendBtn) {
        sendBtn.addEventListener("click", sendMessage);
    }

    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    if (!ensureElements()) {
        return;
    }

    setupUpload();
    setupChat();
});
