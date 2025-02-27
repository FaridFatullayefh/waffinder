import requests
from bs4 import BeautifulSoup, Comment
import re

def a(b):
    c = b.headers
    d = set()
    for e, f in c.items():
        for g in h:
            if re.search(g, e, re.IGNORECASE) or re.search(g, f, re.IGNORECASE):
                d.add(g)
    return d

def i(j):
    k = BeautifulSoup(j, 'html.parser')
    l = set()
    m = k.find_all(string=lambda n: isinstance(n, Comment))
    for o in m:
        for p in h:
            if p.lower() in o.lower():
                l.add(p)
    return l

def q(r):
    s = set()
    for t in h:
        if t.lower() in r.text.lower():
            s.add(t)
    return s

def u(v):
    w = [v, v + '/test', v + '/admin']
    x = set()
    y = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    for z in w:
        try:
            aa = requests.get(z, headers=y, timeout=5)
            if aa.status_code in [403, 406, 429]:
                x.add('Possible WAF detected (403/406/429 Response)')
            x.update(a(aa))
            x.update(q(aa))
        except requests.exceptions.RequestException:
            pass
    return x

def ab(ac):
    ad = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        ae = requests.get(ac, headers=ad, timeout=5)
        af = a(ae)
        ag = i(ae.text)
        ah = q(ae)
        ai = u(ac)
        
        aj = af.union(ag).union(ah).union(ai)
        return aj
    except requests.exceptions.RequestException:
        return {'Error: Could not connect to the website'}

h = [
    'aesecure', 'airlock', 'aliyundun', 'astra', 'awaf', 'barracuda', 'bekchy', 'bigip', 'binarysec',
    'blockdos', 'bluedon', 'bulletproof', 'cisco', 'cloudflare', 'comodo', 'denyall', 'distil',
    'dotdefender', 'f5', 'fortiweb', 'fortinet', 'frontdoor', 'greywizard', 'hyperguard', 'incapsula', 'indusguard',
    'isaserver', 'jiasule', 'kona', 'limelight', 'litespeed', 'malcare', 'modsecurity', 'neustar', 'newdefend',
    'nsfocus', 'naxsi', 'onmessage', 'openresty', 'paloalto', 'perimeterx', 'radware', 'reblaze', 'rsfirewall',
    'safedog', 'safeline', 'secucloud', 'sectigo', 'secureentry', 'sentry', 'shadowd', 'shield', 'sitelock',
    'sonicwall', 'sophos', 'stackpath', 'sucuri', 'trustwave', 'wallarm', 'websecurify', 'webshield', 'webtotem',
    'yundun', 'yunjiasu', 'zenedge',
    'a10', 'ace', 'akamai', 'appgate', 'armorlogic', 'aruba', 'azure', 'barracudawebappfirewall', 'bitninja', 'checkpoint',
    'denypal', 'distil', 'fortiguard', 'imperva', 'kaspersky', 'modsecurity', 'netscaler', 'naxsi',
    'varnish', 'wallarm', 'wordfence', 'zscaler'
]

if __name__ == "__main__":
    ak = input("URL: ")
    al = ab(ak)
    if al:
        print("Detected WAFs:", al)
    else:
        print("No WAF detected.")