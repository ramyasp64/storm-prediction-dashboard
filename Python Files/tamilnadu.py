# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:17:51 2021

@author: Ramya
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:40:44 2021

@author: Ramya
"""


import folium
import os
import json


fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('tamil.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[20,78], zoom_start=55)
tooltip='Click For Storm Info'
#vis=os.path.join('Data','Project json code.json')
folium.Marker([11.059821,78.387451],
              popup='<strong>Tamil Nadu</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
               


m.add_child(fg)

m.save('model.html')
