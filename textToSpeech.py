import os
import azure.cognitiveservices.speech as speechsdk


def synthesize_speech(text):
    speech_key = "b76de4f2c95d4312aeb6ae90b18d3175"
    speech_region = "koreacentral"

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=speech_region
    )
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    speech_config.speech_synthesis_voice_name = "ko-KR-InJoonNeural"

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if (
        speech_synthesis_result.reason
        == speechsdk.ResultReason.SynthesizingAudioCompleted
    ):
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
