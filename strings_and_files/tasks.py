test_string = "imie nazwisko"

# Task 1
name, surname = test_string.split()
name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

# Task 2
vowels = ("a", "e", "i", "o", "u", "y")
number_of_vowels = 0
for vowel in vowels:
    number_of_vowels += test_string.count(vowel)
print(number_of_vowels)

number_of_vowels = 0
for letter in test_string:
    if letter in vowels:
        number_of_vowels += 1
print(number_of_vowels)

# Task 3
letters = {}
for letter in test_string:
    if letter in letters:
        letters[letter] += 1
    elif letter != " ":
        letters[letter] = 1
print(letters)
