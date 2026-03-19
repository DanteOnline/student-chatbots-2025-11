"""
Голосовые сервисы: конвертация OGG/WAV, STT (Faster-Whisper), TTS (Silero).
"""
from .stt_pipeline import (
    load_model as load_stt_model,
    transcribe,
    transcribe_with_fallback,
)
from .tts_pipeline import text_to_audio

__all__ = [
    "load_stt_model",
    "transcribe",
    "transcribe_with_fallback",
    "text_to_audio",
]
