import pandas as pd


class TableCompare:
    def __init__(self, dataframe, texas_path):
        self.dataframe = dataframe
        self.texas_path = texas_path

    def load_taxas(self):
        texas_df = pd.read_csv(self.texas_path)

        self.dataframe = self.dataframe.merge(texas_df, on='number')

    def remove_zero(self):
        self.dataframe = self.dataframe.loc[self.dataframe['cell_type'] != 'unknown']

    def bar_plot(self):
        tax_count = self.dataframe['taxa_name'].value_counts()
        tax_count.plot(kind='bar')

    def data_export_tsv(self, output_path):
        self.dataframe.to_csv(output_path, sep='\t', index=False)


if __name__ == '__main__':
    taxas_path = 'taxas_7.1.csv'
    output_path = 'merged_7.1.tsv'
