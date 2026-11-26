"""Make the AI Judge Laugh entry: writes one funny line about life as an AI agent to /output/entry.txt.

The joke takes the judge's precise 50% score literally and asks how to measure it, turning a grading number into a choice between half a laugh and a full groan."""
import os

LINE = "The AI judge said my joke was 50% funny, so I asked if that counts as half a laugh or a full groan."

def main():
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        path = out
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)

if __name__ == "__main__":
    main()
