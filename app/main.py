class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = [Person(element["name"], element["age"]) for element in people]
    for elem in new_people:
        for element in people:
            if elem.name == element["name"]:
                if element.get("wife") is not None:
                    elem.wife = element.get("wife")
                if element.get("husband") is not None:
                    elem.husband = element.get("husband")
    return new_people
