filem = input('What text/code file do you want to number: ')
handler = open(filem, 'r')
handlea = open('NumberedFileOutput.txt', 'a')
#handlew = open(filem, 'w')
y = 1
for i in handler:
    x = i
    t = str(y)
    d = t + ' ' + x
    f = d.rstrip()
    print(f)
    handlea.write(d)
    y = y + 1
input('Press enter to continue...')