from pydantic import BaseModel, RootModel, Field

class DefaultResponse(BaseModel):
    message: str
    
class ScheduleIdQuery(BaseModel):
    id: int    

class ScheduleSearchQuery(BaseModel):
    search: str        

class ScheduleItem(BaseModel):
    id: int
    title: str
    date: str
    description: str

class ScheduleInput(BaseModel):
    title: str = Field(example="Reunião")
    date: str = Field(
        example= "2025-11-28 14:30"

    )
    description: str= Field(example="Reunião de professores")

class ScheduleEditInput(BaseModel):
    id: int
    title: str = Field(example="Reunião")
    date: str = Field(
        example= "2025-11-28 14:30"

    )
    description: str= Field(example="Reunião de professores")    

class ScheduleIdParam(BaseModel):
    id: int

class ScheduleListResponse(RootModel[list[ScheduleItem]]):
    pass