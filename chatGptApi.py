import openai

# OpenAI API 인증 설정
openai.api_key = os.environ['SECRET_KEY']


# ChatGPT와 상호 작용하는 함수
def interact_with_chatgpt(prompt):
    # ChatGPT API 요청
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # 상호 작용 결과 반환
    if response.choices:
        answer = response.choices[0].text.strip()
        print(answer)
        return answer
    else:
        return None


# interact_with_chatgpt("너 뭐하고 있니")

# 사용자 입력 받기
# while True:
#     user_input = input("사용자: ")

#     # 대화 종료 조건
#     if user_input.lower() == "그만":
#         break

#     # ChatGPT와 상호 작용
#     response = interact_with_chatgpt(user_input)

#     # ChatGPT 응답 출력
#     print("ChatGPT:", response)
