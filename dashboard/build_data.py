import sys, json, pandas as pd
from collections import Counter
src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(src, keep_default_na=False)
def split(s): return [x.strip() for x in s.split(',') if x.strip() and x.strip()!='Unknown'] if s else []
dicts = {k:{} for k in ['country','genre','rating','cast','director','audience']}
castc = Counter(a for s in df['cast'] for a in split(s))
def idx(d,v):
    if v not in dicts[d]: dicts[d][v]=len(dicts[d])
    return dicts[d][v]
rows=[]
for r in df.itertuples():
    ya = int(r.year_added) if str(r.year_added).strip() not in ('','Unknown') else 0
    ma = int(r.month_added) if str(r.month_added).strip() not in ('','Unknown') else 0
    wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'].index(r.weekday_added) if r.weekday_added in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] else -1
    dur = float(r.duration_num) if str(r.duration_num) not in ('','nan') else 0
    rows.append([
        0 if r.type=='Movie' else 1, r.title,
        [idx('director',d) for d in split(r.director)],
        [idx('country',c) for c in split(r.country)],
        ya, ma, wd, int(r.release_year), idx('rating',r.rating or 'Unknown'), int(dur),
        [idx('genre',g) for g in split(r.listed_in)],
        [idx('cast',a) for a in split(r.cast) if castc[a]>=4],
        idx('audience', r.audience or 'Unknown'),
    ])
data={'cols':['t','title','dir','c','ya','ma','wd','ry','rat','dur','g','cast','aud'],
      'dict':{k:list(v.keys()) for k,v in dicts.items()},'rows':rows}
json.dump(data, open(out,'w'), separators=(',',':'), ensure_ascii=False)
print(len(rows), {k:len(v) for k,v in dicts.items()})
print(df['audience'].value_counts().to_dict())
