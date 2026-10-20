"""Generate profile SVG assets from shared design tokens; Python standard library only."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
TOKENS = json.loads((HERE / 'tokens.json').read_text(encoding='utf-8'))

def resolve(match):
    value = TOKENS
    for part in match.group(1).split('.'):
        value = value[part]
    return str(value)

def luminance(hex_color):
    channels = [int(hex_color[i:i+2],16)/255 for i in (1,3,5)]
    channels = [c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in channels]
    return sum(c*w for c,w in zip(channels,(.2126,.7152,.0722)))

allowed = set(TOKENS['color'].values())
for template in sorted((HERE / 'templates').glob('*.svg')):
    svg = re.sub(r'\{\{([a-z_.]+)\}\}',resolve,template.read_text(encoding='utf-8'))
    if '{{' in svg:
        raise ValueError(f'Unresolved token in {template.name}')
    ET.fromstring(svg)
    colors = set(re.findall(r'#[0-9a-fA-F]{6}',svg))
    if not colors.issubset(allowed):
        raise ValueError(f'Non-system colors in {template.name}: {colors-allowed}')
    (HERE.parent / 'assets' / template.name).write_text(svg.rstrip()+'\n',encoding='utf-8',newline='\n')
    print(f'Built {template.name}')

for key in ('primary','accent','ink','muted'):
    ratio = (luminance(TOKENS['color']['surface'])+.05)/(luminance(TOKENS['color'][key])+.05)
    if ratio < 4.5:
        raise ValueError(f'{key} fails normal-text contrast on white: {ratio:.2f}')
    print(f'{key} / white contrast: {ratio:.2f}:1')

for key in ('primary','accent'):
    ratio = (luminance(TOKENS['color'][key+'_soft'])+.05)/(luminance(TOKENS['color'][key])+.05)
    if ratio < 4.5:
        raise ValueError(f'{key} fails normal-text contrast on its tint: {ratio:.2f}')
    print(f'{key} / tint contrast: {ratio:.2f}:1')
