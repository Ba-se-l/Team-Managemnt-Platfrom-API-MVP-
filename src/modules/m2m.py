from sqlalchemy import Column, ForeignKey

from src.database import Base, M2M

ProjectsTechnologies = M2M(
    'projects_technologies',
    Base.metadata,
    Column('project_id', ForeignKey('projects.id', ondelete='CASCADE'), primary_key=True),
    Column('technology_id', ForeignKey('technologies.id', ondelete='CASCADE'), primary_key=True)
)