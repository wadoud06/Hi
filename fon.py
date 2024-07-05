import string 

def encrypt(word,k):
 new_word=""
 for letter in word:
  if letter in string.ascii_letters:
    new_word+=string.ascii_letters[(string.ascii_letters.index(letter)+k)%52]
  else:
    new_word+=letter
 print("the encode word is: ")
 return new_word

 
  
def encrypt_bar(new_word,k):
 word=""
 for letter in new_word:
  if letter in string.ascii_letters:
    word+=string.ascii_letters[(string.ascii_letters.index(letter)-k)%52]
  else:
    new_word+=letter
 print("the word is: ")
 return word
  
