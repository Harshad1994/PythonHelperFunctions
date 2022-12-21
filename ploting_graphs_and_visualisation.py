import seaborn as sns
def plot_correlation_heatmap(df):
    
    f, ax = plt.subplots(figsize=(30, 25))
    corr = df.corr()
    sns.heatmap(corr,annot=True)
    
def plot_continous_variable_for_two_categories(df)
    plt.figure(figsize=(15, 3))

    # Draw a box plot to show Age distributions with respect to survival status.
    sns.boxplot(y = 'Attrition', x = 'Age', data = df,
         palette=["#3f3e6fd1", "#85c6a9"], fliersize = 0, orient = 'h')

    # Add a scatterplot for each category.
    sns.stripplot(y = 'Attrition', x = 'Age', data = df,
         linewidth = 0.6, palette=["#3f3e6fd1", "#85c6a9"], orient = 'h')

    plt.yticks( np.arange(2), ['left', 'stayed'])
    plt.title('Age distribution grouped by attrition',fontsize= 14)
    plt.ylabel('Status of employee')
    plt.tight_layout()
