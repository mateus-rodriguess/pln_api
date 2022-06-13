from pydantic import BaseModel


class Accuracy(BaseModel):
    message: str = "Feedback"
    save: bool = False
    translate: bool = True
    
    class Config:
        orm_mode = True


class AccuracyResponse(BaseModel):
    accuracy: float
    message: str = "Feedback"

    class Config:
        orm_mode = True

class AccuracyModel(BaseModel):
    message: str
    accuracy: float
    
    class Config:
        orm_mode = True
