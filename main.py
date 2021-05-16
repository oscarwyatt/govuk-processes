
class Property:
    def __init__(self, name, accept_any_name=False):
        self.name = name[0]
        self.accept_any_name = accept_any_name

    def matches(self, other_property):
        if self.accept_any_name:
            return type(self) == type(other_property)
        else:
            return type(self) == type(other_property) and self.name == other_property.name


class Process(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.title = title
        self.core_frame_entities = []
        self.lexical_units = []
        self.non_core_entities = []

    def object(self):
        for item in self.title:
            for property in self.core_frame_entities:
                if property.matches(item):
                    return item.name

    def is_described(self):
        return self._do_core_frame_entities_exist() and self._do_lexical_units_exist()

    def _do_core_frame_entities_exist(self):
        return self._does_match_exist(self.core_frame_entities)

    def _do_lexical_units_exist(self):
        return self._does_match_exist(self.lexical_units)

    def _does_match_exist(self, properties):
        for item in self.title:
            for property in properties:
                if property.matches(item):
                    return True


class Subject(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class PersonSubject(Subject):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class Object(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class Verb(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class Application(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.preceded_by = ["BeginApplicationProcess"]
        self.followed_by = ["ApplicationDecision"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationDecision(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.preceded_by = ["Application"]
        self.followed_by = ["ApplicationGranted", "ApplicationDenied"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationGranted(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.preceded_by = ["ApplicationDecision"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationDenied(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.preceded_by = ["ApplicationDecision"]


class SignIn(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.core_frame_entities = [Object("", accept_any_name=True)]
        self.lexical_units = [Verb("get"), Verb("Apply")]
        self.non_core_entities = [PersonSubject]
        self.preceded_by = []
        self.preceded_by = ["ApplicationGranted"]


class BeginApplicationProcess(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs)
        self.core_frame_entities = [Object("", accept_any_name=True)]
        self.lexical_units = [Verb("get"), Verb("Apply")]
        self.non_core_entities = [PersonSubject]
        self.preceded_by = []
        self.leads_to = ["Application"]


if __name__ == '__main__':
    inserts = {}
    for title in [[Verb("Apply"), "for", Object("Universal Credit")], [Verb("Sign in"), "to", "your", Object("Universal Credit")]]:
        for process in [BeginApplicationProcess(title), SignIn(title)]:
            if process.is_described():
                if not process.object() in inserts:
                    inserts[process.object()]
                inserts[process.object()].append(process)
    print(inserts)

