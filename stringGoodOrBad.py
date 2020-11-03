n=input()
for i in n:
    if (n.count(i)>=3 and i =='?') or (n.count(i)>=3 and i in 'bcdfghjklmnpqrstvwxyz'):
        print('Bad')
        break
else:
    for i in n:
        if n.count('?')<=1:
            print('Good')
            break
    else:
        print('Mixed')