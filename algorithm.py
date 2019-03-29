import random


class Algorithm:


    def __init__(self, name, algorithm):

        self.name = name
        self.algorithm = algorithm




algorithms = {
    "Aa": "R2 D' F2 D B2 D' F2 D B2 R2 U'",
    "Ab": "R2 B2 U' F2 U B2 U' F2 U R2 U2",
    "E": "B2 D' R2 U' R2 F2 L2 B2 U' L2 F2 R' U R' B2 R U' R'",
    "F": "F2 L2 R2 U' L2 U B2 R2 U F2 U' R' B2 L2 R2 F2 R'",
    "Ga": "U' F2 U R2 U' L2 U B2 L2 D B2 L R' U2 L' R' ",
    "Gb": "F2 U' R2 U F2 U F2 R2 U2 F2 U' L R F2 L' R'",
    "Gc": "R2 U2 L2 R2 D' B2 D' R2 U R2 U' L' R D2 L' R' ",
    "Gd": "L2 U L2 B2 U B2 U' R2 U L2 U' L R' B2 L R'",
    "H": "L2 B2 F2 R2 D L2 B2 F2 R2 U' ",
    "Ja": "L2 D' B2 D B2 U' B2 U B2 L2 U'",
    "Jb": "L2 F2 U F2 D' L2 D L2 U' L2",
    "Na": "D' F2 D2 F2 R2 U' R2 D2 L2 F2 D L' R U2 F2 L' R'",
    "Nb": "D' L2 B2 D2 R2 F2 D' F2 D2 R2 U' L' R D2 F2 L' R' ",
    "Ra": "L2 U F2 D' F2 R2 U' B2 L2 R2 U L' R U2 L R'",
    "Rb": "R2 U' F2 D F2 L2 U B2 L2 R2 U' L' R U2 L R' ",
    "T": "L2 D' B2 U B2 L2 D F2 U' F2 U'",
    "Ua": "U2 R2 B2 F2 R2 D F2 L2 B2 U L' R' U2 L' R' ",
    "Ub": "R2 U' F2 L2 B2 D B2 L2 F2 U2 R2 ",
    "V": "L2 U' B2 F2 U' R2 U R2 U2 F2 U B' F' R2 B' F L2",
    "Y": "L2 R2 D B2 D2 L2 U F2 U2 L2 D' L' R D2 F2 L' R' U'",
    "Z": "U' F2 U F2 U F2 U F2 U F2 U L' R U2 L R'"
}

def select_algorithms(algs):
    return_algs = []
    for alg in algs:
        return_algs.append(Algorithm(alg, algorithms[alg]))
    return return_algs




algorithms_to_use = ["Aa", "Ab", "E", "F", "Ga", "Gb", "Gc", "Gd", "H", "Ja", "Jb", "Na", "Nb", "Ra", "T", "Ua","Ub", "Z"]


selected = select_algorithms(algorithms_to_use)

