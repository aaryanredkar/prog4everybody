def createlist():
    country_code= dict()
    country_code["India"] = 91
    country_code["UK"] = 44
    country_code["Austraila"] = 61
    country_code["France"] = 33
    country_code["Italy"] = 39
    return country_code


phone_codes = createlist()
print("Country dialing code for India is", phone_codes["India"])
    
