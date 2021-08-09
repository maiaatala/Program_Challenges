import gc
from pathlib import Path
import os
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

# function to delete objects and release used memory

def release(a):
    del a  # delets the variable 
    gc.collect()  # calls garbage collector

def menu1():
    os.system('cls')
    print("\nThe letter sum calculator Program.\n   --we don't take kindly to special chars--   ")
    print("\t1 - input your own word.\n\t2 - Solve reddit's challenges!\n\t3 - byeee.")

def menu2():
    os.system('cls')
    print("\n\t1 - Write all output in a .txt file.\n\t2 - Show words with value above 315.\n\t3 - Show total of words with odd letter sum")
    print('\t4 - Show the most common letter value sum and how many words share it')
    # print('\t5 - Show words with same letter sum and lenght difference of 11 chars.')
    # print('\t6 - Show words with letter sum above 188, equal on their sum but with no chars in commom.')
    # print("\t7 - Show a list of words with different lenghts, descending lenght and ascending letter sum")
    print('\t0 - go out.')

# gets input from file function
def from_file(letters):
    file = Path("word_list.txt")  # path for the file
    if not file.is_file():  # verifies it the file doesn't exists
        print("File not found, download it again on github!")
    else:  # did it like this so the function is not all messy
        f = open(file,'r')  # openns the file
        # gets input
        f_input = f.read().splitlines()  # splitlines() will get rid of \n
        f.close()  # closes file since we got all the inputs.
        #  loop to get the letter sum of each word
        sum_value = []  # list we will keep the values in. Start needed.
        for words in f_input:
            temp_value = 0  # starting the variable needed
            # using assigment expresions to get the sum
            [temp_value := temp_value + letters.get(char) for char in words]  # [] needed
            sum_value.append(temp_value)
        # creates a dic with keys being the sum value, will be helpful for future challenges
        words_dic = {f_input[i]: sum_value[i] for i in range(len(f_input))}
        release(f_input)
        release(sum_value) # maybe clears memory?
        return(words_dic)

def from_user(letters):
    user_input = input("Enter phrase: ")
    #using assigment expresions to get the sum
    value = 0  # starting the variable needed
    # .lower() to allow caps look input
    [value := value + letters.get(char.lower()) for char in user_input]  # [] needed
    print(f'{user_input}: {value}')

#creates output in file function
def in_file(words_dic):
    # output
    f1 = open('word_value_output.txt','w')
    # writing it using comprehension
    [f1.write('%-28s: %s\n' % (keys, words_dic[keys])) for keys in words_dic]  # [] needed. assigment expression? 
    f1.close()  # close the output file

def above_315(words_dic):
    # challenge 1
    # assigment expression to create list of keys if the value of said key is above 315
    above_315 = [k for k, v in words_dic.items() if v >= 315]  # we are putting the keys in the array above_315
    # above_315.sort(key=len) # sorting key string by element lenght
    [print('%-28s: %s' % (keys, words_dic[keys])) for keys in above_315]  # pretty sure this is assigment expressions. [needed

def odd_numbers(words_dic):
    # assigment expression to create list of keys if the value of said key is odd
    odd = [k for k, v in words_dic.items() if v % 2 == 1]  # we are putting the keys in the array above_315
    print(f"The number of words with odd letter sum is: {len(odd)}")

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
        while (words_value_dic := from_file(letter_values)) is not None:  # ASSIGMENT EXPRESSIONS FOR THE WIN
            menu2()
            choice_dic = {
                '1': in_file,
                '2': above_315,
                '3': odd_numbers,
                # '5': sameSum_difLenght
            }
            if (m1 := input("escolha: ")) in choice_dic:
                choice_dic[m1](words_value_dic)
            else:
                release(choice_dic)
                release(words_value_dic)
                break
            os.system('pause')  # so we can read the results
    os.system('pause')  # so we can read the results
    menu1()
else: 
    print("byeee.")