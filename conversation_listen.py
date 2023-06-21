import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "b76de4f2c95d4312aeb6ae90b18d3175"
SPEECH_REGION = "koreacentral"


def standby_and_cobo_recognized():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )
    speech_config.speech_recognition_language = "ko-KR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    # 코보를 인식했을때 작동 시작
    print(speech_recognition_result.text)

    if (
        speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech
        and "코보" in speech_recognition_result.text
    ):
        print("코보 인식됨")
        return 1

    # elif speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
    #     print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print(
            "No speech could be recognized: {}".format(
                speech_recognition_result.no_match_details
            )
        )
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")


# recognize_from_microphone()
