word = input('digite um algo:''\n')

num = word.isnumeric()
alpha = word.isalpha()
low = word.islower()
alpnum = word.isalnum()

if num:
    print("É um numerico :D")
else:
    print('Não é numerico :O')

if alpha:
    print("É alfabético :D")
else:
    print('Não é alfabético :O')

if alpnum:
    print("É um alphanumerico :D")
else:
    print('Não é alphanumerico :O')


if low:
    print("Não tem Capslock :^")
else:
    print('Tem Capslock :^')
