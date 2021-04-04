import requests
from nonebot import on_command, CommandSession

# 来源https://github.com/fz6m/nonebot-plugin
@on_command('joke', aliases=('笑话', '讲个笑话', '来个笑话'), only_to_me=False)
async def joke(session: CommandSession):
    joke_send = await get_joke()
    await session.send(joke_send, at_sender=True)


async def get_joke():
    url = 'https://www.mxnzp.com/api/jokes/list/random'
    header = {'app_id': 'lbeqhqhnhgo22otp', 'app_secret': 'OFpUMnhWOEhoVWNkM3dOaVV2dnhQQT09'}
    res = requests.get(url, headers=header)
    print(res)
    return res.json()['data'][0]['content']
