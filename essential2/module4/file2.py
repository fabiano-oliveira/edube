
filepath = './essential2/module4/file2.txt'
with open(filepath, 'rt') as file: 
    line = file.readline()
    i = 1
    while line != '':
        print(i, ':', line, end='')
        line = file.readline()
        i += 1
    
with open(filepath, 'rt') as file:
    lines = file.readlines(7)
    print(lines)
