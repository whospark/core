import json
from pprint import pprint

from connectivity import api

credentials = json.load(open('../credentials.json', 'r'))

c = credentials['CLIENT_ID']
k = credentials['API_KEY']
s = credentials['API_SECRET']

print('CLIENT_ID  (truncated) = {}[...]'.format(c[0:3]))
print('API_KEY    (truncated) = {}[...]'.format(k[0:10]))
print('API_SECRET (truncated) = {}[...]'.format(s[0:10]))

try:
    pprint(api.buy_limit_order(c, k, s, 0.01, 2000))
except:
    pass

try:
    api.cancel_order(c, k, s, '100')
except:
    pass

pprint(api.user_transactions(c, k, s))

pprint(api.withdrawal_requests(c, k, s))

pprint(api.ticker())

pprint(api.order_book())

pprint(api.transactions())

pprint(api.eur_usd_conversion_rate())
