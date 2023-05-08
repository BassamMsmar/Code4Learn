'''
7. Create a function takes a sentence and a word and prints how many time the word used in the sentence
'''



sentence = str(input("Enter your sentence : "))
word = str(input("Enter your word to remove from sentence : ")) 



def words_counter(sentence, word):
    word_counter = 0
   
    for words in sentence.split():
        if words == word:
            word_counter += 1
        

    print(word_counter)




words_counter(sentence, word)