from collections import deque
from itertools import islice
import copy as cp

class TreeDistance:
    def __init__(self, win0NotInWin1, win1NotInWin0, interDict, interSum, notInterDict, notInterSum, treeDistance):
        self.win0NodesNotInWin1 = win0NotInWin1
        self.win1NodesNotInWin0 = win1NotInWin0
        self.interDict = interDict
        self.interSumOfFreq = interSum
        self.notInterDict = notInterDict
        self.notInterSumOfFreq = notInterSum
        self.treeDistanceMetric = treeDistance

def driftDetectionADWIM(adwin, metric, Window, indexSlider):

    adwinBeforeMetric = cp.deepcopy(adwin)
    adwin.add_element(metric)
    if adwin.detected_change():  # A concept drift was identified
        if metric >= adwinBeforeMetric.estimation:
            Window.prefixTreeList = deque(islice(Window.prefixTreeList, indexSlider, None))
            Window.WinSize = len(Window.prefixTreeList) + 1  # We decrease the Max Size of the window to perform CDD more frequently, as we recently had a drift
            indexSlider = 1  # Reset the slider to perform the drift detection over the remaining trees in the list
            Window.cddFlag = True
        else:
            indexSlider += 1  # Increase the slider to include the next tree as a reference tree in W0
            Window.cddFlag = False
    else:
        indexSlider += 1  # Increase the slider to include the next tree as a reference tree in W0
        Window.cddFlag = False

    return indexSlider

def driftDetectionPH(ph, metric, Window, indexSlider):

    ph.add_element(metric)
    if ph.detected_change():
        print('Change detected by PH in data after: ' + str(Window.prefixTreeList[indexSlider].eventsSeen) + ' events seen.')
        Window.driftsIdentified.append(Window.prefixTreeList[indexSlider].eventsSeen)  # Save the number of events seen
        Window.prefixTreeList = deque(islice(Window.prefixTreeList, indexSlider, None))
        Window.WinSize = len(
            Window.prefixTreeList) + 1  # We decrease the Max Size of the window to perform CDD more frequently, as we recently had a drift
        indexSlider = 1  # Reset the slider to perform the drift detection over the remaining trees in the list
    else:
        indexSlider += 1  # Increase the slider to include the next tree as a reference tree in W0

    return indexSlider

def split_dict_keys(input_dict):
    unique_values = set()
    for key in input_dict.keys():
        if isinstance(key, tuple):
            key = key[0]
        keys = key.strip('()').split(',')
        for k in keys:
            unique_values.add(k.strip())
    return unique_values

def prefixTreeDistances(Window0, Window1):
    activities0 = split_dict_keys(Window0)
    activities1 = split_dict_keys(Window1)
    diff_ac = activities1 - activities0 - {'START'}

    win0NotInWin1 = {k: v ** 2 for k, v in Window0.items() if k not in Window1.keys()}
    win1NotInWin0 = {k: v ** 2 for k, v in Window1.items() if k not in Window0.keys()}

    lenW0NotW1 = len(win0NotInWin1)
    lenW1NotW0 = len(win1NotInWin0) #** 2

    dI = lenW1NotW0
    both = len(set(Window0) & set(Window1))

    interDict = {k: ((Window0[k] - Window1[k]) ** 2) for k in set(Window0) & set(Window1)}
    interSum = sum(interDict.values())

    notInterSum = sum(win0NotInWin1.values()) + sum(win1NotInWin0.values())

    notInterDict = {**win0NotInWin1, **win1NotInWin0}
    sortedNotInterDict = sorted(notInterDict.items(), key=lambda x: x[1], reverse=True)

    # totalTreeDistance = dI + ((interSum + notInterSum) ** (1/2))
    extra = 0
    if 'Added_Activity' in diff_ac:
        extra = 100
    
    if both == 0:
        totalTreeDistance = dI + extra
    else:
        totalTreeDistance = dI / both +extra #+ (interSum + notInterSum)

    treeDistance = TreeDistance(win0NotInWin1, win1NotInWin0, interDict, interSum, sortedNotInterDict, notInterSum, totalTreeDistance)
    #print(Window0)
    #print(Window1)
    return treeDistance


