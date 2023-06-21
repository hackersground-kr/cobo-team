from textToSpeech import synthesize_speech
from speechToText import standby_and_cobo_recognized
from speechToText import conversation_listening
from chatGptApi import interact_with_chatgpt

# standby 함수를 통해 코보를 들을때까지 함수 반복 실행
while True:
    isrecognized = standby_and_cobo_recognized()
    # 코보를 인식하면 recognized를 반환하고 밑에 함수 실행
    if isrecognized == "recognized":
        n = 0
        synthesize_speech("코보를 부르셨나요?")
        while n < 1:
            n = 0
            # conversation_listening 함수를 통해 음성을 텍스트로 변환하고 반환
            answer = conversation_listening()
            if "그만" in answer:
                synthesize_speech("그럼 안녕히 계세요")
                break
            print(answer)
            print("여기쯤")
            # 문장 인식을 못 했을 경우
            while answer == "fail":
                print("인식못함")
                synthesize_speech("잘 못 들었어요")
                answer = conversation_listening()
                if "그만" in answer:
                    synthesize_speech("그럼 안녕히 계세요")
                    break
                print(answer)
                n += 1

                # 문장 인식을 했을 경우
            answer = interact_with_chatgpt(answer)
            synthesize_speech(answer)
