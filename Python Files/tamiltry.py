# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:18:39 2021

@author: Ramya
"""





import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('tamil.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[11,79], zoom_start=7)
tooltip='Click For Storm Info'

folium.Marker([13.0827,80.2707],
              popup='*Chennai\n *Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([12.8185,79.6947],
              popup='*Kanchipuram\n*Heavy Rain \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

folium.Marker([9.9252,78.1198],
              popup='*Madurai\n*Hurricane \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

folium.Marker([8.7642,78.1348],
              popup='*Thoothukudi\n*Rain \n *Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([10.7870,79.1378],
              popup='*Thanjavur\n*Lightning \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([12.9165,79.1325],
              popup='*Vellore\n*Lightning \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([13.1231,79.9120],
              popup='Thiruvallur\nHeavy Rain \nOrange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([12.1211,78.1582],
              popup='*Dharmapuri\n*Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([11.0168,76.9558],
              popup='*Coimbatore\n*Gentle Freeze \n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([10.7905,78.7047],
              popup='*Tiruchirappalli\n*Lightning \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([8.0883,77.5385],
              popup='*Kannyakumari\n*Hurricane\n*Red Aert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([11.3410,77.7172],
              popup='*Erode\n*Hot air\n*Green zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
m.add_child(fg)

m.save('samp.html')
