import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from stock_utils import load_prices, calculate_correlation, get_correlated_pairs, save_analysis


def plot_pairs(df, stock1, stock2):
    plt.figure(figsize=(12, 6))
    date_col = "Date" if "Date" in df.columns else None
    x_axis = df[date_col] if date_col else range(len(df))
    plt.plot(x_axis, df[stock1], label=stock1, linewidth=2)
    plt.plot(x_axis, df[stock2], label=stock2, linewidth=2)
    plt.xlabel("Date" if date_col else "Day")
    plt.ylabel("Price")
    plt.title(f"Price Movement: {stock1} vs {stock2}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_heatmap(correlation_matrix):
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        center=0,
        square=True,
    )
    plt.title("Stock Price Correlation Matrix")
    plt.tight_layout()
    plt.show()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, 'stock_prices.csv')
    json_output = os.path.join(script_dir, 'correlation_matrix.json')

    df = load_prices(csv_file)
    correlation_matrix = calculate_correlation(df)
    correlated_pairs = get_correlated_pairs(correlation_matrix, threshold=0.7)

    print(correlation_matrix)
    if correlated_pairs:
        print(f"{len(correlated_pairs)} pairs with correlation >= 0.7")
        for pair in correlated_pairs:
            print(pair)
    else:
        print("No pairs above threshold")

    save_analysis(correlation_matrix, json_output)
    plot_heatmap(correlation_matrix)

    if correlated_pairs:
        pair = correlated_pairs[0]
        plot_pairs(df, pair.stock1, pair.stock2)


if __name__ == "__main__":
    main()
