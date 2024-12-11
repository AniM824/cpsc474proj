import random

my_file = open("words.txt", "r") 
data = my_file.read() 
words_list = data.split("\n") 

def generate_feedback(guess, target):
    feedback = ["","","","",""]
    target_counts = {}

    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1

    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback[i] = "green"
            target_counts[guess[i]] -= 1

    for i in range(len(guess)):
        if feedback[i] == "":
            if guess[i] in target_counts and target_counts[guess[i]] > 0:
                feedback[i] = "yellow"
                target_counts[guess[i]] -= 1 
            else:
                feedback[i] = "black"

    return feedback


def play_game():
    feedback_history = []
    res = [None, None]

    target_list = words_list
    answer1 = random.choice(words_list)
    answer2 = random.choice(words_list)
    # print("ans: " + answer1)
    # print("ans: " + answer2)
    for i in range(7):
        best_guess = random.choice(target_list)
        # print("turn " + str(i + 1) + " " + best_guess)

        if best_guess == answer1:
            # print("FINISHED WORD 1 IN " + str(i + 1) + " TURNS")
            res[0] = i + 1

        if best_guess == answer2:
            # print("FINISHED WORD 2 IN " + str(i + 1) + " TURNS")
            res[1] = i + 1

        if res[0] != None and res[1] != None:
            # print("COMPLETED")
            return i + 1

        feedback1 = generate_feedback(best_guess, answer1)
        feedback2 = generate_feedback(best_guess, answer2)

        feedback_history.append([feedback1,feedback2])

        temp_list = target_list
        target_list = []
        for target in temp_list:
            for pair in feedback_history:
                if res[0] is None and generate_feedback(best_guess, target) == pair[0]:
                    target_list.append(target)
                if res[1] is None and generate_feedback(best_guess, target) == pair[1]:
                    target_list.append(target)



    return 8


def main():

    # print(play_game())

    play_game()
    results = []
    for i in range(1000):
        print("finished " + str(i))
        results.append(play_game())

    print(sum(results) / 1000)
    print(max(results))
    print(results.count(max(results)))
    print(results)
    # print(generate_feedback('gooey', 'hippo'))

main()