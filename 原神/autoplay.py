import time
import win32api
import win32con
winUserName = win32api.GetUserName()
with open('C:\\Users\\' + winUserName + '\\Desktop\\song.txt')as f:
    st = f.read()
l = list(st)
i = 0
print('需要先在桌面创建song.txt，按下大写键会依次循环桌面song.txt内容的大写字母。')
print('有什么用？你弹琴要打的谱子自己手打可能会打错失去节奏，你先把谱子打到txt上，要大写英文，执行后你就可以敲打一个键弹奏歌曲了。')
key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}


def key_down(key):
    """
    函数功能：按下按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0)


def key_up(key):
    """
    函数功能：抬起按键
    参    数：key:按键值
    """
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def key_press(key):
    """
    函数功能：点击按键（按下并抬起）
    参    数：key:按键值
    """
    key_down(key)
    # time.sleep(0.02)
    time.sleep(0.1)
    key_up(key)


while True:
    enter = win32api.GetKeyState(20)
    if enter < 0 and i < len(l):
        key_press(l[i])
        i += 1
    time.sleep(0.05)

#     开启循环，不需要就禁用
    if i == len(l):
        i = 0
