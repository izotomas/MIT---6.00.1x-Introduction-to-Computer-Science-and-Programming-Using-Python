import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.location = (float(location[0]),float(location[1]))
        self.species_types = species_types
    def get_number_of_species(self, animal):
        return self.species_types.get(animal,0)
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        n = self.species_types.get(species,0)
        if n == 1:
            self.species_types.pop(species)
        elif n > 1:
            self.species_types.update({species:n-1})


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        fct = adoption_center.get_number_of_species
        return float(fct(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self,adoption_center)
        num_other = 0

        for animal in self.considered_species:
            num_other += adoption_center.get_number_of_species(animal)

        score = adopter_score + (0.3 * num_other)

        if score > 0.0:
            return score
        return 0.0

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self,adoption_center)
        num_feared = adoption_center.get_number_of_species(self.feared_species)

        score = adopter_score - (0.3 * num_feared)

        if score > 0.0:
            return score
        return 0.0



class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def  __init__(self,  name,  desired_species,  allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for specie in self.allergic_species:
            if specie in adoption_center.get_species_count().keys():
                return 0.0
        return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self,  name, desired_species, allergic_species,
                 medicine_effectivness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectivness = medicine_effectivness

    def get_score(self, adoption_center):
        adopter_score = Adopter.get_score(self, adoption_center)
        center_species = adoption_center.get_species_count().keys()
        lowest_eff = 1

        for specie in self.medicine_effectivness.keys():
            if specie in center_species:
                if self.medicine_effectivness[specie] < lowest_eff:
                    lowest_eff = self.medicine_effectivness[specie]

        return adopter_score * lowest_eff



class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        a = to_location
        b = self.location
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

    def get_score(self, adoption_center):
        d = self.get_linear_distance(adoption_center.get_location())

        if d < 1:
           ran = 1.0
        elif d < 3:
            ran = random.uniform(0.7, 0.9)
        elif d < 5:
            ran = random.uniform(0.5, 0.7)
        else:
            ran = random.uniform(0.1, 0.5)

        n = adoption_center.get_number_of_species(self.desired_species)
        return ran * n



def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center
    such that the scores for each AdoptionCenter to the Adopter
    will be ordered from highest score to lowest score.
    """
    result = []
    fct = adopter.get_score
    for center in list_of_adoption_centers:
        result.append([center, fct(center)])

    # Sort by names first
    result = sorted(result, key=lambda x: x[0].get_name())
    # Sort by scores then
    result = sorted(result, key=lambda x: x[1], reverse=True)

    return [center[0] for center in result]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters
    from list_of_adopters (in numerical order of score)
    """
    result = []

    for ad in list_of_adopters:
        result.append([ad, ad.get_score(adoption_center)])

    # Sort by names first
    result = sorted(result, key=lambda x: x[0].get_name())
    # Sort by scores then
    result = sorted(result, key=lambda x: x[1], reverse=True)

    return [ad[0] for ad in result[0:n]]


