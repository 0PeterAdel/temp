#!/usr/bin/env python3
"""Validate portable Markdown and export flat GitHub Wiki pages from stable IDs.
No third-party packages. Run from any working directory.
"""
import argparse, json, re, shutil, sys
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
SRC=BASE/'wiki'
MAP=BASE/'tools'/'page-map.json'
LINK=re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)')
ID=re.compile(r'\*\*Page ID:\*\* `([^`]+)`')
def pages():
    out={}; ids=set()
    for f in sorted(SRC.rglob('*.md')):
        content=f.read_text(encoding='utf-8')
        m=ID.search(content)
        if not m:
            if f.name in {'_Sidebar.md','_Footer.md'} and f.parent==SRC: continue
            raise ValueError(f'Missing Page ID: {f.relative_to(SRC)}')
        pid=m.group(1)
        if not re.fullmatch(r'[A-Z0-9-]+',pid) or pid in ids: raise ValueError(f'Invalid/duplicate Page ID {pid}')
        ids.add(pid); out[f.resolve()]=('Home' if pid=='HOME' else pid)
    return out

def local_target(f,target):
    if target.startswith(('http://','https://','mailto:','#')): return None
    part,sep,anchor=target.partition('#')
    return (f.parent/part).resolve(), ('#'+anchor if sep else '')

def validate():
    mapping=pages(); errors=[]; count=0
    for f in sorted(SRC.rglob('*.md')):
        for m in LINK.finditer(f.read_text(encoding='utf-8')):
            dest=local_target(f,m.group(2))
            if dest is None: continue
            count+=1
            if dest[0] not in mapping and not dest[0].is_file(): errors.append(f'{f.relative_to(SRC)} -> {m.group(2)}')
    print(f'{len(mapping)} pages, {count} local links checked, {len(errors)} broken links.')
    if errors: raise ValueError('\n'.join(errors))
    return mapping

def export(out):
    mapping=validate(); out=out.resolve()
    if out==SRC.resolve() or SRC.resolve() in out.parents: raise ValueError('Export outside wiki source.')
    if out.exists() and any(out.iterdir()): raise ValueError(f'Export destination is not empty: {out}. Use a new folder.')
    out.mkdir(parents=True,exist_ok=True)
    for f in sorted(SRC.rglob('*.md')):
        def repl(m):
            dest=local_target(f,m.group(2))
            if dest is None: return m.group(0)
            if dest[0] in mapping: return f'[{m.group(1)}]({mapping[dest[0]]}{dest[1]})'
            return m.group(0)
        name=mapping.get(f.resolve(),f.stem)+'.md'
        (out/name).write_text(LINK.sub(repl,f.read_text(encoding='utf-8')),encoding='utf-8')
    # check flat Wiki links using page slugs
    targets={p.stem for p in out.glob('*.md')}; errors=[]
    for f in out.glob('*.md'):
        for m in LINK.finditer(f.read_text(encoding='utf-8')):
            target=m.group(2).split('#',1)[0]
            if not target or target.startswith(('https://','http://','mailto:')): continue
            if target not in targets: errors.append(f'{f.name}: {target}')
    if errors: raise ValueError('Flat export broken links:\n'+'\n'.join(errors))
    print(f'Exported {len(list(out.glob("*.md")))} Markdown files to {out}; all page links resolve.')

def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True)
    sp.add_parser('validate'); ex=sp.add_parser('export');ex.add_argument('output',type=Path)
    args=p.parse_args()
    if args.cmd=='validate':validate()
    else:export(args.output)
if __name__=='__main__':main()
