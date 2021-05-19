class Property:
    def __init__(self, name, accept_any_name=False):
        self.name = name
        self.accept_any_name = accept_any_name

    def matches(self, other_property):
        if self.accept_any_name:
            return type(self) == type(other_property)
        else:
            # TODO: refactor this & refine what an object() is
            return type(self) == type(other_property) and (
                        self.name == other_property.name or (
                            self.object() == other_property.object() and self.object() is not None
                            )
                        )

    def object(self):
        return None


class Subject(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PersonSubject(Subject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Object(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Verb(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)