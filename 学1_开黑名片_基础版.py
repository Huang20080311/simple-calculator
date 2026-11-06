# -*- coding:utf-8 -*-
"""
开黑名片
========
从键盘读入游戏名、段位、口号和开黑次数，打出一张开黑名片。
每次按 30 分钟计。合计分钟 = 开黑次数 × 30。

文件开头有两行：API_KEY 和 API_SECRET。
这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
到讯飞开放平台开通「星火认知大模型」后，把 APIKey 贴进第一行引号，把 APISecret 贴进第二行引号。
引号里还是空的，下面的名片仍会打出来，可以没有「星火：」那一行。

运行后应看到（样例：王者荣耀、黄金、冲冲冲、12）：

    ══════ 开黑名片 ══════
    游戏：王者荣耀
    段位：黄金
    口号：冲冲冲
    开黑次数：12
    合计分钟：360
    星火：冲就对了。

「星火：」后面那句话每次用词可能不同，有字就对。

要求：
1. 用 input 读入游戏名、段位、口号、开黑次数。次数转成整数。
2. 合计分钟 = 开黑次数 × 30。样例 12 次，合计分钟是 360。次数不转成整数，这一行对不上或会报错。
3. 标题两边用 "═" * 6。资料写成 print("游戏", 游戏名, sep="：")，段位、口号、次数同样写。
4. 最后调用 ask_spark("用不超过八个字点评这句开黑口号：" + 口号)。文件开头那一段不用改。
5. 在 PyCharm 里运行。
"""
import json
import urllib.request

# 这是基础版。地址是 v1，模型名是 lite，两样必须配对。能开通 X2 就用旁边不带「基础版」的那一份。
# 把 APIKey 贴进 API_KEY 的引号，把 APISecret 贴进 API_SECRET 的引号。
# 这两项不要发给别人。引号里还是空的，前面的打印仍会出来。
API_KEY = "093859fa66b669f89d8235986ed52549"
API_SECRET = "NTU2OWM5ZjA1NDQ1NmNjODgyNTVlYTA5"


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


# TODO ① 四个 input（次数转成整数）


# TODO ② 打印名片，并打印合计分钟 = 次数 × 30

game = input("游戏名:")
name =input("昵称:")
rank ="无畏战魂#1"
slogan =input("口号:")
times =int(input("对局次数:"))


print("="* 6 + "开黑名片" + "=" * 6)
print("游戏", game ,sep=":")
print("玩家名称",name,sep=":")
print("段位",rank,sep=":")
print("口号",slogan,sep=":")
print("对局次数",times,sep=":")
print("合计分钟", times * 30, sep=":")

# TODO ③ 调用 ask_spark，把口号交给它
ask_spark("用不超过八个字点评这句开黑口号：" + slogan)
