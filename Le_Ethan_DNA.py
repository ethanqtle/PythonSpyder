# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:22:38 2023

@author: Ethan
"""
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

def clean_sequence(user_input):
    clean_string = ""
    for c in user_input:
        if c.isalpha():
            clean_string += c.upper()
    return clean_string

def nucleotide_response(clean_string):
    i = 0
    if len(clean_string) % 3 != 0:
        print("Error: You must give complete triples.")
    else:
        while i < len(clean_string)/3:
            str3 = clean_string[3*i : 3*i + 3]
            if str3 in amino_acids:
                print(str3, amino_acids[str3])
            else:
                print(str3, "invalid sequence")
            i += 1
while True:
    user_input = str(input("Please enter a nucleotide sequence, or just press ENTER to quit: "))
    clean_string = clean_sequence(user_input)
    if clean_string == "":
        break
    nucleotide_response(clean_string)
