import pandas as pd
from visualizations.vis_life_expectancy import create_vis_life_expectancy
from dash_bootstrap_templates import load_figure_template

load_figure_template('LUX')


def create_visualizations():
    df = pd.read_pickle('data/aanb_data_clean.pkl')

    le_vis = create_vis_life_expectancy(df)

    return le_vis

