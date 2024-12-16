import random
import sys

my_file = open("small_vocab.txt", "r") 
data = my_file.read() 
small_vocab = data.split("\n") 

my_file = open("large_vocab.txt", "r") 
data = my_file.read() 
large_vocab = data.split("\n") 

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


def play_game(words_list, large):
    feedback_history = []
    res = [None, None]
    guesses = []

    target_list = words_list
    answer1 = random.choice(words_list)
    answer2 = random.choice(words_list)
    # print("ans: " + answer1)
    # print("ans: " + answer2)
    for i in range(100):
        # print("guess " + str(i + 1))
        guess_map = {}
        for guess in target_list:
            freq_map = {}

            iter1 = None
            iter2 = None
            if res[0] == None and res[1] == None:
                if not large:
                    if 100 < len(target_list):
                        iter1 = random.sample(target_list, 100)
                        iter2 = random.sample(target_list, 100)
                    else:
                        iter1 = target_list
                        iter2 = target_list
                else:
                    if 50 < len(target_list):
                        iter1 = random.sample(target_list, 50)
                        iter2 = random.sample(target_list, 50)
                    else:
                        iter1 = target_list
                        iter2 = target_list

                for target1 in iter1:
                    feedback1 = tuple(generate_feedback(guess, target1))
                    for target2 in iter2:
                        if target1 != target2:
                            # print(freq_map)
                            feedback2 = tuple(generate_feedback(guess, target2))

                            feedback_pair = tuple([feedback1, feedback2])
                            if feedback_pair in freq_map.keys():
                                freq_map[feedback_pair] = freq_map[feedback_pair] + 1
                            else:
                                freq_map[feedback_pair] = 1
            elif res[0] == None:
                for target1 in target_list:
                    feedback1 = tuple(generate_feedback(guess, target1))
                    if feedback1 in freq_map.keys():
                        freq_map[feedback1] = freq_map[feedback1] + 1
                    else:
                        freq_map[feedback1] = 1
            elif res[1] == None:
                for target2 in target_list:
                    feedback2 = tuple(generate_feedback(guess, target2))
                    if feedback2 in freq_map.keys():
                        freq_map[feedback2] = freq_map[feedback2] + 1
                    else:
                        freq_map[feedback2] = 1
            # print(freq_map)
            max_value = max(freq_map.values())
            guess_map[guess] = max_value
        best_guess = min(guess_map, key=guess_map.get)
        # print("turn " + str(i + 1) + " " + best_guess)

        if best_guess == answer1:
            # print("FINISHED WORD 1 IN " + str(i + 1) + " TURNS")
            res[0] = i + 1

        if best_guess == answer2:
            # print("FINISHED WORD 2 IN " + str(i + 1) + " TURNS")
            res[1] = i + 1

        guesses.append(best_guess)

        if res[0] != None and res[1] != None:
            print("Answers: ", [answer1, answer2])
            print("Guesses: ", guesses)
            return i + 1
        
        feedback1 = generate_feedback(best_guess, answer1)
        feedback2 = generate_feedback(best_guess, answer2)

        feedback_history.append([feedback1,feedback2])

        temp_list = set(target_list)
        target_list = []
        for target in temp_list:
            for pair in feedback_history:
                if res[0] is None and generate_feedback(best_guess, target) == pair[0]:
                    target_list.append(target)
                if res[1] is None and generate_feedback(best_guess, target) == pair[1]:
                    target_list.append(target)



    return 100


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--large":
        large = True
        words_list = large_vocab
    else:
        large = False
        words_list = small_vocab

    print(str(play_game(words_list, large)) + " Turns to Compete")

main()