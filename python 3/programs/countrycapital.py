def createcapitalList():
    capital= dict()
    
    capital["US"] = "Washington D.C."
    capital["China"]= "Beijing"
    capital["Germany"] = "Berlin"
    capital["France"] =  "Paris"
    capital["UK"] = "London"
    capital["India"]= "New Delhi"
    capital["JJ"] = "stupid"
    return capital
country_capital = createcapitalList()
len_country =0

for key in country_capital:
    if (len(key) > len_country):
        len_country =len(key)

print("Countries and their Capitals:")
for key in country_capital:
    print("{country}: {capital}".format(country =key.ljust(len_country+1),capital = country_capital[key]))
