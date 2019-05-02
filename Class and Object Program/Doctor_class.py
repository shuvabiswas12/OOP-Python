class Doctor:

    def __init__(self):
        self._no_of_patient = None  # private variable
        self._passing_year = None  # private variable
        self._earning_per_day = None  # private variable

    @property
    def no_of_patient(self):
        print('Getter called for no_of_patient')
        return self._no_of_patient

    @property
    def passing_year(self):
        print('Getter called passing_year')
        return self._passing_year

    @property
    def earning_per_day(self):
        print('Getter called for earning_per_day')
        return self._earning_per_day

    @no_of_patient.setter
    def no_of_patient(self, value):
        print('Setter called for no_of_patient')
        self._no_of_patient = value

    @no_of_patient.deleter
    def no_of_patient(self):
        print('deleter called for no_of_patient')
        del self._no_of_patient

    @passing_year.setter
    def passing_year(self, value):
        print('Setter called passing_year')
        self._passing_year = value

    @passing_year.deleter
    def passing_year(self):
        print('deleter called passing_year')
        del self._passing_year

    @earning_per_day.setter
    def earning_per_day(self, value):
        print('Setter called passing_year')
        self._earning_per_day = value

    @earning_per_day.deleter
    def earning_per_day(self):
        print('Deleter called passing_year')
        del self._earning_per_day



