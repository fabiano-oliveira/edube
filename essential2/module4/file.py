import sys

file_path = './essential2/module4/file.txt' 

with open(file_path, 'rt') as stream:
    print(stream.read())
    stream.close()

print('=' * 20)

for line in open(file_path, 'rt'):
    print(line)
    
    