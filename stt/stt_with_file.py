import queue
import re
import sys
import time

from google.cloud import speech
import pyaudio

def transcribe_streaming(stream_file: str) -> speech.RecognitionConfig:
    """Streams transcription of the given audio file."""

    client = speech.SpeechClient.from_service_account_file("./responsive-kiosk-api.json")

    with open(stream_file, "rb") as audio_file:
        content = audio_file.read()

    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]

    requests = (
        speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
    )

    streaming_config = speech.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(
        config=streaming_config,
        requests=requests,
    )

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            print(f"Finished: {result.is_final}")
            print(f"Stability: {result.stability}")
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print(f"Confidence: {alternative.confidence}")
                print(f"Transcript: {alternative.transcript}")


transcribe_streaming("audio.mp3")