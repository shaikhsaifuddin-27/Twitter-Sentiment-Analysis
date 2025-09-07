🔗 [`Twitter-Sentiment-Analysis`](https://github.com/AlfaizShaikh03/Twitter-Sentiment-Analysis.git)

---

````markdown
# 🐦 Twitter Sentiment Analysis Web App

A lightweight and interactive web application built with **Flask** that performs **sentiment analysis** on user-submitted tweets using **TextBlob**. The app visualizes the sentiment distribution using **bar and pie charts** powered by `matplotlib` and `seaborn`.

---

## 🔍 Features

- ✅ **Sentiment Classification**: Categorizes tweets into **Positive**, **Neutral**, or **Negative** using TextBlob polarity scores.
- 📊 **Visual Output**: Displays the analysis results as both bar and pie charts.
- 💡 **User-Friendly Interface**: Simple web UI using HTML and Jinja2 templating.
- ⚡ **Flash Messaging**: Shows real-time feedback for user inputs and results.
- 🔒 **Secure Input Handling**: Strips and processes multi-line text safely.
- 🖼️ **Static Chart Generation**: Saves visualizations as images for display on the result page.

---

## 📸 Screenshot

![Sentiment Chart](static/results.png)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AlfaizShaikh03/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis
````

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install Flask textblob matplotlib seaborn
python -m textblob.download_corpora
```

### 4. Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🧠 Sentiment Analysis Logic

* **TextBlob** is used to calculate **polarity** of each tweet:

  * `> 0.1` → **Positive**
  * `< -0.1` → **Negative**
  * Between -0.1 and 0.1 → **Neutral**
* Results are aggregated and visualized.

---

## 🛠️ Technologies Used

* **Backend**: Python, Flask
* **NLP**: TextBlob
* **Visualization**: matplotlib, seaborn
* **Frontend**: HTML, CSS (basic), Jinja2

---

## 📂 Project Structure

```
Twitter-Sentiment-Analysis/
│
├── static/
│   └── results.png            # Auto-generated sentiment charts
│
├── templates/
│   └── index.html             # Main UI
│
├── app.py                     # Main Flask application
└── README.md                  # Project documentation
```

---

## ✨ Future Improvements

* Add support for Twitter API to fetch live tweets.
* Include confidence scores or subjectivity analysis.
* Improve chart interactivity using Plotly or Chart.js.

---

## 📬 Contact

Made with ❤️ by [Alfaiz Shaikh](https://github.com/AlfaizShaikh03)
                 [Shaikh Saifuddin](https://github.com/shaikhsaifuddin-27)
                 [Shaikh Mohammed Musa](https://github.com/mohammedmusa1)
                 

