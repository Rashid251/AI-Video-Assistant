from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)
from core.summarizer import generate_title, split_transcript, summarize

SAMPLE_TRANSCRIPT = (
    "Alice: Welcome everyone to our project sync. "
    "Bob: We decided to use Python for the backend and PostgreSQL for our database. "
    "Charlie: I will create the initial database schema by Thursday. "
    "Alice: Does anyone know if we have budget for cloud deployment?"
)

def test_split_transcript():
    long_text = "Word " * 1000
    chunks = split_transcript(long_text)
    assert isinstance(chunks, list)
    assert len(chunks) > 0

def test_generate_title():
    title = generate_title(SAMPLE_TRANSCRIPT)
    assert isinstance(title, str)
    assert len(title) > 0

def test_summarize():
    summary = summarize(SAMPLE_TRANSCRIPT)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_extractor_functions():
    action_items = extract_action_items(SAMPLE_TRANSCRIPT)
    assert isinstance(action_items, str)
    assert len(action_items) > 0

    decisions = extract_key_decisions(SAMPLE_TRANSCRIPT)
    assert isinstance(decisions, str)
    assert len(decisions) > 0

    questions = extract_questions(SAMPLE_TRANSCRIPT)
    assert isinstance(questions, str)
    assert len(questions) > 0
