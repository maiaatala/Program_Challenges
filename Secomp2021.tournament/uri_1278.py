output = []
indent = []
count = 0

while True:
    numero_linhas = int(input())
    if numero_linhas == 0:
        break
    elif numero_linhas != 0 and count != 0:
        indent.append("")
        output.append("")
    tempindent = 1
    for i in range(numero_linhas):
        texto = (input())
        palavra = " ".join(texto.split())
        output.append(palavra)
        if len(palavra) > tempindent:
            tempindent = len(palavra)
    for i in range(numero_linhas):
        indent.append(tempindent)   
    count = 1

count = 0
for i in output:
    print(f"%{indent[count]}s" % i)
    count += 1
# s = '     ROMEO      AND'
# output = " ".join(s.split())
# i = 14
# print(f"%{i}s" % output)