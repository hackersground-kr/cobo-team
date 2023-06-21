import requests
import json


def call_simsimi_api(utext):
    url = "https://wsapi.simsimi.com/190410/talk"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "0YbM0vc.uydqR1SK5QaKVBM48FmBiTEO5Mb.N9Zg",
    }
    data = {
        "utext": utext,
        "lang": "ko",
        "country": ["KR", "US"],
        "atext_bad_prob_max": 0.7,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()

    return response_data


# API 호출 예시
response = call_simsimi_api("나 심심해")
print(response["atext"])
