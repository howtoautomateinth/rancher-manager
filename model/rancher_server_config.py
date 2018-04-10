class RancherServerConfig(object):

    def __init__(self):
        self.service_id = None
        self.environment = None
        self.name = None

    @property
    def service_id(self):
        return self.__service_id

    @service_id.setter
    def service_id(self, service_id):
        self.__service_id = service_id

    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment):
        self.__environment = environment

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name