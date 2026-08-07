file_name=input('enter the file name:')

try:
    with open(file_name,'r') as f:
        content=f.read()
        print(content)
except FilNotFoundError:
    print('File not Found')

finally:
    print('Execution completed')
    