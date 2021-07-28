from abc import abstractmethod, ABC


class Band():
    bands = []
    members = []

    def __init__(self, name, members: list):
        self.name = name
        self.members = members
        Band.bands.append(self)

    def band_members(self, mname):
        self.mname = mname
        Band.members.append(mname)

    def play_solos(self):
        result = ''
        for i in Band.members:
            result += f'{i.play_solo()}\n'
        return result

    @classmethod
    def to_list(cls):
        return cls.members

    def __str__(self):
        return f"Band <{self.name}>"

    def __repr__(self):
        return f" '{self.name}' "


class Musician():

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f"Musician <{self.name}>"

    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "

    def play_solo(self):
        if self.name == 'Kurt Cobain':
            return 'face melting guitar solo'
        elif self.name == 'Krist Novoselic':
            return 'bom bom buh bom'
        elif self.name == 'Dave Grohl':
            return 'rattle boom crash'

# def test_play_solos_for_whole_band(mname):
#     solos = mname.play_solos()
#     assert len(solos) == 3
#     assert solos[0] == "face melting guitar solo"
#     assert solos[1] == "bom bom buh bom"
#     assert solos[2] == "rattle boom crash"


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'


if __name__ == "__main__":
    Kurt_Cobain = Guitarist('Kurt Cobain')
    Krist_Novoselic = Drummer('Krist Novoselic')
    Dave_Grohl = Bassist('Dave Grohl')

    nirvana = Band('nirvana', [])
    nirvana.band_members(Kurt_Cobain)
    nirvana.band_members(Krist_Novoselic)
    nirvana.band_members(Dave_Grohl)

    print(Band.members)
