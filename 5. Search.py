def search(text, word):
    if word in text:
        result = f'Word found! "{word}" in "{text}"'
    else:
        result = 'Word not found'
    return result

#text = input("Enter the text: ")
#word = input("Enter the word: ")
text = "Hello There"
word = "Hello"

print(search(text, word))