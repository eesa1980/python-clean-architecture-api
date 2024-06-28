from dependency_injector import providers, containers
from src.infrastructure.config import load_environment
from src.infrastructure.repositories import UserRepository
from src.infrastructure.utilities import DictToClassUtility


class InfrastructureContainer(containers.DeclarativeContainer):

    env = providers.Configuration()
    _environment = load_environment()
    env.from_dict(_environment.__dict__)

    dict_to_class_utility = providers.Singleton(DictToClassUtility)
    user_repository = providers.Singleton(UserRepository)

