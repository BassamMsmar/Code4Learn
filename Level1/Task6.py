
'''
Create a function that takes a sentence and word and remove the word from the sentence
'''

sentence = str(input("Enter your sentence : "))
word = str(input("Enter your word to remove from sentence : ")) 

new_sentence = []


def remove_word_from_sentence(sentence, word):
   
    for words in sentence.split():
        if words == word:
            continue
        else:
            new_sentence.append(words)

    print(' '.join(new_sentence))



remove_word_from_sentence(sentence, word)