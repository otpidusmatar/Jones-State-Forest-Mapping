import json
import pandas as pd
import folium

ph = pd.read_csv('CSVs/alkalinity.csv', index_col=0)

with open('GeoJSONS/regionsmap.geojson') as f:
    point_map = json.load(f)

divisions = [0, 0.25, 0.5, 0.75, 1]
quantiles = list(ph['ph'].quantile(divisions))
m = folium.Map(location=[30.227639, -95.494779], zoom_start=17)
folium.Choropleth(
    geo_data=point_map,
    name='JSF',
    data=ph,
    columns=["sample", "ph"],
    key_on='feature.properties.sampleregion',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.3,
    bins=quantiles,
    legend_name='pH of Sample by Location',
).add_to(m)

folium.LayerControl().add_to(m)

m.save("OutputMaps/alkalinitymap.html")