# Noncrossing RNA Secondary Structures

This repository contains a Python implementation to solve the **"Catalan Numbers and RNA Secondary Structures"** problem from the [Rosalind](http://rosalind.info) bioinformatics platform.

## Problem Overview

Given an RNA string `s` that has equal numbers of complementary base pairs (A-U and C-G), the goal is to compute the total number of **noncrossing perfect matchings** of basepair edges in the bonding graph of `s`. A matching is noncrossing if no two pairing edges cross when visualized as arcs above the string.

## Base Pairing Rules

* **A** pairs with **U**
* **C** pairs with **G**

## Example

**Input:** 

```
>Rosalind_57
AUAU
```

**Output:**

```
2
```

## Approach

The number of noncrossing matchings is computed recursively with memoization:

* The function considers pairing the first base with each valid match downstream.
* It recursively computes matchings for the substrings on either side of the pairing.
* The results are summed and taken modulo 1,000,000.

## Files

* `noncrossing_matchings.py` – Main Python script that reads a FASTA file and computes the answer.
* `rosalind_rna_matching.txt` – Sample input file in FASTA format.

## How to Run

1. Make sure you have Python 3 installed.
2. Save your RNA input in `rosalind_rna_matching.txt`.
3. Run the script:

```bash
python noncrossing_matchings.py
```

## Output

The script prints the total number of noncrossing perfect matchings modulo 1,000,000.

## License

MIT License

## Reference

* [Rosalind: Bioinformatics Stronghold](http://rosalind.info/problems/rnas/)
* [Catalan Numbers - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
