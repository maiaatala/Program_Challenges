import gc
from pathlib import Path
import os
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
    # print('\t5 - Show words with same letter sum and lenght difference of 11 chars.')
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
    # assigment expression to create list of keys if the value of said key is odd
    words_value_arr = []
    for word in words:
        words_value_arr.append(calculate_value(word, value))
    odd = 0
    [odd := odd + (1 if words_value_arr[i] % 2 != 0 else 0) for i in range(len(words_value_arr))]
    print(f"The number of words with odd letter sum is: {odd}")

#takes forever, it was a flop
# def sameSum_difLenght(words_dic):
#     inner_list = []
#     keys, values = zip(*words_dic.items())
#     lenght = len(keys)
#     # print(keys)
#     # print(words_dic.values())  #.keys() returns an array with all the keys in the dic and .values() return array with all the values
#     for i in range(lenght):
#         if values.count(values[i]) > 1 and len(keys[i]) > 5: 
#             for j in range(i,lenght):
#                 if values[i] == values[j] and abs(len(keys[i]) - len(keys[j])) == 11:
#                     inner_list.append([keys[i], keys[j]])
#     print(inner_list)

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
                # '5': sameSum_difLenght
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