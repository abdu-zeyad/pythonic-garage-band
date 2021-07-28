from abc import abstractmethod, ABC


class Band():
    members = []
    bands = []

    def __init__(self, name, array):
        self.name = name
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
        return f'{self.name} Play solo'


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
    aziz = Guitarist('Aziz')
    saleh = Drummer('Saleh')
    emad = Bassist('Emad')
    print(aziz)
    print(aziz.get_instrument())
    print(saleh)
    print(saleh.get_instrument())
    print(emad)
    print(emad.get_instrument())
    print(aziz.play_solo())
    print(saleh.play_solo())
    print(emad.play_solo())
    nirvana = Band("Nirvana", )
    nirvana.band_members(aziz)
    nirvana.band_members(saleh)
    nirvana.band_members(emad)
    print(nirvana.bands)
    print(nirvana.__str__())
    print(nirvana.to_list())
    print(nirvana.play_solos())
