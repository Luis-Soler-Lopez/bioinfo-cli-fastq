
# FASTQ CLI Stats

Simple command-line tool to compute basic statistics from FASTQ files.

## Features

- Read count
- Average read length
- GC content

## Usage

```bash
python3 fastq_stats.py --input data/test.fastq

## Input format

The tool expects a FASTQ file as input.

## Project structure

- `fastq_stats.py`: main CLI script
- `data/test.fastq`: example FASTQ file
- `README.md`: project documentation

## Notes

This project was built as an introductory bioinformatics engineering exercise focused on:
- file parsing
- CLI usage
- basic FASTQ statistics
