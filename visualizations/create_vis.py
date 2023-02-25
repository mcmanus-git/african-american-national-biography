import pandas as pd
from visualizations.vis_life_expectancy import create_vis_life_expectancy
from visualizations.vis_education import create_total_education_vis
from visualizations.vis_enslaved import create_total_enslaved_vis, create_before_thirteenth_vis
from visualizations.vis_cultural import create_runaway_rebel_vis, create_religion_vis


def create_visualizations():

    neut_color = '#3C3C3C'
    highlight_color = '#D65250'

    df = pd.read_pickle('data/aanb_data_clean.pkl')

    le_vis = create_vis_life_expectancy(df, neut_color, highlight_color)

    ed_total_vis = create_total_education_vis(df, neut_color, highlight_color)

    ever_enslaved_vis = create_total_enslaved_vis(df, neut_color, highlight_color)
    before_thirteenth_vis = create_before_thirteenth_vis(df, neut_color, highlight_color)

    run_reb_vis = create_runaway_rebel_vis(df, neut_color, highlight_color)
    religion_vis = create_religion_vis(df, neut_color, highlight_color)

    return le_vis, ed_total_vis, ever_enslaved_vis, before_thirteenth_vis, run_reb_vis, religion_vis

