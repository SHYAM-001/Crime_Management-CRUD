
def phone():
    import phonenumbers
    import opencage
    import folium
    from myphone import number
    from opencage.geocoder import OpenCageGeocode
    from phonenumbers import geocoder
    from phonenumbers import carrier
    pepnumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber,"en")
    print(location)
    service_pro=phonenumbers.parse(number)
    print(carrier.name_for_number(service_pro, "en"))
    key = '15836a8f01724c60b05865e4ca77a506'
    geocoder = OpenCageGeocode(key)
    query=str(location)
    results=geocoder.geocode(query)
    #print(results)
    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
    print(lat,lng)
    myMap=folium.Map(location=[lat,lng],zoom_start= 9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html") 
    import os
    filename ='mylocation.html'
    
# Get the default browser command depending on the OS
    if os.name == 'nt':
        # For Windows
        browser = 'start'
    else:
        # For Mac and Linux
        browser = 'open'
    # Open the file in the default browser
    os.system('{} {}'.format(browser, filename))


phone()
