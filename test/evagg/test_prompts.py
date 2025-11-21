import pytest
from pydantic import ValidationError

from lib.evagg.prompts import PROMPT_REGISTRY


def test_render_template_valid_input():
    """Test that valid input passes Pydantic validation and renders."""
    spec = PROMPT_REGISTRY["observations/check_patients"]

    rendered = spec.render_template(
        paper_text="This paper discusses proband with variant X.",
        patient="proband",
    )

    # Check the rendered template contains substituted data
    assert "proband" in rendered
    assert "This paper discusses" in rendered


def test_render_template_invalid_input():
    """Test that invalid input triggers Pydantic validation error."""
    spec = PROMPT_REGISTRY["observations/check_patients"]

    # Missing required field "paper_text"
    with pytest.raises(ValidationError):
        spec.render_template(
            patient="proband",
            extra="not allowed",   # also violates Extra.forbid
        )