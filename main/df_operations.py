import pandas as pd


class SeqOperations:
	def __init__(self, data):
		self.data = data

	def cons_def(self):
		sequences = self.data['Sequence'].tolist()
		cons = ''
		sequence_length = len(sequences[0])
		nucleotides_count = [{
			'A': 0,
			'T': 0,
			'G': 0,
			'C': 0
		}
			for _ in range(sequence_length)]
		for sequence in sequences:
			for i, nucleotide in enumerate(sequence):
				nucleotides_count[i][nucleotide] += 1

		for counts in nucleotides_count:
			max_nucleotide = max(counts, key=counts.get)
			cons += max_nucleotide

		return cons


if __name__ == '__main__':
	dataframe = {
		'Sequence': ['ATG', 'ACT', 'AAG', 'CTT']
	}
	df = pd.DataFrame(dataframe)
	seq_operations = SeqOperations(df)
	print(seq_operations.cons_def())
