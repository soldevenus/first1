animals=['cat','dog','mouse','cow']
for animal in animals:
    print animal

horizontal="cat dog mouse cow"
horizontal=""
for animal in animals:
    horizontal=horizontal+" "+animal
print horizontal


ages=[18,21,14,7,90,12]
total_age=0
for age in ages:
    total_age +=age
print 'total:',total_age

print"average ages:",total_age/len(ages)

print"len :",len(ages)

def has_negative(L):
# esto es una prueba
#me fui
