class Person(object):
    def __init__(self,id, first_name,last_name,age,phone):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.age=age
        self.phone=phone
    def __str__(self):
        return"[%s,%s,%s,%s,%s]"%(self.id,self.first_name,self.last_name,self.age,self.phone)




joe = Person("1","joe","Smith",23, "787-890-2020")
print "joe age:",joe.age
print"joe phone", joe.phone

print"joe:",joe




