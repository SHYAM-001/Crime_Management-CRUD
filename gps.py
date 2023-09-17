import geocoder
import folium

g=geocoder.ip('157.51.162.166')

myaddress = g.latlng

print(myaddress)

my_map1 = folium.Map(location=myaddress,zoom_start=12)
marker=folium.Marker(location=myaddress)
marker.add_to(my_map1)

my_map1.save('mylocation1.html')

import os
filename ='mylocation1.html'
if os.name == 'nt':
    browser = 'start'
else:
    browser = 'open'
os.system('{} {}'.format(browser, filename))

