class Father:
    def father_skill(self):
        print("Driving")
class Mother:
    def mother_skill(self):
        print("Cooking")
class Child(Father,Mother):
    pass
c=Child()
c.father_skill()
c.mother_skill()