import random

def random_line(afile):
    increm = 0
    while increm < 15:
        lines = open(afile).read().splitlines()
        myline =random.choice(lines)
        print(myline)
        increm += 1



random_line('url_4ecoindex_dataset.csv')