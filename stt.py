import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "b76de4f2c95d4312aeb6ae90b18d3175"
SPEECH_REGION = "koreacentral"


def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    subscription_key = SPEECH_KEY
    region = SPEECH_REGION

    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_recognition_language = "ko-KR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    print("Speak into your microphone.")

    # Wait for "코보" keyword to start speech recognition
    while True:
        result = speech_recognizer.recognize_once_async().get()

        if (
            result.reason == speechsdk.ResultReason.RecognizedSpeech
            and "코보" in result.text
        ):
            print("Keyword detected. Starting speech recognition.")
            break

    # Start listening for speech input and save it to a list
    speech_text = []
    sentence_finished = False

    def process_sentence(evt):
        nonlocal sentence_finished

        speech_text.append(evt.result.text)

        if evt.result.text.endswith("."):
            sentence_finished = True

    speech_recognizer.recognized.connect(process_sentence)
    speech_recognizer.start_continuous_recognition()

    # Wait until a sentence is finished
    while not sentence_finished:
        pass

    # Stop listening for speech input
    speech_recognizer.stop_continuous_recognition()
    print("Speech recognition stopped.")

    # Combine the recognized speech into a single string
    final_text = " ".join(speech_text)
    print("Final Text: {}".format(final_text))


recognize_from_microphone()
