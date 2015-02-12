__author__ = 'talluri'

import re
fh = open('west.html')
content = fh.read()
#print content
def topScorer(scores):
    maxim = None
    for player in scores:
        if  maxim is None:
            maxim = player
        elif scores[player] > scores[maxim]:
              maxim = player
    return maxim,scores[maxim]
matches = re.findall(r'<a.*"playerName">(.*)</a>.*\n.*"battingDismissal">(.*)</td>.*\n.*"battingRuns">(.*)</td>.*\n.*"battingDetails">.*</td>.*\n.*"battingDetails">(.*)</td>',content,re.I|re.M)
scores = {}
if matches:
    for player in matches:
        # print "player name: {}".format(player)
        print "{}\nplayer name: {}, dissmissed: {}, runs: {}, balls: {}".format('#'*80,player[0], player[1], player[2], player[3])
        scores[player[0]] = player[2]

top_scorer, top_score = topScorer(scores)
print top_scorer,":", top_score

top_score = max(map(lambda x: x[2], matches))

print 'lambda top score', top_score


