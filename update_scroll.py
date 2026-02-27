import re

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'r') as f:
    html = f.read()

# 1. Update the total scroll height to account for 7 items instead of 6
# tabs_height is currently 600vh -> needs to be 700vh
html = html.replace('height: 600vh; /* 6 items now', 'height: 700vh; /* 7 items now')

# 2. Add a new tab text content for Cabal.town
cabal_tab = """
                        <!-- Tab 2: Cabal Town -->
                        <div class="tabs_let-content">
                            <span class="font-mono text-accent text-sm mb-2 uppercase tracking-wider">Dec 2024 — Nov 2025</span>
                            <h2 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Tech Co-founder <span class="text-textMuted block text-xl md:text-2xl mt-1">@ Cabal.town</span></h2>
                            <div class="tabs_line"></div>
                            <p class="text-textMuted text-sm md:text-base leading-relaxed mb-4">
                                Architected and launched <strong class="text-white">Cabal.town</strong>, a lean social wallet with a monetization layer that rapidly acquired 60K Telegram group users.
                            </p>
                            <p class="text-textMuted text-sm md:text-base leading-relaxed">
                                Integrated TON blockchain capabilities, Web3 onboarding flows, and optimized NoSQL databases to handle high-velocity user scaling.
                            </p>
                        </div>
"""

# Find Tab 2: HSBC and insert Cabal Town before it
html = html.replace('<!-- Tab 2: HSBC -->', cabal_tab + '\n                        <!-- Tab 3: HSBC -->')

# Update the Lumos Tab text slightly so it focuses only on Lumos
lumos_replacement = """<!-- Tab 1: Web3 Startup -->
                        <div class="tabs_let-content is-1">
                            <span class="font-mono text-accent text-sm mb-2 uppercase tracking-wider">Dec 2024 — Nov 2025</span>
                            <h2 class="text-3xl md:text-4xl font-bold text-white mb-2 leading-tight">Tech Co-founder <span class="text-textMuted block text-xl md:text-2xl mt-1">@ Lumos</span></h2>
                            <div class="tabs_line"></div>
                            <p class="text-textMuted text-sm md:text-base leading-relaxed mb-4">
                                Designed and architected <strong class="text-white">Lumos</strong>, a custodial perpetual trading bot that achieved $120M trading volume in just 2 months.
                            </p>
                            <p class="text-textMuted text-sm md:text-base leading-relaxed">
                                Led system analysis, modeling algorithmic trading strategies with PyTorch and XGBoost. Directed end-to-end implementation including Smart Contracts, FastAPI backends, and sub-100ms trade execution tuning.
                            </p>
                        </div>"""

html = re.sub(r'<!-- Tab 1: Web3 Startup -->.*?</div>\s*</div>', lumos_replacement + '\n', html, flags=re.DOTALL)

# 3. Update the Right Column images
# Remove the inset image logic and split into two separate background images
old_image_1 = """<!-- Image 1: Web3 Startup -->
                        <div class="tabs_image is-1" style="background-image: url('lumos.png');">
                            <!-- Inset Cabal Town Image -->
                            <div class="absolute top-8 right-8 w-1/3 rounded-xl overflow-hidden border border-white/10 shadow-2xl transform rotate-3 hover:rotate-0 transition-transform duration-500 z-0">
                                <img src="cabal_town.png" alt="Cabal Town" class="w-full h-auto opacity-90 hover:opacity-100 transition-opacity">
                            </div>
                            <div class="bg-overlay z-10 relative">
                                <div>
                                    <h4 class="text-2xl font-bold text-white mb-1">Web3 Ecosystems</h4>
                                    <p class="text-accent font-mono text-sm">Algorithmic Trading & Social Wallets</p>
                                </div>
                            </div>
                        </div>"""

new_images = """<!-- Image 1: Lumos -->
                        <div class="tabs_image is-1" style="background-image: url('lumos.png');">
                            <div class="bg-overlay z-10 relative">
                                <div>
                                    <h4 class="text-2xl font-bold text-white mb-1">Lumos</h4>
                                    <p class="text-accent font-mono text-sm">High-Frequency Trading Bot</p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Image 2: Cabal Town -->
                        <div class="tabs_image" style="background-image: url('cabal_town.png');">
                            <div class="bg-overlay z-10 relative">
                                <div>
                                    <h4 class="text-2xl font-bold text-white mb-1">Cabal.town</h4>
                                    <p class="text-accent font-mono text-sm">Social Web3 Wallet Ecosystem</p>
                                </div>
                            </div>
                        </div>"""

html = html.replace(old_image_1, new_images)

# Also rename the HTML comments for the rest to be +1
html = html.replace('<!-- Image 2: HSBC -->', '<!-- Image 3: HSBC -->')
html = html.replace('<!-- Image 3: Crypto.com -->', '<!-- Image 4: Crypto.com -->')
html = html.replace('<!-- Image 4: GOGOX -->', '<!-- Image 5: GOGOX -->')
html = html.replace('<!-- Image 5: NTT DATA -->', '<!-- Image 6: NTT DATA -->')
html = html.replace('<!-- Image 6: Liricco -->', '<!-- Image 7: Liricco -->')

html = html.replace('<!-- Tab 3: HSBC -->', '<!-- Tab 3: HSBC -->')
html = html.replace('<!-- Tab 3: Crypto.com -->', '<!-- Tab 4: Crypto.com -->')
html = html.replace('<!-- Tab 4: GOGOX -->', '<!-- Tab 5: GOGOX -->')
html = html.replace('<!-- Tab 5: NTT DATA -->', '<!-- Tab 6: NTT DATA -->')
html = html.replace('<!-- Tab 6: Liricco -->', '<!-- Tab 7: Liricco -->')


with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'w') as f:
    f.write(html)
