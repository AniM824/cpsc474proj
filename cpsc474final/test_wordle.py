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
    target_list = words_list
    answer = random.choice(words_list)
    # print("ans: " + answer)
    for i in range(6):
        guess_map = {}
        for guess in target_list:
            freq_map = {}
            for target in target_list:
                # print(freq_map)
                feedback = tuple(generate_feedback(guess, target))
                if feedback in freq_map.keys():
                    freq_map[feedback] = freq_map[feedback] + 1
                else:
                    freq_map[feedback] = 1
            # print(freq_map)
            max_value = max(freq_map.values())
            guess_map[guess] = max_value
        best_guess = min(guess_map, key=guess_map.get)
        # print("turn " + str(i + 1) + " " + best_guess)

        if best_guess == answer:
            # print("FINISHED THE GAME IN " + str(i + 1) + " TURNS")
            return i + 1
        
        feedback = generate_feedback(best_guess, answer)
        temp_list = target_list
        target_list = []
        for target in temp_list:
            if generate_feedback(best_guess, target) == feedback:
                target_list.append(target)


    return 7


def main():
    print(play_game())
    # results = []
    # for i in range(100):
    #     print("fiished " + str(i))
    #     results.append(play_game())

    # print(sum(results) / 100)
    # print(max(results))
    # print(results)
    # print(generate_feedback('gooey', 'hippo'))

main()