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


def bio_template(df):

    dob = df['dob'].fillna('Unknown').values[0]
    dod = df['dod'].fillna('Unknown').values[0]
    age = df['age_at_death'].round(0).fillna('Unknown').values[0]
    enslaved = df['ever_enslaved_bool'].fillna('Unknown').values[0]
    thirteenth = df['free_before_13_bool'].fillna('Unknown').values[0]
    rr = df['runaways_and_rebels_bool'].fillna('Unknown').values[0]
    ed = df['education_literacy_bool'].fillna('Unknown').values[0]
    occ = ", ".join([v[0].strip() for v in df[[col for col in df.columns if 'Occupation ' in col]].T.dropna().values])
    religion = df['religion_clean'].fillna('Unknown').values[0]
    notes = df['Notes'].fillna('No Records').values[0]

    bio = dcc.Markdown(f"""## {df['full_name'].values[0]}  
<h5>Date of Birth:</h5> {dob}
<h5>Date of Death:</h5>  {dod}  
<h5>Age:</h5>  {age}  
<h5>Ever Enslaved:</h5>  {enslaved}  
<h5>Freed Before 13th Amendment:</h5>  {thirteenth}  
<h5>Runaway or Rebel:</h5>  {rr}  
<h5>Educated and/or Literate:</h5>  {ed}  
<h5>Occupations:</h5>  {occ}  
<h5>Religion:</h5>  {religion}  
<h4>Notes:</h4>  
{notes}  
""",
                       dangerously_allow_html=True
                       )

    bio_container = html.Div(
        [
            bio
        ],
        style={
            'padding': '5% 5% 5% 5%'
        }
    )

    return bio_container


@callback(
    Output('bio-output-container', 'children'),
    Input('bio-select-dropdown', 'value')
)
def update_output(value):

    if value:
        bios = DF[DF['full_name'] == value]

        bio = bio_template(bios)

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
