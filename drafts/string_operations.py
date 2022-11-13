test_text = "ala ma kota\n\t"
print(test_text)

words = test_text.split()
print(words)

stripped_text = test_text.strip()
print(stripped_text)

replaced_text = test_text.replace(" ", "-")
print(replaced_text)

joined_text = ""
for word in words:
    joined_text += word + " "  # joined_text = joined_text + word
print(joined_text)

joined_text2 = "$$$".join(words)
print(joined_text2)

print(test_text.upper())
print(test_text.lower())
print(test_text.capitalize())
