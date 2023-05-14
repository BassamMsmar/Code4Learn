
'''
Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)
'''


sentence = str(input("Enter your sentence : "))


def word_counter(sentence):
   
    list_words = sentence.split()
    print(len(list_words))


word_counter(sentence)