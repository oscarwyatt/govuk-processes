from process import Process
from property import *


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class Application(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preceded_by = ["BeginApplicationProcess"]
        self.followed_by = ["ApplicationDecision"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationDecision(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preceded_by = ["Application"]
        self.followed_by = ["ApplicationGranted", "ApplicationDenied"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationGranted(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preceded_by = ["ApplicationDecision"]
        self.followed_by = ["SignIn"]


# I think that to better encapsulate the process, this may need to inherit from InternalProcess or something
class ApplicationDenied(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preceded_by = ["ApplicationDecision"]


class SignIn(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.core_frame_entities = [Object("", accept_any_name=True)]
        self.lexical_units = [Verb("get"), Verb("Apply")]
        self.non_core_entities = [PersonSubject]
        self.preceded_by = ["ApplicationGranted"]


class BeginApplicationProcess(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.core_frame_entities = [Object("", accept_any_name=True)]
        self.lexical_units = [Verb("get"), Verb("Apply")]
        self.non_core_entities = [PersonSubject]
        self.preceded_by = []
        self.followed_by = ["Application"]
