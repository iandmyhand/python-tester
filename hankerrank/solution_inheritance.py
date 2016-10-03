class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        _sum = 0
        for _score in self.scores:
            _sum += _score
        _average = _sum / len(self.scores)
        if 90 <= _average <= 100:
            return 'O'
        elif 80 <= _average < 90:
            return 'E'
        elif 70 <= _average < 80:
            return 'A'
        elif 55 <= _average < 70:
            return 'P'
        elif 40 <= _average < 5:
            return 'D'
        return 'T'


if "__main__" == __name__:
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
