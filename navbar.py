from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = html.Div(
        [
            dbc.NavbarSimple(
                # class_name='navbar bg-transparent',
                children=[
                    dbc.NavItem(
                        dbc.NavLink(
                            [
                                html.I(className="fa-brands fa-github"),  # Font Awesome Icon
                                " "  # Text beside icon
                            ],
                            href="https://github.com/mcmanus-git/african-american-national-biography",
                            target="_blank"
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            [
                                html.I(className="fa-brands fa-medium"),  # Font Awesome Icon
                                " "  # Text beside icon
                            ],
                            href="https://medium.com/@mcmanus_data_works",
                            target="_blank"
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            [
                                html.I(className="fa-brands fa-linkedin"),  # Font Awesome Icon
                                " "  # Text beside icon
                            ],
                            href="https://www.linkedin.com/in/michael-mcmanus/",
                            target="_blank"
                        )
                    ),
                    dbc.DropdownMenu(
                        nav=True,
                        in_navbar=True,
                        label="Menu",
                        align_end=True,
                        children=[  # Add as many menu items as you need
                            dbc.DropdownMenuItem("Home", href='/'),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Biographies", href='/bios'),
                            dbc.DropdownMenuItem("About", href='/about'),
                        ],
                    ),
                ],
                brand='African American National Biography',
                brand_href="/",
                # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
                # color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
                dark=False,  # Change this to change color of text within the navbar (False for dark text)
                style={
                    'background-color': '#000000',
                    'opacity': '0.75'
                }
            )
        ],
        style={
            'background-image': 'url(/assets/app.jpg)',
            'background-size': 'cover',
            'height': '50vh',
        }
    )

    return navbar
