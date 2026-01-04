def sponge_case(sentence):
    # Should return "wHo aRe yOu cAlLiNg a pInHeAd"
  sentence_list = sentence.split()
  print("sentence_list:", sentence_list)

  new_sentence = []
  sponge_word = ""

  for word in sentence_list:
    sponge_word = ""
    for char in range(len(word)):
      if char % 2 == 0:
        new_char = word[char].lower() 
      else:
        new_char = word[char].upper()
      sponge_word += new_char
    new_sentence.append(sponge_word)
  print(new_sentence)

  return " ".join(new_sentence)

sentence = "Who are YOU calling A Pinhead"
print(sponge_case(sentence))