def search(text, word):
    if word in text:
        result = 'Word found'
    else:
        result = 'Word not found'
    return result

text = input()
word = input()

print(search(text, word))