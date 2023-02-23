from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='About',
    top_nav=True,
    path='/about'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "About Page"
            ]
        )
    ])
    return layout
