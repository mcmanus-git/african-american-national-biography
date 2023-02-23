from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Contact Us',
    path='/contact-us',
    title='Contact Us',
    description='AANB App Contact Us Page'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Contact Us Page"
            ]
        )
    ])
    return layout
