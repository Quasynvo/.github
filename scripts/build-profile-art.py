"""Build the profile hero from the approved mark and a checked-in generated backdrop.

Requires Python 3, Pillow and DejaVu Sans fonts. No network or external services.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import base64
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'profile'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans'

def font(size, bold=False):
    return ImageFont.truetype(FONT + ('-Bold' if bold else '') + '.ttf', size)

# The backdrop is AI-generated; the identity mark is the previously approved asset.
base = Image.open(OUT / 'orbit-background.jpg').convert('RGB').resize((1200, 360))
draw = ImageDraw.Draw(base, 'RGBA')
# Keep typography legible over the artwork without obscuring the orbit.
draw.rectangle((0, 0, 610, 360), fill=(4, 10, 24, 75))
draw.rounded_rectangle((52, 38, 237, 64), radius=13, fill=(20, 51, 61, 190), outline=(116, 235, 218, 120))
draw.ellipse((66, 49, 71, 54), fill=(131, 245, 237, 255))
draw.text((80, 44), 'OPEN SOURCE  /  LOCAL FIRST', font=font(9, True), fill=(177, 249, 238, 255))
draw.text((47, 91), 'Quasynvo', font=font(66, True), fill=(245, 250, 255, 255))
draw.text((52, 180), 'Intelligence, in your orbit.', font=font(25), fill=(166, 249, 236, 255))
draw.text((53, 239), 'Thoughtful AI. Built to stay in your hands.', font=font(15), fill=(187, 201, 219, 255))
draw.line((53, 288, 530, 288), fill=(114, 210, 207, 85), width=1)
draw.text((53, 304), 'PERSONAL  /  PRIVATE BY DESIGN  /  HUMAN IN CONTROL', font=font(9, True), fill=(182, 210, 220, 255))

# Extract the approved orbital Q without the dark square behind it.
source = Image.open(OUT / 'quasynvo-logo.png').convert('RGB')
mask = Image.new('L', source.size)
mask.putdata([min(255, max(0, int((min(r, g, b) - 28) * 1.5))) for r, g, b in source.getdata()])
logo = Image.new('RGBA', source.size, (187, 255, 246, 255))
logo.putalpha(mask)
logo = logo.resize((214, 214), Image.Resampling.LANCZOS)
glow = Image.new('RGBA', base.size, (0, 0, 0, 0))
glow.paste((93, 246, 225, 110), (898, 73, 1112, 287), logo.getchannel('A'))
glow = glow.filter(ImageFilter.GaussianBlur(18))
base = Image.alpha_composite(base.convert('RGBA'), glow)
base.alpha_composite(logo, (898, 73))
base = base.convert('RGB')

# Static-first hero; the optional GIF moves two decorative points only.
base.save(OUT / 'banner.png', optimize=True)
frames = []
for i in range(24):
    frame = base.copy()
    d = ImageDraw.Draw(frame)
    for radius, phase in [(135, 0), (148, math.pi)]:
        angle = i / 24 * math.tau + phase
        x, y = 1005 + radius * math.cos(angle), 180 + radius * math.sin(angle)
        d.ellipse((x-2, y-2, x+2, y+2), fill='#c6fff7')
    frames.append(frame)
palette = frames[0].quantize(colors=128)
animation = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
animation[0].save(OUT / 'banner.gif', save_all=True, append_images=animation[1:], duration=100, loop=0, optimize=True, disposal=1)
data = base64.b64encode((OUT / 'banner.png').read_bytes()).decode()
(OUT / 'banner.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" role="img" aria-label="Quasynvo — Intelligence, in your orbit."><image width="1200" height="360" href="data:image/png;base64,{data}"/></svg>')
print('Banner PNG:', (OUT / 'banner.png').stat().st_size, 'bytes')
print('Banner GIF:', (OUT / 'banner.gif').stat().st_size, 'bytes')
