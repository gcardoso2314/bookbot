BOOK_REPORT_TEMPLATE = """
--- Begin report of {file_path} ---
{num_words} words found in the document

{char_stats}
--- End report ---
"""


def read_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def count_words(file_content: str) -> int:
    return len(file_content.split())


def count_characters(file_content: str) -> dict[str, int]:
    char_count = {}
    for char in file_content:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count


def create_book_report(file_path: str) -> None:
    file_content = read_file("books/frankenstein.txt")

    num_words = count_words(file_content)

    char_count = count_characters(file_content)
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    char_stats = [
        f"The {char} character was found {val} times"
        for char, val in sorted_char_count
        if char.isalpha()
    ]

    print(
        BOOK_REPORT_TEMPLATE.format(
            file_path=file_path, num_words=num_words, char_stats="\n".join(char_stats)
        )
    )


def main():
    create_book_report("books/frankenstein.txt")


if __name__ == "__main__":
    main()
