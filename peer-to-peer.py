password_entry = input('Введите пароль: ')
verification = 1


try:
    password_entry[0]
    result = int(password_entry) / verification
    print('Ваш пароль состоит только из цифр')
except ValueError:
    print('Требования к паролю соблюдены')
except IndexError:
    print('Вы ввели пустой пароль')







