class Employes:
    def setName(self):
        self.name = input ("Enter name:   ")
    def setHours(self):
        self.hours = int(input("Enter hours:   "))
    def setHourpay(self):
        self.hourpay = int(input("Enter hourpay:   "))
    def calculate(self):
        self.salary = self.hours * self.hourpay
    def display(self):
        print("name is: ", self.name)
        print("salary is: ", self.salary)

em = Employes()
em.setName()
em.setHours()
em.setHourpay()
em.calculate()

print("result is: ")
em.display()