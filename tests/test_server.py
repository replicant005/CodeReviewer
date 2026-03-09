import pytest
# for mocking 
from unittest.mock import patch
# connection error is for network failure, http error is for API returned bad status 
from requests.exceptions import ConnectionError, HTTPError

import os, sys

# ensure project root is on right path 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LLM import llm_client


# tets to see if the mcp is able to call Ollama 
def test_successful_generation():
# mock response 
    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "Looks good"}

    with patch("requests.post", return_value=MockResponse()):
        result = llm_client.call_llm("test prompt")

    assert result == "Looks good"


# test to see if ollama is down 
def test_ollama_down():

    with patch("requests.post", side_effect=ConnectionError):

        with pytest.raises(ConnectionError):
            llm_client.call_llm("test prompt")

# if llm returns nothing 
def test_bad_response_format():

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {}  # no response 

    with patch("requests.post", return_value=MockResponse()):
        result = llm_client.call_llm("test prompt")

        assert result == "{}"

# if the request reaching the right endpoint
def test_correct_url_used():

    with patch("requests.post") as mock_post:

        try:
            llm_client.call_llm("test prompt")
        except:
            pass

        args, kwargs = mock_post.call_args

        assert args[0] == llm_client.OLLAMA_URL


# if the model is not there
def test_model_missing():

    class MockResponse:
        def raise_for_status(self):
            raise HTTPError("404 model not found")

        def json(self):
            return {"response": "model missing"}

    with patch("requests.post", return_value=MockResponse()):
        result = llm_client.call_llm("test prompt")

        assert result == "model missing"


# see what prompt is nbeing passed to the llm 
def test_prompt_formatting():

    with patch("requests.post") as mock_post:

        try:
            llm_client.call_llm("print('hello')")
        except:
            pass

        args, kwargs = mock_post.call_args

        payload = kwargs["json"]

        assert payload["model"] == "qwen2.5-coder"
        assert payload["prompt"] == "print('hello')"
        assert payload["stream"] is False


# test that no prompt is sent if tge request is empty , we'll assert that an empty s
def test_no_prompt_sent_when_empty():
    with patch("requests.post") as mock_post:
        llm_client.call_llm("")   

    args, kwargs = mock_post.call_args
    payload = kwargs["json"]

    # prompt is sent but empty
    assert payload["prompt"] == ""
