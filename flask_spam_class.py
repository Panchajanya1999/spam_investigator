# disable E0401, C0301
# pylint: disable=E0401 C0301

"""
Spam Classifier main file
"""


import string
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the data and preprocess it
df = pd.read_csv('dataset/spam.tsv', sep='\t', names=['label', 'message'])
df['message'] = df['message'].apply(lambda text: ''.join(char for char in text if char not in string.punctuation))
CV = CountVectorizer(stop_words='english')
X = df['message'].values
y = df['label'].values

# Train the model
X_train_CV = CV.fit_transform(X)
NB = MultinomialNB()
NB.fit(X_train_CV, y)

# Create the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict the status of a message
    """
    data = request.get_json()
    message = data['message']
    message_cv = CV.transform([message])
    prediction = NB.predict(message_cv)[0]
    status = 'SPAM' if prediction == 'spam' else 'HAM'
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)
