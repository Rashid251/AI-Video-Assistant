from core.transcriber import (
    transcribe_all,
    transcribe_chunk_sarvam,
    transcribe_chunk_whisper,
)


def test_transcribe_chunk_whisper_fallback():
    # Calling whisper on non-existent file should safely fallback to mock transcript without crashing
    text = transcribe_chunk_whisper("non_existent_file.wav")
    assert isinstance(text, str)
    assert len(text) > 0

def test_transcribe_chunk_sarvam_fallback():
    # Calling sarvam without valid key or file should safely fallback
    text = transcribe_chunk_sarvam("non_existent_file.wav")
    assert isinstance(text, str)
    assert len(text) > 0

def test_transcribe_all():
    # Mock chunk list
    transcript = transcribe_all(["fake_chunk_1.wav"], language="english")
    assert isinstance(transcript, str)
    assert len(transcript) > 0
