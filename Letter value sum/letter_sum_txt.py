import gc
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

#function to delete objects and release used memory
def release(a):
    del a
    gc.collect()

# create alphabet list
alphabet = "abcdefghijklmnopqrstuvwxyz"
# dictionary comprehention to get the value to each char in the alphabet
letter_values = {char: (alphabet.find(char)+1) for char in set(alphabet)}
release(alphabet)  # maybe this frees space?
# gets input
f = open("word_list.txt", "r")
f_input = f.read().splitlines() # splitlines() will get rid of \n
f.close() # closes the file since we already got the input from it.
sum_value = [] # list we will keep the values in.

# loop to get the letter sum of each word
for words in f_input:
    temp_value = 0  # starting the variable needed
    # using assigment expresions to get the sum
    [temp_value := temp_value + letter_values.get(char) for char in words]  # [] needed
    sum_value.append(temp_value)

#creates a dic with keys being the sum value, will be helpful for future challenges
words_value_dic = {f_input[i]: sum_value[i] for i in range(len(f_input))}
release(f_input)
release(sum_value) # maybe clears memory?

# output
f1 = open('word_value.txt','w')
# writing it using comprehension
[f1.write('%-28s: %s\n' % (keys, words_value_dic[keys])) for keys in words_value_dic]
f1.close()  # close the output file

# challenge 1
# assigment expression to create list of keys if the value of said key is above 315
above_315 = [k for k, v in words_value_dic.items() if v >= 315]
# above_315.sort(key=len) # sorting key string by element lenght
[print('%-28s: %s' % (keys, words_value_dic[keys])) for keys in above_315]