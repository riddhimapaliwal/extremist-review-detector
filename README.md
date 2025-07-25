# 🧠 Extremist Reviewer Group Detection in Amazon Reviews

A web-based system to detect and characterize extremist reviewer groups in online product reviews. This work is inspired by the paper:

> **Detecting and Characterizing Extremist Reviewer Groups in Online Product Reviews**  
> Viresh Gupta, Aayush Aggarwal, and Tanmoy Chakraborty  
> *Accepted in IEEE Transactions on Computational Social Systems*

---

## 📘 Abstract

Online marketplaces like Amazon often suffer from *opinion spam* — where coordinated reviewer groups post biased reviews (extremely positive or negative) to influence customer perception. This project implements a system that detects such **extremist reviewers**, based on machine learning models trained on Amazon reviews.

---

## 🚀 Features

- 📂 Upload review datasets (CSV format)
- 🧮 Train Naive Bayes classifier on review text
- 🧠 Predict if a new review is from an extremist or moderate reviewer
- 📊 Chart pages and preview options
- 🌐 Web interface built with Flask (Python)

---

## 🏗️ System Architecture

- **Frontend**: HTML + Bootstrap (via Flask templates)
- **Backend**: Flask (Python), Pandas, Scikit-learn
- **ML Model**: Naive Bayes (MultinomialNB)
- **Dataset**: Amazon product reviews manually labeled (`amazon.csv`)

---

## 📁 Project Structure

📁 Project Structure
source code/
├── app.py             # Main Flask application
├── amazon.csv         # Labeled dataset
├── templates/         # HTML templates (index.html, home.html, etc.)
├── static/            # Static assets (CSS/JS/images)
├── requirements.txt   # Python libraries
├── README.md          # Project documentation



## ⚙️ Installation Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/riddhimapaliwal/extremist-review-detector.git
cd extremist-review-detector
Step 2: Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Run the Application
bash
Copy
Edit
python app.py
Then visit your app in the browser




👩‍💻 Developed By
Riddhima Paliwal


📌 Notes
amazon.csv should be placed in the project directory

All predictions are made in real time using the trained model

You can extend this to visualize charts or graphs from reviewer behavior
