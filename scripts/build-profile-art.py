"""Optional developer asset builder: Python 3, Pillow, Linux DejaVu fonts."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import math,base64
root=Path(__file__).resolve().parents[1];out=root/'profile'
logo=Image.open(out/'quasynvo-logo.png').convert('RGB').resize((300,300))
font=lambda size,bold=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if bold else '')+'.ttf',size)
base=Image.new('RGB',(1200,360),'#090d1b');d=ImageDraw.Draw(base)
for x,y in [(32,40),(400,25),(702,300),(765,70),(1138,303),(620,85),(1080,32),(711,199)]:d.ellipse((x,y,x+1,y+1),fill='#56788f')
mask=Image.new('L',(300,300),0);ImageDraw.Draw(mask).ellipse((10,10,290,290),fill=255);mask=mask.filter(ImageFilter.GaussianBlur(20));base.paste(logo,(805,30),mask);d=ImageDraw.Draw(base)
d.text((52,48),'LOCAL-FIRST THINKING. HUMAN-FIRST TOOLS.',font=font(11,True),fill='#9ee9e5')
d.text((47,100),'Quasynvo',font=font(69,True),fill='#f2f7ff');d.text((53,198),'Intelligence, in your orbit.',font=font(25),fill='#a8f5eb')
d.text((53,251),'AI software you can run, understand and shape.',font=font(15),fill='#a7b5cd')
for x,text in [(53,'LOCAL-FIRST'),(213,'OPEN SOURCE'),(383,'VISIBLE BOUNDARIES')]:
 d.ellipse((x,310,x+4,314),fill='#83f5ed');d.text((x+13,303),text,font=font(10,True),fill='#c0cddd')
frames=[]
for i in range(24):
 im=base.copy();draw=ImageDraw.Draw(im)
 for rad,offset in [(151,0),(164,math.pi)]:
  draw.ellipse((955-rad,180-rad,955+rad,180+rad),outline='#83f5ed24',width=1)
  a=i/24*math.tau+offset;x=955+rad*math.cos(a);y=180+rad*math.sin(a)
  draw.ellipse((x-3,y-3,x+3,y+3),fill='#b4fff4')
 frames.append(im)
frames[0].save(out/'banner.png',optimize=True)
palette=frames[0].quantize(colors=128);animation=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
animation[0].save(out/'banner.gif',save_all=True,append_images=animation[1:],duration=100,loop=0,optimize=True,disposal=1)
data=base64.b64encode((out/'banner.png').read_bytes()).decode();(out/'banner.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" role="img" aria-label="Quasynvo — Intelligence, in your orbit."><image width="1200" height="360" href="data:image/png;base64,{data}"/></svg>')
print('Banner GIF:',(out/'banner.gif').stat().st_size,'bytes')
