import math

class Job:
    def __init__(self, job_id: int, exp: int,
                weaponId: int, accessaryId: int, statusId: int) -> None:
        self.id = job_id
        self.exp = exp
        self.weaponId = weaponId
        self.accessaryId = accessaryId
        self.statusId = statusId

    @property
    def status_id(self):
        if not self.id:
            return 0
        return self.id * 1000 + self.get_level

    @property
    def get_level(self):
        exp = self.exp
        if exp < 8:
            return 1
        level = round(math.sqrt(abs((exp-6)/1.5)))
        return level

if __name__ == "__main__":
    print(Job(0, 234, 0, 0, 0).status_id)
    print(Job(1, 234, 0, 0, 0).status_id)
    print(Job(2, 1234, 0, 0, 0).status_id)