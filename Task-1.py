import re

def analyze_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_freq = {}
    word_count = 0

    for line in lines:
        words = re.findall(r"[a-zA-Z0-9]+", line.lower())
        word_count += len(words)

        for w in words:
            word_freq[w] = word_freq.get(w, 0) + 1

    with open(output_file, "w", encoding="utf-8") as result:
        result.write(f"Total lines: {line_count}\n")
        result.write(f"Total words: {word_count}\n")
        result.write("Word frequency:\n")

        for word in word_freq:
            result.write(f"{word} - {word_freq[word]}\n")


if __name__ == "__main__":
    analyze_file("text.txt", "analysis.txt")
