import random

pd6 = ["Ahn,Jae Bum", "Argodale,Jane", "Cahn,David", "Chen,Simon", "Cohen,Eli", "Coppa,Aaron", "Greene,Victoria", "Huang,Edric", "Kozak,Severyn", "Kurtovic,Benjamin", "Lam,Raymond", "Lin,Helen", "Lin,Jing Chao", "Li,Roger", "Lui,Marlena", "Lu,Jasper", "Luo,Jason", "Ong,Timothy", "Rehab,Arfan", "Rein,Dorit", "Tang,Derek", "Venderbush,Sweyn", "Wakefield,Joshua", "Wu,Jia Sen", "Ye,Tyrone", "Yin,Jeffrey", "Yuen,Jared", "Zarenberg,Andrew", "Zheng,Stanley", "Zhen,Jason", "Zhu,Julie", "Zhu,Steve"]

pd7 = ["Attal,Benjamin", "Burke,Christopher", "Cahn,Jack", "Chin,Joshua", "Chuk,Brian", "Chung,Victoria", "Conybeare,Sebastian", "Dai,Nancy", "Dolotov,Glib", "Duda,Justin", "Ezratty,Maia", "Field Thompson,William", "Galasinao,Nicholas", "Han,Jason", "Herman,Hunter", "Hofing,Joshua", "Islam,Yaseen", "Karson,Jeremy", "Khan,Sabrina", "Leung,Alvin", "Lin,Hanson", "Lin,Michele", "Luo,Haoxin", "Mai,Judy", "Mei,Kelvin", "Pedraza,Cristian", "Rosenberg,Noah", "Sheikh,Shaan", "Siu,Isabella", "Sterling,Zane", "Wan,Tak Chi", "Xu,Christine"]

def shuffleandcombine(c1,c2):
    random.shuffle(c1)
    random.shuffle(c2)
    combined = c2 + c1
    return combined

def makegroups(c1,c2):
    class1 = shuffleandcombine(c1,c2);
    groups = ""
    i = 0
    while len(class1) > 0:
        groups += (str)(i/4+1) + "," + class1.pop() + "\n"
        i += 1
    return groups

print makegroups(pd6,pd7)
