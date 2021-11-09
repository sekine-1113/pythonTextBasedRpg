class User:
    def __init__(self, name: str, money: int, jobId: int) -> None:
        self.name = name
        self.money = money
        self.jobId = jobId

user = User("ボブ", 0, 0)

class Job:
    def __init__(self, name: str, statusId: int, exp: int, weaponId: int, accessaryId: int) -> None:
        self.name = name
        self.statusId = statusId
        self.exp = exp
        self.weaponId = weaponId
        self.accessaryId = accessaryId
        self.status = None

job_data = [
    Job("デバッグ", 0, 0, 2001, 3001),
    Job("僧侶", 1001, 0, 2000, 3000)
]

class Status:
    def __init__(self, level: int, HP: int, MP: int,
                    ATK: int, DEF: int,
                    SATK: int, SDEF: int,
                    SPD: int) -> None:
        self.level = level
        self.HP = HP
        self.MP = MP
        self.ATK = ATK
        self.DEF = DEF
        self.SATK = SATK
        self.SDEF = SDEF
        self.SPD = SPD

status_data = {
    0000: Status(99, 999, 999, 999, 999, 999, 999, 999),
    1001: Status( 1,  32,   0,   0,   0,   0,   0,   0),
    1002: Status( 2,  36,   0,   0,   0,   0,   0,   0)
}


print(user.__dict__)
user.jobId = 1
print(job_data[user.jobId].__dict__)
print(status_data[job_data[user.jobId].statusId].__dict__)
job_data[user.jobId].statusId = user.jobId * 1000 + 2 if user.jobId != 0 else 0
print(job_data[user.jobId].statusId)
print(status_data[job_data[user.jobId].statusId].__dict__)