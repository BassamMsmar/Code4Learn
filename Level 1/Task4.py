
'''
4 - Create a function that takes a sentence and prints the sentence without duplicated words
'''

sentence = str(input("Enter your sentence : "))
modified_sentence = []

def print_sentence(sentence):
   
    for word in sentence.split():
        if word not in modified_sentence:
            modified_sentence.append(word)

    print(' '.join(modified_sentence))


print_sentence(sentence)