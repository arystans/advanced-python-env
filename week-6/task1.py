import string

def analyzetext(inputf, outputf):
    wordf = {}
    totall = 0
    totalw = 0

    with open(inputf, "r", encoding="utf-8") as f:
        for line in f:
            totall += 1
            line = line.lower()
            line = line.translate(str.maketrans("", "", string.punctuation))
            n = line.split()

            totalw += len(n)

            for w in n:
                wordf[w] = wordf.get(w, 0) + 1

    with open(outputf, "w", encoding="utf-8") as f:
        f.write(f"Total lines: {totall}\n")
        f.write(f"Total words: {totalw}\n")
        f.write("Word frequencies:\n")
        for w, count in wordf.items():
            f.write(f"{w}: {count}\n")


analyzetext("text.txt", "analysis.txt")
