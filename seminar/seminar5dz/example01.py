# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


data = 'Сегодня былабва хорошая погода, завтра будет дождь иабв абвветер'

words = data.split(' ')

deleteWords = 'абв'

new_words = []
for word in words:
    if deleteWords not in word:
        new_words.append(word)

print(new_words)
