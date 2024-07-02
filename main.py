
def generate_report(path: str, word_count: int, character_counts: dict) -> None:
    print(f"--- Begin Report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for letter in character_counts:
        if letter.isalpha():
            print(f"The '{letter}' character was found {character_counts[letter]} times")

def get_character_count(text: str) -> dict:
    character_count = {}
    for letter in text:
        if letter.lower() in character_count:
            character_count[letter.lower()] += 1
        else:
            character_count[letter.lower()] = 1
    
    return character_count

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    path = "books/frankenstein.txt"
    with open(path, "r") as f:
        file_contents = f.read()
        print(file_contents)

    word_count = get_word_count(file_contents)
    character_counts = get_character_count(file_contents)
    generate_report(path, word_count, character_counts)


if __name__ == "__main__":
    main()

