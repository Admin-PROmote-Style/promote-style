# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_home, build_seo101, build_contact, build_pricing
import build_seo_files
import site_common as S

if __name__ == "__main__":
    S.copy_assets()   # real files in site/assets/ -- needed for og:image to resolve
    build_home.build()
    build_seo101.build()
    build_contact.build()
    build_pricing.build()
    build_seo_files.build()   # robots.txt + sitemap.xml
    print(chr(10) + "All pages built.")
