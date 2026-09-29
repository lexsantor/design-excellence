"""Static check of the two EXPLORE reference pools (visual-references.md, principle-pool.md).

- schema: every entry carries its file's required fields; Principle Pool status is accepted|stale
- ceilings: visual references <= 10; Principle Pool <= 15 and first curation pass <= 8
- freshness: last_verified_date + review_interval_days not passed (an expired entry is reported, not silently kept)
- identity leak: no URL, hex colour, pixel measurement, image file, or any product/host name derived from the
  local source inventories (themes-links.md, figma-links.md) appears in either runtime file; source-identifying
  patterns and screening vocabulary come from the untracked tools/reference-screen.local.json
usage: python tools/check-references.py [YYYY-MM-DD]   exit 1 on any failure."""
import datetime, json, os, re, sys
from urllib.parse import unquote, urlparse

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(REPO, 'design-excellence', 'references')
today = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date.today()
fail = []

VR_FIELDS = ['dimension', 'observed', 'abstracted_principle', 'compatible_with', 'do_not_apply_to',
             'non_application_note', 'freshness']
PP_FIELDS = ['id', 'status', 'dimension', 'organizing_surface', 'observed', 'abstracted_principle',
             'compatible_with.registers', 'compatible_with.genres', 'do_not_apply_to', 'non_application_note',
             'evidence_basis', 'support_breadth.kind', 'support_breadth.cluster_count', 'family',
             'freshness.last_verified_date', 'freshness.review_interval_days']


def entries(text, head):
    parts = re.split(rf'^### ({head}\S*)', text, flags=re.M)
    return list(zip(parts[1::2], parts[2::2]))


def fresh(eid, body):
    d = re.search(r'last_verified_date:\**\s*(\d{4}-\d{2}-\d{2})', body)
    n = re.search(r'review_interval_days:\**\s*(\d+)', body)
    if not (d and n):
        fail.append(f'{eid}: freshness unparseable')
    elif datetime.date.fromisoformat(d.group(1)) + datetime.timedelta(int(n.group(1))) < today:
        fail.append(f'{eid}: expired')


vr_text = open(os.path.join(REFS, 'visual-references.md'), encoding='utf-8').read()
vr = entries(vr_text, 'REF-')
if len(vr) > 10:
    fail.append(f'visual-references: {len(vr)} entries > ceiling 10')
for eid, body in vr:
    fail += [f'{eid}: missing {f}' for f in VR_FIELDS if f'**{f}:**' not in body]
    fresh(eid, body)

pp_text = open(os.path.join(REFS, 'principle-pool.md'), encoding='utf-8').read()
pp = entries(pp_text, 'PRN-')
if len(pp) > 8:
    fail.append(f'principle-pool: {len(pp)} entries > first-pass stop 8 (ceiling 15)')
for eid, body in pp:
    fail += [f'{eid}: missing {f}' for f in PP_FIELDS if f'**{f}:**' not in body]
    st = re.search(r'\*\*status:\*\*\s*(\w+)', body)
    if not st or st.group(1) not in ('accepted', 'stale'):
        fail.append(f'{eid}: status must be accepted|stale')
    fresh(eid, body)

# identity-leak scan: generic patterns + names derived from the inventories
names = set()
for inv in ('themes-links.md', 'figma-links.md'):
    p = os.path.join(REPO, inv)
    if not os.path.exists(p):
        continue
    for u in re.findall(r'https?://\S+?(?=https?://|\s|$)', open(p, encoding='utf-8').read()):
        pu = urlparse(u)
        host = pu.netloc.split('.')[0]
        segs = [host] + (unquote(pu.path.split('/')[3]).split('-') if '/design/' in pu.path else [])
        for w in re.split(r'[^A-Za-z]+', ' '.join(segs)):
            if len(w) >= 5:
                names.add(w.lower())
# Screening vocabulary derived from the inventories stays local and untracked (tools/reference-screen.local.json):
# stop = inventory words too generic to screen, common = ordinary words that are also a product name (warned,
# not failed), extra_leak = source-identifying patterns. Without inventories the name screen is skipped;
# with inventories but no vocabulary it fails rather than screening unfiltered.
warn = []
vocab_path = os.path.join(REPO, 'tools', 'reference-screen.local.json')
vocab = json.load(open(vocab_path, encoding='utf-8')) if os.path.exists(vocab_path) else {}
if not names:
    warn.append('inventory name screen skipped: no local inventories')
elif not vocab:
    fail.append('inventories present but tools/reference-screen.local.json missing: cannot screen names')
names -= set(vocab.get('stop', []))
COMMON = set(vocab.get('common', []))
LEAK = [r'https?://', r'#[0-9a-fA-F]{3,8}\b', r'\b\d+px\b', r'\.(png|jpe?g|webp|svg)\b'] + vocab.get('extra_leak', [])
for fname, text in (('visual-references.md', vr_text), ('principle-pool.md', pp_text)):
    for pat in LEAK:
        for m in re.finditer(pat, text, re.I):
            fail.append(f'{fname}: leak pattern {pat!r}: {m.group(0)}')
    words = set(re.findall(r'[a-z]{5,}', text.lower()))
    fail += [f'{fname}: inventory name {w!r}' for w in sorted((names - COMMON) & words)]
    warn += [f'{fname}: common word that is also an inventory name, review context: {w!r}' for w in sorted(names & COMMON & words)]

print(f'visual-references {len(vr)}/10, principle-pool {len(pp)} (first pass 8, ceiling 15), '
      f'{len(names)} inventory names screened, date {today}')
if warn:
    print('\n'.join(warn))
print('\n'.join(fail) if fail else 'PASS')
sys.exit(1 if fail else 0)
