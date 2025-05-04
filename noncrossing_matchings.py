MOD = 10**6

from functools import lru_cache

# Base pairing rules
def can_pair(a, b):
    return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or \
           (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

# Memoized resursive function
@lru_cache(maxsize=None)
def count_matchings(s):
    if len(s) == 0:
        return 1

    total = 0
    for k in range(1, len(s), 2):
        if can_pair(s[0], s[k]):
            left = count_matchings(s[1:k])
            right = count_matchings(s[k+1:])
            total += (left * right) % MOD
            total %= MOD

    return total

# Read input file
def read_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return ''.join(line.strip() for line in lines if not line.startswith('>'))

# Main
if __name__ == "__main__":
    rna_seq = read_fasta("rosalind_rna_matching.txt")
    print(count_matchings(rna_seq))
