input_strings = []
output = []
quantidade_numeros = int(input())
for i in range(quantidade_numeros):
    input_strings.append(input())

# input_strings =['owe','onw','thrne','owe','one','threw','owe','nhree','too','nne','thren','tne','two','too','throe','oee','tww','thtee','ooe','ont']
# test string

for i in input_strings:
    char_one = 0
    char_two = 0
    count = 0
    word_lenght = len(i)
    if word_lenght == 5:
        output.append(3)
    else:
        for char in i:
            if char in 'one':
                char_one += 1
            if char in 'two':
                char_two += 1
            count += 1
        output.append(1 if char_one >= char_two else 2)

# right_output = [1, 1, 3, 1, 1, 3, 1, 3, 2, 1, 3, 1, 2, 2, 3, 1, 2, 3, 1, 1]
# test results
# print(input_strings)
# print(right_output, output)
# print(output == right_output)

for i in output:
    print(i)