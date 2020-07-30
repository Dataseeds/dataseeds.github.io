import folium

from IPython.display import HTML, display

# m = folium.Map(location=[32, 0],
#                zoom_start=4.3,
#                tiles = "Mapbox Control Room",
#                prefer_canvas = True,
#                max_zoom = 7)

m = folium.Map(
   location=[32, 0],
   zoom_start=3,
   max_zoom = 7,
   tiles='http://{s}.tiles.mapbox.com/v3/mapbox.control-room/{z}/{x}/{y}.png',
   attr='Mapbox attribution')

def colorPicker(population):
    if population < 10000000:
        return 'green'
    elif population >= 10000000 and population < 500000000:
        return 'orange'
    else:
        return 'red'

folium.GeoJson(open('population.json', 'r', encoding='utf-8-sig').read(),
               name = 'Population',
               style_function = lambda x: {
                   'fillColor': colorPicker(x['properties']['POP2005'])
                   },
               tooltip = folium.GeoJsonTooltip(fields=('NAME', 'POP2005',),
                                               aliases=('Country','Population')),
               show = True).add_to(m)


#folium.LayerControl().add_to(m)
# m
m.save('test.html')


