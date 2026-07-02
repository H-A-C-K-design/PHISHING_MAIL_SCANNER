from pydantic import BaseModel


class EmailPredictionRequest(BaseModel):
    subject: str
    content: str
