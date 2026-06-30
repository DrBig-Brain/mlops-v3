from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    trip_distance: float = Field(..., description="trip distance")
    PULocationID: int = Field(..., description="Pick Up location ID")
    DOLocationID: int = Field(..., description="Drop off location ID")
    duration: float = Field(...,description = "duration of trip") 