import fon

word=input("Please tayp your word: ")
k=int(input('Please type your key: '))
new_word=fon.encrypt(word,k)
print(new_word)
word=fon.encrypt_bar(new_word,k)
print(word)


