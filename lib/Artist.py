class Artist:


    def __init__(self, name, city, date_joined, rating, discipline, requests = [], ratings =[]) -> None:
        self.name:str = name
        self.city:str = city
        self.date_joined:str = date_joined
        self.rating:(int, float) = rating
        self.discipline:str = discipline
        self.requests = requests
        self.ratings = ratings

    # ***********************NAME****************************************
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        is_string = isinstance(name, str)
        valid_length = 2 <= len(name) <= 20
        if is_string and valid_length:
            self._name = name
        else:
            return Exception("Name must be a string between 2 and 20 characters.")

# *********************************CITY************************************
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

# *************************************DATE**********************************
    @property
    def date_joined(self):
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        is_string = isinstance(date_joined, str)
        valid_date_length = len(date_joined) == 10
        valid_format = date_joined.index("/") == 2
        if is_string and valid_date_length and valid_format:
            self._date_joined = date_joined
        else:
            raise Exception("Date must be a string in MM/DD/YYYY format.")

# ***************************************RATING*********************************
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        # Add any validation logic if needed
        self._rating = rating

# ************************************DISCIPLINE**********************************
    @property
    def discipline(self):
        return self._discipline

    @discipline.setter
    def discipline(self, discipline):
        is_string = isinstance(discipline, str)
        valid_length = 2 <= len(discipline) <= 20
        if is_string and valid_length:
            self._discipline = discipline
        else:
            raise Exception("Discipline must be a string between 2 and 20 characters.")

# *********************************METHODS***************************************
    def most_common_business(self):
        pass


    def avergage_rating(self):
        pass