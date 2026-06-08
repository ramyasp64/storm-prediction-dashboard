# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:25:54 2021

@author: Ramya
"""


import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('madhya.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[22,78], zoom_start=7)
tooltip='Click For Storm Info'

folium.Marker([23.2599,77.4126],
              popup='*Bhopal\n *Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([26.2183,78.1828],
              popup='*Gwalior\n*Heavy Rain\n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([23.8343,80.3894],
              popup='*Katni\n *Sunny\n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([23.1765,75.7885],
              popup='*Ujjain\n*Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),


m.add_child(fg)

m.save('madhya.html')
