def search(text, word, count):
    lst = list(text.split(" "))
    
    if word in lst:
        result = f"Word found! '{word}'' in '{text}'"
        for i in lst:
            if i == word:
                count += 1
    else:
        result = "Word not found!"
    print(f'Instances: {count}')
    return result

#text = input("Enter the text: ")
#word = input("Enter the word: ")
text = "Dharmik Says Hello there"
word = "Hello"
count = 0
lst = []
print(search(text, word, count))
