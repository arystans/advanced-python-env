import string

def analyze_text(input_file, output_file):
    wordf = {}
    totall = 0
    totalw = 0

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            totall += 1
            line = line.lower()
            line = line.translate(str.maketrans("", "", string.punctuation))
            words = line.split()

            totalw += len(words)

            for word in words:
                wordf[word] = wordf.get(word, 0) + 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Total lines: {totall}\n")
        f.write(f"Total words: {totalw}\n")
        f.write("Word frequencies:\n")
        for word, count in wordf.items():
            f.write(f"{word}: {count}\n")


analyze_text("text.txt", "analysis.txt")
