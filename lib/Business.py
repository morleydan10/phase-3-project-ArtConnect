class Business:


    def __init__(self, name, location, type, date_joined) -> None:
        self.name:str = name
        self.location:str = location
        self.type:str = type
        self.date_joined:str = date_joined
        self.requests = []
        self.ratings = []

# ***********************NAME****************************************

    @property
    def name(self):
        return self._name

    # What if business name includes numbers, i.e. 123 Inc. ?
    @name.setter
    def name(self, name):
        is_string = isinstance(name, str)
        valid_length = 2 <= len(name) <= 20
        if is_string and valid_length:
            self._name = name
        else:
            return Exception("Name must be a string between 2 and 20 characters.")

# **************************************LOCATION**************************************

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        is_string = isinstance(location, str)
        valid_length = 2 <= len(location) <= 20
        if is_string and valid_length:
            self._location = location
        else:
            raise Exception("Location must be a string between 2 and 20 characters.")

# *****************************************TYPE***************************************

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        is_string = isinstance(type, str)
        valid_length = 2 <= len(type) <= 20
        if is_string and valid_length:
            self._type = type
        else:
            raise Exception("Type must be a string between 2 and 20 characters.")

# ***********************************DATE_JOINED**********************************
# Will automatically be assigned when profile is made
    @property
    def date_joined(self):
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        is_string = isinstance(type, str)
        valid_date_length = len(date_joined) == 10
        valid_format = date_joined.index("/") == 2
        if is_string and valid_date_length and valid_format:
            self._date_joined = date_joined
        else:
            raise Exception("Date must be a string in MM/DD/YYYY format.")

# **********************************METHODS****************************************

    def create_request(self, new_request):
        from lib.Request import Request
        unique_request = new_request not in self.requests
        valid_request = isinstance(new_request, Request)
        if unique_request and valid_request:
            self.requests.append(new_request)
        else:
            raise Exception('Request already exists/Must be a valid request.')
        

    def most_used_artist(self):
        pass


    def avergage_rating(self):
        pass