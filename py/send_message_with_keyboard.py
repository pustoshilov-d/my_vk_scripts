import vk_api
print('222')

TOKEN = ""
# vk_session = vk_api.VkApi()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
# print(vk.users.get(
#     id=1,
#     access_token=TOKEN
#     ))

# keyboard = """{
# "one_time":false,
# "buttons":[
# [
# {
# "action":{
# "type":"text",
# "label":"Спасибо, Аля @choko_laka 💘"
# },
# "color":"negative"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Спасибо, Глеб @id166147232 💕"
# },
# "color":"positive"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Спасибо, Ильяс @ilyasatmo 💖"
# },
# "color":"primary"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Спасибо, ЭК 💜"
# },
# "color":"secondary"
# }
# ]
# ]}"""

# keyboard = """{
# "one_time":false,
# "buttons":[
# [
# {
# "action":{
# "type":"text",
# "label":"Да здравствует Глеб @id166147232 😎"
# },
# "color":"negative"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Глеб @id166147232 как ты это вывозишь😲"
# },
# "color":"negative"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"Да здравствует Жанна @segedushka💘"
# },
# "color":"positive"
# }
# ],
# [
# {
# "action":{
# "type":"text",
# "label":"В этот раз не прое...Жанна @segedushka😶"
# },
# "color":"positive"
# }
# ]
# ]}"""

keyboard = """{"buttons":[],"one_time":true}"""

print(vk.messages.send(
    random_id=43652232,
    access_token=TOKEN,
    peer_id=2000000001,
    message=("""До новых встреч! Да здравствует Марк @vuchuy """),
    dont_parse_links=1,
    keyboard=keyboard,
))
