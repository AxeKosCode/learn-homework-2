"""
Домашнее задание №2
Работа с файлами
* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длину получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    try:
        with open('referat.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            len_file = len(content)
            print(' Количество символов в тексте -', len_file)
            words = content.replace('-', ' ').split()
            words_clear = [word.strip('.,:;!?()"«»') for word in words]

            count_words = len(words_clear)
            print(' Количество слов -', count_words)
            file_format = content.replace('.', '!')
    except FileNotFoundError:
        print('Файл с таким именем не найден')
        file_format = ''
        
    if file_format:
        with open('referat2.txt', 'w', encoding='utf-8') as f2:
            try:
                f2.write(file_format)
                print('Новый файл успешно создан')
            except UnboundLocalError:
                print('Файл не удалось записать')


if __name__ == "__main__":
    main()
