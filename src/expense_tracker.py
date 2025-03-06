import pandas as pd

def read_expenses(file_path):
    """Reads expenses from a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def group_expenses_by_category(df):
    """Groups expenses by category and sums the amounts."""
    return df.groupby('Category', as_index=False)['Amount'].sum()

def export_grouped_expenses(df, output_path):
    """Exports the grouped expenses to a CSV file."""
    df.to_csv(output_path, index=False)

def main():
    input_file = "data/expenses.csv"
    output_file = "data/grouped_expenses.csv"
    
    df = read_expenses(input_file)
    grouped_df = group_expenses_by_category(df)
    export_grouped_expenses(grouped_df, output_file)
    
    print("Grouped expenses saved to", output_file)

if __name__ == "__main__":
    main()