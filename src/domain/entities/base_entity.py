class BaseEntity:

    def __init__(self, _id, created_at=None, updated_at=None):
        self._id = _id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        return self._id

