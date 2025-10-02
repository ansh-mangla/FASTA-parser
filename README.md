Here’s a clean **README.md** draft for your FASTA parser project 👇

````markdown
# FASTA Parser & Sequence Statistics

This project provides a simple Python script to parse FASTA files and generate useful sequence statistics such as length, GC content, and nucleotide counts. Results are displayed in a tabular format and can optionally be saved as a CSV file.

---

## Features
- Reads DNA sequences from a FASTA file
- Computes:
  - Sequence length
  - GC percentage
  - Nucleotide counts (A, T, G, C)
- Displays results in a formatted table
- Option to export results to a CSV file

---

## Requirements
- Python 3.7+
- [Biopython](https://biopython.org/)
- [Pandas](https://pandas.pydata.org/)

Install dependencies:
```bash
pip install biopython pandas
````

---

## Usage

1. Run the script:
```bash
   python DNA-fasta-parser.py
```
2. Enter the path to your FASTA file when prompted.
3. Choose whether to save results as a CSV.

---

## Example

**Input FASTA (`example.fasta`):**

```
>seq1
ATGCATGCATGC
>seq2
GGGAAATTTCCC
```

**Output (printed table):**

```
       seq_len   gc%   A   T   G   C
seq1       12   50.0   3   3   3   3
seq2       12   50.0   3   3   3   3
```

**CSV Export (`seq-info.csv`):**

|      | seq_len | gc%  | A | T | G | C |
| ---- | ------- | ---- | - | - | - | - |
| seq1 | 12      | 50.0 | 3 | 3 | 3 | 3 |
| seq2 | 12      | 50.0 | 3 | 3 | 3 | 3 |

---

## Notes

* The script exits with code `101` after execution.
* Invalid file paths are handled gracefully with an error message.

---

## License

This project is licensed under the MIT License. Free to use and modify by anyone. 

