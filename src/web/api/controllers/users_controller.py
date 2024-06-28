from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from src.application.users import GetUserByIdQuery, ListUsersQuery, CreateUserCommand, UpdateUserCommand, \
    DeleteUserCommand
from src.web.api.controllers import common_responses
from src.web.api.crosscutting.containers import ApplicationContainer

router = APIRouter()


@router.get("", status_code=200, response_model=ListUsersQuery.ValidateResponse, responses=common_responses())
@inject
async def list_users_query(
        list_users: ListUsersQuery = Depends(Provide[ApplicationContainer.use_cases.list_users_query])):
    return await list_users.execute()


@router.get("/{user_id}", status_code=200, response_model=GetUserByIdQuery.ValidateResponse, responses=common_responses())
@inject
async def get_user_by_id(
        user_id: int,
        get_user_by_id_query: GetUserByIdQuery = Depends(Provide[ApplicationContainer.use_cases.get_user_by_id_query])):
    return await get_user_by_id_query.execute(user_id)


@router.post("", status_code=201, response_model=CreateUserCommand.ValidateResponse, responses=common_responses())
@inject
async def create_user(
        request_body: CreateUserCommand.ValidateBody,
        create_user_command: CreateUserCommand = Depends(Provide[ApplicationContainer.use_cases.create_user_command])):
    return await create_user_command.execute(request_body)


@router.put("/{user_id}", status_code=204, responses=common_responses())
@inject
async def update_user(
        user_id: int,
        request_body: UpdateUserCommand.UpdateUserRequestBody,
        update_user_command: UpdateUserCommand = Depends(Provide[ApplicationContainer.use_cases.update_user_command])):
    return await update_user_command.execute(user_id, request_body)


@router.delete("/{user_id}", status_code=204, responses=common_responses([401]))
@inject
async def delete_user(
        user_id: int,
        delete_user_command: DeleteUserCommand = Depends(Provide[ApplicationContainer.use_cases.delete_user_command])):
    return await delete_user_command.execute(user_id)
