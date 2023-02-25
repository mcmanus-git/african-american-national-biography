import plotly.express as px


def create_total_enslaved_vis(df):

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
        y='Number of People'
    )

    total_enslaved_vis.update_layout(
        title={
            'text': 'Count of People Ever Enslaved',
            'x': 0.5
        }
    )

    return total_enslaved_vis
