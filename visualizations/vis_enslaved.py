import plotly.express as px


def create_total_enslaved_vis(df, neut_clr, hlt_clr):

    total_enslaved_vis = px.bar(
        (
            df['ever_enslaved_bool']
            .value_counts()
            .reset_index()
            .rename(
                {
                    'index': 'Ever Enslaved',
                    'ever_enslaved_bool': 'Number of People'
                },
                axis=1
            )
        ),
        x='Ever Enslaved',
        y='Number of People',
        color='Ever Enslaved',
        color_discrete_map={
            'Yes': hlt_clr,
            'No': neut_clr
        }
    )

    total_enslaved_vis.update_layout(
        title={
            'text': 'Ever Enslaved During Their Lifetime',
            'x': 0.5
        },
        showlegend=False
    )

    return total_enslaved_vis


def create_before_thirteenth_vis(df, neut_clr, hlt_clr):
    free_before_vis = px.bar(
        (
            df['free_before_13_bool']
            .value_counts()
            .reset_index()
            .rename(
                {
                    'index': 'Freed',
                    'free_before_13_bool': 'Number of People'
                },
                axis=1
            )
        ),
        x='Freed',
        y='Number of People',
        color='Freed',
        color_discrete_map={
            'Yes': hlt_clr,
            'No': neut_clr,
            'Unknown': neut_clr
        }
    )

    free_before_vis.update_layout(
        title={
            'text': 'Freed Prior to the 13th Amendment',
            'x': 0.5
        },
        showlegend=False
    )

    return free_before_vis
