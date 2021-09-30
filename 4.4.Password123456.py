print('Введите пароль:')
password1 = input()
length = len(password1)
if length < 8:
    print('Короткий')
elif '123' in password1:
    print('Простой')
else:
    print('Повторите пароль:')
    password2 = input()
    if password2 != password1:
        print('Различаются')
    else:
        print('OK')
