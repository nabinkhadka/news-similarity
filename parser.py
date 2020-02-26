import os
from fuzzyparsers import parse_date
import dateutil.parser as dparser
import datetime
import json
count = 0
for p,d,files in os.walk('col_sim'):
    for f in files:
        if f.endswith('.json'):
            to_read = os.path.join(p,f)
            with open(to_read, 'r') as f:
                doc = json.loads(f.read())
                for k, news in doc.items():
                    for vv in news.get('links'):
                        entities = vv.get('entities')
                        transformed_date1 = None
                        for entity in entities:
                            try:
                                transformed_date1 = dparser.parse(entities,fuzzy=True)
                                break
                            except:
                                pass
                        #print(transformed_date1)
                        #print(vv.get('title'))
                        #print(vv.get('text'))
                        #print('******')
                    count += 1
