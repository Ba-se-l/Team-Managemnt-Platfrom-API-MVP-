from typing import TYPE_CHECKING
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import (
    UUID as ID,
    uuid4 as id4
)

from src.database import Base
from src.database import CreatedAtUpdatedAtMixin
from src.database import TaskStatus
from src.database import TaskPriority


if TYPE_CHECKING:
    from src.modules.user import User
    from src.modules.project import Project


class Task(Base, CreatedAtUpdatedAtMixin):
    __tablename__ = 'tasks'

    # ======================
    # ==== MAIN COLUMNS ====
    # ======================
    id: Mapped[ID] = mapped_column(primary_key=True, default=id4)

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), nullable=False)

    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), nullable=False)

    # ======================
    # === RELATIONSHIPS ====
    # ======================
    creator_id: Mapped[ID] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'))

    created_by: Mapped['User'] = relationship(
        'User',
        back_populates='tasks_established',
        foreign_keys=[creator_id]
    )


    assignee_to_id: Mapped[ID] = mapped_column(ForeignKey('users.id', ondelete='SET NULL'))

    assignee_to: Mapped['User'] = relationship(
        'User',
        back_populates='tasks_assigned',
        foreign_keys=[assignee_to_id]
    )


    project_id: Mapped[ID] = mapped_column(ForeignKey('projects.id', ondelete='CASCADE'))

    project: Mapped['Project'] = relationship(
        'Project',
        back_populates='tasks',
        foreign_keys=[project_id]
    )