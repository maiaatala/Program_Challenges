lista_numeros = ['one', 'two']
quantidade_numeros = int(input())
input_strings = []
output = []

for i in range(quantidade_numeros):
    input_strings.append(input())

#input_strings =['owe','onw','thrne','owe','one','threw','owe','nhree','too','nne','thren','tne','two','too','throe','oee','tww','thtee','ooe','ont']

for i in input_strings:
    char_one = 0
    char_two = 0
    count = 0
    word_lenght = len(i)
    if word_lenght == 5:
        output.append(3)
    else:
        for char in i:
            if char == lista_numeros[0][count]:
                char_one += 1
            elif char == lista_numeros[1][count]:
                char_two += 1
            count += 1
        output.append(1 if char_one > char_two else 2)

#right_output = [1, 1, 3, 1, 1, 3, 1, 3, 2, 1, 3, 1, 2, 2, 3, 1, 2, 3, 1, 1]
#print(input_strings)
#print(right_output, output)
#print(output == right_output)

for i in output:
    print(i)