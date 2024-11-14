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
    plot = sns.catplot(
        data=df_cat, x = "variable", y = "counts",
        col="cardio", kind="bar", height=4, hue='value', 
        aspect= 1.2)
    plot.set_axis_labels("variable", "total")

    

    # 8
    fig = plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))
                & (df['height'] <= df['height'].quantile(0.975))
                & (df['weight'] >= df['weight'].quantile(0.025))
                & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12

    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr))


    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, ax=ax,
                    linewidth=.5, cbar_kws={"shrink":0.5}, square=True,
                    center=0.1)



    # 16
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()