import math
acm = []
# input block
while True:
    temp_input = input()
    if temp_input == '0':
        break
    else:
        acm.append(temp_input)
# output block
for j in acm:
    output = 0
    fatorial = len(j)
    for i in j:
        output += int(i)*math.factorial(fatorial)
        fatorial -= 1
    print(output)
