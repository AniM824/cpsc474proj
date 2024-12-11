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
        print("guess " + str(i + 1))
        guess_map = {}
        for guess in target_list:

            # iter1 = None
            # iter2 = None
            # if 1000 < len(target_list):
            #     iter1 = random.sample(target_list, 1000)
            #     iter2 = random.sample(target_list, 1000)
            # else:
            #     iter1 = target_list
            #     iter2 = target_list


            if res[0] == None:
                freq_map1 = {}
                for target1 in target_list:
                    feedback1 = tuple(generate_feedback(guess, target1))
                    if feedback1 in freq_map1.keys():
                        freq_map1[feedback1] = freq_map1[feedback1] + 1
                    else:
                        freq_map1[feedback1] = 1

            if res[1] == None:
                freq_map2 = {}
                for target2 in target_list:
                    feedback2 = tuple(generate_feedback(guess, target2))
                    if feedback2 in freq_map2.keys():
                        freq_map2[feedback2] = freq_map2[feedback2] + 1
                    else:
                        freq_map2[feedback2] = 1

            max_value = None
            if res[0] == None and res[1] == None:
                max_value = max([max(freq_map1.values()), max(freq_map2.values())])
            elif res[0] == None:
                max_value = max(freq_map1.values())
            else:
                max_value = max(freq_map2.values())
            guess_map[guess] = max_value

            
        best_guess = min(guess_map, key=guess_map.get)
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

    # play_game()
    results = []
    for i in range(20):
        print("finished " + str(i))
        results.append(play_game())

    print(sum(results) / 20)
    print(max(results))
    print(results.count(max(results)))
    print(results)
    # print(generate_feedback('gooey', 'hippo'))

main()