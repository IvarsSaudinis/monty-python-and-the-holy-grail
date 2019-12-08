# Izveidot Python programmu, kas izveido lēmuma koka zīmējumu, atbilstoši mācību grāmatas 3.4.nodaļas piemēram
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt,
                            textcoords='axes fraction', va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    getTreeDepth(myTree)
    for k in myTree.keys():
        firstStr = k
        break
    # firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, \
              plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
                     cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1, facecolor='white', figsize=(12, 3))
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


def getNumLeafs(myTree):
    '''
    Traverse the entire tree and count only the leaf nodes; then it returns the number.
    '''
    numLeafs = 0
    firstStr = getKeyValue(myTree)
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        '''
        check if a key value is a dictionary, then recursively loop through the dict
        and return its leaf node.
        '''

        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getKeyValue(myTree):
    get = list(myTree.keys())
    ok = ''
    for i in get:
        ok = i
    return ok


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = getKeyValue(myTree)
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
    if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


def retrieveTree(i):
    listOfTrees = [{'tearRate': {'reduced': 'no lenses', 'normal': {'astigmatic': {'yes':
                                                                        {'prescript': {'hyper': {
                                                                            'age': {'pre': 'no lenses', 'presbyopic':
                                                                                'no lenses', 'young': 'hard'}},
                                                                                       'myope': 'hard'}},
                                                                    'no': {'age': {'pre':
                                                                                       'soft', 'presbyopic': {
                                                                        'prescript': {'hyper': 'soft', 'myope':
                                                                            'no lenses'}}, 'young': 'soft'}}}}}}
                   ]
    return listOfTrees[i]





if __name__ == '__main__':
    # createPlot()
    myTree = retrieveTree(0)


    print(myTree)
    n = getNumLeafs(myTree)
    d = getTreeDepth(myTree)
    print(n, d)
    for i in myTree.keys():
        print(i)
    createPlot(myTree)
