import datetime
import json
from datetime import datetime

import vk_api

today = datetime.now()
today_year = today.year
print(f"{today_year=}")

# add user token from url https://oauth.vk.com/oauth/authorize?client_id=7433931&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131&state=123456&slogin_h=0192097430789f7ba3.7f2d407ca793dd02cb&__q_hash=69b18c1d96dce71b9110b6ebceb41486
# or use APP token TEST_VK_APP
json_file = open("../tokens.json")
TOKEN = json.load(json_file)["USER"]

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
atmo_ids = vk.groups.getMembers(group_id=23513715)["items"]
# print(atmo_ids)
print(f"Найдено {len(atmo_ids)} людей")

all_dict = {}
to_file = []

for i, id in enumerate(atmo_ids):
    print(f"{i} из {len(atmo_ids)} загрузка друзей {id}")
    try:
        res = vk.friends.get(user_id=id, fields="bdate")["items"]
        # print(res)
        all_dict[id] = res
        to_file.extend([item["id"] for item in res])
    except Exception as e:
        print(id, e)

print(f"Найдено {len(to_file)} друзей")
with open("data/friends_all.txt", "w") as fp:
    for item in to_file:
        fp.write(str(item) + "\n")


age_filter = (17, 24)
exclude_atmo = True
filtered_dict = {}
to_file = []

i = 0
for key, persons in all_dict.items():
    i += 1
    print(f"{i} из {len(all_dict.keys())} фильтрация {key=}")
    filtered_dict[key] = 0
    for person in persons:
        if bdate := person.get("bdate"):
            if str(bdate).count(".") == 2:
                byear = int(str(bdate).split(".")[2])
                age = today_year - byear
                flag = (
                    not age_filter or (age > age_filter[0] and age < age_filter[1])
                ) and (not exclude_atmo or not person["id"] in atmo_ids)
                if flag:
                    # print(person["bdate"])
                    to_file.append(person["id"])
                    filtered_dict[key] += 1

with open("data/friends_filtered.txt", "w") as fp:
    for item in to_file:
        fp.write(str(item) + "\n")

atmo_sorted = dict(
    sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
)
print(atmo_sorted)
with open("data/atmo_sorted.txt", "w") as fp:
    for key, item in atmo_sorted.items():
        fp.write(f"{str(key)}: {str(item)}\n")
