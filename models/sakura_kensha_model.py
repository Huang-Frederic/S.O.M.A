class LitterInfo:
    def __init__(self, father, mother, pedigree, litter, birthdate, expected_race):
        self.father = father
        self.mother = mother
        self.pedigree = pedigree
        self.litter = litter
        self.birthdate = birthdate
        self.expected_race = expected_race

    def __repr__(self):
        return (f"--------------------------------------------------------\nSakuraLitterInfo\n--------------------------------------------------------"
                f"\n father: '{self.father}'\n mother: '{self.mother}'\n pedigree: '{self.pedigree}'\n "
                f"litter: {self.litter}\n birthdate: {self.birthdate}\n expected_race [roux, sésame, n&f] : {self.expected_race}) \n\n")

    def to_dict(self):
        return {
            "father": self.father,
            "mother": self.mother,
            "pedigree": self.pedigree,
            "litter_quantity": self.litter,
            "birthdate": self.birthdate.isoformat() if self.birthdate else None,
            "expected_race": self.expected_race,
        }
