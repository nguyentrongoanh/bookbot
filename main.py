def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = convert_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)

    print(f" --- Begin report of {book_path} ---")
    print(f"{num_words} was found in the document\n")

    for i in chars_list:
        name = i["character"]
        time = i["times"]

        print(f"The '{name}' characters was found {time}")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def convert_list(dict):
    chars_list = []
    for key in dict:
        converted = {}
        if key.isalpha():
            converted["character"] = key
            converted["times"] = dict[key]
            chars_list.append(converted)

    return chars_list


def sort_on(dict):
    return dict["times"]


main()
