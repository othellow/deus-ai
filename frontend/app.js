/*
----------------------------------------------------
DEUS AI Frontend
----------------------------------------------------
Handles:

✓ Chat conversation
✓ Example prompt buttons
✓ Thinking animation
✓ Auto-growing textarea
✓ Enter to send
✓ Disable button while waiting
✓ Markdown-friendly rendering
✓ Auto scroll
----------------------------------------------------
*/

const API_URL = "http://127.0.0.1:8000/api/v1/chat";

const chatWindow = document.getElementById("chat-window");
const questionBox = document.getElementById("question");
const sendButton = document.getElementById("send");


// ----------------------------------------------------
// Auto-grow textarea
// ----------------------------------------------------

function autoResize() {

    questionBox.style.height = "auto";

    questionBox.style.height =
        questionBox.scrollHeight + "px";

}

questionBox.addEventListener(
    "input",
    autoResize
);


// ----------------------------------------------------
// Scroll
// ----------------------------------------------------

function scrollToBottom() {

    chatWindow.scrollTop =
        chatWindow.scrollHeight;

}


// ----------------------------------------------------
// Escape HTML
// ----------------------------------------------------

function escapeHTML(text) {

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");

}


// ----------------------------------------------------
// Very small Markdown renderer
// ----------------------------------------------------

function renderMarkdown(text) {

    let html = escapeHTML(text);

    // headings

    html = html.replace(
        /^### (.*)$/gm,
        "<h3>$1</h3>"
    );

    html = html.replace(
        /^## (.*)$/gm,
        "<h2>$1</h2>"
    );

    html = html.replace(
        /^# (.*)$/gm,
        "<h1>$1</h1>"
    );

    // bold

    html = html.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );

    // italic

    html = html.replace(
        /\*(.*?)\*/g,
        "<em>$1</em>"
    );

    // bullets

    html = html.replace(
        /^- (.*)$/gm,
        "<li>$1</li>"
    );

    html = html.replace(
        /(<li>.*<\/li>)/gs,
        "<ul>$1</ul>"
    );

    // paragraphs

    html = html.replace(
        /\n\n/g,
        "</p><p>"
    );

    html =
        "<p>" +
        html +
        "</p>";

    return html;

}


// ----------------------------------------------------
// Message Creator
// ----------------------------------------------------

function createMessage(role, html) {

    const wrapper =
        document.createElement("article");

    wrapper.className =
        `message ${role}`;

    if (role === "ai") {

        wrapper.innerHTML = `
        <div class="message-header">

            <div class="avatar">
                D
            </div>

            <div>

                <div class="sender">

                    DEUS AI

                </div>

                <div class="timestamp">

                    Knowledge Companion

                </div>

            </div>

        </div>

        <div class="message-body">

            ${html}

        </div>
        `;

    } else {

        wrapper.innerHTML = `

        <div class="message-header">

            <div class="sender">

                YOU

            </div>

        </div>

        <div class="message-body">

            ${html}

        </div>

        `;

    }

    chatWindow.appendChild(wrapper);

    scrollToBottom();

    return wrapper;

}


// ----------------------------------------------------
// Thinking animation
// ----------------------------------------------------

function createThinkingMessage() {

    return createMessage(
        "ai",
        `
        <div class="thinking-message">

            Thinking

            <span class="typing-dots">

                <span></span>

                <span></span>

                <span></span>

            </span>

        </div>
        `
    );

}


// ----------------------------------------------------
// Enable/Disable UI
// ----------------------------------------------------

function setLoading(loading) {

    sendButton.disabled = loading;

    document.body.classList.toggle(
        "is-loading",
        loading
    );

}


// ----------------------------------------------------
// Ask API
// ----------------------------------------------------

async function askQuestion(question) {

    createMessage(
        "user",
        `<p>${escapeHTML(question)}</p>`
    );

    const thinking =
        createThinkingMessage();

    setLoading(true);

    try {

        const response =
            await fetch(
                API_URL,
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                        "application/json",

                    },

                    body: JSON.stringify({

                        message: question,

                    }),

                }
            );

        const data =
            await response.json();

        thinking.querySelector(
            ".message-body"
        ).innerHTML =
            renderMarkdown(
                data.answer
            );

    }

    catch (error) {

        thinking.classList.add(
            "error-message"
        );

        thinking.querySelector(
            ".message-body"
        ).innerHTML = `

        <strong>

        Unable to reach DEUS AI.

        </strong>

        <br><br>

        Please verify that the backend
        server is running.

        `;

        console.error(error);

    }

    finally {

        setLoading(false);

        scrollToBottom();

    }

}


// ----------------------------------------------------
// Send
// ----------------------------------------------------

function send() {

    const question =
        questionBox.value.trim();

    if (!question) {

        return;

    }

    questionBox.value = "";

    autoResize();

    askQuestion(question);

}


// ----------------------------------------------------
// Button
// ----------------------------------------------------

sendButton.addEventListener(
    "click",
    send
);


// ----------------------------------------------------
// Enter
// ----------------------------------------------------

questionBox.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter"
            &&
            !event.shiftKey
        ) {

            event.preventDefault();

            send();

        }

    }
);


// ----------------------------------------------------
// Suggested questions
// ----------------------------------------------------

document
.querySelectorAll(".example")
.forEach((button) => {

    button.addEventListener(
        "click",
        () => {

            questionBox.value =
                button.dataset.question;

            autoResize();

            send();

        }
    );

});


// ----------------------------------------------------
// Initial
// ----------------------------------------------------

autoResize();

