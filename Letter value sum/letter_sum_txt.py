import gc
from pathlib import Path
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

#function to delete objects and release used memory
def release(a):
    del a  # delets the variable 
    gc.collect()  # calls garbage collector

# gets input from file function
def from_file(letters):
    file = Path("word_list.txt")  # path for the file
    if not file.is_file():  # verifies it the file doesn't exists
        print("File not found, download it again on github!")
    else: # did it like this so the function is not all messy
        f = open(file,'r') # openns the file
        # gets input
        f_input = f.read().splitlines() # splitlines() will get rid of \n
        f.close()  # closes file since we got all the inputs.
        # loop to get the letter sum of each word
        sum_value = [] # list we will keep the values in. Start needed.
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

#creates output in file function
def in_file(words_dic):
    # output
    f1 = open('word_value_output.txt','w')
    # writing it using comprehension
    [f1.write('%-28s: %s\n' % (keys, words_dic[keys])) for keys in words_dic]
    f1.close()  # close the output file

# create alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
# dictionary comprehention to get the value to each char in the alphabet
letter_values = {alphabet[i]: i+1 for i in range(len(alphabet))}
release(alphabet)  # maybe this frees space?
#adds values to spacaces and blank spaces to prevent error in the future.
letter_values[""], letter_values[" "] = 0, 0  # special chars will still result in errors.

words_value_dic = from_file(letter_values)
# if file is not found, the variable will receive None type, therefore the rest of the code can't be run.
if words_value_dic != None: 
    in_file(words_value_dic)
    # challenge 1
    # assigment expression to create list of keys if the value of said key is above 315
    above_315 = [k for k, v in words_value_dic.items() if v >= 315]  # we are putting the keys in the array above_315
    # above_315.sort(key=len) # sorting key string by element lenght
    [print('%-28s: %s' % (keys, words_value_dic[keys])) for keys in above_315] # pretty sure this is assigment expressions. [] needed