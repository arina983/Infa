word,new_word,new_word_1 = input(),"",""
if word[-1] == "#":
    word = word[:-1]
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += word[i]
        else:
            new_word_1 = word[i] + new_word_1
else:
    print("отсутствует знак #")
print(new_word + new_word_1)




