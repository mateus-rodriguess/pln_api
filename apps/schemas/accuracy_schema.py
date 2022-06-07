from pydantic import BaseModel


class Accuracy(BaseModel):
    message: str
    
    class Config:
        orm_mode = True


class AccuracyResponse(BaseModel):
    accuracy: str = None
    message: str

    class Config:
        orm_mode = True

class AccuracyModel(BaseModel):
    message: str
    accuracy: float
    
    class Config:
        orm_mode = True
