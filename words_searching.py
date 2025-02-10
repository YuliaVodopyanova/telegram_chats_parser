import csv


def find_word_in_csv(path, word):
    count = 0
    overall_count = 0
    row = 0
    lemmatized_match = []

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for column in reader:
            row += 1
            lemmas = column[3]
            if f' {word} ' in lemmas or lemmas.endswith(f' {word}') or lemmas.startswith(f'{word} '):
                count += 1
                lemmatized_match.append(lemmas.split(' '))
                result = f'{count}. {column[0]} [{column[1]}. @{column[4]} ({column[2]})].'
                print(result)
                print('--------------------------------------------------------------')
    for item in lemmatized_match:
        overall_count += item.count(word_to_find)
    if count == 0:
        print('\nВхождение не найдено.')
    else:
        print('\nОбщее количество контектов:', count)
        print('Общее количество вхождений:', overall_count)


file_path = 'chats_dataset_2025_final_varsion.csv'
word_to_find = "рефлексия"
find_word_in_csv(file_path, word_to_find)
