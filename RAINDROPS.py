def convert(n):
    return (("" if n % 3 else "Pling") + ("" if n % 5 else "Plang") + 
            ("" if n % 7 else "Plong")) or str(n)
