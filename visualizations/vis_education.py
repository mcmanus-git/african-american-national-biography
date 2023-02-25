import plotly.express as px


def create_total_education_vis(df, neut_clr, hlt_clr):

    total_ed_vis = px.bar(
        (df['education_literacy_bool']
         .value_counts()
         .reset_index()
         .rename(
            {
                'index': "Literate or Educated",
                'education_literacy_bool': 'Number of People'
            },
            axis=1
        )
        ),
        x='Literate or Educated',
        y='Number of People',
        color='Literate or Educated',
        color_discrete_map={
            'Yes': neut_clr,
            'No': hlt_clr,
            'Unknown': neut_clr
        }
    )

    total_ed_vis.update_layout(
        title={
            'text': 'Number of Literate or Educated People',
            'x': 0.5
        },
        showlegend=False
    )

    return total_ed_vis
