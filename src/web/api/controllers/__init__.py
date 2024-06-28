from typing import Optional, Dict, Any

from pydantic import BaseModel


class ExceptionModel(BaseModel):
    message: str
    error_name: str
    status_code: int
    title: str
    meta: Optional[Dict[str, Any]]
    type: str


def common_responses(status_codes=None):
    default_status_codes = [422, 404, 500]

    if status_codes is None:
        status_codes = default_status_codes
    else:
        status_codes = set(status_codes + default_status_codes)
    responses = {}

    for status_code in status_codes:
        responses[status_code] = {
            "model": ExceptionModel,
        }

    return responses
