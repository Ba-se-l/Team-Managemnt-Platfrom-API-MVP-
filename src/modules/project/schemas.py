from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


from src.database import ProjectStatus


class CreateProjectRequest(BaseModel):
    """Schema for creating Project."""

    title: str = Field(..., min_length=5, max_length=100)
    short_description: str = Field(..., min_length=10, max_length=500)
    deadline: datetime | None = Field(default=None)


class UpdateProjectRequest(BaseModel):
    """Schema for updating Project."""
    title: str | None = Field(default=None, min_length=5, max_length=100)
    short_description: str | None = Field(default=None, min_length=10, max_length=100)
    status: ProjectStatus | None = Field(default=None)
    deadline: datetime | None = Field(default=None)



class ProjectResponse(BaseModel):
    """Schema for Project data in API response."""

    # To enable ORM valintate -> ModelClass.model_valintate(orm_instance)
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    short_description: str
    is_active: bool
    status: ProjectStatus
    deadline: datetime | None
    released_at: datetime | None
    creator_int: int | None
    team_int: int | None
    created_at: datetime
    updated_at: datetime