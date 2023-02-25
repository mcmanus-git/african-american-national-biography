from dash import html, register_page, dcc  #, callback # If you need callbacks, import it here.
from visualizations.create_vis import create_visualizations

register_page(
    __name__,
    name='AANB Data Exploration',
    top_nav=True,
    path='/'
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
                    "African American National Biography Data Exploration"
                ]
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
