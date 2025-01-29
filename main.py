def count_letters(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def print_report(letter_count):
    for letter, count in letter_count.items():
        print(f"The '{letter}' character was found {count} times")

def main():
    with open("books/frankenstein.txt") as file:
      file_contents = file.read()
    word_count = len(file_contents.split())
    letter_count = count_letters(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"'{word_count}' words found in the document")
    print_report(letter_count)
main()