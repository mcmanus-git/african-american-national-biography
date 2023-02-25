import pandas as pd
from visualizations.vis_life_expectancy import create_vis_life_expectancy
from visualizations.vis_education import create_total_education_vis


def create_visualizations():
    df = pd.read_pickle('data/aanb_data_clean.pkl')

    le_vis = create_vis_life_expectancy(df)

    ed_total_vis = create_total_education_vis(df)

    return le_vis, ed_total_vis

