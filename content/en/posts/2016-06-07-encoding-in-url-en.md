---
title: "Solution for Incorrect Parameter Encoding in URLs"
date: "2016-06-07 21:29:39"
zhUrl: /encoding-in-url
aliases:
  - /encoding-in-url-en
---

I say "solution", but actually I didn't really solve the problem :wink:

<!--more-->

## Incorrect Parameter Encoding in URLs

I've been working on a Python-Scrapy crawler recently, and wrote a server program with Tornado.
But the problem I ran into is

**Tornado can't parse Chinese in URLs**

For example, here's a sample mini program:

``` python
from tornado.ioloop import IOLoop
import tornado.web as tw

class SampleHandler(tw.RequestHandler):
    def get(self, path):
        self.write(path)

app = tw.Application([(ur'/(.*)', SampleHandler)])
app.listen(8080)
IOLoop.current().start()
```

But visiting `https://localhost:8080/浮云计算` only gives back a pile of garbage like `æµ®äº�è®¡ç®�`...

## Solution

Long story short, this is caused by `Chinese URL decoding being incorrect`.
So we use [Stationmaster Tools url encoding][urlencode] to manually replace the Chinese for access:

Visiting `https://localhost:8080/%e6%b5%ae%e4%ba%91%e8%ae%a1%e7%ae%97` will give back `浮云计算`.

## Detailed Reason

At first I suspected the string wasn't using utf8 encoding,
so I tried different conversion methods:

```
self.write(str(path))
self.write(unicode(path))
self.write(path.encode('utf8'))
```

These either threw errors or made no difference.

Eventually I found [a predecessor's experience][outofmemory], which says:

> It seems you don't know that manually entering Chinese in the browser address bar and clicking a link on a page are handled differently in terms of encoding....
> For example, on a Windows system, you enter "https://localhost/中文.html?m=汉语" in the FF address bar. Here the encoding of "中文" is utf8 (this should be related to browser settings), while "汉语" is gbk, related to the operating system (most Chinese people's Windows should be cp936, which is gbk).
> If you visit this link through some page, then all the character encodings are related to the page's encoding.
> Same on IE.
> So I think you should give up the idea of entering Chinese in the browser address bar, otherwise you have to decode twice, and also make sure the page's encoding is the same as the system, otherwise you can't guarantee compatibility between manual entry and page clicks....


Oh, so it's because `URL decoding completely depends on the browser and operating system`, that is `Chinese might be encoded in GBK`.

No wonder Python/Tornado couldn't recognize it!

So the solution is we manually decode once ourselves~

(Or use Python3 XD)

[urlencode]: https://tool.chinaz.com/tools/urlencode.aspx
[outofmemory]: https://ju.outofmemory.cn/entry/62161
