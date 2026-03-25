import argparse

def count_reads(file_path):
    contador = 0

    with open(file_path, "r") as f:
        for linea in f:
            contador += 1

    reads = contador // 4
    return reads

def average_read_length(file_path):
	total_length = 0
	num_reads = 0

	with open(file_path, "r") as f:
		for i, linea in enumerate(f):
			if i % 4 == 1:
				seq = linea.strip()
				total_length += len(seq)
				num_reads += 1

	return total_length / num_reads

def gc_content(file_path):
	gc = 0
	total = 0

	with open(file_path,"r") as f:
		for i, linea in enumerate(f):
			if i % 4 == 1:
				seq = linea.strip().upper()
				gc += seq.count("G") + seq.count("C")
				total += len(seq)

	return gc / total

def main():
	parser = argparse.ArgumentParser(description="FASTQ basic statistics")
	parser.add_argument("--input", required=True, help="Path to FASTQ file")

	args = parser.parse_args()

	file_path = args.input

	reads = count_reads(file_path)
	avg_len = average_read_length(file_path)
	gc = gc_content(file_path)

	print("Reads:", reads)
	print("Avg length:", avg_len)
	print("GC content:", gc)

if __name__ == "__main__":
	main()
