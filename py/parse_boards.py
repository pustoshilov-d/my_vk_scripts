import vk_api

from datetime import datetime
import json

print('222')
json_file = open('./TOKENS.json')
TOKEN = json.load(json_file)['test_site_app']
print(TOKEN)

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

with open('./output.csv', 'w', encoding='utf-8') as file_to_save:
    max_n = 2451
    for offset in range(0, max_n, 100):
        # try:
        answers = vk.board.getComments(
            group_id=52257019,
            topic_id=31428191,
            access_token=TOKEN,
            sort="desc",
            count=100,
            offset=offset,
            v="5.131"
        )['items']

        print()

        for answer in answers:
            print(answer)
            record = ';'.join([str(answer['id']), str(answer['from_id']),
                        str(datetime.utcfromtimestamp(int(answer['date'])).strftime('%Y.%m.%d %H:%M:%S')), str(answer['text'])]).replace('\n', '`')+'\n'
            print(record)
            file_to_save.write(record)
            print(offset, answer['id'])
        # except Exception as e:
        #     print(e)
