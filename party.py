class BaseParty:
    def __init__(self, default=None) -> None:
        self.members = default or []

    def add(self, member):
        raise NotImplementedError

    def is_over(self):
        raise NotImplementedError

    def alive_members(self, idx=True):
        raise NotImplementedError


class Party(BaseParty):
    def __init__(self, default=None) -> None:
        self.members = default or []

    def add(self, member):
        if len(self.members) > 25:
            raise Exception
        i_list = []
        for i, _member in enumerate(self.members):
            if _member.name == member.name:
                i_list.append(i)
                continue
        for i in i_list:
            self.members[i].disp_name = self.members[i].name + chr(ord("A")+i)
        member.disp_name = member.name + chr(ord("A")+len(i_list))
        self.members.append(member)

    def is_over(self):
        return all([member.is_dead() for member in self.members])

    def alive_members(self, idx=True):
        members = []
        for i, member in enumerate(self.members):
            if member.is_dead():
                continue
            if idx:
                members.append(i)
            else:
                members.append(member)
        return members