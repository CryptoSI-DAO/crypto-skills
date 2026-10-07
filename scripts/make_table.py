#!/usr/bin/env python3
"""Strip snapshot data from gov.json into a compact dated table (data/ JSON)."""
import json, sys

gov = json.load(open(sys.argv[1]))
out = []
for p in gov['proposals'][:gov['past_count']]:
    d = p.get('thread_date') or ''
    y, n = p['votes']['yes'], p['votes']['no']
    out.append({
        'date': d[:10] if d else None,
        'name': p['name'],
        'amount_piv': p['amount_piv'],
        'yes': y, 'no': n,
        'result': p['status'],
        'url': p['forum_url'],
    })
out.sort(key=lambda r: r['date'] or '9999')
json.dump(out, open(sys.argv[2], 'w'), indent=1)
print(len(out), 'rows')
