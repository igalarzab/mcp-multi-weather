from pydantic import BaseModel

Scalar = str | int | float | bool

class Weather(BaseModel):
    address: str
    temperature: float
    description: str

class GeoCode(BaseModel):
    name: str
    country: str
    lat: float
    lon: float

class InvalidAuth(ValueError):
    pass

class QuotaExceeded(Exception):
    pass