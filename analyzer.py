def analyze_dna_stability(dna_string):
    gc_count = 0
    total_count = 0
    for base in dna_string.upper():
        if base == 'G' or base == 'C':
            gc_count += 1
        elif base == 'A' or base == 'T':
            pass
        total_count += 1
    return (gc_count / total_count) * 100
