## Lirian Su 的博客

这个人很懒，README 没啥好看的。
不过你想认识他的话，
可以看看他的自我介绍: [liriansu.com/about](https://liriansu.com/about)

## 本地开发

需要 Hugo extended，版本见 `.github/workflows/hugo.yml` 里的 `HUGO_VERSION`。

```sh
hugo server                                         # 本地预览
hugo --minify && python3 scripts/check_site.py public   # 构建并检查死链、SEO 元数据
```

每篇文章的中英文版本靠 front matter 里相同的 `translationKey` 关联，语言切换、hreflang 和 sitemap 都依赖它。

评论用 utterances，按 `document.title` 匹配 issue，改动文章标题或 `<title>` 格式会让旧评论对不上。

## 今天又学到了什么奇怪的知识？

身边有着一群聪明的朋友的后果就是：
每天奇怪的知识都能增加。
想到什么我都会记在这里：

- **生活**
  - 白俄罗斯的英文叫 Belarus, 当然也可以叫 White Russia. 所以这个译名即时意译，也是音译。[link](https://en.wikipedia.org/wiki/Belarus)
  - 上海日月光商场的英文简称是 ASE Mall, 全称是高级半导体工程商场 (Advanced Semiconductor Engineering Inc. Mall). 这个名字的由来是星云法师起的名字，因为“电和光代表快”。[link](https://zh.wikipedia.org/wiki/%E6%97%A5%E6%9C%88%E5%85%89%E5%8D%8A%E5%B0%8E%E9%AB%94)
  - Bill 这个名字其实是 William 的简称，比如 Bill Gates 全名是 William Henry Gates III. [link](https://en.wikipedia.org/wiki/Bill_Gates)
- **技术**
  - YAML 的官方推荐后缀是 `.yaml`, 而不是 `.yml`. [link](https://yaml.org/faq.html)
  - 命令行获取证书内容：`openssl s_client -showcerts -servername liriansu.example.com -connect 1.2.3.4:443 </dev/null`
  - K8S 资源限制中，`M` 指的是 1000进制，而 `Mi` 表示的是 1024进制，其中 `129M≈123Mi`. [link](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory)
- **Windows**
  - 语言设置里，可以开启全局 utf-8，以避免各种奇怪的 gbk 错误（比如 `pip install`）。[link](https://jingyan.baidu.com/article/25648fc1471e6a9191fd002e.html)
