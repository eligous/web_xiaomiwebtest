# 序言注释
# 本系统使用GUI变成编写友好的可视化界面
# 增加直接呈现全班成绩的功能
# 增加登录功能，使数据更加安全
# 增加对学生成绩修改的操作（增加、删除）

import csv
import tkinter
import os
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import StringVar
# from matplotlib import pyplot as plt


class Login(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("学生成绩分析系统")
        self.root.geometry('750x550')
        # 运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=535, width=734, bd=10)  # 创建画布
        self.image_file = tkinter.PhotoImage(file='tu1.gif')  # 加载图片文件
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（上端）

        # 创建一个`label`名为`账号: `
        self.label_account = tkinter.Label(self.root, text='账号: ')
        # 创建一个`label`名为`密码: `
        self.label_password = tkinter.Label(self.root, text='密码: ')

        # 创建一个账号输入框,并设置尺寸
        self.input_account = tkinter.Entry(self.root, width=15)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tkinter.Entry(self.root, show='*', width=15)

        # 创建一个登录系统的按钮
        self.login_button = tkinter.Button(self.root, command=self.login_sys, text="登录", width=10)

        # 完成布局

    def gui_arrang(self):
        self.label_account.place(x=60, y=480)
        self.label_password.place(x=290, y=480)
        self.input_account.place(x=135, y=480)
        self.input_password.place(x=350, y=480)
        self.login_button.place(x=550, y=480)

    # 进行登录信息验证
    def login_sys(self):
        account = self.input_account.get().ljust(9, " ")
        password = self.input_password.get().ljust(6, " ")
        if account == '190350120' and password == '123456':
            messagebox.showinfo('系统提示', '登录成功!')
            self.root.destroy()
            MainWindow()
        else:
            messagebox.showinfo('系统提示', '登录失败')


# 主要窗口

class MainWindow(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("学生成绩分析系统")
        self.root.geometry('800x550')
        self.setup_UI()
        self.load_file_student_info()
        self.load_treeview(self.all_student_list)

    def setup_UI(self):
        # 设定Style
        self.Style01 = Style()
        self.Style01.configure("left.TPanedwindow", background="deepskyblue")
        self.Style01.configure("right.TPanedwindow", background="deepskyblue")
        self.Style01.configure("TButton", width=10, font=("华文黑体", 13, "bold"))

        # 左边：按钮区域,创建一个容器
        self.Pane_left = PanedWindow(width=160, height=540, style="left.TPanedwindow")
        self.Pane_left.place(x=4, y=10)
        self.Pane_right = PanedWindow(width=700, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=10)

        # 添加左边按钮
        self.Button_add = Button(self.Pane_left, text="添加学生", style="TButton",command = Add)
        self.Button_add.place(x=20, y=20)
        self.Button_delete = Button(self.Pane_left, text="删除学生", style="TButton",command = Delete)
        self.Button_delete.place(x=20, y=50)
        self.Button_max = Button(self.Pane_left, text="最高分", style="TButton",command = self.sort_1)
        self.Button_max.place(x=20, y=80)
        self.Button_min = Button(self.Pane_left, text="最低分", style="TButton",command = self.sort_2)
        self.Button_min.place(x=20, y=110)
        self.Button_avg = Button(self.Pane_left, text="单科平均分", style="TButton",command = self.avg_sub)
        self.Button_avg.place(x=20, y=140)
        self.Button_ave = Button(self.Pane_left, text="单人平均分", style="TButton", command=self.ave_sub)
        self.Button_ave.place(x=20, y=170)
        self.Button_sum = Button(self.Pane_left, text="总分", style="TButton",command = self.sum)
        self.Button_sum.place(x=20, y=200)
        self.Button_pic = Button(self.Pane_left, text="分析图", style="TButton",command = view_win)
        self.Button_pic.place(x=20, y=230)

        # 右侧查询界面
        self.Pane_right = PanedWindow(width=720, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=170, y=10)
        # LabelFrame
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息显示", width=620, height=60)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_sno = Label(self.LabelFrame_query, text="欢迎登录学生成绩分析系统")
        self.Label_sno.place(x=5, y=13)

        # self.var_sno = StringVar()
        # self.Entry_sno = Entry(self.LabelFrame_query, width=8, textvariable=self.var_sno)
        # self.Entry_sno.place(x=40, y=10)

        # self.Button_query = Button(self.LabelFrame_query, text="查询", width=4)
        # self.Button_query.place(x=450, y=10)
        # self.Button_all = Button(self.LabelFrame_query, text="显示全部", width=8)
        # self.Button_all.place(x=510, y=10)

        self.Tree = Treeview(self.Pane_right, columns=("sno", "math", "english", "python"),
                             show="headings", height=20)

        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=150, anchor="center")
        self.Tree.column("math", width=150, anchor="center")
        self.Tree.column("english", width=150, anchor="center")
        self.Tree.column("python", width=150, anchor="center")

        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("math", text="高数")
        self.Tree.heading("english", text="英语")
        self.Tree.heading("python", text="python")
        self.Tree.place(x=10, y=80)

        self.all_student_list = []
        self.file_path = "student_score - 副本.csv"
        # 读取文件

    def load_file_student_info(self):
        if not os.path.exists(self.file_path):
            showinfo("系统消息", "提供的文件名不存在！")
        else:
            try:
                with open(file=self.file_path, mode="r") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        temp_list = current_line.split(",")  # 长字符串分割层三个
                        self.all_student_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
            except:
                showinfo("系统消息", "文件读取出现异常！")

    # 本应该界面内进行的搜索功能,功能无法实现废案
    # # 搜索功能
    #     self.query_result_list = []
    #
    # def get_query_result(self):
    #     # 准备查询条件：获取学号
    #     query_condition = self.Entry_sno.get()
    #     # 遍历List获取符合条件的学生信息
    #     for item in self.all_student_list:
    #         if query_condition in item[0]:
    #             # 满足条件的学生
    #             self.query_result_list.append(item)
    #     # 把结果加载的TreeView中
    #     self.load_treeview(self.query_result_list)

    # def load_all_student(self):
    #     # 加载所有的学生信息到treeview
    #     self.load_treeview(self.all_student_list)

    # 加载数据,输入到二维列表中
    def load_treeview(self, current_list: list):
        # 判断是否有数据：
        if len(current_list) == 0:
            showinfo("系统消息", "没有数据加载")
        else:
            for index in range(len(current_list)):
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3],
                                                    ))
        self.Tree = Treeview(self.Pane_right, columns=("sno", "math", "english", "python"),
                             show="headings", height=40)


    # 排序，输出最高分
    def sort_1(self):
        win_sort = tkinter.Tk()
        win_sort.geometry('300x110')
        win_sort.title("最高分")
        # 排序
        score_01.sort()
        score_02.sort()
        score_03.sort()
        # 输出最高分
        label_math = Label(win_sort, text="高数最高分为{}".format(score_01[len(score_01) - 1]))
        label_math.pack()
        label_english = Label(win_sort, text="英语最高分为{}".format(score_02[len(score_02) - 1]))
        label_english.pack()
        label_py = Label(win_sort, text="python最高分为{}".format(score_03[len(score_03) - 1]))
        label_py.pack()
        win_sort.mainloop()


    # 排序，输出最低分
    def sort_2(self):
        win_sort = tkinter.Tk()
        win_sort.geometry('300x110')
        win_sort.title("最低分")
        # 排序
        score_01.sort()
        score_02.sort()
        score_03.sort()
        # 输出最高分
        label_math = Label(win_sort, text="高数最低分为{}".format(score_01[0]))
        label_math.pack()
        label_english = Label(win_sort, text="英语最低分为{}".format(score_02[0]))
        label_english.pack()
        label_py = Label(win_sort, text="python最低分为{}".format(score_03[0]))
        label_py.pack()
        win_sort.mainloop()


    # 平均分
    # 每科目平均分
    def avg_sub(self):
        win_ave_subject = tkinter.Tk()
        win_ave_subject.geometry('300x110')
        win_ave_subject.title("平均分")
        num_ave_subject1 = 0
        num_ave_subject2 = 0
        num_ave_subject3 = 0
        for i in range(len(score)):
            num_ave_subject1 = num_ave_subject1 + eval(score[i][1])
        for i in range(len(score)):
            num_ave_subject2 = num_ave_subject2 + eval(score[i][2])
        for i in range(len(score)):
            num_ave_subject3 = num_ave_subject3 + eval(score[i][3])
        label1 = Label(win_ave_subject, text="高数的平均分为{:.2f}".format(num_ave_subject1 / len(score)))
        label1.pack()
        label2 = Label(win_ave_subject, text="英语的平均分为{:.2f}".format(num_ave_subject2 / len(score)))
        label2.pack()
        label3 = Label(win_ave_subject, text="python的平均分为{:.2f}".format(num_ave_subject3 / len(score)))
        label3.pack()
        win_ave_subject.mainloop()

    # 单人平均分
    def ave_sub(self):
        win_ave_student = tkinter.Tk()
        win_ave_student.geometry('250x800')
        win_ave_student.title("平均分")
        for i in range(len(score)):
            num_01 = "%.2f" % ((eval(score[i][1]) + eval(score[i][2]) + eval(score[i][3])) / 3)
            label = Label(win_ave_student, text="学号为{}的同学，平均分为：".format(score[i][0]) + num_01)
            label.pack()
        win_ave_student.mainloop()


    # 总分计算
    def sum(self):
        win_generalPoints = tkinter.Tk()
        win_generalPoints.geometry('200x600')
        win_generalPoints.title("总分")
        for i_points in range(len(score)):
            num_01 = "%.2f" % (eval(score[i_points][1]) + eval(score[i_points][2]) + eval(score[i_points][3]))
            label = Label(win_generalPoints, text="{}的总分为：".format(score[i_points][0]) + num_01)
            label.pack()
        win_generalPoints.mainloop()


# 成绩的可视化
def view(x_view):
    num_view1 = 0  # 优秀
    num_view2 = 0  # 良好
    num_view3 = 0  # 中等
    num_view4 = 0  # 不合格

    for i_view in range(len(x_view)):
        if 95 <= x_view[i_view] <= 100:
            num_view1 = num_view1 + 1
            continue
        if 80 <= x_view[i_view] <= 94:
            num_view2 = num_view2 + 1
            continue
        if 60 <= x_view[i_view] <= 79:
            num_view3 = num_view3 + 1
            continue
        if x_view[i_view] < 60:
            num_view4 = num_view4 + 1
            continue

    num_view1 = float("%.2f" % (num_view1 / len(x_view) * 100))
    num_view2 = float("%.2f" % (num_view2 / len(x_view) * 100))
    num_view3 = float("%.2f" % (num_view3 / len(x_view) * 100))
    num_view4 = float("%.2f" % (100 - num_view1 - num_view2 - num_view3))

    labels = 'excellent', 'good', 'pass', 'fail'
    sizes = [num_view1, num_view2, num_view3, num_view4]
    fig1, (ax1) = plt.subplots(1)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    plt.show()

def view_02(x_view):
    num_view1 = 0  # 优秀
    num_view2 = 0  # 良好
    num_view3 = 0  # 中等
    num_view4 = 0  # 不合格

    for i_view in range(len(x_view)):
        if 261 <= x_view[i_view] <= 300:
            num_view1 = num_view1 + 1
            continue
        if 241 <= x_view[i_view] <= 260:
            num_view2 = num_view2 + 1
            continue
        if 221 <= x_view[i_view] <= 240:
            num_view3 = num_view3 + 1
            continue
        if x_view[i_view] < 200:
            num_view4 = num_view4 + 1
            continue

    num_view1 = float("%.2f" % (num_view1 / len(x_view) * 100))
    num_view2 = float("%.2f" % (num_view2 / len(x_view) * 100))
    num_view3 = float("%.2f" % (num_view3 / len(x_view) * 100))
    num_view4 = float("%.2f" % (100 - num_view1 - num_view2 - num_view3))

    # labels = '优秀', '良好', '中等', '不合格'
    labels = 'A', 'B', 'C', 'D'
    sizes = [num_view1, num_view2, num_view3, num_view4]
    fig1, (ax1) = plt.subplots(1)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    ax1.axis('equal')
    plt.show()

# 高数的视图
def view1():
    view(score_01)

# 英语的视图
def view2():
    view(score_02)

# python视图
def view3():
    view(score_03)

#总分的视图
def view4():
    view_02(score)

# 可视化界面
def view_win():
    # 创建一个页面
    win_view = tkinter.Tk()
    win_view.title("分析图")
    win_view.geometry('200x150')
    button1_view = Button(win_view, text="高数",command=view1)
    button2_view = Button(win_view, text="英语",command=view2)
    button3_view = Button(win_view, text="python", command=view3)
    button4_view = Button(win_view, text="总分", command=view4)

    button1_view.pack()
    button2_view.pack()
    button3_view.pack()
    button4_view.pack()
    win_view.mainloop()

# # 添加其他学生成绩的功能
def Add():
    window = tkinter.Tk()
    window.title("增加学生")
    frame = Frame(window)
    frame.pack(padx=8, pady=8, ipadx=4)

    lab1 = Label(frame, text="学号")
    lab1.grid(row=0, column=0, padx=5, pady=5)

    lab2 = Label(frame, text="高数")
    lab2.grid(row=1, column=0, padx=5, pady=5)

    lab3 = Label(frame, text="英语")
    lab3.grid(row=2, column=0, padx=5, pady=5)

    lab4 = Label(frame, text="python")
    lab4.grid(row=3, column=0, padx=5, pady=5)

    lab5 = Label(frame, text="结果")
    lab5.grid(row=4, column=0, padx=5, pady=5)

    # 绑定对象到Entry

    p1 = StringVar(master=window)
    ent1 = Entry(frame, textvariable=p1)
    ent1.grid(row=0, column=1)

    p2 = StringVar(master=window)
    ent2 = Entry(frame, textvariable=p2)
    ent2.grid(row=1, column=1)

    p3 = StringVar(master=window)
    ent3 = Entry(frame, textvariable=p3)
    ent3.grid(row=2, column=1)

    p4 = StringVar(master=window)
    ent4 = Entry(frame, textvariable=p4)
    ent4.grid(row=3, column=1)

    p5 = StringVar(master=window)
    ent5 = Entry(frame, textvariable=p5)
    ent5.grid(row=4, column=1, sticky='ew', columnspan=2)

    def submit():
        num = 0  # 一个计数的变量，记录你是否学号相同
        for i in range(len(score)):
            if eval(p1.get()) == eval(score[i][0]):
                num = 1
                p5.set("添加失败")
        if num == 0:
            student = [p1.get(), p2.get(), p3.get(), p4.get()]
            score.append(student)
            close_csv()
            p5.set("添加成功")

    button = Button(frame, text="提交", command=submit)
    button.grid(row=5, column=1)
    window.mainloop()

# 删除学生成绩
def Delete():
    window2 = tkinter.Tk()
    window2.title("删除成绩")
    window2.geometry('300x120')
    frame = Frame(window2)
    frame.pack(padx=8, pady=8, ipadx=4)
    lab1 = Label(frame, text="学号")
    lab1.grid(row=0, column=0, padx=5, pady=5)
    lab2 = Label(frame, text="结果")
    lab2.grid(row=1, column=0, padx=5, pady=5)
    # 绑定对象到Entry

    p1 = StringVar(master=window2)
    ent1 = Entry(frame, textvariable=p1)
    ent1.grid(row=0, column=1)

    p2 = StringVar(master=window2)
    ent2 = Entry(frame, textvariable=p2)
    ent2.grid(row=1, column=1)

    def submit():
        num = 0
        for a in range(len(score)):
            if eval(score[a][0]) == eval(ent1.get()):
                del score[a]
                num = 1
                p2.set("删除成功")
                close_csv()
                break
        if num == 0:
            p2.set("查无此学生")

    button = Button(frame, text="提交", command=submit)
    button.grid(row=5, column=1)
    window2.mainloop()

# 读取文件并保存到列表中
# 读取文件
with open("student_score - 副本.csv", "r",encoding='utf-8') as f:
    score_01 = []
    score_02 = []
    score_03 = []
    reader = csv.reader(f)
    # 将文件放入到列表里面
    score = [row for row in reader]
    for i in range(len(score)):
        score_01.append(eval(score[i][1]))
        score_02.append(eval(score[i][2]))
        score_03.append(eval(score[i][3]))
# 关闭文件时将文件写入csv
def close_csv():
    with open("student_score - 副本.csv", 'w') as f:
        for item in score:
            f.write(','.join(item) + '\n')

def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()
