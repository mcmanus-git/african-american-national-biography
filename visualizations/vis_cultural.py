import plotly.express as px


def create_runaway_rebel_vis(df, neut_clr, hlt_clr):

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
        y='Number of People',
        color='Runaway or Rebel',
        color_discrete_map={
            'Yes': hlt_clr,
            'No': neut_clr,
            'Unknown': neut_clr
        }
    )

    rr_vis.update_layout(
        title={
            'text': 'People Identified as Runaways or Rebels',
            'x': 0.5
        },
        showlegend=False
    )

    return rr_vis


def create_religion_vis(df, neut_clr, hlt_clr):
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

    religion_vis.update_traces(
        marker_color=neut_clr
    )

    religion_vis.update_layout(
        title={
            'text': 'Religious Affiliation',
            'x': 0.5
        }
    )

    return religion_vis
