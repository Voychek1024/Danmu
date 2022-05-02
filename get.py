import json.decoder
import requests
j = 0

for page in range(15, 3120, 15):
    phantom = j + 1619428070067
    j += 1
    url = 'https://mfm.video.qq.com/danmu'
    params = {
        'otype': 'json',
        'target_id': '3076236791&vid=v0027a575oh',
        'session_key': '323,9,1619428072',
        'timestamp': page,
        '_': "{}".format(phantom),
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36 '
    }
    try:
        response = requests.get(url=url, params=params, headers=headers)
        json_data = response.json()
        contents = json_data['comments']
        for i in contents:
            content = i['content']
            with open('content_4.txt', mode='a', encoding='utf-8') as f:
                f.write(content)
                f.write('\n')
        print(page)
    except json.decoder.JSONDecodeError:
        continue
