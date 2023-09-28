from load_csv import load
import matplotlib.pyplot as plt


def ft_projection_life():
    """Loads income_data and life_data respectively, extract from both data
from year 1900, the make a scatter plot from it"""
    try:
        income_data = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_data = load("life_expectancy_years.csv")
        income_list = income_data['1900']
        life_list = life_data['1900']
        plt.scatter(income_list, life_list)
        plt.xlabel('Gross domestic produt')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.xlim(300, 10000)
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    ft_projection_life()
