import pandas
import vk_api
print('222')

# vk_session = vk_api.VkApi()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
print(vk.users.get(id=1))