#!/usr/bin/env python3
"""Rewrite the site's status numbers from a public checkout. Rerunnable.

Usage: python3 tools/update_numbers.py <public-checkout> <YYYY-MM-DD>   (run from the site repo root)
Rewrites the profile, device, and product counts, the status table rows, and the
"Status on <date>" heading. Fails loudly if a marker is not found exactly once.
"""
import json, re, sys, subprocess
pub, day = sys.argv[1], sys.argv[2]; site = 'index.html'
profiles = len([p for p in __import__('os').listdir(f'{pub}/carriers/open') if p.endswith('.json')])
devices = json.load(open(f'{pub}/generated/devices/index.json'))
android = devices['platforms']['android']; apple = devices['platforms']['apple']
counts = android['carrier_data_coverage_counts']
meanings = {
    'inventory_only': 'Listed by a maintained inventory, nothing else known',
    'exact_source_indexed': 'An exact vendor artifact is indexed with a digest',
    'source_checked_no_artifact': 'Vendor scope checked in full, no current artifact',
    'exact_source_extracted': 'Artifact downloaded and integrity-checked',
    'exact_carrier_data_observed': 'Carrier evidence names this exact model',
    'source_not_queryable': 'Inventory lacks the identifier the vendor service needs',
    'source_terms_restrict_extraction': 'Official firmware source known, its terms block inspection',
    'source_transport_untrusted': 'Source known, transport lacks a trustworthy digest',
    'platform_out_of_scope': 'ChromeOS, emulator, or similar target',
    'carrier_data_not_applicable': 'Official source says the exact variant has no cellular radio',
    'source_discovery_in_progress': 'Scheduled vendor checks still have work left',
}
s = open(site).read()
def sub_once(pattern, repl, flags=0):
    global s
    n = len(re.findall(pattern, s, flags))
    assert n == 1, (pattern[:50], n)
    s = re.sub(pattern, repl, s, flags=flags)
sub_once(r'Status on \d{4}-\d{2}-\d{2}', f'Status on {day}')
rows = ''.join(f'            <tr><td><code>{k}</code></td><td>{v:,}</td><td>{meanings.get(k, "")}</td></tr>\n'
               for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
sub_once(r'(<table class="counts">\s*<thead>.*?</thead>\s*<tbody>\n)(.*?)(\s*</tbody>)', lambda m: m.group(1) + rows + m.group(3), re.S)
new_count_cmd = "python3 -c 'import json; print(json.load(open(\"generated/devices/index.json\"))[\"platforms\"][\"android\"][\"carrier_data_coverage_counts\"])'"
old_count_cmd = r"python3 -m json.tool generated/devices/index.json \| grep -m1 -A \d+ '\"carrier_data_coverage_counts\"'"
if re.search(old_count_cmd, s):
    sub_once(old_count_cmd, new_count_cmd)
assert s.count(new_count_cmd) == 1, ('count command', s.count(new_count_cmd))
print(f'site: profiles={profiles} android={sum(counts.values())} apple={apple.get("product_count") or ""} statuses={len(counts)} date={day}')
open(site, 'w').write(s)
