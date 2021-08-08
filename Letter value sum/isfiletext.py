from pathlib import Path

file = Path("word_list.txt")
if file.is_file():
    print('it exists')
    f = open(file,'r')
    print(f.read(2))
else:
    print("not found")