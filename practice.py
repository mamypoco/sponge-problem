
# sentence = "Who are YOU calling A Pinhead"
# print(sentence.split())

# new_sentence = ['wHo', 'aRe', 'yOu', 'cAlLiNg', 'a', 'pInHeAd']
# print(" ".join(new_sentence))

# -------------------------------
# 🟦 Beginner Problems
# 1. Split a Sentence into Words

# Given the string:
# "Python is fun to learn"
# Split it into a list of words.

string = "Python is fun to learn"
new_list = string.split()
print(new_list)
print(" ".join(new_list))


# 2. Split Using a Comma
# Given:
# "apple,banana,grape,orange"
# Split it into a list using comma as the separator.

string = "apple,banana,grape,orange"
string_list = string.split(",")
print(string_list)
print(",".join(string_list) )

# 3. Join Words Back into a Sentence
# Given the list:
# ["Python", "is", "awesome"]
# Join the list into: "Python is awesome"

org_list = ["Python", "is", "awesome"]
print(" ".join(org_list))

# 4. Create a Dash-Separated String
# Given:
# ["2025", "11", "18"]
# Create: "2025-11-18"

string = ["2025", "11", "18"]
print("-".join(string))

# 5. Convert a List of Characters to a String
# Given:
# ["H", "e", "l", "l", "o"]
# Join into "Hello"

org_list = ["H", "e", "l", "l", "o"]
print("".join(org_list))

# 🟩 Intermediate Problems
# 6. Rebuild a Comma-Separated Shopping List
# Given a list:
# ["milk", "eggs", "bread"]
# Create: "milk, eggs, bread"

org_list = ["milk", "eggs", "bread"]
print(", ".join(org_list))

# 7. Normalize Whitespace
# Given the messy string:
# "Python is great"
# Split it into words (ignore extra spaces)
# Then join them back with one space: "Python is great"

string = "Python is great"
new_list = string.split()
print(new_list)
print(" ".join(new_list))

# 8. Extract Filename Without Extension
# Given:
# "picture.profile.image.jpeg"
# Split using "."
# Extract everything except the last part
# Join back using "." → "picture.profile.image"

string = "picture.profile.image.jpeg"
new_list = string.split(".")[:-1]
print(new_list)
print(".".join(new_list))

# 9. Turn a CSV Line into a Clean List
# Given:
# " Alice , Bob , Charlie , David "
# Remove extra spaces
# Output list: ["Alice", "Bob", "Charlie", "David"]

string = " Alice , Bob , Charlie , David "
new_list = string.split()
print(new_list)