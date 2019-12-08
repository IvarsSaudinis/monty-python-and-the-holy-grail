# Pārveidot 11.nodaļas kongresa vēlēšanu piemēru par Python3 programmu
# Association analysis with the Apriori algorithm

from classes import apriori
# uzstādīts atbalsts priekš python3 no pull requesta - https://github.com/votesmart/python-votesmart/pull/15
from votesmart import votesmart

'''
Your membership status will be reviewed. If approved, you will receive an activation e-mail with your API key. Your key may take up to 1 business day to be approved.
Order Number: 5777320191208904
'''
# :( votesmart.VotesmartApiError: Authorization failed
votesmart.apikey = 'a7fa40adec6f4a77178799fae4441030'
bills = votesmart.votes.getBillsByStateRecent()
for bill in bills:
     print (bill.title,bill.billId)
# it kā vajadzētu būt tādam ar id 11820
bill = votesmart.votes.getBill(11820)
for action in bill.actions:
     if action.stage=='Passage':
          print(action.actionId)


actionIdList,billTitles = apriori.getActionIds()











