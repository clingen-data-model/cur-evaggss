from pydantic import BaseModel, Extra


class CheckPatientsInput(BaseModel, extra=Extra.forbid):
    paper_text: str
    patient: str


class CheckPatientsResponse(BaseModel, extra=Extra.forbid):
    is_patient: bool
