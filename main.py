import time
import random
from textToSpeech import synthesize_speech
from speechToText import standby_and_cobo_recognized
from speechToText import conversation_listening
from chatGptApi import interact_with_chatgpt
from datetime import datetime


def check_time_and_ask():
    now = datetime.now()
    if now.minute == 0 and now.hour == 8:
        return "아침"
    elif now.minute == 0 and now.hour == 12:
        return "점심"
    elif now.minute == 0 and now.hour == 18:
        return "저녁"
    return None

def ask_question(time_of_day):
    question = get_random_question(time_of_day)
    synthesize_speech(question)
        
    answer = 0
    while answer != "fail" or answer != "0":
        answer = conversation_listening()
        if answer == "fail":
            synthesize_speech("잘 못 들었어요")
        else:
            answer = interact_with_chatgpt(answer)
            synthesize_speech(answer)

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

# standby 함수를 통해 코보를 들을때까지 함수 반복 실행
while True:
    now = datetime.now()
    time_of_day = check_time_and_ask()
    
    if time_of_day:
        ask_question(time_of_day)
        
    isrecognized = standby_and_cobo_recognized()
    # 코보를 인식하면 recognized를 반환하고 밑에 함수 실행
    if isrecognized == "recognized":
        synthesize_speech("코보를 부르셨나요?")
        # conversation_listening 함수를 통해 음성을 텍스트로 변환하고 반환
        answer = 0
        while answer != "fail" or answer != "0":
            answer = conversation_listening()
            # 문장 인식을 못 했을 경우
            if answer == "fail":
                synthesize_speech("잘 못 들었어요")
            else:  # 문장 인식을 했을 경우
                answer = interact_with_chatgpt(answer)
                synthesize_speech(answer)
