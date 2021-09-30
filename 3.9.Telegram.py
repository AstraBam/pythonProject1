print('Введите сообщение:')
message = input()
length = len(message)
cost = length * 40
print(cost // 100, 'р.', cost % 100, 'коп.')
