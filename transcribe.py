def transcribe():
    dna = input("enter DNA sequence")
    DNA = dna.upper()
    RNA = DNA.replace("T", "U")
    print(RNA)


transcribe()
