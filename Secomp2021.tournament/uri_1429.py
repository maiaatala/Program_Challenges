import math
acm = []
while True:
    temp_input = input()
    if temp_input == '0':
        break
    else:
        acm.append(temp_input)
for j in acm:
    output = 0
    fatorial = len(j)
    for i in j:
        output += int(i)*math.factorial(fatorial)
        fatorial -= 1
    print(output)
