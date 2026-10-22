"""Build compact, theme-aware profile cards and self-contained technology badges."""
from pathlib import Path
import html
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets/compact'
OUT.mkdir(parents=True, exist_ok=True)
FONT = 'Arial, Helvetica, sans-serif'
TECH = [
    ('react', 'React', '#176479'), ('nextdotjs', 'Next.js', '#24292F'),
    ('typescript', 'TypeScript', '#2765A5'), ('javascript', 'JavaScript', '#806600'),
    ('tailwindcss', 'Tailwind CSS', '#08677D'), ('nodedotjs', 'Node.js', '#35652C'),
    ('nestjs', 'NestJS', '#B51A42'), ('postgresql', 'PostgreSQL', '#345F82'),
    ('prisma', 'Prisma', '#334155'), ('supabase', 'Supabase', '#146447'),
    ('docker', 'Docker', '#1762A5'), ('githubactions', 'GitHub Actions', '#225AA1'),
]

def svg(name, width, height, label, body):
    data = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{html.escape(label)}</title>{body}</svg>\n'
    ET.fromstring(data)
    (OUT / name).write_text(data, encoding='utf-8', newline='\n')

for slug, label, color in TECH:
    icon = ET.parse(OUT / 'icons' / f'{slug}.svg').getroot()
    paths = ''.join(f'<path d="{p.attrib["d"]}"/>' for p in icon.iter() if p.tag.endswith('path'))
    width = round(46 + len(label)*7.8)
    svg(f'badge-{slug}.svg', width, 32, label, f'<rect width="{width}" height="32" rx="5" fill="{color}"/><g transform="translate(9 7) scale(.75)" fill="#FFFFFF">{paths}</g><text x="35" y="21" font-family="{FONT}" font-size="14" font-weight="700" fill="#FFFFFF">{html.escape(label)}</text>')

PROJECTS = [
    ('worklink', 'WorkLink', '#D99046',
     ['Job matching, applications,', 'and interview scheduling.'],
     ['Past-slot validation across', 'the interface and API.'],
     ['React', 'NestJS', 'PostgreSQL'], 'TEAM PROJECT / MY CONTRIBUTIONS',
     '<rect x="25" y="32" width="24" height="19" rx="3"/><path d="M32 32v-5h10v5M25 40h24M35 40v4h4v-4"/>'),
    ('pageforce', 'Pageforce', '#79A9F5',
     ['A visual website builder', 'powered by typed JSON blocks.'],
     ['One renderer for the editor', 'and published pages.'],
     ['Next.js', 'Prisma', 'Supabase'], 'SCHEMA / EDITOR / PUBLIC PAGES',
     '<rect x="25" y="27" width="25" height="24" rx="3"/><path d="M25 34h25M33 34v17"/>'),
    ('san-ngon', 'Sân Ngon', '#BC9BEA',
     ['Find a sports venue, choose', 'a time, and reserve a court.'],
     ['Database reservation rules', 'and payment confirmation.'],
     ['Next.js', 'PostgreSQL', 'SePay'], 'BOOKING / DATABASE / PAYMENTS',
     '<rect x="25" y="29" width="25" height="23" rx="3"/><path d="M31 25v8M44 25v8M25 37h25M32 44l4 4 8-8"/>'),
]
for theme, bg, border, ink, muted, tag in [
    ('dark', '#0D1117', '#30363D', '#E6EDF3', '#A6AFBA', '#212B3B'),
    ('light', '#FFFFFF', '#D0D7DE', '#1F2328', '#59636E', '#EEF2F7'),
]:
    for slug, title, accent, desc, focus, badges, footer, icon in PROJECTS:
        body = f'<rect x="1" y="1" width="358" height="250" rx="12" fill="{bg}" stroke="{border}"/><g fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon}</g><g font-family="{FONT}"><text x="62" y="47" font-size="23" font-weight="700" fill="{ink}">{html.escape(title)}</text><path d="M319 47l13-13m-11 0h11v11" fill="none" stroke="{muted}" stroke-width="1.8"/>'
        for i, line in enumerate(desc):
            body += f'<text x="25" y="{85+i*23}" font-size="17" fill="{ink}">{html.escape(line)}</text>'
        for i, line in enumerate(focus):
            body += f'<text x="25" y="{140+i*22}" font-size="16" fill="{muted}">{html.escape(line)}</text>'
        x=25
        for label in badges:
            w=round(20+len(label)*7.3)
            body += f'<rect x="{x}" y="182" width="{w}" height="27" rx="5" fill="{tag}"/><text x="{x+w/2}" y="200" text-anchor="middle" font-size="13" font-weight="700" fill="{ink}">{label}</text>'
            x += w+6
        body += f'<path d="M25 223h310" stroke="{border}"/><text x="25" y="241" font-size="10" font-weight="700" letter-spacing="1.1" fill="{muted}">{footer}</text></g>'
        svg(f'{slug}-{theme}.svg',360,252,f'{title}. '+ ' '.join(desc+focus),body)
print('Built 12 badges and 6 project cards.')
