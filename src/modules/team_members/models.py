from typing import TYPE_CHECKING
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import (
    UUID as ID
)

from src.database import Base, UserRoles

if TYPE_CHECKING:
    from src.modules.user import User
    from src.modules.team import Team

class TeamMember(Base):
    __tablename__ = 'team_members'

    # ======================
    # === RELATIONSHIPS ====
    # ======================
    member_id: Mapped[ID] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)

    team_id: Mapped[ID] = mapped_column(ForeignKey('teams.id', ondelete='CASCADE'), primary_key=True)

    role: Mapped[UserRoles] = mapped_column(Enum(UserRoles), nullable=False)

    
    member: Mapped['User'] = relationship(
        'User',
        back_populates='teams_memberships',
        foreign_keys=[member_id]
    )

    
    team: Mapped['Team'] = relationship(
        'Team',
        back_populates='members',
        foreign_keys=[team_id]
    )
    

