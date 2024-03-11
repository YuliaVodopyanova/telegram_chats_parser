from telethon.sync import TelegramClient
import csv
import spacy

api_id =
api_hash = ''
chat_id = ''
chat_id_2 = ''

nlp = spacy.load("ru_core_news_sm")


def lemmatize_text(text):
    doc = nlp(text)
    result = " ".join([token.lemma_ for token in doc])
    return result


with TelegramClient('session_', api_id, api_hash, system_version="4.16.30-vxCUSTOM") as client:
    messages = client.iter_messages(chat_id) #if there are too many messages limit=... can be used

    with open('chat_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Message', 'Network', 'Year', 'Lemmas'])

        for message in messages:
            if message.text:
                message_text = message.text
                network = 'telegram'
                message_date = message.date.year

                lemmatized_text = lemmatize_text(message_text)

                writer.writerow([message_text, network, message_date, lemmatized_text])

print('Data saved in chat_data.csv')
