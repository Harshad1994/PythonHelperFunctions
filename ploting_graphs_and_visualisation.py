def plot_correlation_heatmap(df):
    import seaborn as sns
    f, ax = plt.subplots(figsize=(30, 25))
    corr = df.corr()
    sns.heatmap(corr,annot=True)
