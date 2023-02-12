from pydantic import BaseModel


class TaskType(BaseModel):
    type: int = 1