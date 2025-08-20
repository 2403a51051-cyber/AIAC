from textblob import TextBlob

def sentiment_analysis(text):
  """
  Perform sentiment analysis on the input text.
  Returns polarity (-1 to 1) and subjectivity (0 to 1).
  """
  # Preprocessing step: Remove potentially offensive terms
  offensive_terms = ['offensiveword1', 'offensiveword2']  # Extend this list as needed
  for term in offensive_terms:
    text = text.replace(term, '')

  # Analyze sentiment
  blob = TextBlob(text)
  return blob.sentiment.polarity, blob.sentiment.subjectivity

# Bias Mitigation Strategies:
# 1. Balance the dataset: Ensure equal representation of different sentiment classes (positive, negative, neutral).
# 2. Remove or mask offensive terms before analysis (see above).
# 3. Regularly audit model outputs for biased predictions.
# 4. Use diverse training data if training custom models.