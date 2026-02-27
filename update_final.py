import re

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'r') as f:
    html = f.read()

# 1. Add Calendly Section right before footer
calendly_section = """
    <!-- Calendly Integration -->
    <section class="py-24 bg-[#050505] relative z-10 border-t border-white/5 reveal-up">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h2 class="text-4xl md:text-5xl font-bold mb-6 tracking-tight">Let's Build Together</h2>
            <p class="text-textMuted text-lg mb-12">Book a 30-minute discovery call to discuss Web3 architecture, full-stack systems, or potential collaborations.</p>
            
            <!-- Calendly inline widget begin -->
            <div class="calendly-inline-widget rounded-xl overflow-hidden shadow-2xl shadow-black/50 border border-white/10" data-url="https://calendly.com/ketherchau/30min?hide_event_type_details=1&hide_gdpr_banner=1&background_color=111111&text_color=fcfcfc&primary_color=3b82f6" style="min-width:320px;height:700px;"></div>
            <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
            <!-- Calendly inline widget end -->
        </div>
    </section>

    <!-- Footer -->"""

html = html.replace('<!-- Footer -->', calendly_section)

# 2 & 3. Update Footer (Email trigger, LinkedIn, GitHub)
old_footer = """    <footer class="bg-[#050505] py-12 border-t border-white/10 text-center relative z-10">
        <p class="font-mono text-textMuted text-sm mb-2">Designed & Built by Kether Chau</p>
        <div class="flex justify-center gap-6 mt-6 mb-4">
            <a href="mailto:Ketherchau@gmail.com" class="text-textMuted hover:text-white transition-colors text-xl"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://0x-kchau.github.io" class="text-textMuted hover:text-white transition-colors text-xl"><i class="fa-solid fa-globe"></i></a>
        </div>
        <p class="font-mono text-textMuted text-xs opacity-50">© 2026</p>
    </footer>"""

new_footer = """    <footer class="bg-[#050505] py-16 border-t border-white/10 text-center relative z-10">
        <h2 class="text-2xl font-bold mb-8 tracking-tighter">Connect with me</h2>
        <div class="flex justify-center gap-8 mb-10">
            <a href="mailto:ketherchau@gmail.com?subject=Inquiry%20from%20Portfolio" class="text-textMuted hover:text-accent transition-colors text-2xl transform hover:scale-110 duration-200" title="Email Me">
                <i class="fa-solid fa-envelope"></i>
            </a>
            <a href="https://www.linkedin.com/in/kether-chau-1777a31a4/" target="_blank" rel="noopener noreferrer" class="text-textMuted hover:text-accent transition-colors text-2xl transform hover:scale-110 duration-200" title="LinkedIn">
                <i class="fa-brands fa-linkedin"></i>
            </a>
            <a href="https://github.com/ketherchau" target="_blank" rel="noopener noreferrer" class="text-textMuted hover:text-accent transition-colors text-2xl transform hover:scale-110 duration-200" title="GitHub">
                <i class="fa-brands fa-github"></i>
            </a>
            <a href="https://0x-kchau.github.io" target="_blank" rel="noopener noreferrer" class="text-textMuted hover:text-accent transition-colors text-2xl transform hover:scale-110 duration-200" title="Website">
                <i class="fa-solid fa-globe"></i>
            </a>
        </div>
        <p class="font-mono text-textMuted text-sm">Designed & Built by Kether Chau</p>
        <p class="font-mono text-textMuted text-xs mt-3 opacity-50">© 2026. All rights reserved.</p>
    </footer>"""

html = html.replace(old_footer, new_footer)

with open('/Users/0xplayerone/Dev/resume/portfolio/index.html', 'w') as f:
    f.write(html)
