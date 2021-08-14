import gc  # garbage collector
from pathlib import Path  # file path
import os  # system cls and pause
from collections import Counter # most common
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

# function to delete objects and release used memory
def release(a):
    del a  # delets the variable 
    gc.collect()  # calls garbage collector
# show main menu, take user input or reddit challenge
def menu1():
    os.system('cls')
    print("\nThe letter sum calculator Program.\n   --we don't take kindly to special chars--   ")
    print("\t1 - input your own word.\n\t2 - Solve reddit's challenges!\n\t3 - byeee.")
# Show reddit challenge menu
def menu2():
    os.system('cls')
    print("\n\t1 - Write all output in a .txt file.\n\t2 - Show words with value above 315.\n\t3 - Show total of words with odd letter sum")
    print('\t4 - Show the most common letter value sum and how many words share it')
    print('\t5 - Show words with same letter sum and lenght difference of 11 chars.')
    # print('\t6 - Show words with letter sum above 188, equal on their sum but with no chars in commom.')
    # print("\t7 - Show a list of words with different lenghts, descending lenght and ascending letter sum")
    print('\t0 - go out.')
# calculates the value of each word, takes the word and the dic with each word value
def calculate_value(word, letter_value):
    value = 0
    # .lower() to allow caps look input
    [value := value + letter_values.get(char.lower()) for char in word]  # [] needed
    return(value)
# makes the word value dic with all the words form the file. takes words array and the dic with each word value
def word_value_dictionary(words, value):
    keys_values = []
    for word in words:
        keys_values.append(calculate_value(word, value))
    word_value_dic = {words[i]: keys_values[i] for i in range(len(words))}
    return(word_value_dic)
# gets input from file function
def from_file():
    file = Path("word_list.txt")  # path for the file
    if not file.is_file():  # verifies it the file doesn't exists
        print("File not found, download it again on github!")
    else:  # did it like this so the function is not all messy
        f = open(file,'r')  # openns the file
        # gets input
        f_input = f.read().splitlines()  # splitlines() will get rid of \n
        f.close()  # closes file since we got all the inputs.
        return(f_input)
# getts user imput and outputs the value
def from_user(value):
    user_input = input("Enter phrase: ")
    #using assigment expresions to get the sum
    value = calculate_value(user_input, value)
    
    print(f'{user_input}: {value}')
# creates output in file function. takes the file input and and the dic with each word value
def in_file(words, value):
    # output
    f1 = open('word_value_output.txt','w')
    # writing it using comprehension
    [f1.write('%-28s: %s\n' % (word, calculate_value(word, value))) for word in words]  # [] needed. assigment expression? 
    f1.close()  # close the output file
    print("sucesseful")
# outputs words with value above 315 and. takes the file input and and the dic with each word value
def above_315(words, value):
    # challenge 1
    # creates the word dic
    words_dic = word_value_dictionary(words, value)
    # assigment expression to create list of keys if the value of said key is above 315
    above_315 = [k for k, v in words_dic.items() if v >= 315]  # we are putting the keys in the array above_315
    # above_315.sort(key=len) # sorting key string by element lenght
    [print('%-28s: %s' % (keys, words_dic[keys])) for keys in above_315]  # pretty sure this is assigment expressions. [needed
# outputs the ammount of odd sums vallue in the word file. takes the file input and and the dic with each word value
def odd_numbers(words, value):
    words_value_arr = []  # starting list needed
    [words_value_arr.append(calculate_value(word, value)) for word in words]
    odd = 0 # needed
    # assigment expression to create list of keys if the value of said key is odd
    [odd := odd + (1 if words_value_arr[i] % 2 != 0 else 0) for i in range(len(words_value_arr))]
    print(f"The number of words with odd letter sum is: {odd}")
# outputs the most common letter value sum 
def most_common_value_sum(words, value):
    words_value_arr = []  # starting list needed
    [words_value_arr.append(calculate_value(word, value)) for word in words]
    c = Counter(words_value_arr)
    #print(c.most_common(1))  # outputs [(93, 1965)], the value sum of 93 appears 1965 times
    print(f"The Letter sum value of {c.most_common(1)[0][0]} Appears {c.most_common(1)[0][1]} times, being the most commmom letter sum")
# outuputs words with same sum but lenght dif by 11 chars
def sameSum_difLenght(words, value):
    print("it takes 8 min...")
    outputarr = []
    x = len(words) - 1 
    words.sort(key = len)
    for i in range(4971, 170495):  #last 4 lettered word and last word that will be below 11 lenght dif
        for j in range(x, i, -1):
            templendif = abs(len(words[i]) - len(words[j]))
            if templendif < 11:
                break
            elif templendif == 11:
                if calculate_value(words[i], value) == calculate_value(words[j], value):
                    outputarr.append([words[i], words[j]])
    print(outputarr)
    #[['zyzzyva', 'biodegradabilities'], ['voluptuously', 'electroencephalographic']]

# create alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
# dictionary comprehention to get the value to each char in the alphabet
letter_values = {alphabet[i]: i+1 for i in range(len(alphabet))}
release(alphabet)  # maybe this frees space?
# adds values to spacaces and blank spaces to prevent error in the future.
letter_values[""], letter_values[" "] = 0, 0  # special chars will still result in errors.

menu1()
while (m := input("escolha: ")) in ['1', '2']:
    if m == '1':
        from_user(letter_values)
    elif m == '2':
        # if file is not found, the variable will receive None type, therefore the rest of the code can't be run.
        while (words_file := from_file()) is not None:  # ASSIGMENT EXPRESSIONS FOR THE WIN
            menu2()
            choice_dic = {
                '1': in_file,
                '2': above_315,
                '3': odd_numbers,
                '4': most_common_value_sum,
                '5': sameSum_difLenght
            }
            if (m1 := input("escolha: ")) in choice_dic:
                choice_dic[m1](words_file, letter_values)
            else:
                release(choice_dic)
                release(words_file)
                break
            os.system('pause')  # so we can read the results
    os.system('pause')  # so we can read the results
    menu1()
else: 
    print("byeee.")