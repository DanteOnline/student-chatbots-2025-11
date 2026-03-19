import random
import torch
import soundfile


async def text_to_audio(
        input_text: str,
        output_path: str = './voice_replies/output.wav'
    ) -> tuple[str, str]:

    language = 'ru'
    speaker_id = "v5_2_ru"
    sample_rate = 48000

    # Загружаем модель через torch.hub
    model, utils = torch.hub.load(
        repo_or_dir="snakers4/silero-models",
        model="silero_tts",
        language=language,
        speaker=speaker_id,
        trust_repo=True
    )

    speakers = [
        'aidar', 'baya', 'kseniya', 'eugene', 'xenia'
    ]

    current_speaker = random.choice(speakers)

    audio = model.apply_tts(
        text=input_text,
        speaker=current_speaker,
        sample_rate=sample_rate,
        put_accent=True,  # для русского: расстановка ударений
        put_yo=True  # для русского: буква "ё"
    )

    soundfile.write(output_path, audio, sample_rate)
    return output_path, current_speaker
