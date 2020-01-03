import requests
import config
import json
from time import sleep

token = config.token
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

def get_updates():
    url  = URL + 'getupdates'
    resp = requests.get(url)
    return resp.json()

def get_message():

    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id        
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {
        'chat_id' : chat_id,
        'text' : message_text
        }

        return message
    return None

def send_message(chat_id, text='Жди, пидр, блять!'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)




def main():

    while True:        
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if 'ЖЕЛАЙ СПОКОЙНОЙ НОЧИ!' in text:
                send_message(chat_id, 'Спокойной ночи , Кристина)!')
        else:
            continue

        sleep(2)

if __name__ == '__main__':
    main()
