# 💬 A Flask-based NLP web app that classifies text as positive, negative, or neutral using TextBlob sentiment analysis.

### Give a piece of text a mood — and a couple of numbers to explain it.

How positive is a sentence?

How negative?

And is it mostly expressing an opinion, or simply stating something?

This project turns those questions into a small web application using **Flask and TextBlob**.

Enter a sentence, submit it, and the application analyzes two dimensions of the text:

```text
                  Your Text
                      │
                      ▼
                 ┌─────────┐
                 │ TextBlob│
                 │ Analysis│
                 └────┬────┘
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
        Polarity            Subjectivity
            │                   │
            ▼                   ▼
      Positive /             Objective /
      Negative /              Subjective /
       Neutral                 Balanced
```

The result is then presented through a simple browser-based interface.

---

## 🧠 What Is Being Measured?

The application doesn't just return a label.

It calculates **two sentiment-related scores**.

### Polarity

Polarity describes the emotional direction of the text.

It ranges from:

```text
-1 ─────────── 0 ─────────── +1
Negative     Neutral       Positive
```

For example:

```text
"I absolutely loved the experience."
                 ↓
             Positive
```

while:

```text
"The service was terrible."
                 ↓
             Negative
```

---

### Subjectivity

Subjectivity indicates how much the text resembles an opinion or personal expression.

The score ranges from:

```text
0 ───────────────────────── 1
Objective                 Subjective
```

For example:

```text
"The Earth revolves around the Sun."
                ↓
          More objective
```

versus:

```text
"I think this is the best movie ever."
                ↓
         More subjective
```

The application displays both values so the result isn't reduced to simply **“positive” or “negative.”**

---

## 🎚️ How the Final Label Is Decided

TextBlob provides the polarity score.

The application then applies its own classification threshold:

```text
                    Polarity
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       < -0.15     -0.15 to       > +0.15
                    +0.15
          │            │            │
          ▼            ▼            ▼
      Negative      Neutral      Positive
```

In the application:

```python
if polarity_score > 0.15:
    sentiment_category = "Positive"
elif polarity_score < -0.15:
    sentiment_category = "Negative"
else:
    sentiment_category = "Neutral"
```

The **±0.15 threshold** means small polarity values are treated as neutral instead of being immediately classified as positive or negative.

---

# 🖥️ From Text Box to Result

The application follows a simple request cycle:

```text
┌─────────────────┐
│     Browser     │
│  Enter some text│
└────────┬────────┘
         │
         │ POST /
         │ text_input
         ▼
┌─────────────────┐
│      Flask      │
│      Route      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     TextBlob    │
│  NLP Analysis   │
└────────┬────────┘
         │
         ├──── Polarity
         ├──── Subjectivity
         └──── Sentiment
                   │
                   ▼
          ┌────────────────┐
          │     Jinja2     │
          │ HTML Template  │
          └───────┬────────┘
                  │
                  ▼
            Result Page
```

There is **no database involved**.

The text is submitted, analyzed, and returned to the page.

---

## ✨ The Result Isn't Just a Word

Once the text is analyzed, the interface turns the output into a visual summary.

### Overall Sentiment

```text
        ┌───────────────────┐
        │     POSITIVE      │
        └───────────────────┘
```

or:

```text
        ┌───────────────────┐
        │      NEUTRAL      │
        └───────────────────┘
```

or:

```text
        ┌───────────────────┐
        │     NEGATIVE      │
        └───────────────────┘
```

### Polarity

A visual progress indicator represents the polarity score.

### Subjectivity

Another progress indicator represents the subjectivity score.

### Subjectivity Insight

The interface also gives a simple interpretation:

```text
Subjectivity > 0.7
        │
        ▼
Highly subjective


Subjectivity < 0.3
        │
        ▼
Highly objective


0.3 ───────── 0.7
        │
        ▼
    Balanced
```

So instead of returning raw numbers alone, the application gives the user something easier to interpret.

---

# 🔬 Inside the NLP Engine

The core logic lives inside:

```python
def analyze_sentiment(text):
```

Its workflow is intentionally simple:

```text
                Input Text
                    │
                    ▼
             Is it empty?
              /          \
            Yes           No
             │             │
             ▼             ▼
       Return message   TextBlob
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                Polarity     Subjectivity
                    │             │
                    └──────┬──────┘
                           ▼
                    Apply ±0.15 rule
                           │
                           ▼
                    Structured Result
```

The function returns a Python dictionary containing the analysis:

```python
{
    "text_input": text,
    "sentiment": sentiment_category,
    "polarity": polarity_score,
    "subjectivity": subjectivity_score
}
```

This keeps the actual sentiment-processing logic separate from the Flask route.

---

# 🌐 Where Flask Comes In

Flask isn't performing the sentiment analysis itself.

It acts as the **bridge between the browser and the Python NLP logic**.

The application uses one main route:

```text
/
│
├── GET
│    └── Display the application
│
└── POST
     ├── Receive text_input
     ├── Run analyze_sentiment()
     └── Render result
```

This makes the project a useful example of taking a Python function and exposing it through an interactive web application.

---

# 🧩 A Small Full-Stack Flow

Although this is a compact project, several layers work together:

```text
┌─────────────────────────────┐
│        USER INTERFACE       │
│     HTML + Bootstrap 5      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│           FLASK             │
│     Request / Response      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       PYTHON LOGIC          │
│    analyze_sentiment()      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          TEXTBLOB           │
│     NLP Sentiment Scores    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       JINJA2 TEMPLATE       │
│      Render the result      │
└─────────────────────────────┘
```

That's the interesting part of this project:

**a small NLP function becomes a usable web application.**

---

# 📁 Project Anatomy

```text
sentiment-analyzer-flask/
│
├── 📄 app.py
│
├── 📄 requirements.txt
│
├── 📂 templates/
│   └── 📄 index.html
│
└── 📄 README.md
```

### `app.py`

The heart of the project.

It contains:

* Flask configuration
* sentiment-analysis function
* polarity classification
* subjectivity calculation
* GET/POST route handling

### `templates/index.html`

The browser-facing interface.

It contains:

* text input area
* result card
* sentiment display
* polarity progress bar
* subjectivity progress bar
* subjectivity interpretation

### `requirements.txt`

The Python dependencies required to run the project.

---

# 🛠️ Technology Stack

| Technology         | Purpose                      |
| ------------------ | ---------------------------- |
| 🐍 **Python**      | Core application logic       |
| 🌐 **Flask**       | Web application framework    |
| 🧠 **TextBlob**    | NLP sentiment analysis       |
| 🎨 **Bootstrap 5** | Interface styling and layout |
| 🧩 **Jinja2**      | Dynamic HTML rendering       |
| ⭐ **Font Awesome** | Interface icons              |

---

# 🚀 Get It Running

## 1️⃣ Clone the repository

```bash
git clone https://github.com/taniiishaa/sentiment-analyzer-flask.git
cd sentiment-analyzer-flask
```

## 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Start the application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

And start experimenting with text.

---

# 🧪 Give It Something to Think About

Try different kinds of sentences and compare their scores.

### 💚 Strongly positive

```text
"This is absolutely fantastic!"
```

### ❤️ Strongly negative

```text
"The product was disappointing and the service was terrible."
```

### ⚪ Neutral

```text
"The package arrived on Tuesday."
```

### 🌓 Mixed sentiment

```text
"The product looks great, but the delivery was extremely slow."
```

The interesting part isn't only the final label.

Look at how the **polarity and subjectivity values change** between examples.

---

# 🧹 What Happens With Empty Input?

The application also checks for empty or whitespace-only input.

Instead of trying to analyze nothing, it returns:

```text
Sentiment: Neutral
Polarity: 0.0
Subjectivity: 0.0

Please enter some text to analyze.
```

This is a small but important example of **input validation before processing**.

---

# 🧠 What This Project Taught Me

This project brought together concepts that are often learned independently.

```text
Python
   │
   ▼
NLP
   │
   ▼
Sentiment Analysis
   │
   ▼
Flask Backend
   │
   ▼
Jinja2
   │
   ▼
Interactive Web UI
```

### The bigger lesson?

A Python function doesn't have to stay inside a terminal.

It can become a **web-based tool that someone else can actually interact with.**

That connection between **Python development, backend development, NLP, and frontend presentation** is the main learning milestone behind this project.

---

# ⚠️ The Human-Language Problem

TextBlob is useful for learning and lightweight sentiment analysis, but sentiment isn't always straightforward.

Consider:

```text
"Great, another two-hour meeting."
```

A human might immediately recognize the sarcasm.

A basic sentiment-analysis approach may not.

Language contains:

* sarcasm
* slang
* context
* irony
* mixed opinions
* domain-specific terminology

So the scores generated by this project should be understood as **NLP estimates**, not perfect interpretations of human emotion.

---

# 🔮 Where Could This Go Next?

The current project analyzes **one piece of text at a time**.

A natural evolution would be to turn it into a larger sentiment-analysis workspace:

```text
                   ┌───────────────────┐
                   │   SENTIMENT HUB   │
                   └─────────┬─────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
       Single Text       CSV Upload       Live Data
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                       NLP Processing
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          Positive        Neutral        Negative
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                      Visual Dashboard
```

Possible future additions:

* 📂 CSV review analysis
* 📊 sentiment distribution charts
* 🔎 keyword-level analysis
* 📝 review classification
* 📈 sentiment history
* 🔌 REST API support
* 🤖 transformer-based NLP models
* ☁️ cloud deployment

---

# 🌱 From a Small Script to a Web App

The project started with a simple question:

> **Can Python estimate the emotional direction of a sentence?**

The answer becomes a complete workflow:

```text
        TEXT
         │
         ▼
     TEXTBLOB
         │
    ┌────┴────┐
    ▼         ▼
 POLARITY  SUBJECTIVITY
    │         │
    └────┬────┘
         ▼
   CLASSIFICATION
         │
         ▼
       FLASK
         │
         ▼
    WEB INTERFACE
```

And that's what makes this project valuable as a learning milestone.

It's not just a sentiment classifier.

It's a small demonstration of how **NLP logic can be wrapped inside a backend and transformed into an interactive web experience.**

---

<p align="center">
  <b>🐍 Python · 🌐 Flask · 🧠 NLP · 💬 TextBlob · 🎨 Web Development</b>
</p>
