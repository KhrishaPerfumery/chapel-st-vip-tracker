import json,sys
sys.path.insert(0,'.')
import dms
out={k:{"knows":v[0],"dm":v[1]} for k,v in dms.DMS.items()}
json.dump(out,open('dms.json','w'),ensure_ascii=False,indent=1)
print(len(out))
