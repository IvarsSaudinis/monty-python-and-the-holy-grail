# Izveidot pēc mācību grāmatas 5.3.nodaļas norādēm Python programmu, kas nosaka zirga veselības prognozes.
# Datu faili pieejami arī šīs nodarbības mapē "data"
import matplotlib.pyplot as plt
from numpy import *


def loadDataSet():
    DatuMasivs = [];
    Kategorija = []
    Fails = open('data/testSet.txt')
    for Rinda in Fails.readlines():
        Vards = Rinda.strip().split()
        DatuMasivs.append([1.0, float(Vards[0]), float(Vards[1])])
        Kategorija.append(int(Vards[2]))
    return DatuMasivs, Kategorija


def sigmoid(inX):

    return 1.0 / (1 +  exp(-inX ))


def gradAscent(IevadDati, Kategorijas):
    Datumasivs = mat(IevadDati)
    KategorijuMasivs = mat(Kategorijas).transpose()
    m, n = shape(Datumasivs)
    Alfa = 0.001;
    CikluSkaits = 500
    Koeficienti = ones((n, 1))
    for k in range(CikluSkaits):
        h = sigmoid(Datumasivs * Koeficienti)
        Kluda = (KategorijuMasivs - h)
        Koeficienti = Koeficienti + Alfa * Datumasivs.transpose() * Kluda
    return Koeficienti


def plotBestFit(Koeficienti):
    Svars = mat(Koeficienti).getA()
    DatuMasivs, Kategorijas = loadDataSet()
    Dati = array(DatuMasivs)
    n = shape(Dati)[0]
    x1 = [];
    y1 = []
    x2 = [];
    y2 = []
    for i in range(n):
        if int(Kategorijas[i]) == 1:
            x1.append(Dati[i, 1]);
            y1.append(Dati[i, 2])
        else:
            x2.append(Dati[i, 1]);
            y2.append(Dati[i, 2])
    Attels = plt.figure()
    Ass = Attels.add_subplot(111)
    Ass.scatter(x1, y1, s=30, c='red', marker='s')
    Ass.scatter(x2, y2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-Svars[0] - Svars[1] * x) / Svars[2]
    Ass.plot(x, y)
    plt.xlabel('X1');
    plt.ylabel('X2');
    plt.show()


def stocGradAscent0(DatuMasivs, Kategorijas):
    m, n = shape(DatuMasivs)
    Alfa = 0.01
    Koeficienti = ones(n)
    for i in range(m):
        h = sigmoid(sum(DatuMasivs[i] * Koeficienti))
        Kluda = Kategorijas[i] - h
        Koeficienti = Koeficienti + Alfa * Kluda * DatuMasivs[i]
    return Koeficienti


def stocGradAscent1(DatuMasivs, Kategorijas, IteracijuSkaits=150):
    m, n = shape(DatuMasivs)
    Koeficienti = ones(n)
    for j in range(IteracijuSkaits):
        Indekss = range(m)
    for i in range(m):
        Alfa = 4 / (1.0 + j + i) + 0.01
        Izvele = int(random.uniform(0, len(Indekss)))
        h = sigmoid(sum(DatuMasivs[Izvele] * Koeficienti))
        Kluda = Kategorijas[Izvele] - h
        Koeficienti = Koeficienti + Alfa * Kluda * DatuMasivs[Izvele]
    return Koeficienti


def classifyVector(IevadDati, Koeficienti):
    Varbutiba = sigmoid(sum(IevadDati * Koeficienti))
    if Varbutiba > 0.5:
        return 1.0
    else:
        return 0.0


def colicTest():

    MacibuFails = open('data/horseColicTraining.txt')
    TestaFails = open('data/horseColicTest.txt')
    MacibuKopa = []
    MacibuKategorijas = []
    for Rinda in MacibuFails.readlines():
        Kartejais = Rinda.strip().split('\t')
        RinduMasivs = []
        for i in range(21):
            RinduMasivs.append(float(Kartejais[i]))
        MacibuKopa.append(RinduMasivs)
        MacibuKategorijas.append(float(Kartejais[21]))
    MacibuKoeficienti = stocGradAscent1(array(MacibuKopa), MacibuKategorijas, 500)
    KluduSkaits = 0
    TestaVektors = 0.0
    for Rinda in TestaFails.readlines():
        TestaVektors += 1.0
        Kartejais = Rinda.strip().split('\t')
        RinduMasivs = []
        for i in range(21):
            RinduMasivs.append(float(Kartejais[i]))
        if int(classifyVector(array(RinduMasivs), MacibuKoeficienti)) != int(Kartejais[21]):
            KluduSkaits += 1
    KludasLimenis = (float(KluduSkaits) / TestaVektors)
    print("Saja testa kludu limenis ir ", KludasLimenis)
    return KludasLimenis


def multiTest():
    TestuSkaits = 10
    KluduSumma = 0.0
    for k in range(TestuSkaits):
        KluduSumma += colicTest()
    print("Pec ", TestuSkaits, " iteracijam videjais kludu limenis ir : ",
          KluduSumma / float(TestuSkaits))

# ==============================
Dati, Kategorijas = loadDataSet()
print(gradAscent(Dati, Kategorijas))  ###
Koeficienti = gradAscent(Dati, Kategorijas)
plotBestFit(Koeficienti.getA())  # p.91
Koeficienti = stocGradAscent0(array(Dati), Kategorijas)  # p.92
#plotBestFit(Koeficienti.getA())
Koeficienti = stocGradAscent1(array(Dati), Kategorijas)  # p.95
#plotBestFit(Koeficienti.getA())
multiTest()  # p.99
