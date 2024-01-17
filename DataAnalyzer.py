import re
from textblob import TextBlob
import nltk
from matplotlib import pyplot as plt
import string


class DataAnalyzer:
    def __init__(self, script, file_path):
        self.script = script
        self.file_path = file_path

    @staticmethod
    def basic_clean(script):
        pattern = re.compile(r'<(/?b|/?pre)>|CUT TO:|EXT\..*|INT\..*|\([^)]*\)|[012345789]|.*&amp.*|.*Written by.*\n?',
                             re.MULTILINE)
        modified_script = re.sub(pattern, '', script)
        return modified_script

    def prepare_for_nlp(self):
        script = self.basic_clean(self.script)
        return script

    def get_overall_sentiment(self):
        script = self.basic_clean(self.script)
        script_blob = TextBlob(script)
        return script_blob.sentiment

    def plot_sentiment_over_time(self):
        script = self.prepare_for_nlp()
        script_count = len(nltk.word_tokenize(script))
        total_points = 20
        part_size = script_count // total_points  # Divide the script into 100 parts
        sentiments = []
        for i in range(0, script_count, part_size):
            part_script = script[i:i + part_size]
            part_blob = TextBlob(part_script)
            sentiments.append(part_blob.sentiment.polarity)
        # Ensure sentiments has exactly 100 elements
        # Plotting sentiment over time
        plt.plot(range(1, total_points + 2), sentiments, marker='o')
        plt.xlabel('Script Parts')
        plt.ylabel('Sentiment Polarity')
        plt.xticks(range(1, total_points + 1))
        plt.title('Sentiment Analysis Over Time')
        plt.show()

    def prepare_for_word_analysis(self):
        script = self.prepare_for_nlp()
        script = ''.join(char.lower() for char in script if char not in string.punctuation)
        words = nltk.word_tokenize(script)
        return words

    def word_count(self):
        return len(self.prepare_for_word_analysis())

    def count_word(self, match):
        script_list = self.prepare_for_word_analysis()
        count = 0
        for x in script_list:
            if match.lower() == x.lower():
                count += 1
        return count
