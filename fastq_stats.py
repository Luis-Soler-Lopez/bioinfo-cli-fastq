import argparse

from core import count_reads, average_read_length, gc_content

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
print("debug")
