import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        table = str.maketrans("", "", string.punctuation)
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words_text = []
                for line in file:
                    words_text += line.lower().translate(table).split()
                all_words[name] = words_text
        return all_words

    def find(self, word):
        for i in self.get_all_words().items():
            l_word = word.lower()
            if l_word in i[1]:
                return {i[0]: (i[1].index(l_word) + 1)}

    def count(self, word):
        count_words = 0
        for i in self.get_all_words().items():
            list_words = i[1]
            if word.lower() in list_words:
                for j in range(len(list_words)):
                    if list_words[j] == word.lower():
                        count_words += 1
                return {i[0]: count_words}
