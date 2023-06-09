import random
import string

                        
def main():
    question_1 = question().upper()
    i = 1
    list = []

    while i<7:
        print(f"CHANCE {i}/ TYPE 'IQUIT' IF YOU ARE WEAK.")
        guess_1 = answer()

        if guess_1 =='IQUIT':
            print("************************************************")
            break    

        #TO MAKE SURE NO GUESS IS BEING REPEATED.
        elif guess_1 not in list:     
            list.append(guess_1)

            #CALLING THE FUNCTIONS TO PRINT ON CMD
            correct(guess_1,question_1)
            misplaced_letter(guess_1, question_1)
            wrong_option(guess_1, question_1)

            #WHEN THE GUESS IS CORRECT
            if guess_1 == question_1:
                print("************************************************")
                print(f"CONGRATULATIONS!!! IT TOOK YOU {i} TURN TO GUESS THE WORD.")
                print("************************************************")
                quit()
            i+=1

        else:
            print("You have already gussed this word.")

        print("************************************************")
    print(f"The correct word was {question_1}")


     #WORD TO GUESS
def question():
    with open("words.txt") as file:
        files = file.read().split('\n')
        word = random.choice(files)
        return word
    

def answer():   #GETTING THE USERS INPUT
    while True:
        guess =input("GUESS: ").upper()
        digit = list(map(lambda x:x.isdigit(), guess)) 
        punct = list(map(lambda x: x in string.punctuation,guess))

        if len(guess) != 5:
            print("The input should be of 5 letters.")
            print("************************************************")
        elif True in digit:
            print("The input should not contain any numbers.")
            print("************************************************")
        elif True in punct:
            print("The input should not contain any punctuation letters.")
            print("************************************************")           
        else:
            return guess


def correct(guess,word): #CHECKING WHICH LETTERS ARE PLACED IN CORRECT POSIITON
    print("CORRECT LETTERS: ",end='')
    for i in range(5):                                          #for i,j in zip(word,guess):
        if word[i] == guess[i]:                                 #    if word == guess:
            print(f"{word[i]} in {i+1} positon, ",end='')       #        print(f"{i} is in  positon, ",end='')
    print('')


#DISPLAYS CHARACTER WHICH ARE RIGHT BUT NOT IN CORRECT POSITION
def misplaced_letter(guess,word):    
    #CREATING A LIST OF INCORRECT WORDS
    new_option = []
    for i in range(5):
        if word[i] != guess[i]:
            new_option.append(guess[i])

    print("MISPLACED LETTERS: ",end='')
    for j in set(new_option):
        for k in range(5):
            if j == word[k] and word[k] != guess[k]:
                print(f"{j}, ",end='')
    print('')

            
def wrong_option(guess,word):    #DISPLAYS WRONG LETTERS

    print("WRONG LETTERS: ",end='')
    for i in range(5):
        if guess[i] not in word:
            print(f"{guess[i]}",end='')
    print('')


if __name__ == "__main__":
    main()
