import re
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
english_stopwords = stopwords.words('english')

with open('./files/miracle_in_the_andes.txt', 'r') as file:
    book = file.read()


    def find_most_common_word(file_path):
        word_counter = {}  # Initialize an empty dictionary
        filtered_words = {}
        with open(file_path, 'r') as file:
            book = file.read()
            pattern = re.compile("[a-zA-Z]+")
            words_list = re.findall(pattern, book.lower())
            for word in words_list:
                if word not in word_counter:
                    word_counter[word] = 1
                else:
                    word_counter[word] += 1

        for key, value in word_counter.items():
            if key not in english_stopwords:
                filtered_words[key] = value
        # Find the word(s) with the highest count
        max_count = max(filtered_words.values())
        most_common_words = [word for word, count in filtered_words.items() if count == max_count]

        return most_common_words

# Example usage
file_path = './files/miracle_in_the_andes.txt'
most_common_words = find_most_common_word(file_path)
print(f"The most common word(s) in the file: {', '.join(most_common_words)}")

analyzer = SentimentIntensityAnalyzer()

def find_chapter_content():
    with open('./files/miracle_in_the_andes.txt', 'r') as file:
        book = file.read()
        chapter_pattern = re.compile('Chapter [0-9]+')
        chapters = re.split(chapter_pattern, book)
        chapters = chapters[1:]

        for index, chapter in enumerate(chapters):
            scores = analyzer.polarity_scores(chapter)
            max_positivity = max(scores['pos'])
            print(f'Chapter {index + 1 } has {scores}', max_positivity)
        

result = find_chapter_content()
