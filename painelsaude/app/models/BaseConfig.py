class BaseConfig:
    __instance = None

    _host = None 
    _database = None 
    _user= None 
    _passwd= None 
    _port = None 
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if BaseConfig.__instance == None:
            BaseConfig()
        return BaseConfig.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if BaseConfig.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            BaseConfig.__instance = self