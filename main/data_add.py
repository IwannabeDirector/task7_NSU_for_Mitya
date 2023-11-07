import pandas as pd
import math
import numpy as np


class SequencesDistance:
	def __init__(self, dataframe, consensus):
		self.consensus = consensus
		self.dataframe = dataframe

	def mismatch(self, sequence):
		return sum(1 for a, b in zip(self.consensus, sequence) if a != b) / len(self.consensus)

	def kimura(self, sequence):
		proportion_mismatch = self.mismatch(sequence)

		transverses = sum(
			1 for a, b in zip(self.consensus, sequence)
			if a != b and ((a == 'A' and b == 'G') or (a == 'G' and b == 'A')
							or (a == 'C' and b == 'T') or (a == 'T' and b == 'C'))
		)
		transitions = sum(
			1 for a, b in zip(self.consensus, sequence)
			if a != b and ((a == 'A' and b == 'T') or (a == 'T' and b == 'A')
							or (a == 'C' and b == 'G') or (a == 'G' and b == 'C'))
		)

		try:
			kimura_distance = -(1 / 2) * math.log(
				1 - (2 / 3) * (proportion_mismatch - (transverses / len(self.consensus))) * (
						1 - (1 / 2) * (transitions / len(self.consensus)))
			)
		except ValueError:
			kimura_distance = np.nan
		return kimura_distance

	def jc(self, sequence):
		proportion_mismatch = self.mismatch(sequence)

		try:
			jc_distance = -0.75 * math.log(1 - (4 / 3 * proportion_mismatch))
		except ValueError:
			jc_distance = np.nan
		return jc_distance

	def add_in_dataframe(self):
		self.dataframe['Mismatch'] = self.dataframe['Sequence'].apply(self.mismatch)
		self.dataframe['JC'] = self.dataframe['Sequence'].apply(self.jc)
		self.dataframe['Kimura'] = self.dataframe['Sequence'].apply(self.kimura)


if __name__ == '__main__':

	data = {
		'ID': [1, 2, 3, 4],
		'Sequence': ['ATG', 'ACT', 'AAG', 'CTT']
	}
	consensus_sequence = 'ATT'
	df_sequences = pd.DataFrame(data)

	calculator = SequencesDistance(df_sequences, consensus_sequence)
	calculator.add_in_dataframe()
	print(df_sequences)
