from flask import Flask, render_template, url_for, request
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib

app = Flask(__name__)

@app.route('/')
@app.route('/index') 
def index():
    return render_template('index.html')

@app.route('/login') 
def login():
    return render_template('login.html')    

@app.route('/abstract') 
def abstract():
    return render_template('abstract.html') 
 
@app.route('/future') 
def future():
    return render_template('future.html')    

@app.route('/chart') 
def chart():
    return render_template('chart.html')     

@app.route('/upload') 
def upload():
    return render_template('upload.html') 

@app.route('/preview', methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset, encoding='unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html", df_view=df)    

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load dataset
    df = pd.read_csv("F:/JPPY2011-Detecting and Characterizing Extremist Reviewer/SOURCE CODE/product_review/amazon.csv", encoding="latin-1")
    X = df['REVIEW_TEXT']
    y = df['LABEL']

    # Feature Extraction
    cv = CountVectorizer()
    X = cv.fit_transform(X)

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Train Model
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # Prediction
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        prediction = clf.predict(vect)

        if prediction[0] == "__label1__":
            label = "extremist"
        elif prediction[0] == "__label2__":
            label = "moderate"
        else:
            label = "unknown"

    return render_template('home.html', prediction=label)

@app.route('/chart1') 
def chart1():
    return render_template('chart1.html')     

@app.route('/uploads') 
def uploads():
    return render_template('uploads.html') 

@app.route('/previews', methods=["POST"])
def previews():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset, encoding='unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("previews.html", df_view=df) 

@app.route('/chart2') 
def chart2():
    return render_template('chart2.html') 

# ✅ THIS MUST BE AT THE END!
if __name__ == '__main__':
    print("Flask app is starting...")  # Optional debug message
    app.run(debug=True)
