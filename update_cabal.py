import re

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'r') as f:
    html = f.read()

# I want to add cabal_town.png to the Web3 Startup image container so both are visible.
# Let's find the first image div:
# <div class="tabs_image is-1" style="background-image: url('lumos.png');">
#                             <div class="bg-overlay">
replacement = """<div class="tabs_image is-1" style="background-image: url('lumos.png');">
                            <!-- Inset Cabal Town Image -->
                            <div class="absolute top-8 right-8 w-1/3 rounded-xl overflow-hidden border border-white/10 shadow-2xl transform rotate-3 hover:rotate-0 transition-transform duration-500 z-0">
                                <img src="cabal_town.png" alt="Cabal Town" class="w-full h-auto opacity-90 hover:opacity-100 transition-opacity">
                            </div>
                            <div class="bg-overlay z-10 relative">"""

html = html.replace("""<div class="tabs_image is-1" style="background-image: url('lumos.png');">
                            <div class="bg-overlay">""", replacement)

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'w') as f:
    f.write(html)
