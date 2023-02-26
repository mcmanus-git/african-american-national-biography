from dash import html, register_page, dcc, Input, Output, callback # If you need callbacks, import it here.
import pandas as pd

register_page(
    __name__,
    name='Biographies',
    path='/bios',
    title='Biographies',
    description='AANB App Biography Page'
)

DF = pd.read_pickle('data/aanb_data_clean.pkl')
BIO_LIST = DF['full_name'].to_list()


def bio_template(df, val):

    bio_items_style = {'padding': '2% 0% 0% 0%'}

    name = val
    dob = df['dob'].fillna('Unknown').values[0]
    dod = df['dod'].fillna('Unknown').values[0]
    age = df['age_at_death'].round(0).fillna('Unknown').values[0]
    enslaved = df['ever_enslaved_bool'].fillna('Unknown').values[0]
    free_meth = df['How was freedom attained'].fillna('Unknown').values[0]
    thirteenth = df['free_before_13_bool'].fillna('Unknown').values[0]
    rr = df['runaways_and_rebels_bool'].fillna('Unknown').values[0]
    ed = df['education_literacy_bool'].fillna('Unknown').values[0]
    occupation_list = [v[0].strip() for v in df[[col for col in df.columns if 'Occupation ' in col]].T.dropna().values]
    if len(occupation_list) == 0:
        occ = 'Unknown'
    else:
        occ = ", ".join(occupation_list)
    religion = df['religion_clean'].fillna('Unknown').values[0]
    notes = df['Notes'].fillna('No Records').values[0]

    bio_container = dcc.Loading(
        html.Div(
            [
                html.H2(name, style={'text-align': 'center'}),
                html.Div([html.H5('Date of Birth: '), dob], style=bio_items_style),
                html.Div([html.H5('Date of Death: '), dod], style=bio_items_style),
                html.Div([html.H5('Age: '), age], style=bio_items_style),
                html.Div([html.H5('Ever Enslaved: '), enslaved], style=bio_items_style),
                html.Div([html.H5('Freed Before 13th Amendment: '), thirteenth], style=bio_items_style),
                html.Div([html.H5('Runaway or Rebel: '), rr], style=bio_items_style),
                html.Div([html.H5('Educated and/or Literate: '), ed], style=bio_items_style),
                html.Div([html.H5('Occupations: '), occ], style=bio_items_style),
                html.Div([html.H5('Religion: '), religion], style=bio_items_style),
                html.Div([html.H5('Was Freedom Attained: '), free_meth], style=bio_items_style),
                html.Div([html.H4('Notes: '), notes], style=bio_items_style),
                # html.Div([html.H4('Notes: '), notes], style=bio_items_style),
            ],
            style={
                'padding': '5% 5% 5% 5%'
            }
        )
    )

    return bio_container


@callback(
    Output('bio-output-container', 'children'),
    Input('bio-select-dropdown', 'value')
)
def update_output(value):

    if value:
        bios = DF[DF['full_name'] == value]
        bio = bio_template(bios, value)

        # return f'You have selected {value} and df returned {bios.shape} {bios["ever_enslaved_bool"].values[0]}'
        return bio
    else:
        pass


def layout():

    layout = html.Div(
        [
            html.H1(
                [
                    "Biographies Page - Coming Soon"
                ]
            ),
            dcc.Dropdown(
                BIO_LIST,
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
