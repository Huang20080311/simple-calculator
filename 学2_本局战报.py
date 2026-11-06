# -*- coding:utf-8 -*-
"""
本局战报
========
打完一局，在屏幕上打印一个战报。

KDA = (击杀 + 助攻) / 死亡。死亡是 0 时，不能除，KDA = 击杀 + 助攻，用 float 写成小数，屏幕上是 0.0。

评价从上往下问，问到成立的就停：
KDA 大于等于 5，超神。
大于等于 3，优秀。
大于等于 1，及格。
不到 1，送了。

称号写成两层 if。外面先问是不是 MVP。
是 MVP，里面再问是不是送了。不是送了打印「金牌」，送了打印「名不副实」。
不是 MVP，打印「无」。不要写成一句 and。

排位：模式是「排位」或「巅峰」，并且评价不是送了，才打印「记分：记上」。
否则打印「记分：不记」。模式写成 mode in ("排位", "巅峰")。

运行后应看到（排位、8、2、6、y）：

    ══════ 本局战报 ══════
    模式：排位
    击杀：8
    死亡：2
    助攻：6
    KDA：7.0
    评价：超神
    称号：金牌
    记分：记上

再跑三组：
排位、0、4、0、y：KDA 0.0，送了，名不副实，记分不记。
匹配、6、2、4、n：KDA 5.0，超神，无，记分不记。
巅峰、3、1、0、n：KDA 3.0，优秀，无，记分记上。

要求：
1. 模式、击杀、死亡、助攻、是不是 MVP，都用 input 读入。击杀、死亡、助攻转成整数。MVP 是就输入 y。
2. 先算 KDA。死亡是 0 走一条，不是 0 走另一条。
3. 评价用 if / elif / else，从上往下问，问到成立的就停。
4. 称号用 if 里面再写 if。
5. 排位用 and，模式用 in。
6. 标题两边用 "═" * 6。上面四组都运行一遍。
"""
# TODO ① 五个 input（击杀、死亡、助攻转整数）
kills = int(input("击杀"))
deaths = int(input("死亡"))
assist = int(input("助攻"))
# TODO ② 算 KDA。死亡是 0 不能除
if deaths ==0:
    kda =float(kills+assist)
else:
    kda = float(kills+assist)/deaths

if kda >=5:
    rating ="超神"
elif kda >=3:
    rating ="优秀"
elif kda >=1:
    rating ="及格"
else:
    rating ="拉完了"


mvp = input("是否mvp(是输入y)")
if mvp =="y":
    if rating !="l=拉完了":
        title ="金牌"
    else:
        title ="名不副实"
else:
    title ="无"

model = input("模式（排位，匹配，巅峰）")
if model in ("排位","巅峰")and rating !="拉完了":
    ranked ="记分"
else:
    ranked ="不记"

print("="*6+"本局战报"+"="*6)
print("KDA", kda , sep=":")
print("评价", rating , sep=":")
print("称号", title , sep=":")
print("记分",ranked , sep=":")
# TODO ③ 评价、称号、排位，再把战报打出来
