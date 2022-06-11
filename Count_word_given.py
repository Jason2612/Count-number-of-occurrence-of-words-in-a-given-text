def count_words(input_text):
    num_words = dict()
    words = input_text.split()
    
    for word in words:
        if word in num_words:
            num_words[word] += 1
        else:
            num_words[word] = 1
    
    return num_words

test = count_words("Hi my name is Phong")
print(test)




   