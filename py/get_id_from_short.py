import vk_api
print('222')

TOKEN = ""

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

str1 = "m.gorelko,efidanii"
users = str1.split(",")


for user in users:
    try:
        print(user + ","+str(vk.utils.resolveScreenName(
            screen_name=user,
            access_token=TOKEN,
            v="5.131"
        )['object_id']))
    except Exception as e:
        print(user + ",no")
