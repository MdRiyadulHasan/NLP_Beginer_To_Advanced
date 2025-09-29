import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (first time only)
nltk.download('punkt')
nltk.download('stopwords')

# Example dataset in a DataFrame
data = {
    "id": [1, 2, 3, 4],
    "text": [
        "This is the first document.",
        "Natural Language Processing is amazing for text analysis!",
        "Stop words should be removed before training a model.",
        "Sometimes stop words are important in sentiment analysis."
    ]
}

df = pd.DataFrame(data)

# English stop words
stop_words = set(stopwords.words('english'))

# Function to clean text
def remove_stopwords(text):
    words = word_tokenize(text)
    filtered = [w for w in words if w.lower() not in stop_words]
    return " ".join(filtered)

# Apply stopword removal to 'text' column
df["cleaned_text"] = df["text"].apply(remove_stopwords)

# Show results
print(df)
