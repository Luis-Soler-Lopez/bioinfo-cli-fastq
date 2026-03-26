def count_reads(file_path):
    contador = 0
    with open(file_path, "r") as f:
        for linea in f:
            contador += 1
    return contador // 4


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

    with open(file_path, "r") as f:
        for i, linea in enumerate(f):
            if i % 4 == 1:
                seq = linea.strip().upper()
                gc += seq.count("G") + seq.count("C")
                total += len(seq)

    return gc / total
