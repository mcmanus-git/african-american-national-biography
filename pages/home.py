from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "African American National Biography Data Exploration"
            ]
        )
    ])
    return layout
