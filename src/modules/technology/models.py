from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import (
    UUID as ID,
    uuid4 as id4
)

from src.database import Base, CreatedAtUpdatedAtMixin
from src.modules.m2m import ProjectsTechnologies

if TYPE_CHECKING:
    from src.modules.project import Project

class Technology(Base, CreatedAtUpdatedAtMixin):
    __tablename__ = 'technologies'

    # ======================
    # ==== MAIN COLUMNS ====
    # ======================

    id: Mapped[ID] = mapped_column(primary_key=True, default=id4)
    
    name: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str | None] = mapped_column(String)

    class_or_url: Mapped[str | None] = mapped_column(String)

    # ======================
    # === RELATIONSHIPS ====
    # ======================

    projects: Mapped[list['Project']] = relationship(
        'Project',
        back_populates='technologies',
        secondary=ProjectsTechnologies
    )