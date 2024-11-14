import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = df.apply(lambda x: 1 if (x['weight'] / (x['height']/100)**2) > 25 else 0, axis = 1)

# 3
df['cholesterol'] = df.apply(lambda x: 0 if x['cholesterol'] == 1 else 1, axis = 1)
df['gluc'] = df.apply(lambda x: 0 if x['gluc'] == 1 else 1, axis = 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                    var_name = 'variable', value_name = 'value')

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'counts')
    
    # 7
    fig = sns.catplot(
        data=df_cat, x = "variable", y = "counts",
        col="cardio", kind="bar", height=4, hue='value', 
        aspect= 1.2)

    

    # 8
    fig = fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()