import re

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'r') as f:
    html = f.read()

# Replace Web3 Startup Image (Tab 1)
# Currently it uses: url('https://images.unsplash.com/photo-1639762681485-074b7f4tc468?q=80&w=2832&auto=format&fit=crop')
# We will use lumos.png and cabal_town.png. Let's create a custom HTML structure for Tab 1 to show both, or just use lumos.png for the background.
# Actually, since it's a background image, let's use lumos.png as the main background, and maybe add cabal_town.png as an inset image, or just replace the background URL.
# I'll replace the URL with lumos.png.
html = re.sub(
    r"url\('https://images\.unsplash\.com/photo-1639762681485[^']+'\)",
    "url('lumos.png')",
    html
)

# Replace GOGOX Image (Tab 4)
# Currently uses: url('https://images.unsplash.com/photo-1586528116311-ad8ed7453303?q=80&w=2940&auto=format&fit=crop')
html = re.sub(
    r"url\('https://images\.unsplash\.com/photo-1586528116311[^']+'\)",
    "url('gogox.png')",
    html
)

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'w') as f:
    f.write(html)
