from dash import html, register_page, dcc, Input, Output, callback # If you need callbacks, import it here.
import pandas as pd

register_page(
    __name__,
    name='Biographies',
    path='/bios',
    title='Biographies',
    description='AANB App Biography Page'
)


def bio_select(df):
    bio_select_dropdown = dcc.Dropdown(
        df['full_name'].to_list(),
        id='bio-select-dropdown',
        placeholder='Select a Biography'
    )

    return bio_select_dropdown

@callback(
    Output('bio-output-container', 'children'),
    Input('bio-select-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'

def layout():

    df = pd.read_pickle('data/aanb_data_clean.pkl')
    bios_list = df['full_name'].to_list()

    layout = html.Div(
        [
            html.H1(
                [
                    "Biographies Page - Coming Soon"
                ]
            ),
            dcc.Dropdown(
                bios_list,
                id='bio-select-dropdown',
                placeholder='Select a Biography'
            ),
            html.Div(id='bio-output-container')
        ],
        style={
            'padding': '5% 5% 5% 5%'
        }
    )
    return layout
