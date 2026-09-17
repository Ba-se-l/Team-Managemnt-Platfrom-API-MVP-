from typing import TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.database import Base, CreatedAtUpdatedAtMixin
from src.modules.m2m import ProjectsTechnologies

if TYPE_CHECKING:
    from src.modules.project import Project

class Technology(Base, CreatedAtUpdatedAtMixin):
    __tablename__ = 'technologies'

    # ======================
    # ==== MAIN COLUMNS ====
    # ======================

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    description: Mapped[str | None] = mapped_column(String)

    documentation_url: Mapped[str | None] = mapped_column(String)


    def __repr__(self):
        return f"Techonolgy(id={self.id}, name={self.name})"

    # ======================
    # === RELATIONSHIPS ====
    # ======================

    projects: Mapped[list['Project']] = relationship(
        'Project',
        back_populates='technologies',
        secondary=ProjectsTechnologies
    )