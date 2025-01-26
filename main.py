def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dictionary_book = get_dictionary_book(text)
    report = get_report_book(dictionary_book, text)
    print(report)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_dictionary_book(text):
    words = text.lower()
    dictionary_book = {}
    for word in words:
        for i in range(0, len(word)):
            letter = word[i]
            dictionary_book[letter] = dictionary_book.get(letter, 0) + 1

    return dictionary_book

def sort_on(dict):
    return dict[""]

def get_report_book(dictionary_book, text):
    dict_list = []
    report = []
    words = text.split()

    for key, value in dictionary_book.items():
        dict_list.append({ 'char': key, 'num': value })

    filtered_list = [item for item in dict_list if item['char'].isalpha()]
    filtered_list.sort(reverse=True, key=lambda item: item['num'])

    report.append('--- Begin report of books/frankenstein.txt ---')
    report.append(f'{len(words)} unique characters found in the document')
    for item in filtered_list:
        char = item['char']
        num = item['num']
        report.append(f"The '{char}' character was found {num} times")
    report.append('--- End report ---')
    return '\n'.join(report)
    

main()
