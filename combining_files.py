import pandas as pd

data1 = pd.read_csv("chat_data.csv")

data2 = pd.read_csv("path to the file with info from 2nd chat")

combined_data = pd.concat([data1, data2], ignore_index=True)

combined_data.to_csv('two_chats_data.csv', index=False)
