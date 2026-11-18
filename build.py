import json, glob, os, re
files=[f for f in glob.glob('data/*.json') if not f.endswith('manifest.json')]
slugs=[os.path.splitext(os.path.basename(f))[0] for f in files]
entries=[json.load(open(f)) for f in files]
json.dump({"entries":slugs,"count":len(slugs)}, open('data/manifest.json','w'), indent=2)
inline=json.dumps(entries, ensure_ascii=False)
for hf in glob.glob('*.html'):
    html=open(hf).read()
    new=re.sub(r'(const FALLBACK = /\*__ENTRIES__\*/ ).*?(;\s*\n)',
               lambda m: m.group(1)+inline+m.group(2), html, count=1, flags=re.S)
    if new!=html:
        open(hf,'w').write(new); print('re-inlined fallback into', hf)
print('manifest entries:', slugs)
