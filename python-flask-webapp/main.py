import time
import random
from textToSpeech import synthesize_speech
from speechToText import standby_and_cobo_recognized
from speechToText import conversation_listening
from chatGptApi import interact_with_chatgpt
from datetime import datetime



#시간을 인식하는 함수
def check_time_and_ask():
    now = datetime.now()
    if now.minute == 0 and now.hour == 8:
        return "아침"
    elif now.minute == 0 and now.hour == 12:
        return "점심"
    elif now.minute == 0 and now.hour == 18:
        return "저녁"
    return None

# 질문을 하고 이후에 코보를 부를 필요없이 그대로 대화
def ask_question(time_of_day):
    question = get_random_question(time_of_day)
    synthesize_speech(question)
    n = 0   
    while n < 1:
            n = 0
            # conversation_listening 함수를 통해 음성을 텍스트로 변환하고 반환
            answer = conversation_listening()
            if "그만" in answer:
                synthesize_speech("그럼 안녕히 계세요")
                return
            print(answer)
            print("여기쯤")
            # 문장 인식을 못 했을 경우
            while answer == "fail":
                print("인식못함")
                synthesize_speech("잘 못 들었어요")
                answer = conversation_listening()
                if "그만" in answer:
                    synthesize_speech("그럼 안녕히 계세요")
                    return
                print(answer)
                n += 1

                # 문장 인식을 했을 경우
            answer = interact_with_chatgpt(answer)
            synthesize_speech(answer)

#랜덤으로 질문을 뽑아주는 함수
def get_random_question(time_of_day):
    if time_of_day == "아침":
        questions = [
            "아침에는 어떤 음식을 드셨나요?",
            "하루를 시작하기 전에 무엇을 하시나요?",
            "오늘 아침에 일어나서 느낀 감정은 어땠나요?"
        ]
    elif time_of_day == "점심":
        questions = [
            "점심 식사로 어떤 음식을 선택하셨나요?",
            "오늘 점심에 무엇을 계획하셨나요?",
            "즐거운 점심시간을 보내고 계신가요?"
        ]
    elif time_of_day == "저녁":
        questions = [
            "오늘 저녁으로 어떤 요리를 준비하셨나요?",
            "저녁에 하고 싶은 휴식 활동이 있으신가요?",
            "하루를 마무리하면서 느끼는 감정을 말해주세요."
        ]
    if questions:
        return random.choice(questions)
    else:
        return None

def start_watching():
    cnt = 0
    # standby 함수를 통해 코보를 들을때까지 함수 반복 실행
    while True:
        now = datetime.now()
        time_of_day = None
        time_of_day = check_time_and_ask()
        
        if cnt != 0:
            cnt-=1
        
        if time_of_day and cnt == 0:
            ask_question(time_of_day)
            cnt = 10
        print("cnt: ", cnt)
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
