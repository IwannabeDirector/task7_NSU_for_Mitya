import pandas as pd


class PandasImport:
	def __init__(self, file_path):
		self.file_path = file_path

	def file_read(self):
		return pd.read_excel(self.file_path)


if __name__ == '__main__':
	file_folder = 'sequences_7.1.xlsx'
	excel_reader = PandasImport(file_folder)
	data = excel_reader.file_read()
	data.columns = ['number', 'Sequence']
