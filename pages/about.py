from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='About',
    path='/about',
    title="About",
    description="AANB App About Page.",
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
