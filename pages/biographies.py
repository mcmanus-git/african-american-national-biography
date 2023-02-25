from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Biographies',
    path='/bios',
    title='Biographies',
    description='AANB App Biography Page'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Biographies Page - Coming Soon"
            ]
        )
    ])
    return layout
