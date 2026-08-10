import argparse


def DNAct(args):
    dna = args.dna
    DNA = dna.upper()
    A = DNA.count("A")
    T = DNA.count("T")
    C = DNA.count("C")
    G = DNA.count("G")
    print(f"A:{A}\nT:{T}\nC:{C}\nG:{G}")


def transcribe(args):
    dna = args.dna
    DNA = dna.upper()
    RNA = DNA.replace("T", "U")
    print(RNA)


def complement(args):
    dna = args.dna
    DNA = dna.upper()
    complementmap = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
    complement = DNA.translate(complementmap)
    print(complement)


def revcomp(args):
    dna = args.dna
    DNA = dna.upper()
    complementmap = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
    complement = DNA.translate(complementmap)
    print(complement[::-1])


def main():
    parser = argparse.ArgumentParser("simple sequence manipulation suite")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # DNAct subparser
    DNActsp = subparsers.add_parser("DNAct", help="count characters in DNA string")
    DNActsp.add_argument("dna", type=str, help="DNA string")
    DNActsp.set_defaults(func=DNAct)
    # transcribe subparser
    transcribesp = subparsers.add_parser(
        "transcribe", help="transcribe DNA string to RNA"
    )
    transcribesp.add_argument("dna", type=str, help="DNA string")
    transcribesp.set_defaults(func=transcribe)
    # complement subparser
    complementsp = subparsers.add_parser(
        "complement", help="display complement of a DNA string"
    )
    complementsp.add_argument("dna", type=str, help="DNA string")
    complementsp.set_defaults(func=complement)
    # revcomp subparser
    revcompsp = subparsers.add_parser(
        "revcomp", help="display reverse complement of a DNA string"
    )
    revcompsp.add_argument("dna", type=str, help="DNA string")
    revcompsp.set_defaults(func=revcomp)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
