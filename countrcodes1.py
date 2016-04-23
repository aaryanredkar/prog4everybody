country= {"India": 91, "UK": 44, "Austraila": 61, "France":33, "Italy": 39, "US":1,"Afghanistan":93}
print (country)
for key in country.keys():
    v = str(country[key])    
    print ('{0:15} {1}'.format(key,v))
