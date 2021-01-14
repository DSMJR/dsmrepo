file1 = input('Enter First File: ')
file2 = input('Enter Second File: ')
handle1 = open(file1, encoding="utf8")
handle2 = open(file2, encoding="utf8")
i1 = handle1.readlines()
i2 = handle2.readlines()
if i1 == i2:
    print('Files are the same.')
    input('Press Enter to continue...')
else:
    print('Files ar NOT the same.')