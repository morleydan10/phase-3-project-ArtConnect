class Request:


    def __init__(self, artist, business, date, compensation) -> None:
        self._artist = artist
        self._business = business
        self._date:str = date
        self._compensation: (str, float) = compensation

# *********************ARTIST********************************************
    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        from lib.Artist import Artist
        valid_artist = isinstance(artist, Artist)
        if valid_artist:
            self._artist = artist
        else:
            raise Exception("Must be an Artist.")

# ****************************************BUSINESS*****************************
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, business):
        from lib.Business import Business
        valid_business = isinstance(business, Business)
        if valid_business:
            self._business = business
        else:
            raise Exception("Business must be a business.")

# *****************************************DATE******************************

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        is_string = isinstance(type, str)
        valid_date_length = len(date) == 10
        valid_format = date.index("/") == 2
        if is_string and valid_date_length and valid_format:
            self._date = date
        else:
            raise Exception("Date must be a string in MM/DD/YYYY format.")

# *********************************COMPENSATION********************************

    @property
    def compensation(self):
        return self._compensation

    @compensation.setter
    def compensation(self, compensation):
        is_number = isinstance(compensation, (str, float))
        if is_number:
            self._compensation = compensation
        else:
            raise Exception("Compensation must be a float/integer.")