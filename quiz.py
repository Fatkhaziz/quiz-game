questions = {
        "Who created Python?: ": "A",
        "What year was Python created?: ": "B",
        "Python is tributed to which comedy group?: ": "C",
        "Is the Earth round?: ": "A"
    }

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

def new_game():
    question_num = 1
    guesses = []
    correct_answers = 0
    for key in questions.keys():
        print(key)
        print("__________")
        for el in options[question_num - 1]:
            print(el)
        print("__________")
        guess = input("select answer (A, B, C, D)").upper()
        while guess not in "ABCD" or guess == '':
            guess = input("Answer is out of range. select answer (A, B, C, D)").upper()
        guesses.append(guess)
        print(guesses)
        correct_answers += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_answers, len(guesses))


def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT')
        return 1
    else:
        print('WRONG')
        return 0


def display_score(correct_ans, guesses):
    total = (correct_ans / guesses) * 100
    print("your total score is:", total, "%")


def admin_mode():
    while True:
        change_mode = input("press 'space' three times to get access to the admin mode")
        if change_mode == "   ":
            print("You are in admin mode now!")
            choice = input("Create a new question? (YES or NO)").upper()
            if choice != "YES" and choice != "NO":
                print("Enter only YES or NO")
            elif choice == "YES":
                new_question = input("Enter the new question:").upper()
                new_options = []
                options_abcd = "ABCD"
                for i in range(4):
                    new_option = input("Enter the new option:")
                    new_options.append(options_abcd[i] + ". " + new_option)
                options.append(new_options)
                while True:
                    option_for_new_question = input(
                        "Enter the correct option for new question (A, B, C, D):").upper()
                    if option_for_new_question != "A" and option_for_new_question != "B" and option_for_new_question != "C" and option_for_new_question != "D":
                        print("Enter only A, B, C, D")
                    else:
                        break
                questions.setdefault(new_question, option_for_new_question.upper())
            else:
                print("Bye")
                break
        

def play_again():
    response = input("Do you want to play?: (yes, no or enter admin mode)").upper()
    if response == "YES":
        return True
    elif response == "NO":
        return False
    elif response == "ADMIN MODE":
        return admin_mode()



def main():
    while play_again():
        new_game()
    print("Bye Bye")


main()
