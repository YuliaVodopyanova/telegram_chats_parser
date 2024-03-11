import csv

chat_id = ''
chat_id_2 = ''


def find_word_in_csv(path, word):
    count = 0
    overall_count = 0
    row = 0
    source = ''
    lemmatized_match = []

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for column in reader:
            row += 1
            lemmas = column[3]
            if f' {word} ' in lemmas or lemmas.endswith(f' {word}') or lemmas.startswith(f'{word} '):
                count += 1
                lemmatized_match.append(lemmas.split(' '))
                if row <= 531525: #number of messages from 1st chat + 1 (titles)
                    source = chat_id
                elif row > 531525:
                    source = chat_id_2
                result = f'{count}. {column[0]} [{column[1]}. @{source} ({column[2]})].'
                print(result)
                print('--------------------------------------------------------------')
    for item in lemmatized_match:
        overall_count += item.count(word_to_find)
    if count == 0:
        print('\nВхождение не найдено.')
    else:
        print('\nОбщее количество контектов:', count)
        print('Общее количество вхождений:', overall_count)


file_path = 'two_chats_data.csv'
word_to_find = ''
find_word_in_csv(file_path, word_to_find)
