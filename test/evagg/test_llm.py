from functools import reduce
from unittest.mock import AsyncMock, MagicMock, call, mock_open, patch

from openai import AsyncAzureOpenAI

from lib.evagg.llm import OpenAIClient


@patch("lib.evagg.llm.aoai.AsyncAzureOpenAI", return_value=AsyncMock())
async def test_openai_client_prompt(mock_openai, test_file_contents) -> None:
    prompt_template = test_file_contents("phenotype.txt")
    prompt_params = {"gene": "GENE", "variant": "VARIANT", "passage": "PASSAGE"}
    prompt_text = reduce(lambda x, kv: x.replace(f"{{{{${kv[0]}}}}}", kv[1]), prompt_params.items(), prompt_template)

    mock_openai.return_value.chat.completions.create.return_value.choices[0].message.content = "response"
    client = OpenAIClient(
        "AsyncAzureOpenAI",
        {
            "deployment": "gpt-8",
            "endpoint": "https://ai",
            "api_key": "test",
            "api_version": "test",
            "timeout": 60,
        },
    )
    with patch("builtins.open", mock_open(read_data=prompt_template)):
        response = await client.prompt_file(
            user_prompt_file="phenotype.txt",
            system_prompt="Extract field",
            params=prompt_params,
            prompt_settings={"temperature": 1.5, "prompt_tag": "phenotype"},
        )

    assert response == "response"
    mock_openai.assert_called_once_with(azure_endpoint="https://ai", api_key="test", api_version="test", timeout=60)
    mock_openai.return_value.chat.completions.create.assert_called_once_with(
        messages=[
            {"role": "system", "content": "Extract field"},
            {"role": "user", "content": prompt_text},
        ],
        max_tokens=1024,
        frequency_penalty=0,
        presence_penalty=0,
        temperature=1.5,
        model="gpt-8",
    )
