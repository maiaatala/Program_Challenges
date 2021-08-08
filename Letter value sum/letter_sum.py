# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
# create alphabet list
alphabet = "abcdefghijklmnopqrstuvwxyz"
# dictionary comprehention to get the value to each char in the alphabet
letter_values = {char: (alphabet.find(char)+1) for char in set(alphabet)}

#gets input
user_input = input("Enter phrase: ")

#using assigment expresions to get the sum
user_input_value = 0  # starting the variable needed
[user_input_value := user_input_value + letter_values.get(char) for char in user_input]  # [] needed

#output
print(f'{user_input_value}')