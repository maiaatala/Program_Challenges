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
    print("\nThe letter sum calculator Program.\n   --special chars have neutral value--   ")
    print("\t1 - input your own word.\n\t2 - Solve reddit's challenges!\n\t3 - byeee.")
# Show reddit challenge menu
def menu2():
    os.system('cls')
    print("\n  Reddit's Challenges!")
    print("\t1 - Write all output in a .txt file.\n\t2 - Show words with value above 315.\n\t3 - Show total of words with odd letter sum")
    print('\t4 - Show the most common letter value sum and how many words share it')
    print('\t5 - Show words with same letter sum and lenght difference of 11 chars.')
    # print('\t6 - Show words with letter sum above 188, equal on their sum but with no chars in commom.')
    # print("\t7 - Show a list of words with different lenghts, descending lenght and ascending letter sum")
    print('\t0 - go out.')
# calculates the value of each word, takes the word and the dic with each word value
def calculate_value(word, LvalueD):
    value = 0
    # .lower() to allow caps lock input
    [value := value + tempv for char in word if (tempv := LvalueD.get(char.lower())) is not None] # this if prevents errors in case of special chars
    return(value)
# makes the word value dic with all the words form the file. takes words array and the dic with each word value
def word_value_dictionary(words, LvalueD):
    word_value_dic = {word: calculate_value(word, LvalueD) for word in words}
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
def from_user(LvalueD):
    value = calculate_value(user_input := input("Enter phrase: "), LvalueD) # calls the function to calculate the value
    print(f'{user_input}: {value}')
# creates output in file function. takes the file input and and the dic with each word value
def in_file(words, LvalueD):
    # output
    f1 = open('word_value_output.txt','w')
    # writing it using comprehension
    [f1.write('%-28s: %s\n' % (word, calculate_value(word, LvalueD))) for word in words]  # [] needed. assigment expression? 
    f1.close()  # close the output file
    print("Done and dusted")
# outputs words with value above 315 and. takes the file input and and the dic with each word value
def above_315(words, LvalueD):
    above_315 = {word: value for word in words if (value := calculate_value(word, LvalueD)) >= 315} # this verifies the if first
    [print('%-28s: %s' % (k, v)) for k, v in above_315.items()]
# outputs the ammount of odd sums vallue in the word file. takes the file input and and the dic with each word value
def odd_numbers(words, LvalueD):
    words_value_arr = [calculate_value(word, LvalueD) for word in words]
    odd = 0 # needed
    # assigment expression to create a count of the odd values in the words_value_array
    [odd := odd + (1 if v % 2 != 0 else 0) for v in words_value_arr]
    print(f"The number of words with odd letter sum is: {odd}")
# outputs the most common letter value sum 
def most_common_value_sum(words, LvalueD):
    words_value_arr = [calculate_value(word, LvalueD) for word in words]
    c = Counter(words_value_arr)
    #print(c.most_common(1))  # outputs [(93, 1965)], the value sum of 93 appears 1965 times
    print(f"The Letter sum value of {c.most_common(1)[0][0]} Appears {c.most_common(1)[0][1]} times, being the most commmom letter sum")
# outuputs words with same sum but lenght dif by 11 chars
def sameSum_difLenght(words, LvalueD):
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
                if calculate_value(words[i], LvalueD) == calculate_value(words[j], LvalueD):
                    outputarr.append([words[i], words[j]])
    print("Words with same letter value sum and lenght differnece of 11 chars:")
    print(outputarr)
    #[['zyzzyva', 'biodegradabilities'], ['voluptuously', 'electroencephalographic']]

# create alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"
# dictionary comprehention to get the value to each char in the alphabet
letter_values = {alphabet[i]: i+1 for i in range(len(alphabet))}
release(alphabet)  # maybe this frees space?

menu1()
# the menuin loop
while (m := input("escolha: ")) in ['1', '2']:  # walrus operator
    if m == '1':
        print() # formatting
        from_user(letter_values)
        print() # formatting
        os.system('pause')  # so we can read the results
    elif (words_file := from_file()) is not None:
        # if file is not found, the variable will receive None type, therefore the rest of the code can't be run.
        # put it outside of the loop or it'd run that function everytime.
        choice_dic = {
            '1': in_file,
            '2': above_315,
            '3': odd_numbers,
            '4': most_common_value_sum,
            '5': sameSum_difLenght
        }
        menu2()
        while (m1 := input("escolha: ")) in choice_dic:  # ASSIGMENT EXPRESSIONS FOR THE WIN
            print() # formatting
            choice_dic[m1](words_file, letter_values)
            print() # formatting
            os.system('pause')  # so we can read the results
            menu2()
        else:
            release(choice_dic)
            release(words_file)
    menu1()
else: 
    print("byeee.")