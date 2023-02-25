import pandas as pd
import plotly.express as px


def create_vis_life_expectancy(df, neut_clr, hlt_clr):
    min_n_records = 2
    birthyear_counts = (
        df[df['birthYearClean'] < 9999]['birthYearClean']
        .value_counts()
        .reset_index()
        .rename(
            {
                'index': 'birthYear',
                'birthYearClean': 'count'
            },
            axis=1
        )
    )

    avg_life_exp = px.line(
        (
            df[df['birthYearClean'].isin(birthyear_counts[birthyear_counts['count'] > min_n_records]['birthYear'])]
            .groupby(['ever_enslaved_bool', 'birthYearClean'])['age_at_death']
            .mean()
            .dropna()
            .reset_index()
            .rename(
                {
                    'age_at_death': 'Age',
                    'ever_enslaved_bool': 'Ever Enslaved',
                    'birthYearClean': 'Birth Year'
                },
                axis=1
            )
        ),
        x='Birth Year',
        y='Age',
        color='Ever Enslaved',
        color_discrete_map={
            'Yes': hlt_clr,
            'No': neut_clr
        }
    )
    avg_life_exp.update_layout(
        title={
            'text': 'Average Life Span by Birth Year',
            'x': 0.5
        }
    )

    return avg_life_exp
