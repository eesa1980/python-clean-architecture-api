from dependency_injector import providers, containers

from .infrastructure import InfrastructureContainer
from .use_cases import UseCasesContainer


class ApplicationContainer(containers.DeclarativeContainer):
    infrastructure = providers.Container(InfrastructureContainer)
    use_cases = providers.Container(UseCasesContainer)
    env = infrastructure.container.env
