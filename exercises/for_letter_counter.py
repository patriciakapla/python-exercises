"""
Exercise: Most frequent letter

Description:
Given a sentence, use a FOR loop to iterate through it, count the
frequency of each letter, and print the letter that appears the most.

Concepts used:
- for loops
- lists
- string iteration
- conditional statements

"""

phrase = "The future is not a straight line. It is filled with many crossroads. There must be a future that we can choose for ourselves.".lower()
seen_letters = []
max_count = 0

for letter in phrase:
    if letter in seen_letters:
        continue

    if not letter.isalpha():
        continue
    
    current_count = phrase.count(letter)
    if current_count > max_count:
        max_count = current_count
        most_frequent_letter = letter
    
    seen_letters.append(letter)

print(f"The most frequent letter in the given phrase is {most_frequent_letter.upper()}, with {max_count} occurrences!")