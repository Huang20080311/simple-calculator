# -*- coding:utf-8 -*-
"""
追星歌单
========
先读入爱豆名、身高（厘米）和入坑天数。身高转成小数再除以 100，得到米。天数转成整数再乘 10，得到应援能量。
然后读入今晚三首歌，放进列表。再读入安可曲名。三首歌原来的期待是 [3, 5, 8]，换上安可后把第 2 个数改成 9。
先打出安可的第一个字，交给 ask_spark 猜。猜完再公布全名，并把第 2 首换成这首安可。

文件开头有两行：API_KEY 和 API_SECRET。
这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
到讯飞开放平台开通「星火认知大模型」后，把 APIKey 贴进第一行引号，把 APISecret 贴进第二行引号。
引号里还是空的，前面的打印仍会出来，可以没有「星火：」那一行。

运行后应看到（样例：一只橙子、168.5、30，春日、夜曲、晴天，安可曲海阔天空）：

    爱豆：一只橙子
    身高（米）：1.685
    应援能量：300 点
    原定歌单： ['春日', '夜曲', '晴天']
    期待： [3, 9, 8]
    安可竞猜：第一个字是 海
    星火：我猜是海阔天空。
    公布安可： 海阔天空
    今晚歌单： ['春日', '海阔天空', '晴天']

「星火：」后面那句话每次用词可能不同，有字就对。

要求：
1. 用 input 读入爱豆名、身高、入坑天数。身高写成小数，再除以 100。样例 168.5 应打出 1.685。天数写成整数，应援能量 = 天数 × 10，样例应打出 300。
2. 再用 input 分别读入三首歌名，放进一个列表，先打印原定歌单。
3. 再读入安可曲名。另写一行 expect = [3, 5, 8]。换安可后中间那首期待更高，写成 expect[1] = 9。打印后应看到 [3, 9, 8]。
4. 先打印「安可竞猜：第一个字是」和安可曲名的第一个字，写成 安可曲名[0]。这一行只打第一个字。
5. 调用 ask_spark，把第一个字交给它，让它猜安可是哪一首。ask_spark 已经写在文件开头，那一段不用改。
6. 再打印「公布安可：」和全名。最后写成 songs[1] = 安可曲名，打印今晚歌单。下标从 0 起，第 2 首是 [1]。
7. 在 PyCharm 里运行。
"""
import json
import urllib.request

# 这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
# 把 APIKey 贴进 API_KEY 的引号，把 APISecret 贴进 API_SECRET 的引号。
# 这两项不要发给别人。引号里还是空的，前面的打印仍会出来。
API_KEY = ""
API_SECRET = ""


def ask_spark(question):
    """向星火提一句。两项还是空的就跳过。回了字会自己打印「星火：」。"""
    if not (API_KEY and API_SECRET):
        print("还没有填写 API_KEY 和 API_SECRET，前面的内容已经打完。")
        return
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    body = json.dumps({
        "model": "lite",
        "messages": [{"role": "user", "content": question}],
        "max_tokens": 60,
        "temperature": 0.5,
        "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": "Bearer " + API_KEY + ":" + API_SECRET,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        choices = result.get("choices") or []
        if not choices:
            print("星火没有返回正文。")
            return
        text = ((choices[0].get("message") or {}).get("content") or "").strip()
        if text:
            print("星火：", text)
        else:
            print("星火没有返回正文。")
    except Exception as exc:
        print("请求没有发出：", exc)


# TODO ① 爱豆名、身高（小数）、天数（整数）；打印米和应援能量
idol = input("爱豆名:")
height = float(input("身高(cm):"))
days = int(input("入坑天数："))
encore = input("安可歌名")



meters = height /100
energy = days *10


print(idol)
print("身高(m):" + str(meters))
print("应援能量", str(energy), "点")
print("安可竞猜 第一个字是", encore[0])
# TODO ② 三首歌名读进来，放进列表，打印原定歌单


# TODO ③ 读入安可曲名；期待 [3, 5, 8] 改成 [3, 9, 8]


# TODO ④ 先打竞猜第一个字，再问星火猜是哪一首


# TODO ⑤ 公布安可全名，第 2 首换成它，打印今晚歌单
