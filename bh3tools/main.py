import win32con, win32api, win32gui, time, random, re, math
from win32clipboard import GetClipboardData, OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData

default = '#fac'  # 默认颜色粉色
colorlist = ['#f20','#f70','#ff0','#7f0','#3c9','#69e','blue','#fcc','#f6c','#fac','#f1a','#eae','#d7d','#c39','#da7']  # 颜色列表
any = random.choice(colorlist)  # 随机颜色列表

# 读取剪贴板的数据
def get_clipboard():
    OpenClipboard()
    d = GetClipboardData(win32con.CF_TEXT)
    CloseClipboard()
    e = d.decode('GBK','ignore')
    # 矫正在崩坏3程序内获取的剪贴内容
    nonum = re.sub(r'[0-9a-zA-Z]', '', e)
    nonumlen = len(nonum)
    numlen = len(e) - nonumlen
    fixlen = math.ceil(nonumlen / 3 * 2)
    if nonumlen == 0:
        fixlen = -numlen
    f = e[:-fixlen]

    # print(f)
    return f


# 写入剪贴板数据
def set_clipboard(astr):
    OpenClipboard()
    EmptyClipboard()
    time.sleep(0.1)
    SetClipboardData(win32con.CF_UNICODETEXT, astr)
    CloseClipboard()


# 全选复制
def copyall():
    win32api.keybd_event(17, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(65, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(67, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


# 粘贴
def paste():
    win32api.keybd_event(17, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(86, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)

def instruction():
    print("崩坏3聊天文字变色助手")
    print("一般情况下，本程序只有管理员身份才能在崩坏3桌面版内运行")
    print("F2:发送彩色字体")
    print("F4:变更颜色")
    print("输入any开始不停的变色")
    print("不输入按下enter为粉色")


# 用法说明.txt
instruction()
while True:
    inputcolor = input("\n请输入你要变换的颜色，字节建议不超过4。\n")
    if inputcolor == "":
        inputcolor = default
        break
    #
    elif len(inputcolor) > 4:
        print("你输入的颜色代码超过长度4，这样会影响你的打字体验。")
        print("是否继续？输入yes意外的内容视为否")
        colorlen = input("Yes?\n")
        if colorlen == "yes" or colorlen == "Yes" or colorlen == "y" or colorlen == "Y":
            break
        else:
            print("请你重新输入颜色代码。")
            continue
    else:
        break
print("你的颜色已经设置成" + inputcolor + "，现在已经可以开始使用了")

while True:
    # 获取窗口句柄
    hwnd = win32gui.GetForegroundWindow()
    # 获取窗口标题
    winname = win32gui.GetWindowText(hwnd)
    # winname = "崩坏3"
    # print(winname)

    # F2
    enter = win32api.GetKeyState(113)
    # F3
    recode = win32api.GetKeyState(114)
    # 特殊
    anyzero = 0
    bytelen = 20
    # 按下F2执行变色与判断是否崩坏3窗口
    if enter < 0 and str(winname) == '崩坏3':
        # 全选复制
        copyall()
        # 读取剪贴板&报错检测
        try:
            gettext = get_clipboard()
        except:
            print("未知错误")
            continue

        # 这是一个随机彩蛋，当你输入的为any时，每次的颜色都不一样，anyzero为专属引导器
        if inputcolor == "any":
            any = random.choice(colorlist)
            inputcolor = any
            anyzero = anyzero + 1

        # 当超过颜色字节数超过长度时进行剩余可用长度计算
        if len(inputcolor) > 4:
            bytelen = bytelen - (len(inputcolor) - 4)

        # 判断字节长度
        if len(gettext) > bytelen:
            win32api.keybd_event(39, 0, 0, 0)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
            print("字节超过" + str(bytelen) + ",请减少输入的文字数量")
            continue

        # 颜色导入
        outtext = '<color=' + inputcolor + '>' + gettext + '</color>'
        # print(outtext)
        set_clipboard(outtext)
        # 粘贴
        paste()
        time.sleep(0.1)
        # 回车发送消息
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        # 发送的信息
        print(gettext)
        # any彩蛋永动器
        if anyzero == 1:
            inputcolor = "any"

    # 按下F3重新定义颜色
    elif recode < 0:
        inputcolor = input("你正在更换颜色，请输入新的颜色吧\n")
        print("你的颜色已经设置成" + inputcolor + "，现在已经可以开始使用了")
