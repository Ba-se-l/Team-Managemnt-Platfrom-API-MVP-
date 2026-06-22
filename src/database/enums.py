from enum import StrEnum


class UserStatus(StrEnum):
    ONLINE = 'online'
    OFFLINE = 'offline'

class ProjectStatus(StrEnum):
    DONE = 'done'
    ACTIVE = 'active'
    IN_PROGRESS = 'in_progress'
    TODO = 'todo'
    IN_REVIEW = 'in_review'
    ARCHIVED = 'archived'

class TaskStatus(StrEnum):
    DONE = 'done'
    ACTIVE = 'active'
    IN_PROGRESS = 'in_progress'
    TODO = 'todo'
    IN_REVIEW = 'in_review'
    ARCHIVED = 'archived'

class TaskPriority(StrEnum):
    CRITICAL = 'critical'
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class UserRoles(StrEnum):
    SUPER_ADMIN = 'super_admin'
    ADMIN = 'admin'
    DEVELOPER = 'developer'
    VIEWER = 'viewer'