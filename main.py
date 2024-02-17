import re

pattern = re.compile("love")
with open('./files/miracle_in_the_andes.txt', 'r') as file:
    search_words = ["love"]
    book = file.read()
    sentences = book.split(".")
    for sentence in sentences:
        if any(re.search(rf"\b{search_word}\b", sentence, re.IGNORECASE) for search_word in search_words):
            print(len(sentence))



pattern_two = re.compile("[A-Z]{1}[^.]* love[^a-zA-Z][^.]*.")
with open("./files/miracle_in_the_andes.txt", "r") as file:
    book = file.read()
    findings = re.findall(pattern_two, book)
    print(len(findings))


def find_most_common_word(file_path):
    word_counter = {}  # Initialize an empty dictionary

    with open(file_path, 'r') as file:
        book = file.read()
        pattern = re.compile("[a-zA-Z]+")
        words_list = re.findall(pattern, book.lower())
        for word in words_list:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

    # Find the word(s) with the highest count
    max_count = max(word_counter.values())
    most_common_words = [word for word, count in word_counter.items() if count == max_count]

    return most_common_words

# Example usage
file_path = './files/miracle_in_the_andes.txt'
most_common_words = find_most_common_word(file_path)
print(f"The most common word(s) in the file: {', '.join(most_common_words)}")


def find_chapter_title(file_path):
    pattern = re.compile("([a-zA-Z ]+)\n\n")
    with open(file_path, 'r') as file:
        book = file.read()
        findings = re.findall(pattern, book)
        print(findings)

find_chapter_title("./files/miracle_in_the_andes.txt")



def count_term_occurrences(filename, search_term):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            occurrences = re.findall(rf'\b{re.escape(search_term)}\b', content, flags=re.IGNORECASE)
            if len(occurrences) != 0:
                # return len(occurrences)
                return f"Occurrences of '{search_term}' in '{filename}': {len(occurrences)}"
            else:
                return f"Sorry the word '{search_term}' is not in the book"
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Example usage
if __name__ == "__main__":
    filename = "./files/miracle_in_the_andes.txt"  # Replace with the actual file path
    term_to_search = "china"

    term_count = count_term_occurrences(filename, term_to_search)
    print(term_count)