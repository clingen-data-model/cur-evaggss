from pathlib import Path
from typing import Type, NamedTuple

from jinja2 import Environment, FileSystemLoader

from lib.evagg.prompts.models import *

# Templates relative to this __init__.py
template_dir = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(str(template_dir)))


class PromptSpec(NamedTuple):
    template_name: str
    input_model: Type[BaseModel]
    output_model: Type[BaseModel]

    def render_template(self, **kwargs) -> str:
        validated = self.input_model(**kwargs)
        template = env.get_template(self.template_name)
        return template.render(**validated.dict())


PROMPT_REGISTRY = {
    "observations/check_patients": PromptSpec(
        template_name="observations/check_patients.jinja2",
        input_model=CheckPatientsInput,
        output_model=CheckPatientsResponse,
    ),
}

__all__ = ["PROMPT_REGISTRY"]
