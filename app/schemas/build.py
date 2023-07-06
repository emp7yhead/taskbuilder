from pydantic import BaseModel, Field


class BuildIn(BaseModel):
    build: str = Field(description='Name of build')
