import pytest

from core import count_reads, average_read_length, gc_content


def test_count_reads():
    result = count_reads("data/test.fastq")
    assert result == 3


def test_average_read_length():
    result = average_read_length("data/test.fastq")
    assert result == 4.0


def test_gc_content():
    result = gc_content("data/test.fastq")
    assert result == 8 / 12

def test_missing_file_raises_error():
	with pytest.raises(FileNotFoundError):
		count_reads("data/does_not_exit.fastq")
