import leafmap
import solara
import pandas as pd
import openpyxl

zoom = solara.reactive(9)
center = solara.reactive((13.4,41))


class Map(leafmap.Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add what you want below
        # self.add_stac_gui()
        urlname='https://raw.githubusercontent.com/pd-allen/pd-allen.github.io/main/docs/8thHussarsItaly.geojson'

     

        self.add_geojson(urlname,layer_name='routename',style = {
                "stroke": True,
                "color": 'blue',
                "weight": 4,
                "opacity": 1,
                "fill": False,
                "fillColor": "#0000ff",
                "fillOpacity": 0.1,
            })
        fname= 'https://raw.githubusercontent.com/pd-allen/pd-allen.github.io/main/docs/8thHussarsItaly.xlsx'

        data =  pd.read_excel(fname,dtype={'Comments': str},na_values=[''])
        self.add_points_from_xy(data, x="Longitude", y="Latitude",color="red",popup=["Location","Date", "Comments"],layer_name='points')
        self.add_layer_control()
        self.add_basemap("OpenTopoMap")
        
#print(data)
@solara.component
def Page():
    with solara.Column(style={"min-width": "500px"}):
        # solara components support reactive variables
        # solara.SliderInt(label="Zoom level", value=zoom, min=1, max=20)
        # using 3rd party widget library require wiring up the events manually
        # using zoom.value and zoom.set
        Map.element(  # type: ignore
            zoom=zoom.value,
            on_zoom=zoom.set,
            center=center.value,
            on_center=center.set,
            scroll_wheel_zoom=True,
            toolbar_ctrl=False,
            data_ctrl=False,
            height="780px",
        )
       
        #Map.add_basemap("OpenTopoMap")

    solara.Text(f"Zoom: {zoom.value}")
    solara.Text(f"Center: {center.value}")