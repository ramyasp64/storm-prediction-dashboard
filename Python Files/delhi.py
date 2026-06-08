# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:25:54 2021

@author: Ramya
"""


import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('delhi.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[28,77], zoom_start=7)
tooltip='Click For Storm Info'

folium.Marker([28.6643,77.2167],
              popup='*Central\n *Heavy Rain \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([28.7886,77.1412],
              popup='*North\n*Haze \n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),




m.add_child(fg)

m.save('delhi.html')
