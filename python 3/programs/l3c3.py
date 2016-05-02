def createDictionary():
    eng_spanish = dict()
    eng_spanish ["Hello"] = "Hola"
    eng_spanish ["Cheap"] = "Barato"
    eng_spanish ["Dress"] = "Vestido"
    eng_spanish ["Hello"] = "Hola"
    eng_spanish ["I do not like"] = "Me gusta "
    eng_spanish ["JayJay is very ugly"] = "JayJay es muy feo"
    eng_spanish ["dance"] = "bailar"
    
    
      
    
    
    return eng_spanish
dictionary = createDictionary()
val = input("Enter english word:")
print (val, "in spanish is",dictionary[val])
print()
print (val,"Printing all the English and Spanish words:")
for key in sorted (dictionary.keys()):
    print ("%s:%s"% (key,dictionary[key]))
