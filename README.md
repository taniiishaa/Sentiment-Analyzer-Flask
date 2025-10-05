# Realtime Sentiment Analyzer: Flask & NLP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-lightgray)](https://flask.palletsprojects.com/)

**Repository Description (Set this in GitHub's settings):** A production-ready Full-Stack web application built with Python Flask and the TextBlob library for real-time natural language sentiment analysis, featuring professional data visualization and a responsive UI.

## 💡 Project Goal & Technical Highlights
The objective of this project was to build a robust, reproducible system that not only classifies text sentiment but also clearly explains the numerical basis of that classification.

* **Full-Stack Integration:** Seamlessly connects Python **Flask** (backend) for business logic with a responsive HTML/CSS/**Bootstrap 5** frontend, demonstrating full-stack capability.
* **Nuanced NLP Logic:** Implements a custom threshold in the Python logic for the neutral range ($|\text{Polarity}| \le 0.15$), demonstrating a realistic and nuanced approach to sentiment categorization beyond simple positive/negative binary checks.
* **Data Visualization Focus:** Leverages dynamic **Jinja templating** to render **color-coded results cards and progress bars**, transforming raw scores into immediate, executive-level insights.
* **Modular Architecture:** Sentiment logic is isolated in a clear, easy-to-read Python function, promoting **clean code** and **testability**.

## ⚙️ Tech Stack

| Component | Technology | Role in Project |
| :--- | :--- | :--- |
| **Backend Framework** | `Flask` | Routing, request handling, and serving Jinja templates. |
| **Core NLP Library** | `TextBlob` | Used for calculating polarity and subjectivity scores. |
| **Frontend Styling** | `Bootstrap 5` | Ensures a professional, responsive, and mobile-friendly user interface. |
| **Templating Engine** | `Jinja2` | Used for injecting dynamic data (scores, sentiment category, input text) into the HTML structure. |

## 📑 Process Summary

1.  **Environment Setup:** Created an isolated Python virtual environment (`venv`) to prevent dependency conflicts and ensure project portability.
2.  **Back-end Logic Development:** Wrote the core Flask application (`app.py`), defining the necessary routes (`/` for `GET` and `POST` requests).
3.  **NLP Implementation:** Integrated the `TextBlob` library and defined the custom logic to convert the raw floating-point polarity score into one of three distinct categories: 'Positive', 'Negative', or 'Neutral'.
4.  **Front-end Design:** Developed a single, cohesive template (`templates/index.html`) using **Bootstrap 5** for a professional and adaptive layout.
5.  **Data Presentation Layer:** Used **Jinja templating** to inject analysis results into the HTML, dynamically updating UI elements (e.g., changing card background colors and setting progress bar widths) based on the computed scores.

## 📊 Understanding the Output

The application provides two key numerical metrics visualized in the final result card:

1.  **Polarity Score (Range: $[-1.0, 1.0]$):**
    * Measures the emotional charge of the text.
    * $-1.0$ is the most negative, $1.0$ is the most positive, and $0.0$ is perfectly neutral.
    * *Visualization:* Represented by a progress bar showing the magnitude of the score, color-coded for direction (Red/Danger for Negative, Green/Success for Positive).

2.  **Subjectivity Score (Range: $[0.0, 1.0]$):**
    * Measures how much the text is based on personal opinion versus objective fact.
    * $1.0$ is highly subjective (opinion-based); $0.0$ is highly objective (fact-based).
    * *Visualization:* Represented by a blue progress bar showing the percentage of subjectivity.

## 📦 Getting Started Locally

### Prerequisites

You must have Python 3.9+ installed on your system.

### Installation & Setup

1.  **Clone the repository and navigate into the directory:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your Username]/flask-sentiment-analyzer-nlp.git
    cd flask-sentiment-analyzer-nlp
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate # Use `.\venv\Scripts\activate` on Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    
    # TextBlob requires downloading language data
    python -m textblob.download_corpora
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    The web application will be accessible at `http://127.0.0.1:5000/`.
