from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd 

print("This script takes a fasta and outputs stastics related to the sequence(s), and prints a table, you can also choose to save stats as a csv.\n")
try:
    file = input("Enter file path: ") 
    fasta =  SeqIO.parse(file, "fasta") 
except FileNotFoundError:
    print("Oop! Invalid path!")
else:
    save = input("Do you want to save result as csv[y/n]: ")
    data = {}
    for record in fasta:
        seq = record.seq
        data[record.id] = {
            "seq_len":  len(seq),
            "gc%":round(gc_fraction(record.seq) * 100, 1),
            'A': seq.count("A"),
            'T': seq.count("T"),
            'G': seq.count("G"),
            'C': seq.count("C")
        }

    df = pd.DataFrame(data).T
    print(df)

    if save == 'y':
        df.to_csv("seq-info.csv")
finally:
    print("Ext code 101")