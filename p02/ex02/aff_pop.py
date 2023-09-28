from load_csv import load
import matplotlib.pyplot as plt


def convert_population(value):
    """Remove the 'M' and 'k' char from the data toease graph
plotting."""
    if 'M' in value:
        return float(value.rstrip('M'))
    elif 'k' in value:
        return float(value.rstrip('k')) / 1000
    else:
        return float(value)


def ft_aff_pop():
    """Loads population total data, extract from data of France and Belgium
then extract the population data from both into respective_life. Finally,
plot a line graph with both data."""
    try:
        data = load("population_total.csv")
        malaysia_data = data[data['country'] == 'Malaysia']
        france_data = data[data['country'] == 'France']
        years = list(data.columns[1:-50])
        malaysia_life = malaysia_data.iloc[0][1:-50]
        france_life = france_data.iloc[0][1:-50]
        new_malaysia_life = \
            [convert_population(value) for value in malaysia_life]
        new_france_life = [convert_population(value) for value in france_life]
        plt.plot(years, new_france_life, 'b', label='France')
        plt.plot(years, new_malaysia_life, 'g', label='Malaysia')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        custom_xticks = ['1800', '1840', '1880', '1920',
                         '1960', '2000', '2040']
        plt.xticks(custom_xticks)
        plt.ylim(0.0, 70.0)
        plt.yticks([20.0, 40.0, 60.0], ['20M', '40M', '60M'])
        plt.legend(loc='lower right')
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    ft_aff_pop()
