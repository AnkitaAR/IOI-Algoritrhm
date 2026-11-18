# Parrot Bird (complete activity 3, DSCM2L3). Python 3 standard library only.
# Run: python parrot_bird.py  (or paste into one Google Colab cell and press Run)


class Parrot:
    species = "bird"                                           # A: class variable

    def __init__(self, name, age):
        """Runs by itself every time a Parrot is made: Parrot("Blu", 10)."""
        # Step 1: Instance variables
        self.name = name
        if age < 0:
            age = 0
        self.age = age


# Step 2: Make two parrots
parrot_name = input("Name of the first parrot? ")
blu = Parrot(parrot_name, 10)
woo = Parrot("Woo", 15)
print(blu.name, "is a", blu.species)                          # B: class variable
print(woo.name, "is also a", Parrot.species)                  #    read two ways
print(blu.name, "is", blu.age, "years old")                   # C: instance
print(woo.name, "is", woo.age, "years old")                   #    variables

# Step 3: Edge case: bad age
ghost = Parrot("Ghost", -3)
print(ghost.name, "is", ghost.age, "years old")
