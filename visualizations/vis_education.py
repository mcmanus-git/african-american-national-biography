import plotly.express as px


def create_total_education_vis(df):

    total_ed_vis = px.bar(
        df['education_literacy_bool'].value_counts().reset_index().rename({'index': "Literate or Educated", 'education_literacy_bool': 'Number of People'}, axis=1),
        x='Literate or Educated',
        y='Number of People',
    )

    total_ed_vis.update_layout(
        title={
            'text': 'Number of Literate or Educated People',
            'x': 0.5
        }
    )

    return total_ed_vis
