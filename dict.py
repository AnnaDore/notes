n = int(input())
# dictionary comprehension
name_numb = [input().split() for _ in range(n)]
phoneBook = {k: v for k,v in name_numb}
# let's try to find the numbers
while(1):
    try:
        name = input()
        if name in phoneBook:
            print('%s=%s' % (name, phoneBook[name]))
        else:
            print('Not found')
    except:
        break
