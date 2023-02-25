from dash import html, register_page, dcc  #, callback # If you need callbacks, import it here.
import dash_bootstrap_components as dbc

# register_page(
#     __name__,
#     name='About',
#     path='/about',
#     title="About",
#     description="AANB App About Page.",
# )
#
#
# def layout():
#     layout = html.Div([
#         html.H1(
#             [
#                 "About Page"
#             ]
#         )
#     ])
#     return layout

register_page(
    __name__,
    name='About',
    path='/about',
    title="About",
    description="AANB Data Exploration - About Page",
)

header = html.H1('About', style={'textAlign': 'center'})
line_break = html.Div([dcc.Markdown("""___""")], style={'margin': '5% 0% 5% 0%'})


data_sources_header = html.H3('-Data Source-', style={'textAlign': 'center'})
data_sources = dcc.Markdown('''
#### Overview
The [Enslaved People in the African American National Biography, 1508-1865](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FIEYGJ) 
dataset is derived from the [African American National Biography](https://hutchinscenter.fas.harvard.edu/AANB) 
by [Steven J. Niven](https://hutchinscenter.fas.harvard.edu/people/steven-j-niven) and contains records of over 1,300 
people who lived prior to ratification of The 13th Amendment of the United States Constitution between the 
years 1508-1865.
<br>
#### Considerations While Exploring this Data  

While exploring the visualizations on the home page, please keep in mind this is but a subset of all African 
American people living during this time and includes records of approximately 1,300 people. Of these 
1,300 records, many are incomplete. As such, it is impossible to make 
concrete inferences between these accounts and what life may have been truly like for African Americans
during this time in aggregate.  
<br>
For instance, you'll notice in the visualization below that 651 individuals have been recorded as 
having ever been enslaved. Of the 1,300 records, this is roughly 50%. It is unlikely this is an accurate
 ratio as, according to the Trans-Atlantic Slave Trade Database estimates, 388,000 Africans were 
transported directly to the United States to be sold as slaves 
[[1]](https://www.pbs.org/wnet/african-americans-many-rivers-to-cross/history/how-many-slaves-landed-in-the-us/). 
As you can see, 1,300 biographies of African Americans during the same time period is only 0.3% of just
those who were transported to the United States directly from Africa. Therefore, it is unsafe to assume 
the same ratios will be applicable universally.  
<br>
#### Data Cleaning and Presentation

As records were hand recorded, significant data cleaning was necessary to enable aggregation of information found 
therein. All data cleaning methods are documented in a 
[Jupyter Notebook](https://github.com/mcmanus-git/african-american-national-biography/blob/main/data_pipelines/data%20cleaning%20eda.ipynb) 
hosted in the 
[Project Repository on GitHub](https://github.com/mcmanus-git/african-american-national-biography) 
as well as both the 
[raw dataset](https://github.com/mcmanus-git/african-american-national-biography/blob/main/data/AANB-Data-Final-Revised20210414.csv) 
and the 
[cleaned dataset](https://github.com/mcmanus-git/african-american-national-biography/blob/main/data/aanb_data_clean.pkl)
 for reference and reproducibility. Data contents and dictionary are explained fully in the 
 [documentation](https://github.com/mcmanus-git/african-american-national-biography/blob/main/data/AANB-Documentation-Final20201221.xlsx).
''',
dangerously_allow_html=True
)

creator_header = html.H1('About the Creator', style={'textAlign': 'center'})
contact_creator_header = html.H4('-   Contact Me   -', style={'textAlign': 'center'})
about_the_creator = dcc.Markdown("""Michael McManus is a Data Scientist who works for a regulated gas and electric 
utility in Michigan, U.S. His work focuses on electric grid reliability and resiliency as it relates to forestry 
related power outages. Michael graduated from the University of Michigan School of Information with a Master's Degree 
in Applied Data Science in May of 2022. Michael loves all things data and is constantly looking for new opportunities 
to do good with his Data Science skills and leave the world better than he found it.  
"Information Changes Everything" - UMSI.
""")


contact_links = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-github"), " GitHub"],
                                             href="https://github.com/mcmanus-git",
                                             target="_blank"))
                    ], width={"size": 3, 'offset': 2}
                ),
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-medium"), " Medium"],
                                             href="https://medium.com/@mcmanus_data_works",
                                             target="_blank")),
                    ], width={"size": 3}
                ),
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-linkedin"), " LinkedIn"],
                                             href="https://www.linkedin.com/in/michael-mcmanus/",
                                             target="_blank"))
                    ], width={"size": 3}
                )
            ], justify="center"
        )
    ]
)


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    # About Description
                    html.Br(),
                    data_sources_header,
                    html.Br(),
                    data_sources,
                    html.Br(),
                    line_break,
                    creator_header,
                    html.Br(),
                    about_the_creator,
                    html.Br(),
                    html.Br(),
                    contact_creator_header,
                    html.Br(),
                    contact_links,
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    # More Children
                ], style={'margin': '5% 10% 5% 10%'}
            )
        ]
    )
    return layout