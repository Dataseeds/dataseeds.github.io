import folium

from IPython.display import HTML, display

m = folium.Map(location=[32, 0],
               zoom_start=4.3,
               tiles = "CartoDB positron",
               max_zoom = 100)

def colorPicker(population):
    if population < 10000000:
        return 'green'
    elif population >= 10000000 and population < 500000000:
        return 'orange'
    else:
        return 'red'

folium.GeoJson(open('population.json', 'r', encoding='utf-8-sig').read(),
               name = 'Population',
               style_function = lambda x: {'fillColor': colorPicker(x['properties']['POP2005'])},
               tooltip = folium.GeoJsonTooltip(fields=('NAME', 'POP2005',),
                                               aliases=('Country','Population')),
               show = True).add_to(m)


#folium.LayerControl().add_to(m)
m

m.save('test.html')


# LDN_COORDINATES = (51.5074, 0.1278) 
# myMap = folium.Map(location=LDN_COORDINATES, zoom_start=12)
# myMap._build_map()
# mapWidth, mapHeight = (400,500) # width and height of the displayed iFrame, in pixels
# srcdoc = myMap.HTML.replace('"', '&quot;')
# embed = HTML('<iframe srcdoc="{}" '
#              'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
#              'border: none"></iframe>'.format(srcdoc, width, height))
# embed