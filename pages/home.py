from dash import html, register_page, dcc  #, callback # If you need callbacks, import it here.
from visualizations.create_vis import create_visualizations

register_page(
    __name__,
    name='AANB Data Exploration',
    top_nav=True,
    path='/'
)


life_expectancy_vis, education_total_vis, ever_enslaved_vis = create_visualizations()


def layout():
    layout = html.Div(
        [
            html.H1(
                [
                    "African American National Biography Data Exploration"
                ]
            ),
            dcc.Graph(figure=life_expectancy_vis),
            dcc.Graph(figure=education_total_vis),
            dcc.Graph(figure=ever_enslaved_vis),
        ],
        style={
            'padding': '5% 5% 5% 5%'
        }
    )
    return layout
