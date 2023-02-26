from dash import html, register_page, dcc  #, callback # If you need callbacks, import it here.
from visualizations.create_vis import create_visualizations

register_page(
    __name__,
    name='AANB Data Exploration',
    top_nav=True,
    path='/',
    description="African American National Biography Data Exploration"
)

# Create Visualizations
life_expectancy_vis, \
    education_total_vis, \
    ever_enslaved_vis, \
    before_thirteenth_vis, \
    runaways_rebels_vis, \
    religion_vis \
    = create_visualizations()

vis_style = {
    'padding': '5% 0% 5% 0%'
}


def layout():
    layout = html.Div(
        [
            html.H1(
                [
                    "African American National Biography"
                ],
                style={
                    'text-align': 'center'
                }
            ),
            html.H2(
                [
                    "Data Exploration"
                ],
                style={
                    'text-align': 'center'
                }
            ),
            dcc.Markdown(
                """This dashboard is an exploration of a subset of data derived from the 
                [African American National Biography](https://hutchinscenter.fas.harvard.edu/AANB) of over 1,300 people 
                who lived prior to ratification of The 13th Amendment of the United States Constitution between the 
                years 1508-1865. Below you will find some visualizations which aim to gain a clearer picture of people
                living during this time. If you would like a more detailed view of individuals, please visit the 
                [Biographies Page](/bios). 
                ***Prior to exploring this data and for more information about the dataset please see our*** 
                [About Page](/about).""",
                dangerously_allow_html=True,
                style={
                    'padding': '5% 5% 5% 5%'
                }
            ),
            html.Div(
                [
                    dcc.Graph(figure=life_expectancy_vis),
                ],
                style=vis_style
            ),
            html.Div(
                [
                    dcc.Graph(figure=education_total_vis),
                ],
                style=vis_style
            ),
            html.Div(
                [
                    dcc.Graph(figure=ever_enslaved_vis),
                ],
                style=vis_style
            ),
            html.Div(
                [
                    dcc.Graph(figure=before_thirteenth_vis),
                ],
                style=vis_style
            ),
            html.Div(
                [
                    dcc.Graph(figure=runaways_rebels_vis),
                ],
                style=vis_style
            ),
            html.Div(
                [
                    dcc.Graph(figure=religion_vis),
                ],
                style=vis_style
            ),
        ],
        style={
            'padding': '5% 5% 5% 5%'
        }
    )
    return layout
