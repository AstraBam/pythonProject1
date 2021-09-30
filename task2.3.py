print('Привет! Какое у тебя настроение?')
answer = input()
if 'хорош' in answer or 'отличн' in answer or 'прекасн' in answer:
    print('Классно! У меня тоже всё хорошо.')
elif 'плох' in answer or 'грустн' in answer or 'печаль' in answer:
    print('Не грусти, всё наладится!')
elif 'не ' in answer or '?' in answer:
    print('Хм... Не понимаю тебя, но надеюсь, что всё хорошо')
else:
    print('Главное никогда не вешать нос!')
