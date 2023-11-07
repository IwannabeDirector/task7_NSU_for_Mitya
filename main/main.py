from file_open import PandasImport
from df_operations import SeqOperations
from data_add import SequencesDistance
from violin_plot import ViolinPlot
from compare import TableCompare


def main():
	file_path = 'sequences_7.1.xlsx'

	excel_reader = PandasImport(file_path)
	data = excel_reader.file_read()
	data.columns = ['number', 'Sequence']

	seq_operations = SeqOperations(data)
	consensus = seq_operations.cons_def()

	seq_distances = SequencesDistance(data, consensus)
	seq_distances.add_in_dataframe()

	plot_visualizer = ViolinPlot(data)
	plot_visualizer.distance()
	plot_visualizer.plot_draw()

	t_p = 'taxas_7.1.csv'
	output_name = 'merged_7.1.tsv'
	table_compare = TableCompare(data, t_p)
	table_compare.load_taxas()
	table_compare.remove_zero()
	table_compare.bar_plot()
	table_compare.data_export_tsv(output_name)


if __name__ == '__main__':
	main()
