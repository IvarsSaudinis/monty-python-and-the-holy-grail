# Izmantojot mācību grāmatas 4.nodaļas piemērus, izveidot Python programmu, kas grupē iepriekš atlasīto
# e-pasta vēstuļu (failu) tekstus spama un "labo" vēstuļu grupās
from numpy import *
import re  # RegEx jeb regularas izteiksmes


def loadDataSet():
    vestulesVardi = \
        [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
         ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
         ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
         ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
         ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
         ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    varduVektors = [0, 1, 0, 1, 0, 1]  # 1 - ir izskaross, 0 - nav aizskaross
    return vestulesVardi, varduVektors


def createVocabList(DatuKopa):
    Vardnicas = set([])
    for dokuments in DatuKopa:
        Vardnicas = Vardnicas | set(dokuments)
    return list(Vardnicas)


def setOfWords2Vec(Vardnicas, IevadDati):
    Vektors = [0] * len(Vardnicas)
    for vards in IevadDati:
        if vards in Vardnicas:
            Vektors[Vardnicas.index(vards)] = 1
        else:
            print("Vards ", vards, " nav vardnica!")
    return Vektors


def trainNB0(MacibuMatrica, MacibuKategorija):
    MacibuDokumentuSkaits = len(MacibuMatrica)
    VarduSkaits = len(MacibuMatrica[0])
    pAizskaross = sum(MacibuKategorija) / float(MacibuDokumentuSkaits)
    p0skaits = zeros(VarduSkaits);
    p1skaits = zeros(VarduSkaits)
    p0dalitajs = 0.0;
    p1dalitajs = 0.0
    for i in range(MacibuDokumentuSkaits):
        if MacibuKategorija[i] == 1:
            p1skaits += MacibuMatrica[i]
            p1dalitajs += sum(MacibuMatrica[i])
        else:
            p0skaits += MacibuMatrica[i]
            p0dalitajs += sum(MacibuMatrica[i])
    p1vektors = p1skaits / p1dalitajs
    p0vektors = p0skaits / p0dalitajs
    return p0vektors, p1vektors, pAizskaross


def classifyNB(Klasifikacija, p0vektors, p1vektors, pKlase1):
    p1 = sum(Klasifikacija * p1vektors) + log(pKlase1)
    p0 = sum(Klasifikacija * p0vektors) + log(1.0 - pKlase1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    ePasts, Klases = loadDataSet()
    Vardnicas = createVocabList(ePasts)
    MacibuMatrica = []
    for zinaIeksDokumenta in ePasts:
        MacibuMatrica.append(setOfWords2Vec(Vardnicas, zinaIeksDokumenta))
    p0V, p1V, pAb = trainNB0(array(MacibuMatrica), array(Klases))
    TestaDati = ['love', 'my', 'dalmation']
    sisDokuments = array(setOfWords2Vec(Vardnicas, TestaDati))
    print(TestaDati, ' klasificejas ka: ', classifyNB(sisDokuments, p0V, p1V, pAb))
    TestaDati = ['stupid', 'garbage']
    sisDokuments = array(setOfWords2Vec(Vardnicas, TestaDati))
    print(TestaDati, ' klasificejas ka: ', classifyNB(sisDokuments, p0V, p1V, pAb))


def bagOfWords2VecMN(Vardnicas, ievadDati):
    Vektors = [0] * len(Vardnicas)
    for vards in ievadDati:
        if vards in Vardnicas:
            Vektors[Vardnicas.index(vards)] += 1
    return Vektors


def textParse(GaraVirkne):
    VarduSaraksts = re.split(r'\W*', GaraVirkne)
    return [vards.lower() for vards in VarduSaraksts if len(vards) > 2]


def spamTest():
    Dokumenti = [];
    Klases = [];
    VissTeksts = []
    for i in range(1, 26):
       # print(i)
        VarduSaraksts \
            = textParse(open("data/spam/" + str(i) + ".txt").read())
        Dokumenti.append(VarduSaraksts)
        VissTeksts.extend(VarduSaraksts)
        Klases.append(1)
        VarduSaraksts \
            = textParse(open("data/ham/" + str(i) + ".txt").read())
        Dokumenti.append(VarduSaraksts)
        VissTeksts.extend(VarduSaraksts)
        Klases.append(0)
    Vardnicas = createVocabList(Dokumenti)
    MacibuDati = range(50);
    TestaDati = []
    for i in range(10):
        Numurs = int(random.uniform(0, len(MacibuDati)))
        TestaDati.append(MacibuDati[Numurs])
       #del (MacibuDati[Numurs])
    MacibuMatrica = [];
    MacibuKlases = []
    for DokumentaNr in MacibuDati:
        MacibuMatrica.append(setOfWords2Vec(Vardnicas, Dokumenti[DokumentaNr]))
        MacibuKlases.append(Klases[DokumentaNr])
    p0V, p1V, pSpam = trainNB0(array(MacibuMatrica), array(MacibuKlases))
    KluduSkaits = 0
    for DokumentaNr in TestaDati:
        wordVector = setOfWords2Vec(Vardnicas, Dokumenti[DokumentaNr])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != \
                Klases[DokumentaNr]: KluduSkaits += 1
    print("Kludu limenis: ", float(KluduSkaits) / len(TestaDati))



ePasts, Klases = loadDataSet()
testaVardnica = createVocabList(ePasts)
print("Testa vardnica:\n", testaVardnica)
print("\nVardi no 0.dokumenta:\n", setOfWords2Vec(testaVardnica, ePasts[0]))
print("\nVardi no 3.dokumenta:\n", setOfWords2Vec(testaVardnica, ePasts[3]))


testaVardnica = createVocabList(ePasts)
print("\nTesta vardnica:\n", testaVardnica)
MacibuMatrica = []
for zinaIeksDokumenta in ePasts:
    MacibuMatrica.append(
        setOfWords2Vec(testaVardnica, zinaIeksDokumenta))
p0V, p1V, pAb = trainNB0(MacibuMatrica, Klases)
print("\npAb:", pAb)
print("\np0V:\n", p0V)
print("\np1V:\n", p1V)


testingNB()


Zina = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
regEx = re.compile('\\W*')
VarduSaraksts = regEx.split(Zina)
Vardi = [vards.lower() for vards in VarduSaraksts if len(vards) > 0]
print("\nVardi: \n", Vardi)
ePasts = open("data/ham/3.txt").read()
VarduSaraksts = regEx.split(ePasts)


spamTest()
