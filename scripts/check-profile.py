"""Organization profile checks: Python 3 + Pillow, no network or credentials."""
from pathlib import Path
import re,unittest,xml.etree.ElementTree as ET
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
class ProfileChecks(unittest.TestCase):
 def test_brand_and_primary_links(self):
  text=(ROOT/'profile/README.md').read_text()
  for value in ['Quasynvo','Quasnooze','Intelligence, in your orbit.','https://github.com/Quasynvo/Quasnooze','profile/banner.gif','profile/banner.png']:self.assertIn(value,text)
 def test_no_obsolete_active_org_urls(self):
  for p in [*ROOT.glob('*.md'),*ROOT.glob('ISSUE_TEMPLATE/*'),ROOT/'profile/README.md']:
   text=p.read_text();self.assertNotIn('github.com/pinchfoundry',text,str(p));self.assertNotIn('pinchfoundry.github.io',text,str(p))
 def test_local_markdown_and_profile_asset_targets(self):
  for p in [*ROOT.glob('*.md'),ROOT/'profile/README.md']:
   for target in re.findall(r'\]\(([^)\s]+)\)',p.read_text()):
    if target.startswith(('http:','https:','#','mailto:')):continue
    self.assertTrue((p.parent/target.split('#')[0]).exists(),f'{p}: {target}')
  for name in ['banner.gif','banner.png','quasynvo-logo.png']:self.assertTrue((ROOT/'profile'/name).is_file())
 def test_banner_is_small_decorative_animation(self):
  p=ROOT/'profile/banner.gif'
  with Image.open(p) as im:self.assertEqual(im.size,(1200,360));self.assertEqual(im.n_frames,24)
  self.assertLess(p.stat().st_size,200000)
 def test_static_fallback_and_svg_parse(self):
  with Image.open(ROOT/'profile/banner.png') as im:self.assertEqual(im.size,(1200,360))
  svg=ET.parse(ROOT/'profile/banner.svg').getroot();self.assertIn('Quasynvo',svg.attrib['aria-label'])
 def test_product_boundaries_remain_explicit(self):
  text=(ROOT/'profile/README.md').read_text()
  for phrase in ['previews','OS-sandboxed','2.5D','Physical wake-word','sensitive actions','Optional cloud providers']:self.assertIn(phrase,text)
 def test_profile_is_static_first_and_preview_is_labelled(self):
  text=(ROOT/'profile/README.md').read_text()
  first_image=re.search(r'<img\s+src="([^"]+)"\s+alt="([^"]+)"',text)
  self.assertIsNotNone(first_image)
  self.assertTrue(first_image.group(1).endswith('/profile/banner.png'))
  self.assertTrue(first_image.group(2))
  self.assertIn('scripted UI preview',text)
  self.assertNotIn('<script',text.lower())
  self.assertTrue((ROOT/'profile/orbit-background.jpg').is_file())
if __name__=='__main__':unittest.main(verbosity=2)
