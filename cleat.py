class Month(object):

    def __init__(self, name, birthdaymonth):
        print("Tyreese's birthday Month!")
        self.name = name
        self.__birthdaymonth = birthdaymonth

    def talk(self):
        print("\nI'm", self.name)
        print("My bithday month is", self.__birthdaymonth, "\n")

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a private method.")
        self.__private_method()

mont = Month(name = "Tyreese", birthdaymonth = "August")
mont.talk()
mont.public_method()

        