import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


class ViolinPlot:
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def distance(self):
		self.dataframe['Категория'] = self.dataframe.apply(
			lambda row: 'Определены все' if not (
					np.isnan(row['Mismatch']) or np.isnan(row['JC']) or np.isnan(row['Kimura']))
			else 'Не все определены', axis=1
		)

	def plot_draw(self):
		plt.figure(figsize=(10, 8))
		ax = sb.violinplot(
			data=self.dataframe, x='Категория', y='Mismatch', inner='stick', legend=False, hue='Категория',
			palette={'Определены все': 'pink', 'Не все определены': 'red'}
		)
		plt.title('Violin plot')
		plt.xlabel('Категория')
		plt.ylabel('Посимвольное различие')

		cat_gif = plt.imread('smart_crop_516x290.jpg')
		plt.figimage(cat_gif, xo=1000, yo=300, alpha=1)

		plt.show()


if __name__ == '__main__':
	data = {
		'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
		'Sequence': ['ATGATCGTAC', 'ACGATCGTAC', 'GTACGATCGT', 'CATCGATCGT', 'ATTATCGTAC', 'ATCCTGAAAA',
		             'ATGTTCGTAC', 'GCTGACCCGG', 'TAAAGTAAAA', 'ACGAGCGTAC', 'ACTTTATATA', 'CCAACAGCGG',
		             'ATCATAGTAC', 'CTAACCGAAT', 'ATGATCCTAC', 'ATGATCGCAC', 'ATGATCGTTC', 'CTCATTCTTA',
		             'GAAGTTGGTA', 'ATGATCGTAC'],
		'Mismatch': [0.0, 0.1, 0.9, 1.0, 0.1, 0.6, 0.1, 0.9, 0.8, 0.2, 0.8, 0.8, 0.2, 0.5, 0.1, 0.1, 0.1, 0.6, 0.8,
		             0.0],
		'JC': [-0.0, 0.107326, np.nan, np.nan, 0.107326, 1.207078, 0.107326, np.nan, np.nan, 0.232616, np.nan, np.nan,
		       0.232616, 0.823959, 0.107326, 0.107326, 0.107326, 1.207078, np.nan, -0.0],
		'Kimura': [-0.0, -0.0, 0.155077, 0.292894, 0.034496, 0.166572, 0.032714, 0.128523, 0.166572, 0.034496,
		           0.252643, 0.105361, 0.067719, 0.067719, 0.032714, -0.0, 0.032714, 0.166572, 0.137218, -0.0]
	}
	df = pd.DataFrame(data)

	plotter = ViolinPlot(df)
	plotter.distance()
	plotter.plot_draw()
