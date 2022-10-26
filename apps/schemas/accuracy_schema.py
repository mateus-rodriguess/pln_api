from pydantic import BaseModel


class Accuracy(BaseModel):
    save: bool = False
    message: str = "Ótimo produto"

    class Config:
        orm_mode = True


class AccuracyResponse(BaseModel):
    accuracy: float
    message: str

    class Config:
        orm_mode = True


class AccuracyModel(BaseModel):
    accuracy: float
    message: str

    class Config:
        orm_mode = True
