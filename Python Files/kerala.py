# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:53:11 2021

@author: Ramya
"""

import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('kerala.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[10,76], zoom_start=7)
tooltip='Click For Storm Info'
iframe = folium.IFrame(
                       width=500,
                       height=500)

folium.Marker([9.4981, 76.3388],
              
           #  popup="<b>Place :</b>Alappuzha<br><b>Climatic condition :</b>Heavyrain<br><b>Zone :</b>Orange Zone<br>",
              popup = folium.Popup(iframe,
                     max_width=500),
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 

folium.Marker([9.9816,76.2999],
              popup='*Ernakulam\n*Heavy Rain \n*Orange Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),


folium.Marker([8.5241,76.9366],
              popup='*Thiruvananthapuram\n*Clear clouds \n *Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([10.7867,76.6548],
              popup='*Palakkad\n*Hot air \n*Green Zone',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

m.add_child(fg)

m.save('kerala.html')
