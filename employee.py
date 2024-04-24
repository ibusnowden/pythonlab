class Employee:
    def __init__(self, __name, __ID_Number, __department, __job_title):
        self.__name = __name
        self.__ID__Number = __ID_Number
        self.__department = __department
        self.__job_title = __job_title

    def __str__(self):
        return f'{self.__name}\t{self.__ID__Number}\t{self.__department}\t{self.__job_title}'
