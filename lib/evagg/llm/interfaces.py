from typing import Any, Dict, Optional, Protocol


class IPromptClient(Protocol):
    async def prompt(
        self,
        user_prompt: str,
        params: Optional[Dict[str, str]] = None,
        prompt_settings: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Get the response from a prompt."""
        ...  # pragma: no cover

    async def prompt_file(
        self,
        user_prompt_file: str,
        params: Optional[Dict[str, str]] = None,
        prompt_settings: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Get the response from a prompt with an input file."""
        ...  # pragma: no cover

    async def prompt_json(
        self,
        user_prompt_file: str,
        params: Optional[Dict[str, str]] = None,
        prompt_settings: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Get the response from a prompt with an input file."""
        ...  # pragma: no cover
