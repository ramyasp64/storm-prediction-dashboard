# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:53:48 2021

@author: Ramya
"""

import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('goa.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[15,74], zoom_start=7)
tooltip='Click For Storm Info'

folium.Marker([15.5163,73.9830],
              popup='*North Goa\n *Lightning \n*Red Alert Area',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 



m.add_child(fg)

m.save('goa.html')
