# 定义价格区间
def moneyRate(x):
    if 0 <= x < 200000:
        return ('0~20w')
    if 200000 <= x < 400000:
        return ('20~40w')
    if 400000 <= x < 600000:
        return ('40~60w')
    if 600000 <= x < 800000:
        return ('60~80w')
    if 800000 <= x < 1000000:
        return ('80~100w')
    if x >= 1000000:
        return ('>100w')


# 购买年限区间的转换
def yearRange(x):
    if 0 <= x < 2:
        return ('0~2年')
    if 2 <= x < 4:
        return ('2~4年')
    if 4 <= x < 6:
        return ('4~6w')
    if 6 <= x < 8:
        return ('6~8年')
    if 8 <= x < 10:
        return ('8~10年')
    if x >= 10:
        return ('>10年')
