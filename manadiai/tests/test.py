import os
import pytest
from manadiai.logger import GenAILogger

@pytest.fixture
def test_filepath(tmp_path):
    return tmp_path / "test_interactions.jsonl"


def test_log_interaction_creates_file(test_filepath):
    logger = GenAILogger(storage_path=str(test_filepath))
    prompt = "Explain consistent hashing"
    response = "Consistent hashing distributes data..."
    feedback = "Simplify more"

    logger.log_interaction(prompt, response, feedback)

    assert test_filepath.exists()


def test_log_interaction_data_integrity(test_filepath):
    logger = GenAILogger(storage_path=str(test_filepath))
    prompt = "Define CRAQ"
    response = "Chain Replication with Apportioned Queries..."

    logger.log_interaction(prompt, response)

    interactions = logger.get_all_interactions()
    assert len(interactions) == 1
    assert interactions[0]['prompt'] == prompt
    assert interactions[0]['response'] == response
    assert interactions[0]['feedback'] is None


def test_log_multiple_interactions(test_filepath):
    logger = GenAILogger(storage_path=str(test_filepath))

    interactions_data = [
        ("What is sdist?", "Source distribution format."),
        ("What is bdist?", "Binary distribution format.")
    ]

    for prompt, response in interactions_data:
        logger.log_interaction(prompt, response)

    interactions = logger.get_all_interactions()
    assert len(interactions) == 2
    for idx, interaction in enumerate(interactions):
        assert interaction['prompt'] == interactions_data[idx][0]
        assert interaction['response'] == interactions_data[idx][1]
        assert interaction['feedback'] is None

