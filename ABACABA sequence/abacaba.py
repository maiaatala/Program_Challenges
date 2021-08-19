# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/
print(" --The abacaba Sequence-- ")
print("¶ Made by: Ana C. M. Atala\n")

interactions  = int(input("quantas interações faremos? (1 à 26) "))
if interactions > 26:
    interactions = 26
elif interactions < 1:
    interactions = 1

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_old = ""
string_next_char = ""
for i in ascii_uppercase[:interactions]:
    string_next_char = string_old + i + string_old
    string_old = string_next_char.lower()
    print(f"{ascii_uppercase.find(i)+1}° iteração: {string_next_char}")
#print(len(string_next_char), string_next_char.find('Z'))

print("byeee.")