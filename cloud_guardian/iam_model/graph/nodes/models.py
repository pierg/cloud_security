from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Type, Dict   
from loguru import logger

@dataclass(frozen=True)
class Entity:
    """Defines a base IAM entity"""
    id: str
    name: Optional[str] = None
    includes: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self):
        # Convert list to tuple for any dynamically added includes to maintain immutability
        object.__setattr__(self, 'includes', tuple(self.includes))
        logger.info(f"Entity instance created: {self.id}")


    @staticmethod
    def create_from_dict(class_name: str, class_attrs: Dict[str, any]) -> Type['Entity']:
        logger.info(f"Creating entity class {class_name}")
        return type(class_name, (Entity,), class_attrs)

@dataclass(frozen=True)
class Resource:
    """Defines a base Resource entity"""
    id: str
    name: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self):
        logger.info(f"Entity instance created: {self.id}")

    @staticmethod
    def create_from_dict(class_name: str, class_attrs: Dict[str, any]) -> Type['Resource']:
        logger.info(f"Creating entity class {class_name}")
        return type(class_name, (Resource,), class_attrs)