class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = [Person(element["name"],
                         element["age"]) for element in people]
    for element in people:
        obiekt = Person.people[element["name"]]
        if "wife" in element:
            zona = element["wife"]
            obiekt.wife = Person.people.get(zona)
        if "husband" in element:
            maz = element["husband"]
            obiekt.husband = Person.people.get(maz)
    return new_people
