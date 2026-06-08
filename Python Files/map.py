import folium
import os
import json
fg=folium.FeatureGroup("mymap")
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))
m=folium.Map(location=[20,78], zoom_start=5)
tooltip='Click For Storm Info'
folium.Marker([11.059821,78.387451],
              popup='<a herf="tamilnadu"><button><strong>Tamil Nadu</strong></button></a>',              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 
folium.Marker([17.123184,79.208824],
              popup='<strong><button>Telangana</button></strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([23.473324,77.947998],
              popup='<strong><button>Madhya Pradesh</button></strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

folium.Marker([10.8505,76.2711],
              popup='<a herf="kerala"><button><strong>Kerala</strong></button></a>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
          #    response = redirect('/redirect-success/') 
folium.Marker([15.9129,79.7400],
              popup='<button><strong>Andra Pradesh<strong></button>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([15.2993,74.1240],
              popup='<button><strong>Goa</strong></button>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([28.644800,77.216721],
              popup='<button><strong>Delhi</strong></button>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),

m.add_child(fg)
m.save('map.html')