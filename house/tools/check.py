"""Offline publication checks. Does not inspect or execute a House runtime."""
from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT=Path(__file__).resolve().parents[1]


def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
        and '__pycache__' not in p.parts and p.suffix!='.pyc'
        and p.name!='MANIFEST.json')


def write_manifest():
    rows=[{'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'bytes':p.stat().st_size} for p in files()]
    (ROOT/'MANIFEST.json').write_text(json.dumps({'schema':'house-book-publication-v1','files':rows},
        ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    manuscript=json.loads((ROOT/'book/manuscript.json').read_text(encoding='utf-8'))
    evidence=json.loads((ROOT/'book/evidence.json').read_text(encoding='utf-8'))
    ids={x['id'] for x in evidence['entries']}
    assert len(manuscript['chapters'])==24
    assert len(ids)==16
    assert all(ref in ids for c in manuscript['chapters'] for ref in c['refs'])
    local_links=0
    for p in files():
        if p.suffix in ('.md','.json','.svg','.txt'):
            text=p.read_text(encoding='utf-8')
            # Publication boundary: these are private paths/identifiers, not a ban on
            # explaining sessions, resources or authority in architectural language.
            for pattern in (r'/home/',r'/tmp/',r'\b127\.0\.0\.1\b',r'\b192\.168\.\d+\.\d+\b',
                r'\$\s*\d+',r'\b(?:USDT|USD|EUR)\b'):
                assert not re.search(pattern,text,re.I),(p.name,pattern)
        if p.suffix=='.md':
            for url in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
                u=urlparse(url)
                if u.scheme:
                    assert u.scheme=='https',(p.name,url)
                    continue
                dest=(p.parent/unquote(u.path)).resolve() if u.path else p
                assert dest.is_file(),(p.name,url)
                if u.fragment and dest.name=='EVIDENCE.md':
                    assert u.fragment.upper() in ids,(p.name,url)
                local_links+=1
        if p.suffix=='.svg':
            node=ET.fromstring(p.read_text(encoding='utf-8'))
            assert node.tag.endswith('svg')
            assert not any(n.tag.rsplit('}',1)[-1] in ('script','image','foreignObject') for n in node.iter())
    manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
    assert {x['path'] for x in manifest['files']}=={p.relative_to(ROOT).as_posix() for p in files()}
    for record in manifest['files']:
        p=ROOT/record['path']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256'],record['path']
    for lang in ('en','uk'):
        pdf=ROOT/'pdf'/f'the-house-{lang}.pdf'
        assert pdf.read_bytes().startswith(b'%PDF-') and pdf.stat().st_size>30000
        assert len(list((ROOT/'book'/lang).glob('[0-9][0-9]-*.md')))==24
    print(json.dumps({'result':'PUBLICATION_CHECKS_PASS','languages':['en','uk'],
        'chapters_per_language':24,'evidence_groups':16,'svg_figures':len(list((ROOT/'assets/diagrams').glob('*.svg'))),
        'local_links_checked':local_links,'manifest_files':len(manifest['files'])}))


if __name__=='__main__':main()
