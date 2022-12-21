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
    
    
   
def plot_continuous_against2_variables(df):
    plt.figure(figsize=(20, 5))
    palette = "Set3"

    plt.subplot(1, 3, 1)
    sns.boxplot(x = 'Sex', y = 'Age', data = age_1_class,
         palette = palette, fliersize = 0)
    sns.stripplot(x = 'Sex', y = 'Age', data = age_1_class,
         linewidth = 0.6, palette = palette)
    plt.title('1st class Age distribution by Sex',fontsize= 14)
    plt.ylim(-5, 80)

    plt.subplot(1, 3, 2)
    sns.boxplot(x = 'Sex', y = 'Age', data = age_2_class,
         palette = palette, fliersize = 0)
    sns.stripplot(x = 'Sex', y = 'Age', data = age_2_class,
         linewidth = 0.6, palette = palette)
    plt.title('2nd class Age distribution by Sex',fontsize= 14)
    plt.ylim(-5, 80)

    plt.subplot(1, 3, 3)
    sns.boxplot(x = 'Sex', y = 'Age',  data = age_3_class,
         order = ['female', 'male'], palette = palette, fliersize = 0)
    sns.stripplot(x = 'Sex', y = 'Age', data = age_3_class,
         order = ['female', 'male'], linewidth = 0.6, palette = palette)
    plt.title('3rd class Age distribution by Sex',fontsize= 14)
    plt.ylim(-5, 80)

    plt.show()
