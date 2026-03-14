"""
Exercise: Most frequent letter

Description:
Given a sentence, use a while loop to iterate through it, count the
frequency of each letter, and print the letter that appears the most.

Concepts used:
- while loops
- dictionaries
- string iteration
"""

phrase = "The future is not a straight line. It is filled with many crossroads. There must be a future that we can choose for ourselves.".lower()
i = 0
max_count = 0
counted_letters = []

while i < len(phrase):
    letter = phrase[i]
    if not letter.isalpha():
        i += 1
        continue

    current_count = phrase.count(letter)
    if letter in counted_letters:
        i += 1
        continue

    if current_count > max_count:
        most_frequent_letter = letter
        max_count = current_count

    counted_letters.append(letter)
    i += 1

print(f"The most frequent letter in the given phrase is {most_frequent_letter.upper()}, with {max_count} occurrences!")