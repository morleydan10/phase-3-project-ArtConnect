class Business:


    def __init__(self, name, city, type, image) -> None:
        self.name:str = name
        self.city:str = city
        self.type:str = type
        self.image = image
        # self.rating = rating
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

# **************************************CITY**************************************

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        is_string = isinstance(city, str)
        valid_length = 2 <= len(city) <= 20
        if is_string and valid_length:
            self._city = city
        else:
            raise Exception("City must be a string between 2 and 20 characters.")

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
# *************************************IMAGE*************************************
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image
        # is_string = isinstance(image, str)
        # valid_length = 2 <= len(image) <= 20
        # if is_string and valid_length:
        # else:
        #     raise Exception("Image must be a string between 2 and 20 characters.")

# ***********************************DATE_JOINED**********************************
# # Will automatically be assigned when profile is made
#     @property
#     def date_joined(self):
#         return self._date_joined

#     @date_joined.setter
#     def date_joined(self, date_joined):
#         is_string = isinstance(type, str)
#         valid_date_length = len(date_joined) == 10
#         valid_format = date_joined.index("/") == 2
#         if is_string and valid_date_length and valid_format:
#             self._date_joined = date_joined
#         else:
#             raise Exception("Date must be a string in MM/DD/YYYY format.")

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
        rating_counter= 0
        for rating in self.ratings:
            rating_counter += rating
        average_rating = rating_counter / len(self.ratings)
        return average_rating
    
    # **************to dict*************************

    def to_dict(self):
        return {"name":self.name,
                "city": self.city,
                "type": self.type,
                # "rating": self.rating,
                "image": self.image}