print('------Регистрация почты------')
print('Введите логин:')
login = input()
print('Введите резервный адрес:')
address = input()
if '@' in login:
    print('Некорректный логин')
elif '@' not in address:
    print('Некорректный адрес')
else:
    print('ОК')
