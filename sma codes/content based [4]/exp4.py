import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob

# Load the dataset
df = pd.read_csv('synthetic_social_media_data.csv')
# Display basic info and first few rows
print(df.info())

print(df.head())
# Predefined list of stopwords
custom_stopwords = set([
 "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
"your", "yours", "yourself",
 "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
"herself", "it", "its", "itself",
 "they", "them", "their", "theirs", "themselves", "what", "which",
"who", "whom", "this", "that",
 "these", "those", "am", "is", "are", "was", "were", "be", "been",
"being", "have", "has", "had",
 "having", "do", "does", "did", "doing", "a", "an", "the", "and",
"but", "if", "or", "because",
 "as", "until", "while", "of", "at", "by", "for", "with", "about",
"against", "between", "into",
 "through", "during", "before", "after", "above", "below", "to",
"from", "up", "down", "in", "out",
 "on", "off", "over", "under", "again", "further", "then", "once",
"here", "there", "when", "where",
 "why", "how", "all", "any", "both", "each", "few", "more", "most",
"other", "some", "such", "no",
 "nor", "not", "only", "own", "same", "so", "than", "too", "very",
"s", "t", "can", "will", "just",
 "don", "should", "now"
])

def preprocess_text(text):
    """Cleans and preprocesses text data."""
    text = text.lower() # Convert to lowercase
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r"[^\w\s]", "", text) # Remove punctuation
    text = re.sub(r"\d+", "", text) # Remove numbers
    text = " ".join([word for word in text.split() if word not in custom_stopwords]) # Remove stopwords
    
    return text

# Apply preprocessing to "Post Content"
df["Cleaned Post Content"] = df["Post Content"].astype(str).apply(preprocess_text)

# Generate Word Cloud
text_corpus = " ".join(df["Cleaned Post Content"])
wordcloud = WordCloud(width=800, height=400,
background_color="white").generate(text_corpus)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.title("Word Cloud of Social Media Posts", fontsize=14)
plt.show()

# Function for sentiment analysis
def get_sentiment(text):
    """Classifies text sentiment as Positive, Neutral, or Negative."""
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# # Apply sentiment analysis
# df["Sentiment"] = df["Cleaned Post Content"].apply(get_sentiment)

# Plot sentiment distribution
plt.figure(figsize=(6, 4))
df["Sentiment Label"].value_counts().plot(kind="bar", color=["green", "blue","red"])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")

plt.ylabel("Count")
plt.show()

# Save the updated dataset with sentiment labels
df.to_csv("processed_social_media_data.csv", index=False)
print("Processing complete! Sentiment analysis results saved.")