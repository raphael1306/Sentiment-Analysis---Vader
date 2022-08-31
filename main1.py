from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import nltk
nltk.download('vader_lexicon')

sentences = ["yaun is good"]

comments = [" yuan is so bad "]
           
for i in range(len(sentences)):
    vs = analyzer.polarity_scores(sentences[i])
    print("{:-<65} {:-<65} {}".format(sentences[i], comments[i], str(vs)))
