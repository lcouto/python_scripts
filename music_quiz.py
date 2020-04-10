import requests
import json
import random
import html

endGame = ''

score_correct = 0
score_incorrect = 0

while endGame != 'quit':
    r = requests.get("https://opentdb.com/api.php?amount=5&category=12&difficulty=easy&type=multiple")
    if r.status_code != 200 :
        endGame = input("there was a problem retrieving the question please hit enter to try again or type 'quit' to exit")
    else:
        valid_answer = False
        choice_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        choices = data['results'][0]['incorrect_answers']
        choices.append(data['results'][0]['correct_answer'])
        random.shuffle(choices)
        answer = data['results'][0]['correct_answer']
        print(html.unescape(question) +"\n")
        for choice in choices:
            print(str(choice_number) + " - " + html.unescape(choice))
            choice_number += 1
        while valid_answer == False:
            guess = (input(""))
            try:
                guess = int(guess)
                if guess > len(choices) or guess <= 0:
                    print("invalid answer")
                else:
                    valid_answer = True
            except:
                print("invalid answer, use only numbers")
        if str(choices[int(guess)-1]) == answer:
            print("Correct!")
            score_correct +=1
        else:
            print("Incorrect, the correct answer was: ", answer)
            score_incorrect +=1
        print("\n############################")
        print("Your Score is: ")
        print("Correct: " + str(score_correct))
        print("Incorrect: " + str(score_incorrect))
        print("\n############################")
        endGame = input("press enter to play again or type 'quit' to exit ").lower()
            
print("Thanks for playing!")
