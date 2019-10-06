with open('mails.txt') as file:
    x = file.readlines()

    print(x)
    for i in x:
        print(i.rstrip())
