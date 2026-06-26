import pandas as pd


class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)

        print(f"Removed {before - after} duplicate rows.")
        return self

    def fill_missing_values(self, value=0):
        self.df = self.df.fillna(value)

        print("Missing values filled.")
        return self

    def standardize_columns(self):
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        print("Column names standardized.")
        return self

    def show_info(self):
        print("\nDataset Info:")
        print(self.df.info())
        return self

    def get_data(self):
        return self.df


# Sample Data
data = {
    " Name ": ["Harsh", "Aman", "Harsh", None],
    " Age ": [20, 21, 20, 22],
    " City ": ["Jaipur", "Delhi", "Jaipur", None]
}

df = pd.DataFrame(data)

# Using the Data Cleaner
cleaner = DataCleaner(df)

cleaned_df = (
    cleaner
    .standardize_columns()
    .remove_duplicates()
    .fill_missing_values("Unknown")
    .get_data()
)

print("\nCleaned Data:")
print(cleaned_df)