# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/
interactions  = int(input("quantas interações faremos? "))
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_old = ""
string_next_char = ""
for i in ascii_uppercase[:interactions]:
    string_next_char = string_old + i + string_old
    string_old = string_next_char.lower()
    print(f"{ascii_uppercase.find(i)+1}° iteração: {string_next_char}")
#print(len(string_next_char), string_next_char.find('Z'))