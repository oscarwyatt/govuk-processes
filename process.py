from property import Property
import processes.application_process as application_process


class Process(Property):
    def __init__(self, title, **kwargs):
        super().__init__(title, **kwargs)
        self.title = title
        self.core_frame_entities = []
        self.lexical_units = []
        self.non_core_entities = []
        self.preceded_by = []
        self.followed_by = []

    def object(self):
        for item in self.title:
            for property in self.core_frame_entities:
                if property.matches(item):
                    return item.name

    def link_to(self, other_process, preceeding=False, following=False):
        # TODO: Refactor this so it's less mind bending
        if preceeding:
            for preceding_process in self.preceded_by:
                preceding_process = self._str_to_instance(preceding_process)
                if preceding_process.matches(other_process):
                    other_process.followed_by.append(self)
                    self.preceding_process.append(other_process)
                    return True
                if preceding_process.link_to(other_process, preceeding=True, following=False):
                    preceding_process.followed_by.append(self)
                    self.preceding_process.append(preceding_process)
                    return True
        if following:
            for following_process in self.followed_by:
                following_process = self._str_to_instance(following_process)
                if following_process.matches(other_process):
                    other_process.preceded_by.append(self)
                    self.followed_by.append(other_process)
                    return True
                if following_process.link_to(other_process, preceeding=False, following=True):
                    following_process.preceded_by.append(self)
                    self.followed_by.append(following_process)
                    return True
        return False

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

    def _str_to_instance(self, instance_or_instance_name):
        if isinstance(instance_or_instance_name, str):
            # This will have to change when there are more process types
            instance_or_instance_name = getattr(application_process, instance_or_instance_name)("", accept_any_name=True)
        return instance_or_instance_name
