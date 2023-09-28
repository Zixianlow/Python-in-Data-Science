from load_csv import load
import matplotlib.pyplot as plt


def ft_aff_life():
    """Loads life expectancy data, extract from data of France, then extract
the life expectancy data respective to France. Finally, plot a line graph
using the data."""
    try:
        data = load("life_expectancy_years.csv")
        malaysia_data = data[data['country'] == 'Malaysia']
        years = list(data.columns[1:])
        life = malaysia_data.iloc[0][1:]
        plt.plot(years, life)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.title('Malaysia Life expectancy Projections')
        custom_ticks = ['1800', '1840', '1880', '1920',
                        '1960', '2000', '2040', '2080']
        plt.xticks(custom_ticks)
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    ft_aff_life()
