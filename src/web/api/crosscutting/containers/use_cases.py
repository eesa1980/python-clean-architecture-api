from dependency_injector import providers, containers

from src.application.users import GetUserByIdQuery, ListUsersQuery, CreateUserCommand, UpdateUserCommand, DeleteUserCommand
from src.web.api.crosscutting.containers.infrastructure import InfrastructureContainer


class UseCasesContainer(containers.DeclarativeContainer):
    get_user_by_id_query = providers.Factory(GetUserByIdQuery, InfrastructureContainer.user_repository)
    list_users_query = providers.Factory(ListUsersQuery, InfrastructureContainer.user_repository)
    create_user_command = providers.Factory(CreateUserCommand, InfrastructureContainer.user_repository)
    update_user_command = providers.Factory(UpdateUserCommand, InfrastructureContainer.user_repository)
    delete_user_command = providers.Factory(DeleteUserCommand, InfrastructureContainer.user_repository)
