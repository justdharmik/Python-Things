def search(text, word, count):
    lst = list(text.split(" "))
    for i in lst:
        if i == word:
            result = f'Word found! " {word}" in " {text}"'
            count = count + 1
        else:
            result = 'Word not found'
    print(f'Instances: {count}')
    return result

#text = input("Enter the text: ")
#word = input("Enter the word: ")
text = "Hello There Hello"
word = "Hello"
count = 0
lst = []
print(search(text, word, count))
