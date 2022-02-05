from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class headlines(BaseModel):
    id: PyObjectId = Field(alias='_id')
    type: str
    headline: str

    class Config:
        arbitrary_types_allows = True
        json_encoders = {
            ObjectId: str
        }