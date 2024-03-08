import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd


def load_wine_data() -> tuple:
    """
    Load wine data from CSV files and return a DataFrame containing all wines and a dictionary of wine types.

    Returns:
        tuple: A tuple containing a DataFrame of all wines and a dictionary mapping file names to wine types.
    """
    wine_types = {
        'wine_red': 'Red',
        'wine_white': 'White',
        'wine_rose': 'Rose',
        'wine_sparkling': 'Sparkling',
        'wine_dessert': 'Dessert',
        'wine_fortified': 'Fortified',
    }
    all_wines = pd.DataFrame()
    for file_name, wine_type in wine_types.items():
        df = pd.read_csv(f'wine_data/{file_name}.csv')
        df['Winery'] = df['Winery'].fillna("N/A")  # Clean the data
        df['Region'] = df['Region'].apply(lambda x: "N/A" if len(x) < 3 else x)
        df['Vintage'] = df['Vintage'].apply(lambda x: "N/A" if pd.isna(x) else int(x))
        df['Type'] = wine_type  # Assign wine type
        all_wines = pd.concat([all_wines, df])  # Combine all wine data into a single DataFrame
    return all_wines, wine_types


def show_error(message: str) -> None:
    messagebox.showerror("Error", message)


def submit_budget(budget_entry: tk.Entry, tree: ttk.Treeview, all_wines: pd.DataFrame, wine_selection: dict, results_label: ttk.Label) -> None:
    """
    Submit budget, filter wines based on the budget and selected wine types, and update the Treeview with filtered results.

    Parameters:
        budget_entry (tk.Entry): Entry widget to get the budget from.
        tree (ttk.Treeview): Treeview widget to display filtered wine data.
        all_wines (pd.DataFrame): DataFrame containing all wine data.
        wine_selection (dict): Dictionary mapping wine types to their BooleanVar selection status.
        results_label (ttk.Label): Label widget to display the number of wines found.
    """
    budget = budget_entry.get()  # Retrieve budget from entry widget
    try:
        budget = int(budget)
    except ValueError:
        show_error("請將您的預算設定為整數！")  # Show error if conversion fails
        return

    # Filter wines based on selected types
    selected_types = [wine_type for wine_type, selected in wine_selection.items() if selected.get()]
    if not selected_types:
        show_error("請至少選擇一種葡萄酒類型！")  # Show error if no wine type is selected
        return

    # Filter wines based on budget and selected types
    filtered_df = all_wines[(all_wines['Price'] <= budget) & (all_wines['Type'].isin(selected_types))]

    # Update Treeview with filtered results
    for i in tree.get_children():
        tree.delete(i)  # Clear existing entries in the Treeview
    for index, row in filtered_df.iterrows():
        tree.insert("", tk.END, values=list(row))  # Insert filtered wines into the Treeview

    tree.yview_moveto(0)  # Scroll back to the top of the Treeview
    results_label.config(text=f'共有{len(filtered_df)}款酒可供選擇')  # Update results label


def treeview_sort_column(tv: ttk.Treeview, col: str, reverse: bool) -> None:
    """
    Sort Treeview column in ascending or descending order.

    Parameters:
        tv (ttk.Treeview): The Treeview widget to sort.
        col (str): The column identifier to sort by.
        reverse (bool): Whether to sort in descending order.
    """
    items = [(tv.set(k, col), k) for k in tv.get_children('')]  # Retrieve all items from the Treeview

    # Sort items by column value, handling numeric values appropriately
    if col in ('Price', 'RatingsCount'):
        items.sort(key=lambda t: float(t[0]) if t[0] != 'N/A' else float('-inf'), reverse=reverse)
    else:
        items.sort(reverse=reverse)  # Sort items based on column values

    # Reinsert items into the Treeview in sorted order
    for index, (val, k) in enumerate(items):
        tv.move(k, '', index)

    # Bind sort function to column header with reversed order for next click
    tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))


def setup_ui(root: tk.Tk, all_wines: pd.DataFrame, wine_types: dict) -> tuple:
    """
    Set up the user interface.

    Parameters:
        root (tk.Tk): The root Tkinter window.
        all_wines (pd.DataFrame): DataFrame containing all wine data.
        wine_types (dict): Dictionary of wine types.

    Returns:
        tuple: A tuple containing wine selection variables, the Treeview widget, and the results label.
    """
    # Configure styles
    style = ttk.Style()
    style.configure('Large.TButton', padding=[8, 8], font=('Microsoft JhengHei', 12))
    style.configure('CustomCheck.TCheckbutton', font=('Helvetica', 12))
    style.configure('CustomLabel.TLabel', font=('Microsoft JhengHei', 12))
    style.configure('ResultLabel.TLabel', font=('Microsoft JhengHei', 12, 'bold'))

    # Create and configure the main frame
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.grid(column=0, row=0, sticky="wens")

    # Configure column and row weights for layout
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    # Initialize wine selection variables
    wine_selection = {wine_type: tk.BooleanVar(value=False) for wine_type in wine_types.values()}

    # Create budget entry label and widget
    budget_label = ttk.Label(frame, text="請輸入購買葡萄酒的預算：", style='CustomLabel.TLabel')
    budget_label.grid(column=0, row=0, sticky=tk.W)

    budget_entry = ttk.Entry(frame, style='CustomEntry.TEntry')
    budget_entry.grid(column=1, row=0, sticky=tk.W)

    # Create submit button
    submit_button = ttk.Button(frame, text="查詢", command=lambda: submit_budget(budget_entry, tree, all_wines, wine_selection, results_label), style='Large.TButton')
    submit_button.grid(column=6, row=0, sticky=tk.W)

    # Create checkboxes for wine type selection
    for i, (wine, var) in enumerate(wine_selection.items()):
        cb = ttk.Checkbutton(frame, text=wine, variable=var, width=10, style='CustomCheck.TCheckbutton')
        cb.grid(column=1+i % 6, row=1, sticky=tk.W)

    # Create results label
    results_label = ttk.Label(frame, text="", style='ResultLabel.TLabel')
    results_label.grid(column=0, row=1, columnspan=7, sticky=tk.W)

    # Create and configure the Treeview widget
    columns = all_wines.columns.tolist()
    tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
    for col in columns:
        if col in ('Vintage', 'Rating', 'RatingsCount', 'Price', 'Type'):
            tree.column(col, width=100, anchor='center')
        elif col in ('Winery', 'Region'):
            tree.column(col, width=175, anchor='w')
        else:
            tree.column(col, width=300, anchor='w')
        tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree, _col, False))

    # Create a vertical scrollbar for the tree
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=4, column=8, sticky='ns')
    tree.configure(yscrollcommand=scrollbar.set)

    tree.grid(row=4, column=0, columnspan=7, sticky='nsew')

    return wine_selection, tree, results_label


def main():
    """
    Main function to load wine data, set up the UI, and start the Tkinter event loop.
    """
    all_wines, wine_types = load_wine_data()  # Load wine data
    root = tk.Tk()  # Initialize the root Tk window
    root.title("WRS.v2 - Wine Recommendation System")
    root.geometry("1185x600")
    wine_selection, tree, results_label = setup_ui(root, all_wines, wine_types)
    root.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":
    main()
