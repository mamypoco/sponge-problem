# 10. Reformat Date

# Given:
# "2025/11/18"
# Convert to: "18-11-2025"

mydate = "2025/11/18"
mydate_list = mydate.split("/")
print("-".join(mydate_list))


# 🟥 Advanced Problems
# 11. Reverse Each Word in a Sentence
# Given:
# "Python makes coding enjoyable"

sentense = "Python makes coding enjoyable"
reversed = ""
for i in range(len(sentense) - 1, -1, -1):
  reversed += sentense[i]
print(reversed)

# Split into words
sentense_list = reversed.split()
print(sentense_list)

# Reverse each word
reversed_words = []
for word in range(len(sentense_list) - 1, -1, -1):
  reversed_words.append(sentense_list[word])
print(reversed_words)

# Join back: "nohtyP sekam gnidoc elbayojne"
print(" ".join(reversed_words))

# 12. Word Frequency (Simple)
# Given:
# "apple banana apple grape banana apple"
fruits = "apple banana apple grape banana apple"

# Split into words
fruits_list = fruits.split()
print(fruits_list)
# Create a list of "word:count" strings
# Example: ["apple:3", "banana:2", "grape:1"]

# ['apple', 'banana', 'apple', 'grape', 'banana', 'apple']
names_list = []
counts_list = []

for fruit in fruits_list:
  if fruit in names_list:
    index = names_list.index(fruit)
    counts_list[index] += 1
  else:
    names_list.append(fruit)
    counts_list.append(1)

result = []
for i in range(len(names_list)):
  result.append(f"{names_list[i]}:{counts_list[i]}")
print(result)

# Join with comma: "apple:3, banana:2, grape:1"
print(", ".join(result))

# 13. Convert a Sentence into a URL-Slug
# Given:
# "React Native is Fun!"

# Lowercase

# Remove !

# Replace spaces with -
# → "react-native-is-fun"

sentense_react = "React Native is Fun!"
print(sentense_react[:-1])
print(sentense_react.strip("!"))
print(sentense_react.replace("!", ""))



# 14. Split Email Address into Username and Domain
# Given:
# "mami.nishiwaki@example.com"
# # Output list: ["mami.nishiwaki", "example.com"]

email = "mami.nishiwaki@example.com"
print(email.split("@"))


# 15. Parse and Rebuild Key-Value Pairs
# Given:
# "name=Alice;age=30;city=Tokyo"
# Split into pairs
# Turn into list:
# ["name: Alice", "age: 30", "city: Tokyo"]

person = "name=Alice;age=30;city=Tokyo"
print(person.replace("=", ":").split(";"))






# Join using " | "
# → "name: Alice | age: 30 | city: Tokyo"