# Importing the folium modual.
import folium
from folium import IFrame
import base64


# Storing the map with starting location and zoom in a variable.
map = folium.Map(location=[35.677830, 139.714499], zoom_start=17)

# Here we are adding a marker onto our map,
# First we set the location,
# Then we add the popup method adn enter the text to popup,
# Then we use the icon method and enter the color we want it to show.
# Here we have added in a few restarants around the olympic park.
# Using onlinr resorses we hace got custom icons for diffrent markers.

map.add_child(folium.Marker(location=[35.676635, 139.712433], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.678827, 139.710568], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.680049, 139.716088], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.679535, 139.719275], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.675206, 139.709339], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.674572, 139.709487], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.673649, 139.712344], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))

# Here we are using a tooltip method to add a message on out marker.
tooltip1 = "Kasumigaokamachi stadium"
tooltip2 = "Meiji Jingu Stadium"
tooltip3 = "jingu secondary stadium"
tooltip4 = "Metropolitan Gymnasium Futsal Court"
tooltip5 = "Metropolitan Gymnasium"
tooltip6 = "Historical landmark"
tooltip7 = "Historical landmark"
tooltip8 = "Japan Olympic Museum"
tooltip9 = "Chichibunomiya Rugby Stadium"
tooltip10 = "Meiji Jingu Gaien Ice Skating Rink"
tooltip11 = "Meiji Jingū Gaien Rubber Baseball Field"
tooltip12 = "聖徳記念絵画館前広場 (Plaza)"

# Base64 to help decode adn encode images into html.
html = '<img src="data:image/png;base64,{}">'.format

# Here we have added our first pop up image onto the screen, picture 1.
picture1 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/Kasumigaokamachi.jpg','rb').read()).decode()
iframe1 = IFrame(html(picture1), width=400+15, height=300+15)
popup1 = folium.Popup(iframe1, max_width=600)
icon1 = icon=folium.Icon(color='green')
marker1 = folium.Marker(location=[35.677916, 139.714545], popup=popup1, tooltip=tooltip1, icon=icon1).add_to(map)


# Picture 2
picture2 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/stadium1.jpg','rb').read()).decode()
iframe2 = IFrame(html(picture2), width=400+15, height=300+15)
popup2 = folium.Popup(iframe2, max_width=600)
icon2 = icon=folium.Icon(color='green')
marker2 = folium.Marker(location=[35.674270, 139.716959], popup=popup2, tooltip=tooltip2, icon=icon2).add_to(map)


# Picture 3
picture3 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/second.jpg','rb').read()).decode()
iframe3 = IFrame(html(picture3), width=400+15, height=300+15)
popup3 = folium.Popup(iframe3, max_width=600)
icon3 = icon=folium.Icon(color='green')
marker3 = folium.Marker(location=[35.675993, 139.716263], popup=popup3, tooltip=tooltip3, icon=icon3).add_to(map)

# Picture 4
picture4 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/gym.jpg','rb').read()).decode()
iframe4 = IFrame(html(picture4), width=400+15, height=300+15)
popup4 = folium.Popup(iframe4, max_width=600)
icon4 = icon=folium.Icon(color='green')
marker4 = folium.Marker(location=[35.678594, 139.712182], popup=popup4, tooltip=tooltip4, icon=icon4).add_to(map)

# Picture 5
picture5 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/gym2.jpg','rb').read()).decode()
iframe5 = IFrame(html(picture5), width=400+15, height=300+15)
popup5 = folium.Popup(iframe5, max_width=600)
icon5 = icon=folium.Icon(color='green')
marker5 = folium.Marker(location=[35.679792, 139.712508], popup=popup5, tooltip=tooltip5, icon=icon5).add_to(map)

# Picture 6
picture6 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/history.jpg','rb').read()).decode()
iframe6 = IFrame(html(picture6), width=400+15, height=300+15)
popup6 = folium.Popup(iframe6, max_width=600)
icon6 = icon=folium.Icon(color='blue', icon="glyphicon-header")
marker6 = folium.Marker(location=[35.679775, 139.711419], popup=popup6, tooltip=tooltip6, icon=icon6).add_to(map)

# Picture 7
picture7 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/history2.jpg','rb').read()).decode()
iframe7 = IFrame(html(picture7), width=400+15, height=300+15)
popup7 = folium.Popup(iframe7, max_width=600)
icon7 = icon=folium.Icon(color='blue', icon="glyphicon-header")
marker7 = folium.Marker(location=[35.679417, 139.717373], popup=popup7, tooltip=tooltip7, icon=icon7).add_to(map)

# Picture 8
picture8 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/musium.jpg','rb').read()).decode()
iframe8 = IFrame(html(picture8), width=400+15, height=300+15)
popup8 = folium.Popup(iframe8, max_width=600)
icon8 = icon=folium.Icon(color='blue', icon="glyphicon-home")
marker8 = folium.Marker(location=[35.674920, 139.715184], popup=popup8, tooltip=tooltip8, icon=icon8).add_to(map)

# Picture 9
picture9 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/rugby.jpg','rb').read()).decode()
iframe9 = IFrame(html(picture9), width=400+15, height=300+15)
popup9 = folium.Popup(iframe9, max_width=600)
icon9 = icon=folium.Icon(color='green')
marker9 = folium.Marker(location=[35.672738, 139.718335], popup=popup9, tooltip=tooltip9, icon=icon9).add_to(map)

# Picture 10 
picture10 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/ice.jpg','rb').read()).decode()
iframe10 = IFrame(html(picture10), width=400+15, height=300+15)
popup10 = folium.Popup(iframe10, max_width=600)
icon10 = icon=folium.Icon(color='green')
marker10 = folium.Marker(location=[35.680303, 139.714809], popup=popup10, tooltip=tooltip10, icon=icon10).add_to(map)

# Picture 11
picture11 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/rubber.png','rb').read()).decode()
iframe11 = IFrame(html(picture11), width=400+15, height=300+15)
popup11 = folium.Popup(iframe11, max_width=600)
icon11 = icon=folium.Icon(color='green')
marker11 = folium.Marker(location=[35.676709, 139.718876], popup=popup11, tooltip=tooltip11, icon=icon11).add_to(map)

# Picture 12
picture12 = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/plaza.jpg','rb').read()).decode()
iframe12 = IFrame(html(picture12), width=400+15, height=300+15)
popup12 = folium.Popup(iframe12, max_width=600)
icon12 = icon=folium.Icon(color='blue', icon="glyphicon-home")
marker12 = folium.Marker(location=[35.677883, 139.718066], popup=popup12, tooltip=tooltip12, icon=icon12).add_to(map)

# Here we will put the diffrenc olour codes into different feture groupes we so we can turn them on and of to use as a menue.

fg_red_markers = folium.FeatureGroup(name = "Restaurants")
fg_red_markers.add_child(map.add_child(folium.Marker(location=[35.676635, 139.712433], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.678827, 139.710568], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.680049, 139.716088], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.679535, 139.719275], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.675206, 139.709339], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.674572, 139.709487], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))
map.add_child(folium.Marker(location=[35.673649, 139.712344], popup="Restaurant", icon=folium.Icon(color='red', icon="glyphicon-cutlery")))):

fg_green_markers = folium.FeatureGroup(name = "Olympic attractions")

fg_blue_markers = folium.FeatureGroup(name = "Land marks")

map.add_child(fg_red_markers)
map.add_child(fg_green_markers)
map.add_child(fg_blue_markers)

map.add_child(folium.LayerControl())

# Saving the code in a html file.
map.save("alextokyointeractivemap.html")


# Picture 
# picture = base64.b64encode(open('C:/Users/Alex/Documents/Programming/InteractiveMAP/images/','rb').read()).decode()
# iframe = IFrame(html(picture), width=400+15, height=300+15)
# popup = folium.Popup(iframe, max_width=600)
# icon = icon=folium.Icon(color='green')
# marker = folium.Marker(location=[], popup=popup, tooltip=tooltip, icon=icon).add_to(map)