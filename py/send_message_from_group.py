import vk_api
print('222')

TOKEN=""
# vk_session = vk_api.VkApi()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
# print(vk.users.get(
#     id=1,
#     access_token=TOKEN
#     ))

print(vk.messages.send(
    random_id=42422222241,
    access_token=TOKEN,
    peer_id=2000000006,
    message=("""
#НоминацииПрофсоюза

◾ Результаты
Ниже. Первые места и отдельные поощрения по мнению организаторов были награждены на Выезде либо получили электронные версии дипломов.

Спасибо за участие!

С любовью,
*proff_union(Ваш Профсоюз)"""),
    attachment="",
    dont_parse_links=1
    ))
    