import urllib
from urlparse import urlparse

topHostPostfix = (
    '.com','.la','.io',
    '.co',
    '.info',
    '.net',
    '.org',
    '.me',
    '.mobi',
    '.us',
    '.biz',
    '.xxx',
    '.ca',
    '.co.jp',
    '.com.cn',
    '.net.cn',
    '.org.cn',
    '.mx',
    '.tv',
    '.ws',
    '.ag',
    '.com.ag',
    '.net.ag',
    '.org.ag',
    '.am',
    '.asia',
    '.at',
    '.be',
    '.com.br',
    '.net.br',
    '.bz',
    '.com.bz',
    '.net.bz',
    '.cc',
    '.com.co',
    '.net.co',
    '.nom.co',
    '.de',
    '.es',
    '.com.es',
    '.nom.es',
    '.org.es',
    '.eu',
    '.fm',
    '.fr',
    '.gs',
    '.in',
    '.co.in',
    '.firm.in',
    '.gen.in',
    '.ind.in',
    '.net.in',
    '.org.in',
    '.it',
    '.jobs',
    '.jp',
    '.ms',
    '.com.mx',
    '.nl',
    '.nu',
    '.co.nz',
    '.net.nz',
    '.org.nz',
    '.se',
    '.tc',
    '.tk',
    '.tw',
    '.com.tw',
    '.idv.tw',
    '.org.tw',
    '.hk',
    '.co.uk',
    '.me.uk',
    '.org.uk',
    '.vg')


def get_top_host(url):
    parts = urlparse(url)
    host = parts.netloc
    extractPattern = r'[^\.]+('+'|'.join([h.replace('.',r'\.') for h in topHostPostfix])+')$'
    pattern = re.compile(extractPattern,re.IGNORECASE)
    m = pattern.search(host)
    return m.group() if m else host

get_top_host("tieba.baidu.com/p/1580276377")

