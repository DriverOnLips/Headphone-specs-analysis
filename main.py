import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    data = pd.read_excel('./data/data.xlsx')
    return data


def clear_missing_values(data):
    data = data.dropna()
    return data


def drop_duplicates(data):
    new_data = data.drop_duplicates()
    # print(new_data.equals(data), len(new_data))
    return new_data


def clear_zeros(data):
    data = data[(data['Production_Price'] > 0) & (data['Selling_Price'] > 0)]
    # print(len(data))
    return data


def get_tuple_with_highest_price(data):
    max_price_tuple_index = data['Selling_Price'].idxmax()
    max_price_tuple_title = data.loc[max_price_tuple_index, 'Title']
    max_price_tuple_price = data.loc[max_price_tuple_index, 'Selling_Price']
    # print(f"Tuple with highest selling price: {max_price_tuple_title}, {max_price_tuple_price}")


def describe_all_columns(data):
    description = data.describe(include='all')
    # print(description)


def diagram_connectivity_type(data):
    connectivity_types = data['Connectivity_Type'].unique()
    counts = data['Connectivity_Type'].value_counts()
    percentages = counts / len(data) * 100

    fig, ax = plt.subplots()
    ax.pie(percentages, labels=connectivity_types, autopct='%1.1f%%')
    ax.axis('equal')

    plt.show()


def diagram_avg_price_per_brand(data):
     average_prices = data.groupby('Brand')['Selling_Price'].mean()
     average_prices = average_prices.sort_values(ascending=False)
     average_prices.plot(kind='bar')

     plt.title('Средняя цена наушников бренда')
     plt.xlabel('Бренд')
     plt.ylabel('Средняя цена наушников')
     plt.show()


def diagram_num_headphones_by_connection_type(data):
    bluetooth_counts = data[data['Connectivity_Type'] == 'Bluetooth'].groupby('Brand').size()
    wired_counts = data[data['Connectivity_Type'] == 'Wired'].groupby('Brand').size()

    plt.figure(figsize=(10, 5))

    plt.bar(bluetooth_counts.index, bluetooth_counts, color='b', alpha=0.5, label='Беспроводные')
    plt.bar(wired_counts.index, wired_counts, color='r', alpha=0.5, label='Проводные')

    plt.title('Количество беспроводных и проводных наушников по каждому бренду')
    plt.xlabel('Бренд')
    plt.ylabel('Количество товаров')
    plt.legend()

    plt.show()


def diagram_num_headphones_by_form_factor(data):
    on_ear = data[data['Form_Factor'] == 'On Ear'].groupby('Brand').size()
    in_ear = data[data['Form_Factor'] == 'In Ear'].groupby('Brand').size()

    plt.figure(figsize=(10, 5))

    plt.bar(on_ear.index, on_ear, color='b', alpha=0.5, label='Накладные')
    plt.bar(in_ear.index, in_ear, color='r', alpha=0.5, label='Вкладыши')

    plt.title('Количество наушников разного форм-фактора по каждому бренду')
    plt.xlabel('Бренд')
    plt.ylabel('Количество товаров')
    plt.legend()

    plt.show()


def diagram_headphones_color(data):
    color_counts = data['Colour'].value_counts()
    percentages = color_counts / len(data) * 100

    plt.figure(figsize=(10, 5))
    plt.pie(percentages, labels = color_counts.index, autopct='%1.1f%%')
    plt.title('Процент наушников определенного цвета')
    plt.show()


def diagram_avg_price_by_form_factor(data):
    form_factor_prices = data[data['Form_Factor'].isin(['On Ear', 'In Ear'])]
    average_prices = form_factor_prices.groupby('Form_Factor')['Selling_Price'].mean()

    plt.figure(figsize=(10, 5))
    average_prices.plot(kind='barh')

    plt.title('Средняя цена наушников определенного форм фактора')
    plt.xlabel('Средняя цена')
    plt.ylabel('Форм фактор')
    plt.show()


def diagram_avg_selling_production_price(data):
    selling_price_avg = data['Selling_Price'].mean()
    production_price_avg = data['Production_Price'].mean()

    print(selling_price_avg / production_price_avg)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(['Цена продажи', 'Цена производства'], [selling_price_avg, production_price_avg])
    plt.title('Средняя цена производства и продажи')
    plt.ylabel('Средняя цена')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., yval, round(yval, 2), ha='center', va='bottom')

    plt.show()



def correlation_selling_production_price(data):
    correlation = data['Production_Price'].corr(data['Selling_Price'])
    print(correlation)


def main():
    data = load_data()
    data = clear_missing_values(data)
    data = drop_duplicates(data)
    data = clear_zeros(data)

    get_tuple_with_highest_price(data)
    describe_all_columns(data)

    # diagram_connectivity_type(data)
    # diagram_avg_price_per_brand(data)
    # diagram_num_headphones_by_connection_type(data)
    # diagram_num_headphones_by_form_factor(data)
    # diagram_headphones_color(data)
    # diagram_avg_price_by_form_factor(data)
    # diagram_avg_selling_production_price(data)

    correlation_selling_production_price(data)


if __name__ == '__main__':
    main()
