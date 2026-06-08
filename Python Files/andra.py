# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:15:42 2021

@author: Ramya
"""

import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('andrapradesh.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[15,79], zoom_start=7)
tooltip='Click For Storm Info'

folium.Marker([14.6819,77.6006],
              popup='*Anantapur\n *Rain \n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([13.13,79.08],
              popup='*Chittoor\n*Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),


folium.Marker([14.4426,79.9865],
              popup='*Nellore\n*Thunderstorm \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([17.6868, 83.2185],
              popup='*Vishakhapatnam\n*Gentle Breeze \n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

m.add_child(fg)

m.save('andra.html')
