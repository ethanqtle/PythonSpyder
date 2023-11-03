# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:26:41 2023

@author: Ethan
"""

# Define a dictionary mapping nucleotide triplets to amino acids.
amino_acids = {
    "TTT": "Phe", "TCT": "Ser", "TGT": "Cys", "TAT": "Tyr",
    "TTC": "Phe", "TCC": "Ser", "TGC": "Cys", "TAC": "Tyr",
    "TTG": "Leu", "TCG": "Ser", "TGG": "Trp", "TAG": "***",
    "TTA": "Leu", "TCA": "Ser", "TGA": "***", "TAA": "***",
    "CTT": "Leu", "CCT": "Pro", "CGT": "Arg", "CAT": "His",
    "CTC": "Leu", "CCC": "Pro", "CGC": "Arg", "CAC": "His",
    "CTG": "Leu", "CCG": "Pro", "CGG": "Arg", "CAG": "Gln",
    "CTA": "Leu", "CCA": "Pro", "CGA": "Arg", "CAA": "Gln",
    "GTT": "Val", "GCT": "Ala", "GGT": "Gly", "GAT": "Asp",
    "GTC": "Val", "GCC": "Ala", "GGC": "Gly", "GAC": "Asp",
    "GTG": "Val", "GCG": "Ala", "GGG": "Gly", "GAG": "Glu",
    "GTA": "Val", "GCA": "Ala", "GGA": "Gly", "GAA": "Els",
    "ATT": "Ile", "ACT": "Thr", "AGT": "Ser", "AAT": "Asn",
    "ATC": "Ile", "ACC": "Thr", "AGC": "Ser", "AAC": "Asn",
    "ATG": "Met", "ACG": "Thr", "AGG": "Arg", "AAG": "Lys",
    "ATA": "Ile", "ACA": "Thr", "AGA": "Arg", "AAA": "Lys"
}

def clean_sequence(sequence):
    cleaned_sequence = ''
    for char in sequence:
        if char.isalpha():
            cleaned_sequence += char.upper()
    return cleaned_sequence

def main():
    while True:
        sequence = input("Enter a nucleotide sequence, or just press ENTER to quit: ")
        if not sequence:
            break

        sequence = clean_sequence(sequence)

        if len(sequence) % 3 != 0:
            print("Error: You must give complete triples.")
        else:
            i = 0
            while i < len(sequence):
                triplet = sequence[i:i + 3]
                if triplet in amino_acids:
                    print(f"{triplet} {amino_acids[triplet]}")
                else:
                    print(f"{triplet} invalid sequence")
                i += 3

if __name__ == "__main":
    main()
