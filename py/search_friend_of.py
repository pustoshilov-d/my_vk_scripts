import vk_api
print('222')

TOKEN = ""

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

str1 = "363711078,342647228"
users = str1.split(",")
print(len(users))

list = []

for user in users:
    try:
        print(user)
        friends = vk.friends.get(
            user_id=user,
            access_token=TOKEN,
            v="5.131"
        )['items']

        if 225306465 in friends:
            list += user

    except Exception as e:
    print(e)

print(list)
