import codecs

import aiohttp
from yarl import URL

from mixed_decoder import mixed_decoder

codecs.register_error("mixed", mixed_decoder)

resp: aiohttp.ClientResponse

session = aiohttp.ClientSession(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/82.0.4077.0 "
                      "Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;"
                  "q=0.9,image/webp,image/apng,*/*;"
                  "q=0.8,application/signed-exchange;v=b3;"
                  "q=0.9",
    }
)

session.cookie_jar.update_cookies(
    dict(_ga="GA1.3.2135817731.1583954916", _gid="GA1.3.1662457840.1583954916"),
    URL("http://www4.tjrj.jus.br/")
)

markup = b"<h1>Test</h1>"
f = open("scratch.html", "wb")
f.write(markup)
f.close()
