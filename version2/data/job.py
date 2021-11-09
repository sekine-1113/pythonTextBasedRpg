
class Job:
    def __init__(self, job_id: int, exp: int,
                weaponId: int, accessaryId: int, statusId: int) -> None:
        self.id = job_id
        self.exp = exp
        self.weaponId = weaponId
        self.accessaryId = accessaryId
        self.statusId = statusId
