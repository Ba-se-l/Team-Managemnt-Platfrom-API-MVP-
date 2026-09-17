from sqlalchemy.ext.asyncio import create_async_engine
from src.database.base import Base
from src.conf import settings 


# For Testing | sqlite+aiosqlite
async_engine = create_async_engine(
    url= settings.DATABASE_URL,
    echo= settings.ECHO
)



# ----- For PostgreSQL -----
# async_engine = create_async_engine(
#     url= settings.DATABASE_URL,
#     echo= settings.ECHO,
#     pool_size= settings.POOL_SIZE,
#     pool_timeout= settings.POOL_TIMEOUT,
#     max_overflow= settings.MAX_OVERFLOW
# )



async def create_database():

    from src.modules.user import User
    from src.modules.auth import RefreshSession
    from src.modules.project import Project
    from src.modules.task import Task
    from src.modules.team import Team
    from src.modules.team_members import TeamMember
    from src.modules.technology import Technology


    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    
    