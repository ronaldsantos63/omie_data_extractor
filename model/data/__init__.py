from sqlalchemy.orm import registry
from sqlalchemy.orm import declarative_base

mapper_registry = registry()

BaseEntity = declarative_base()

import model.data.entity
