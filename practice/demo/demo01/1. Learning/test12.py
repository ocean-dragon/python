import random
import time
import tkinter as tk  # 导入tkinter库
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import requests

thread_num = 100
show_data = []


# 弹窗
def PopWindow(content):
    root = tk.Tk()
    root.title("Poem")  # 设置标题
    # root.iconbitmap("D:\\Python\\python\\practice\\demo\\demo01\\1.Learning\\favicon.ico")  # 自定义弹窗的图标
    root.attributes("-alpha", 0.9)  # 设置创建为透明度状态
    # 获取电脑屏幕的范围，用于在屏幕随机位置生成窗口
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    random_w = random.randint(0, width)
    random_h = random.randint(0, height)

    root.geometry("220x220" + "+" + str(random_w) + "+" + str(random_h))  # 设置生成窗口的大小
    tk.Label(root, text=f"{content}", bg="skyblue", font=("黑体", 20), width=50,
             height=50).pack()  # 设置窗口中的内容，text是显示的文本
    root.mainloop()  # 显示窗口


# https://www.gushiwen.cn/gushi/sanbai.aspx
# //*[@id="html"]/body/div[3]/div[1]/div[2]/div/span/a
# 获取网站内容
def getData():
    url = "https://www.gushiwen.cn/gushi/sanbai.aspx"
    re = requests.get(url).text  # 获取网站的html数据
    e = etree.HTML(re)  # 把HTML转成etree对象，便于获取HTML的节点信息
    node_li = e.xpath('//*[@id="html"]/body/div[3]/div[1]/div[2]/div/span/a')  # 通过xpath筛选出所有目标节点
    for i in node_li:
        show_data.append(i.text)


def main():
    getData()


if __name__ == '__main__':
    main()
    # 使用多线程
    with ThreadPoolExecutor(max_workers=thread_num) as tp:
        for item in show_data:
            tp.submit(PopWindow, item)  # 让多线程去执行弹窗
            time.sleep(0.1)

    # 最后打包软件
    # 用pyinstaller库
    # pyinstaller -F -w -i "icon_path"
