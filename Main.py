"""
Author: David Anderson
File: Main.py

Purpose: This is a really short and crude way of seeing if an exact sentence is found
in a source text file. It reads from a Wikipedia entry about the novel "Moby Dick" and scans
for the selected sentence.
"""


# This function searches for a sentence within a larger text file
# @param f is the source file to be searched
# @param sentence is the sentence we are looking for
def find_text(f, sentence):
    for line in f.readlines():
        if sentence in line:
            print("Plagiarism found!")
            return

    print("This sentence is original.")


file = open("test.txt", "r+")  # this assumes test.txt is in the root directory
quote = "Melville began writing Moby-Dick in February 1850, " \
        "and finished 18 months later, a year longer than he had anticipated."

# changed "began writing" to "wrote"
changedSentence = "Melville wrote Moby-Dick in February 1850, " \
                  "and finished 18 months later, a year longer than he had anticipated."

# Temporary test cases
print("Should find plagiarism: ")
find_text(file, quote)
print()
print("Should say original: ")
find_text(file, changedSentence)
