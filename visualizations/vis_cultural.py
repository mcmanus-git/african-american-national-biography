import plotly.express as px


def create_runaway_rebel_vis(df):

    rr_vis = px.bar(
        (
            df['runaways_and_rebels_bool']
            .value_counts()
            .reset_index()
            .rename(
                {
                    'index': 'Runaway or Rebel',
                    'runaways_and_rebels_bool': 'Number of People'
                },
                axis=1
            )
        ),
        x='Runaway or Rebel',
        y='Number of People'
    )

    rr_vis.update_layout(
        title={
            'text': 'People Identified as Runaways or Rebels',
            'x': 0.5
        }
    )

    return rr_vis


def create_religion_vis(df):
    religion_vis = px.bar(
        (
            df['religion_clean']
            .value_counts()
            .reset_index()
            .rename(
                {
                    'index': 'Religion',
                    'religion_clean': 'Number of People'
                },
                axis=1
            )
            .sort_values(
                'Number of People'
            )
        ),
        x='Number of People',
        y='Religion',
        orientation='h'
    )

    religion_vis.update_layout(
        title={
            'text': 'Religious Affiliation',
            'x': 0.5
        }
    )

    return religion_vis
