class BadRequestException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)


class InternalServerErrorException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.status_code = 500
        super().__init__(self.message)


class NotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.status_code = 404
        super().__init__(self.message)


class ValidationException(Exception):
    def __init__(self, message: str, meta: dict):
        self.message = message
        self.status_code = 422
        self.meta = meta
        super().__init__(self.message)
