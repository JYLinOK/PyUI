from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
import tkinter.colorchooser
import tkinter.filedialog
import tkinter as tk
import HS

import config as config

allconfig = config.config


# class of Main interface
class PyUI(Tk):
    # Main interface Define
    def __init__(self):
        super().__init__()
        # Main interface parameter setting
        w = 1000
        h = 700
        self.minsize(w, h)  # 最小化固定

        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)

        self.state('zoomed')
        self.title('PyUI')
        self.BiaoTi_Text = 'PyUI'
        self.BiaoTi_Text_YanSe = 'black'
        self.ChuangKou_JiXia_YanSe = 'black'
        self.ChuangKou_BianTiLan_YanSe = 'white'
        self.ChuangKou_BeiJing_YanSe = 'white'

        # Scale setting
        self.Sca_JiZhi_X = 1000
        self.Sca_JiZhi_Y = 1000

        # parameter setting
        self.ChuangKou_BianYan_YanSe = 'black'
        self.ChuangKou_BiaoTiLan_YanSe = 'green'

        # Control component initial parameter setting
        # Button parameter
        self.Button_H = 50
        self.Button_W = 100
        self.Button_NO = 0
        self.Button_YanSe = 'gray'
        self.Button_Text_YanSe = 'white'

        # Boolean value setting
        
        allconfig['flag_CK_GuDing'] = FALSE
        self.flag_WangGe = FALSE
        self.flag_SongKai = FALSE
        self.flag_BuJian_YinCang = FALSE

        # Original canvas parameter
        self.Yuan_canva_H = 600  # height 对应 Y
        self.Yuan_canva_W = 800  # width  对应 X

        # Canvas parameter
        allconfig['canva_H'] = self.Yuan_canva_H
        allconfig['canva_W'] = self.Yuan_canva_W
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        # Frame parameter
        self.fram_H = allconfig['canva_H']  # height 对应 Y
        self.fram_W = allconfig['canva_W']  # width  对应 X

        # Menu bar width
        self.bar_W = allconfig['bar_W']

        # Grid width parameter
        self.WangGe_YanSe = 'gray'

        # 属性框参数
        self.V_Scal_Y1 = StringVar()
        self.V_Scal_Y2 = StringVar()

        # 设置画布的放大调节及参数定义设置
        self.vy = StringVar()
        self.vx = StringVar()
        self.vx_Text_font = StringVar()

        self.ent_y = StringVar()
        self.ent_x = StringVar()

        self.GuDing_Text = StringVar()
        self.GuDing_Text.set('Lock')

        self.Btn_WG_Text = StringVar()
        self.Btn_WG_Text.set('Grid')

        self.Btn_YinCang_Text = StringVar()
        self.Btn_YinCang_Text.set('Hide')

        self.Btn_ShuXing_Text = StringVar()
        self.Btn_ShuXing_Text.set('<=')

        self.Tv_BianYi_Text = StringVar()
        self.Tv_BianYi_Text.set('Text')

        self.Tv_Canva_Hide = StringVar()
        self.Tv_Canva_Hide.set('Paint')

        # 网格参数设定
        allconfig['WangGe_ShuMu_X'] = (allconfig['canva_H'] - self.bar_W) / allconfig['WangGe_KuanDu']
        allconfig['WangGe_ShuMu_Y'] = allconfig['canva_W'] / allconfig['WangGe_KuanDu']

        # Switch to the main interface UI setting
        self.Set_UI()

    # ____________________________________________________________________________________________________________

    def Set_UI(self):
        # Set Canvas
        self.canva = Canvas(bg='white', width=allconfig['canva_W'], height=allconfig['canva_H'])  # scrollregion=(0, 0, 1000, 1000))  # 创建canva
        self.canva.place(x=allconfig['canva_X'], y=allconfig['canva_Y'])  # 放置canva的位置

        # 画 Menu
        self.it_Menu = self.canva.create_rectangle(0, 0, 0, 0)

        # 画外边框
        self.it1 = self.canva.create_rectangle(2, allconfig['canva_H'] - 1, allconfig['canva_W'] - 1, 2,
                                               fil=self.ChuangKou_BeiJing_YanSe)
        # 画标题栏
        self.it2 = self.canva.create_rectangle(2, self.bar_W, allconfig['canva_W'] - 1, self.bar_W,
                                               fil=self.ChuangKou_BiaoTiLan_YanSe)

        # 画标题
        self.it_BiaoTi = self.canva.create_text(43, 16, text=self.BiaoTi_Text,
                                                font=('Consol', 11),
                                                fill=self.BiaoTi_Text_YanSe)

        # 画标题栏按钮
        self.it_BiaoTi_AnNiu_ZuiXiao = self.canva.create_text(allconfig['canva_W'] - 116, 16, text='—',
                                                              font=('Consol', 11),
                                                              fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_ZuiDa = self.canva.create_text(allconfig['canva_W'] - 70, 16, text='□',
                                                            font=('Consol', 11),
                                                            fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_GuanBi = self.canva.create_text(allconfig['canva_W'] - 28, 16, text='X',
                                                             font=('Helvetica', 11),
                                                             fill=self.BiaoTi_Text_YanSe)

        self.Menubar = Menu(self)
        # 定义下拉菜单栏
        FileMenu = Menu(self.Menubar, tearoff=0)
        FileMenu.add_command(label='Compile', command=self.BianYi)
        FileMenu.add_command(label='Generate', command=self.BianYi)
        FileMenu.add_command(label='Copy', command=self.BianYi)
        FileMenu.add_separator()
        FileMenu.add_command(label='Quit', command=self.quit)
        self.Menubar.add_cascade(label='File', menu=FileMenu)

        # 定义控件菜单栏
        KongJianMenu = Menu(self.Menubar, tearoff=0)
        KongJianMenu.add_command(label='Button', command=self.Hua_Button)
        KongJianMenu.add_command(label='Canvas', command=self.Hua_Canvas)
        KongJianMenu.add_command(label='Checkbutton', command=self.Hua_Checkbutton)
        KongJianMenu.add_command(label='Combobox', command=self.Hua_Combobox)
        KongJianMenu.add_command(label='Entry', command=self.Hua_Entry)
        KongJianMenu.add_command(label='Frame', command=self.Hua_Frame)
        KongJianMenu.add_command(label='Label', command=self.Hua_Label)
        KongJianMenu.add_command(label='LabelFrame', command=self.Hua_LabelFrame)
        KongJianMenu.add_command(label='Listbox', command=self.Hua_Listbox)
        KongJianMenu.add_command(label='Menu', command=self.Hua_Menu)
        KongJianMenu.add_command(label='Message', command=self.Hua_Message)
        KongJianMenu.add_command(label='PanedWindow', command=self.Hua_PanedWindow)
        KongJianMenu.add_command(label='Radiobutton', command=self.Hua_Radiobutton)
        KongJianMenu.add_command(label='Scale_X', command=self.Hua_Scale_X)
        KongJianMenu.add_command(label='Scale_Y', command=self.Hua_Scale_Y)
        KongJianMenu.add_command(label='Spinbox', command=self.Hua_Spinbox)
        KongJianMenu.add_command(label='Text', command=self.Hua_Text)
        self.Menubar.add_cascade(label='Control', menu=KongJianMenu)

        # 定义自画控件菜单栏
        SheZhiMenu = Menu(self.Menubar, tearoff=0)
        SheZhiMenu.add_command(label='System Setup', command=HS.hello)
        # self.Menubar.add_cascade(label='Setup', menu=SheZhiMenu)


        # 定义窗口菜单栏
        ChuangKouMenu = Menu(self.Menubar, tearoff=0)
        ChuangKouMenu.add_command(label='New son_win', command=HS.hello)
        ChuangKouMenu.add_command(label='Current win set', command=HS.hello)
        ChuangKouMenu.add_command(label='Win control information', command=HS.hello)
        # self.Menubar.add_cascade(label='Win', menu=ChuangKouMenu)

        # 定义对话框菜单栏
        DuiHuaKuangMenu = Menu(self.Menubar, tearoff=0)
        DuiHuaKuangMenu.add_command(label='New news dialog', command=HS.hello)
        DuiHuaKuangMenu.add_command(label='New flie dialog', command=HS.hello)
        DuiHuaKuangMenu.add_command(label='New colour dialog', command=HS.hello)
        # self.Menubar.add_cascade(label='Dialog', menu=DuiHuaKuangMenu)

        # 定义帮助菜单栏
        BangZhuMenu = Menu(self.Menubar, tearoff=0)
        BangZhuMenu.add_command(label='About', command=HS.hello)
        # self.Menubar.add_cascade(label='Help', menu=BangZhuMenu)

        # ____________________________________________________________________________________________________________
        # 定义右键菜单
        # 新建控件右键菜单
        self.New_kj_menu = Menu(self.Menubar, tearoff=0)
        self.New_kj_menu.add_command(label='Button', command=self.Hua_Button)
        self.New_kj_menu.add_command(label='Canvas', command=self.Hua_Canvas)
        self.New_kj_menu.add_command(label='Checkbutton', command=self.Hua_Checkbutton)
        self.New_kj_menu.add_command(label='Combobox', command=self.Hua_Combobox)
        self.New_kj_menu.add_command(label='Entry', command=self.Hua_Entry)
        self.New_kj_menu.add_command(label='Frame', command=self.Hua_Frame)
        self.New_kj_menu.add_command(label='Label', command=self.Hua_Label)
        self.New_kj_menu.add_command(label='LabelFrame', command=self.Hua_LabelFrame)
        self.New_kj_menu.add_command(label='Listbox', command=self.Hua_Listbox)
        self.New_kj_menu.add_command(label='Menu', command=self.Hua_Menu)
        self.New_kj_menu.add_command(label='Message', command=self.Hua_Message)
        self.New_kj_menu.add_command(label='PanedWindow', command=self.Hua_PanedWindow)
        self.New_kj_menu.add_command(label='Radiobutton', command=self.Hua_Radiobutton)
        self.New_kj_menu.add_command(label='Scale_X', command=self.Hua_Scale_X)
        self.New_kj_menu.add_command(label='Scale_Y', command=self.Hua_Scale_Y)
        self.New_kj_menu.add_command(label='Spinbox', command=self.Hua_Spinbox)
        self.New_kj_menu.add_command(label='Text', command=self.Hua_Text)

        # ____________________________________________________________________________________________________________
        # 编辑控件右键菜单
        self.BianJi_kj_menu = Menu(self.Menubar, tearoff=0)
        self.BianJi_kj_menu.add_command(label='OK', command=self.BianJi_OK)
        self.BianJi_kj_menu.add_command(label='Move', command=self.BianJi_Move)
        self.BianJi_kj_menu.add_command(label='Design', command=self.BianJi_Design)
        self.BianJi_kj_menu.add_command(label='Delete', command=self.BianJi_Delete)
        self.BianJi_kj_menu.add_command(label='Cancel', command=self.BianJi_Cancel)

        # 展示主菜单
        self.config(menu=self.Menubar)

        # X:横向  Y:纵向 设置部件
        self.Lab1 = Label(text='Y:', font=('Consol', '26', 'bold'), foreground='DarkBlue')
        self.Lab1.place(x=0, y=0)

        self.Lab2 = Label(text='X:', font=('Consol', '26', 'bold'), foreground='DarkBlue')
        self.Lab2.place(x=60, y=0)

        self.Lab_CK_X_len = Label(text='X length', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_CK_X_len.place(x=623, y=0)

        self.Lab_CK_Y_len = Label(text='Y length', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_CK_Y_len.place(x=623, y=26)

        self.Lab_font_size = Label(text='font size', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_font_size.place(x=1250, y=760)
        self.Lab_font_size.lower()

        # ____________________________________________________________________________________________________________

        self.Btn_CK_ZhuanDao = Button(text='To win', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                      command=self.ChuangKouZhuan)
        self.Btn_CK_ZhuanDao.place(x=762, y=0)  # 要想以后修改Btn_CK_ZhuanDao，必须先定义后摆放！

        self.Btn_CK_FuWei = Button(text='Reset win', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                      command=self.FuWeiKouZhuan)
        self.Btn_CK_FuWei.place(x=762, y=26)

        self.Btn_CK_Set = Button(text='Win_Set', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                                   command=self.Set_KouZhuan)
        self.Btn_CK_Set.place(x=826, y=26)

        # ____________________________________________________________________________________________________________
        # Hide or Show 键
        self.Btn_YinCang = Button(textvariable=self.Btn_YinCang_Text, font=('Consol', 10), foreground='DarkBlue', width=6, height=1,
                           command=self.YinCang)
        self.Btn_YinCang.place(x=1482, y=0)

        # ____________________________________________________________________________________________________________
        # Update 键
        self.Btn_Update = Button(text='Update', font=('Consol', 10), foreground='DarkBlue',
                                  width=6, height=1,
                                  command=self.UI_Ban_Btn_OK)
        self.Btn_Update.place(x=2000, y=26)
        # ____________________________________________________________________________________________________________
        #  属性键
        self.Btn_ShuXing = Button(textvariable=self.Btn_ShuXing_Text, font=('Consol', 10), foreground='DarkBlue',
                                  width=6, height=1,
                                  command=self.ShuXing_Zhan)
        self.Btn_ShuXing.place(x=1482, y=26)

        self.Btn_BianYi = Button(text='Compi', font=('Consol', 10), foreground='black', width=5, height=2,
                           command=self.BianYi)
        self.Btn_BianYi.place(x=6, y=600)
        self.Btn_BianYi.lower()

        self.Btn_BianYi_FuZhi = Button(text='Copy', font=('Consol', 10), foreground='black', width=5, height=2,
                                 command=self.BianYi_Color_Green)
        self.Btn_BianYi_FuZhi.place(x=6, y=650)
        self.Btn_BianYi_FuZhi.lower()

        self.Btn_BianYi_ShengCheng = Button(text='Gener', font=('Consol', 10), foreground='black', width=5, height=2,
                                 command=self.BianYi_Color_Green)
        self.Btn_BianYi_ShengCheng.place(x=6, y=700)
        self.Btn_BianYi_ShengCheng.lower()

        # ____________________________________________________________________________________________________________
        # 下排按钮
        self.Btn_BianYi_Text = Button(textvariable=self.Tv_BianYi_Text, font=('华文行楷', 12), foreground='red', width=5, height=1,
                                      command=self.BianYi_Text)
        self.Btn_BianYi_Text.place(x=60, y=746)
        self.Btn_BianYi_Text.lower()

        self.Btn_Canva_Hide = Button(textvariable=self.Tv_Canva_Hide, font=('华文行楷', 12), foreground='DarkBlue', width=5,
                                      height=1,
                                      command=self.Canva_Hide)
        self.Btn_Canva_Hide.place(x=120, y=746)
        self.Btn_Canva_Hide.lower()

        self.Btn_BianYi_Color_White = Button(text='Color', font=('华文行楷', 12), foreground='black', background='white', width=5, height=1,
                                      command=self.BianYi_Color_White)
        self.Btn_BianYi_Color_White.place(x=180, y=746)
        self.Btn_BianYi_Color_White.lower()

        self.Btn_BianYi_Color_Black = Button(text='Color', font=('华文行楷', 12), foreground='white', background='black', width=5, height=1,
                                       command=self.BianYi_Color_Black)
        self.Btn_BianYi_Color_Black.place(x=240, y=746)
        self.Btn_BianYi_Color_Black.lower()

        self.Btn_BianYi_Color_YangPiZhi = Button(text='Color', font=('华文行楷', 12), foreground='black', background='LemonChiffon', width=5, height=1,
                                       command=self.BianYi_Color_YangPiZhi)
        self.Btn_BianYi_Color_YangPiZhi.place(x=300, y=746)
        self.Btn_BianYi_Color_YangPiZhi.lower()

        self.Btn_BianYi_Color_Green = Button(text='Color', font=('华文行楷', 12), foreground='white', background='green', width=5, height=1,
                                       command=self.BianYi_Color_Green)
        self.Btn_BianYi_Color_Green.place(x=360, y=746)
        self.Btn_BianYi_Color_Green.lower()

        self.Btn_WangGe = Button(textvariable=self.Btn_WG_Text, font=('华文行楷', 13), foreground='DarkBlue',
                                 width=5, height=1, command=self.QiYong_WangGe)
        self.Btn_WangGe.place(x=420, y=746)
        self.Btn_WangGe.lower()

        self.GuDing = Button(textvariable=self.GuDing_Text, font=('华文行楷', 13),foreground='DarkBlue', width=5, height=1,
                             command=self.GuDingChuangKou)
        self.GuDing.place(x=0, y=746)
        self.GuDing.lower()

        # ____________________________________________________________________________________________________________

        self.Ent_X = Entry(textvariable=self.ent_x, width=5, font=('Consol', '12', 'bold'), foreground='Darkblue')
        self.Ent_X.place(x=703, y=0)

        self.Ent_Y = Entry(textvariable=self.ent_y, width=5, font=('Consol', '12', 'bold'), foreground='Darkblue')
        self.Ent_Y.place(x=703, y=26)

        # ____________________________________________________________________________________________________________

        self.Sca_Y = Scale(from_=0, to=self.Sca_JiZhi_Y, orient=VERTICAL, variable=self.vy, length=500,
                      resolution=1, command=self.HuaBuFangDa_Y)
        self.Sca_Y.place(x=0, y=40)

        self.Sca_X = Scale(from_=0, to=self.Sca_JiZhi_X, orient=HORIZONTAL, variable=self.vx, length=500,
                      resolution=1, command=self.HuaBuFangDa_X)
        self.Sca_X.place(x=100, y=0)

        # ____________________________________________________________________________________________________________
        # 字体调节滚动条
        self.Sca_Text_front = Scale(from_=8, to=50, orient=HORIZONTAL, variable=self.vx_Text_font, length=200,
                           resolution=1, command=self.Text_font)
        self.Sca_Text_front.set(16)
        self.Sca_Text_front.place(x=1328, y=739)
        self.Sca_Text_front.lower()

        self.ent_x.set(allconfig['canva_W'])
        self.ent_y.set(allconfig['canva_H'])

        self.PanedWin_X1 = PanedWindow(width=1480, height=690, sashwidth=6,  sashrelief=SUNKEN)
        self.PanedWin_X1.place(x=2000, y=50)
        self.PanedWin_X1.lower()

        self.Text_BianYi = ScrolledText(self.PanedWin_X1, width=74, height=22, font=('Consolas', '20'), insertbackground='black')
        self.PanedWin_X1.add(self.Text_BianYi)
        self.Text_BianYi.lower()

        self.PanedWin_Y1 = PanedWindow(self.PanedWin_X1, orient=VERTICAL, sashwidth=6,  sashrelief=SUNKEN)
        self.PanedWin_X1.add(self.PanedWin_Y1)

        self.Paned_Frame_Y1 = Frame(self.PanedWin_Y1,  width=300, height=380, bg='red')
        self.PanedWin_Y1.add(self.Paned_Frame_Y1)

        self.Paned_Frame_Y2 = Frame(self.PanedWin_Y1, width=330, height=300, bg='green')
        self.PanedWin_Y1.add(self.Paned_Frame_Y2)

        # ____________________________________________________________________________________________________________

        self.PanedF_Canvas_Y1 = Canvas(self.Paned_Frame_Y1, bg='white', width=300, height=1700)
        self.PanedF_Canvas_Y1.place(x=48, y=0)

        self.Scal_Y1 = Scale(self.Paned_Frame_Y1, from_=0, to=100, fg='white', bg='white', resolution=2, length=380,
                             variable=self.V_Scal_Y1, command=self.V_P_Scal_Y1)
        self.Scal_Y1.pack(side=LEFT, fill=Y)

        self.PanedF_Canvas_Y2 = Canvas(self.Paned_Frame_Y2, bg='white', width=300, height=1700)
        self.PanedF_Canvas_Y2.place(x=48, y=0)

        self.Scal_Y2 = Scale(self.Paned_Frame_Y2, from_=0, to=100, fg='white', bg='white', resolution=2, length=380,
                             variable=self.V_Scal_Y2, command=self.V_P_Scal_Y2)
        self.Scal_Y2.pack(side=LEFT, fill=Y)

        # ____________________________________________________________________________________________________________
        # 上属性框部件设置
        self.lab_ControlType = StringVar()
        self.ent_ControlName = StringVar()
        self.ent_X0 = IntVar()
        self.ent_Y0 = IntVar()
        self.ent_width = IntVar()
        self.ent_height = IntVar()
        self.ent_length = IntVar()
        self.ent_fontSize = IntVar()
        self.combt_fontType = StringVar()
        self.combt_foreground = StringVar()
        self.combt_background = StringVar()
        self.combt_anchor = StringVar()
        self.combt_justify = StringVar()
        self.ent_text = StringVar()
        self.combt_state = StringVar()
        self.combt_relief = StringVar()
        self.combt_highlightcolor = StringVar()
        self.combt_highlightbackground = StringVar()
        self.combt_bitmap = StringVar()
        self.ent_image = StringVar()
        self.combt_padx = IntVar()
        self.combt_pady = IntVar()
        self.combt_takefocus = StringVar()
        self.combt_cursor = StringVar()
        self.ent_container = StringVar()
        self.ent_command = StringVar()


        # 上属性框部件设置
        self.lab_ControlType.set(allconfig['lab_ControlType'])
        self.ent_ControlName.set(allconfig['ent_ControlName'])
        self.ent_X0.set(allconfig['ent_X0'])
        self.ent_Y0.set(allconfig['ent_Y0'])
        self.ent_width.set(allconfig['ent_width'])
        self.ent_height.set(allconfig['ent_height'])
        self.ent_length.set(allconfig['ent_length'])
        self.ent_fontSize.set(allconfig['ent_fontSize'])
        self.combt_fontType.set(allconfig['combt_fontType'])
        self.combt_foreground.set(allconfig['combt_foreground'])
        self.combt_background.set(allconfig['combt_background'])
        self.combt_anchor.set(allconfig['combt_anchor'])
        self.combt_justify.set(allconfig['combt_justify'])
        self.ent_text.set(allconfig['ent_text'])
        self.combt_state.set(allconfig['combt_state'])
        self.combt_relief.set(allconfig['combt_relief'])
        self.combt_highlightcolor.set(allconfig['combt_highlightcolor'])
        self.combt_highlightbackground.set(allconfig['combt_highlightbackground'])
        self.combt_bitmap.set(allconfig['combt_bitmap'])
        self.ent_image.set(allconfig['ent_image'])
        self.combt_padx.set(allconfig['combt_padx'])
        self.combt_pady.set(allconfig['combt_pady'])
        self.combt_takefocus.set(allconfig['combt_takefocus'])
        self.combt_cursor.set(allconfig['combt_cursor'])
        self.ent_container.set(allconfig['ent_container'])
        self.ent_command.set(allconfig['ent_command'])

        self.JG_Y=70
        self.JG_X=6
        self.FuDong=6
        self.FuDong_Scal_Y=30

        # ____________________________________________________________________________________________________________
        # Control Type
        self.l = Label(self.PanedF_Canvas_Y1, text='control type', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 0 + self.FuDong)

        self.Ent_ControlType = Label(self.PanedF_Canvas_Y1, textvariable=self.lab_ControlType, width=20, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_ControlType.place(x=self.JG_X + 120, y=self.JG_Y * 0 + self.FuDong)

        # ____________________________________________________________________________________________________________
        # Control Name
        self.l = Label(self.PanedF_Canvas_Y1, text='control name', bg='white')
        self.l.place(x=self.JG_X, y=40)

        self.Ent_ControlName = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_ControlName, width=16, bg='LightGreen',
                            foreground='black')
        self.Ent_ControlName.place(x=self.JG_X + 120, y=40)

        self.Btn_Ok_ControlName = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                     , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_ControlName.place(x=self.JG_X + 241, y=40)

        # ____________________________________________________________________________________________________________
        # X0
        self.l = Label(self.PanedF_Canvas_Y1, text='X0', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y*1 + self.FuDong)

        self.Ent_X0 = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_Y0, width=16, bg='DeepSkyBlue',
                          foreground='Darkblue')
        self.Ent_X0.place(x=self.JG_X + 120, y=self.JG_Y*1 + self.FuDong)

        self.Btn_Ok_X0 = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                     , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_X0.place(x=self.JG_X + 241, y=self.JG_Y*1 + self.FuDong)

        self.Sca_X0 = Scale(self.PanedF_Canvas_Y1, from_=0, to=1800, orient=HORIZONTAL, variable=self.ent_X0,
                     length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_X0.place(x=self.JG_X, y=self.JG_Y*1 + self.FuDong_Scal_Y)

        # ____________________________________________________________________________________________________________
        # Y0

        self.l = Label(self.PanedF_Canvas_Y1, text='Y0', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 2 + self.FuDong)

        self.Ent_Y0 = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_Y0, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_Y0.place(x=self.JG_X + 120, y=self.JG_Y * 2 + self.FuDong)

        self.Btn_Ok_Y0 = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                            , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_Y0.place(x=self.JG_X + 241, y=self.JG_Y * 2 + self.FuDong)

        self.Sca_Y0 = Scale(self.PanedF_Canvas_Y1, from_=0, to=1600, orient=HORIZONTAL, variable=self.ent_Y0,
                       length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_Y0.place(x=self.JG_X, y=self.JG_Y * 2 + self.FuDong_Scal_Y)

        # ____________________________________________________________________________________________________________
        # width
        self.l = Label(self.PanedF_Canvas_Y1, text='width', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 3 + self.FuDong)

        self.Ent_width = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_width, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_width.place(x=self.JG_X + 120, y=self.JG_Y * 3 + self.FuDong)

        self.Btn_Ok_width = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                            , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_width.place(x=self.JG_X + 241, y=self.JG_Y * 3 + self.FuDong)

        self.Sca_width = Scale(self.PanedF_Canvas_Y1, from_=0, to=300, orient=HORIZONTAL, variable=self.ent_width,
                            length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_width.place(x=self.JG_X, y=self.JG_Y * 3 + self.FuDong_Scal_Y)

        # ____________________________________________________________________________________________________________
        # height
        self.l = Label(self.PanedF_Canvas_Y1, text='height', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 4 + self.FuDong)

        self.Ent_height = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_height, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_height.place(x=self.JG_X + 120, y=self.JG_Y * 4 + self.FuDong)

        self.Btn_Ok_height = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                               , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_height.place(x=self.JG_X + 241, y=self.JG_Y * 4 + self.FuDong)

        self.Sca_height = Scale(self.PanedF_Canvas_Y1, from_=0, to=100, orient=HORIZONTAL, variable=self.ent_height,
                            length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_height.place(x=self.JG_X, y=self.JG_Y * 4 + self.FuDong_Scal_Y)

        # ____________________________________________________________________________________________________________
        # length
        len_scal = 16
        D = 18
        self.l = Label(self.PanedF_Canvas_Y1, text='length', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * len_scal - D)

        self.Ent_length = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_length, width=16, bg='DeepSkyBlue',
                                foreground='Darkblue')
        self.Ent_length.place(x=self.JG_X + 120, y=self.JG_Y * len_scal - D)

        self.Btn_Ok_length = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_length.place(x=self.JG_X + 241, y=self.JG_Y * len_scal - D)

        self.Sca_length = Scale(self.PanedF_Canvas_Y1, from_=0, to=2000, orient=HORIZONTAL, variable=self.ent_length,
                                length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_length.place(x=self.JG_X, y=self.JG_Y * len_scal + self.FuDong_Scal_Y - 6 - D)

        # ____________________________________________________________________________________________________________
        # fontSize
        self.l = Label(self.PanedF_Canvas_Y1, text='fontSize', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 5 + self.FuDong)

        self.Ent_fontSize = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_fontSize, width=16, bg='DeepSkyBlue',
                                foreground='Darkblue')
        self.Ent_fontSize.place(x=self.JG_X + 120, y=self.JG_Y * 5 + self.FuDong)

        self.Btn_Ok_fontSize = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_fontSize.place(x=self.JG_X + 241, y=self.JG_Y * 5 + self.FuDong)

        self.Sca_fontSize = Scale(self.PanedF_Canvas_Y1, from_=1, to=100, orient=HORIZONTAL, variable=self.ent_fontSize,
                                length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_fontSize.place(x=self.JG_X, y=self.JG_Y * 5 + self.FuDong_Scal_Y)

        # ____________________________________________________________________________________________________________
        # fontType
        self.l = Label(self.PanedF_Canvas_Y1, text='fontType', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 6 + self.FuDong)

        self.comb_FontType_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_fontType)
        self.comb_FontType_Chose['values'] = \
            (
                'TkDefaultFont','Consolas', 'Arial', 'Algerian', 'Arial Rounded MT Bold', 'Bell MT', 'Bauhaus 93', 'BankGothic Md BT'
            , 'Bradley Hand ITC', 'CASTELLAR', 'Elephant', 'French Script MT', 'Helvetica', 'Palace Script MT'
            , 'MS UI Gothic', 'MingLiU_HKSCS-ExtB', 'Vineta BT', 'Swis721 BlkEx BT', '微软雅黑', '华文宋体'
            , '华文行楷', '华文隶书', '华文新魏', '华文楷体', '华文细黑', '华文中宋', '华文彩云', '华文琥珀'
            , '方正舒体', '方正姚体', '楷体', '宋体', '隶书', '幼圆', '新宋体'
            )
        self.comb_FontType_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 6 + self.FuDong)
        self.comb_FontType_Chose.current(0)

        self.Btn_Ok_fontSize = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                  , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_fontSize.place(x=self.JG_X + 241, y=self.JG_Y * 6 + self.FuDong)

        # ____________________________________________________________________________________________________________
        # foreground
        self.l = Label(self.PanedF_Canvas_Y1, text='foreground', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 - 20)

        self.Btn_foreground = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                     command=self.More_foreground)
        self.Btn_foreground.place(x=self.JG_X+215, y=self.JG_Y * 7 - 20)

        self.Btn_Ok_foreground = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                  , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_foreground.place(x=self.JG_X + 241, y=self.JG_Y * 7 - 20)

        self.comb_foreground_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15, textvariable=self.combt_foreground)
        self.comb_foreground_Chose['values'] = \
            (
                'SystemButtonText','black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
            , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet','Beige'
            , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue','Aqua'
            , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
            , 'SlateGray', 'LightSlateGray', 'CadetBlue','DodgerBlue'
            )
        self.comb_foreground_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 - 20)
        self.comb_foreground_Chose.current(0)

        # ____________________________________________________________________________________________________________
        # background
        self.l = Label(self.PanedF_Canvas_Y1, text='background', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 20)

        self.Btn_background = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                     command=self.More_background)
        self.Btn_background.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 20)

        self.Btn_Ok_background = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_background.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 20)

        self.comb_background_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15, textvariable=self.combt_background)
        self.comb_background_Chose['values'] = \
            (
                'SystemButtonFace','black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
            , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
            , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
            , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
            , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_background_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 20)
        self.comb_background_Chose.current(0)

        # ____________________________________________________________________________________________________________
        # anchor
        self.l = Label(self.PanedF_Canvas_Y1, text='anchor', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 60)

        self.combt_anchor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_anchor)
        self.combt_anchor_Chose['values'] = \
            (
               'center', 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'
            )
        self.combt_anchor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 60)
        self.combt_anchor_Chose.current(0)

        self.Btn_Ok_anchor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_anchor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 60)

        # ____________________________________________________________________________________________________________
        # justify
        self.l = Label(self.PanedF_Canvas_Y1, text='justify', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 100)  # y 方向每 40一间隔

        self.combt_justify_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_justify)
        self.combt_justify_Chose['values'] = \
            (
                'center', 'left', 'right'
            )
        self.combt_justify_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 100)
        self.combt_justify_Chose.current(0)

        self.Btn_Ok_justify = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_justify.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 100)

        # ____________________________________________________________________________________________________________
        # text
        self.l = Label(self.PanedF_Canvas_Y1, text='text', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 140)  # y 方向每 40一间隔

        self.Ent_text = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_text, width=26, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_text.place(x=self.JG_X+50, y=self.JG_Y * 7 + 140)

        self.Btn_Ok_text = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                 , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_text.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 140)

        # ____________________________________________________________________________________________________________
        # state
        self.l = Label(self.PanedF_Canvas_Y1, text='state', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 180)  # y 方向每 40一间隔

        self.combt_state_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_state)
        self.combt_state_Chose['values'] = \
            (
                'normal', 'active', 'disabled'
            )
        self.combt_state_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 180)
        self.combt_state_Chose.current(0)

        self.Btn_Ok_state = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                              , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_state.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 180)

        # ____________________________________________________________________________________________________________
        # relief
        self.l = Label(self.PanedF_Canvas_Y1, text='relief', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 220)  # y 方向每 40一间隔

        self.combt_relief_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_relief)
        self.combt_relief_Chose['values'] = \
            (
                'raised', 'sunken', 'flat', 'ridge', 'solid', 'groove'
            )
        self.combt_relief_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 220)
        self.combt_relief_Chose.current(0)

        self.Btn_Ok_relief = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                               , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_relief.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 220)

        # ____________________________________________________________________________________________________________
        # highlightcolor
        self.l = Label(self.PanedF_Canvas_Y1, text='highlight', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 260)

        self.Btn_highlightcolor = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                         command=self.More_highlightcolor)
        self.Btn_highlightcolor.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 260)

        self.Btn_Ok_highlightcolor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_highlightcolor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 260)

        self.comb_highlightcolor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15,
                                                      textvariable=self.combt_highlightcolor)
        self.comb_highlightcolor_Chose['values'] = \
            (
                'SystemWindowFrame', 'black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
            , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
            , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
            , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
            , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_highlightcolor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 260)
        self.comb_highlightcolor_Chose.current(0)

        # ____________________________________________________________________________________________________________
        # highlightbackground
        self.l = Label(self.PanedF_Canvas_Y1, text='highlight_B', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 300)

        self.Btn_highlightbackground = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                              font=('Consol', '9'), command=self.More_highlightbackground)
        self.Btn_highlightbackground.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 300)

        self.Btn_Ok_highlightcolor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                        , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_highlightcolor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 300)

        self.comb_highlightbackground_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15,
                                                           textvariable=self.combt_highlightbackground)
        self.comb_highlightbackground_Chose['values'] = \
            (
                'SystemButtonFace', 'black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
            , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
            , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
            , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
            , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_highlightbackground_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 300)
        self.comb_highlightbackground_Chose.current(0)

        # ____________________________________________________________________________________________________________
        # bitmap
        self.l = Label(self.PanedF_Canvas_Y1, text='bitmap', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 340)  # y 方向每 40一间隔

        self.comb_bitmap_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19,
                                                           textvariable=self.combt_bitmap)
        self.comb_bitmap_Chose['values'] = \
            (
                '', 'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning'
            )
        self.comb_bitmap_Chose.place(x=self.JG_X + 53, y=self.JG_Y * 7 + 340)
        self.comb_bitmap_Chose.current(0)

        self.Btn_bitmap = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                              font=('Consol', '9'),
                                              command=self.More_bitmap)
        self.Btn_bitmap.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 340)

        self.Btn_Ok_bitmap = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_bitmap.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 340)

        # ____________________________________________________________________________________________________________
        # image
        self.l = Label(self.PanedF_Canvas_Y1, text='image', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 380)  # y 方向每 40一间隔

        self.Ent_image = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_image, width=22, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_image.place(x=self.JG_X + 53, y=self.JG_Y * 7 + 380)

        self.Btn_image = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                 font=('Consol', '9'),
                                 command=self.More_image)
        self.Btn_image.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 380)

        self.Btn_Ok_image = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_image.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 380)

        # ____________________________________________________________________________________________________________
        # padx
        self.l = Label(self.PanedF_Canvas_Y1, text='padx', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 420)  # y 方向每 40一间隔

        self.combt_padx_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_padx)
        self.combt_padx_Chose['values'] = \
            (
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            )
        self.combt_padx_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 420)
        self.combt_padx_Chose.current(0)

        self.Btn_Ok_padx = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                               , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_padx.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 420)

        # ____________________________________________________________________________________________________________
        # pady
        self.l = Label(self.PanedF_Canvas_Y1, text='pady', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 460)  # y 方向每 40一间隔

        self.combt_pady_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_pady)
        self.combt_pady_Chose['values'] = \
            (
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            )
        self.combt_pady_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 460)
        self.combt_pady_Chose.current(0)

        self.Btn_Ok_pady = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                              , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_pady.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 460)

        # ____________________________________________________________________________________________________________
        # takefocus
        self.l = Label(self.PanedF_Canvas_Y1, text='takefocus', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 500)  # y 方向每 40一间隔

        self.combt_takefocus_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_takefocus,
                                                  state='readonly')
        self.combt_takefocus_Chose['values'] = \
            (
                '', 0, 1
            )
        self.combt_takefocus_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 500)
        self.combt_takefocus_Chose.current(0)

        self.Btn_Ok_takefocus = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                              , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_takefocus.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 500)

        # ____________________________________________________________________________________________________________
        # cursor
        self.l = Label(self.PanedF_Canvas_Y1, text='cursor', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 540)  # y 方向每 40一间隔

        self.combt_cursor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_cursor)
        self.combt_cursor_Chose['values'] = \
            (
                '', 'arrow', 'based_arrow_up', 'based_arrow_down', 'boat', 'bogosity', 'bottom_left_corner ', 'bottom_right_corner', 'bottom_side',
                'bottom_tee', 'box_spiral', 'center_ptr', 'circle', 'clock', 'coffee_mug', 'cross', 'cross_reverse', 'crosshair',
                'diamond_cross', 'dot', 'dotbox', 'double_arrow', 'draft_large', 'draft_small', 'draped_box', 'exchange',
                'fleur', 'gobbler', 'gumby', 'hand1', 'hand2', 'heart', 'icon', 'iron_cross', 'left_ptr', 'left_side', 'left_tee',
                'leftbutton', 'll_angle', 'lr_angle', 'man', 'middlebutton', 'mouse', 'pencil', 'pirate', 'plus', 'question_arrow',
                'right_ptr', 'right_side', 'right_tee', 'rightbutton', 'rtl_logo', 'sailboat', 'sb_down_arrow',
                'sb_h_double_arrow', 'sb_left_arrow', 'sb_right_arrow', 'sb_up_arrow', 'sb_v_double_arrow', 'shuttle',
                'sizing', 'spider', 'spraycan', 'star', 'target', 'tcross', 'top_left_arrow', 'top_left_corner', 'top_right_corner',
                'top_side', 'top_tee', 'trek', 'ul_angle', 'umbrella', 'ur_angle', 'watch', 'xterm', 'X_cursor'
            )
        self.combt_cursor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 540)
        self.combt_cursor_Chose.current(0)

        self.Btn_Ok_cursor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                   , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_cursor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 540)

        # ____________________________________________________________________________________________________________
        # container
        self.l = Label(self.PanedF_Canvas_Y1, text='container', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 580)  # y 方向每 40一间隔

        self.Ent_container = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_container, width=22, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_container.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 580)

        self.Btn_Ok_container = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_container.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 580)

        # ____________________________________________________________________________________________________________
        # 下事件框事件设置
        # ____________________________________________________________________________________________________________
        # command
        self.l = Label(self.PanedF_Canvas_Y2, text='command', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 0 + 6)  # y 方向每 40一间隔

        self.Ent_command = Entry(self.PanedF_Canvas_Y2, textvariable=self.ent_command, width=22, bg='LightCyan',
                                   foreground='Darkblue')
        self.Ent_command.place(x=self.JG_X + 80, y=6)

        self.Btn_Ok_command = Button(self.PanedF_Canvas_Y2, text='=>', width=2, height=1, font=('Consol', '9'),
                                     command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_command.place(x=246, y=6)

        # ____________________________________________________________________________________________________________
        # button_press_1
        self.ent_button_press_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click left mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 40)  # y 方向每 40一间隔

        self.Btn_button_press_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_press_1)
        self.Btn_button_press_1.place(x=220, y=6 + 40)

        # ____________________________________________________________________________________________________________
        # button_release_1
        self.ent_button_release_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Release left mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 80)  # y 方向每 40一间隔

        self.Btn_button_release_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_release_1)
        self.Btn_button_release_1.place(x=220, y=6 + 80)

        # ____________________________________________________________________________________________________________
        # button_press_right_1
        self.ent_button_press_right_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click right mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 120)  # y 方向每 40一间隔

        self.Btn_button_press_right_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_press_right_1)
        self.Btn_button_press_right_1.place(x=220, y=6 + 120)

        # ____________________________________________________________________________________________________________
        # button_press_left_2
        self.ent_button_press_left_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click left mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 160)  # y 方向每 40一间隔

        self.Btn_button_press_left_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                               font=('Consol', '10'),
                                               command=self.SJ_button_press_left_2)
        self.Btn_button_press_left_2.place(x=220, y=6 + 160)

        # ____________________________________________________________________________________________________________
        # button_press_right_2
        self.ent_button_press_right_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 160)  # y 方向每 40一间隔

        self.Btn_button_press_right_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                              font=('Consol', '10'),
                                              command=self.SJ_button_press_right_2)
        self.Btn_button_press_right_2.place(x=220, y=6 + 160)

        # ____________________________________________________________________________________________________________
        # button_press_middle_1
        self.ent_button_press_middle_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click middle mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 200)  # y 方向每 40一间隔

        self.Btn_button_press_middle_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                               font=('Consol', '10'),
                                               command=self.SJ_button_press_middle_1)
        self.Btn_button_press_middle_1.place(x=220, y=6 + 200)

        # ____________________________________________________________________________________________________________
        # button_press_middle_2
        self.ent_button_press_middle_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 240)  # y 方向每 40一间隔

        self.Btn_button_press_middle_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                font=('Consol', '10'),
                                                command=self.SJ_button_press_middle_2)
        self.Btn_button_press_middle_2.place(x=220, y=6 + 240)

        # ____________________________________________________________________________________________________________
        # button_press_left_move
        self.ent_button_press_left_move = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 240)  # y 方向每 40一间隔

        self.Btn_button_press_left_move = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                font=('Consol', '10'),
                                                command=self.SJ_button_press_left_move)
        self.Btn_button_press_left_move.place(x=220, y=6 + 240)

        # ____________________________________________________________________________________________________________
        # cursor_enter
        self.combt_cursor_enter = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Cursor enter the control area', bg='white')
        self.l.place(x=self.JG_X, y=6 + 280)  # y 方向每 40一间隔

        self.Btn_cursor_enter = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                 font=('Consol', '10'),
                                                 command=self.SJ_cursor_enter)
        self.Btn_cursor_enter.place(x=220, y=6 + 280)

        # ____________________________________________________________________________________________________________
        # cursor_leave
        self.combt_cursor_leave = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Cursor the leave control area', bg='white')
        self.l.place(x=self.JG_X, y=6 + 320)  # y 方向每 40一间隔

        self.Btn_cursor_leave = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                       font=('Consol', '10'),
                                       command=self.SJ_cursor_leave)
        self.Btn_cursor_leave.place(x=220, y=6 + 320)

        # ____________________________________________________________________________________________________________
        # get_key_focus
        self.ent_get_key_focus = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Get the focus of the keyboard', bg='white')
        self.l.place(x=self.JG_X, y=6 + 360)  # y 方向每 40一间隔

        self.Btn_get_key_focus = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                       font=('Consol', '10'),
                                       command=self.SJ_get_key_focus)
        self.Btn_get_key_focus.place(x=220, y=6 + 360)

        # ____________________________________________________________________________________________________________
        # press_a_key
        self.ent_press_a_key = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press a key of the keyboard', bg='white')
        self.l.place(x=self.JG_X, y=6 + 400)  # y 方向每 40一间隔

        self.Btn_press_a_key = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                        font=('Consol', '10'),
                                        command=self.SJ_press_a_key)
        self.Btn_press_a_key.place(x=220, y=6 + 400)

        # ____________________________________________________________________________________________________________
        # press_enter_key
        self.ent_press_enter_key = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press the enter key', bg='white')
        self.l.place(x=self.JG_X, y=6 + 440)  # y 方向每 40一间隔

        self.Btn_press_enter_key = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                      font=('Consol', '10'),
                                      command=self.SJ_press_enter_key)
        self.Btn_press_enter_key.place(x=220, y=6 + 440)

        # ____________________________________________________________________________________________________________
        # when_control_change
        self.ent_when_control_change = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='When the control change', bg='white')
        self.l.place(x=self.JG_X, y=6 + 480)  # y 方向每 40一间隔

        self.Btn_when_control_change = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                          font=('Consol', '10'),
                                          command=self.SJ_when_control_change)
        self.Btn_when_control_change.place(x=220, y=6 + 480)

        # ____________________________________________________________________________________________________________
        # control_mouseWheel
        self.ent_control_mouseWheel = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press control and mouse_wheel', bg='white')
        self.l.place(x=self.JG_X, y=6 + 520)  # y 方向每 40一间隔

        self.control_mouseWheel = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                              font=('Consol', '10'),
                                              command=self.SJ_control_mouseWheel)
        self.control_mouseWheel.place(x=220, y=6 + 520)

        # ____________________________________________________________________________________________________________
        # shift_mouseWheel
        self.ent_shift_mouseWheel = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text="Press shift and mouse_wheel", bg='white')
        self.l.place(x=self.JG_X, y=6 + 560)  # y 方向每 40一间隔

        self.Btn_shift_mouseWheel = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                          font=('Consol', '10'),
                                          command=self.SJ_shift_mouseWheel)
        self.Btn_shift_mouseWheel.place(x=220, y=6 + 560)

        # ____________________________________________________________________________________________________________
        # canva 事件绑定
        self.canva.bind("<ButtonPress-1>", self.HuoQu_Canvas_ZuoBiao)  # 绑定获取 Canvas 坐标事件
        self.canva.bind("<ButtonPress-3>", self.Button3_Press)  # 绑定获取 Canvas 坐标事件

        self.Text_BianYi.bind("<Control-MouseWheel>", self.Text_Wheel)  # 绑定获取 Text_BianYi 滚轮事件
        # 组合键之间用 - 连接，只能同时使用

        self.Scal_Y1.bind("<MouseWheel>", self.Y1_win_Wheel)
        self.Scal_Y2.bind("<MouseWheel>", self.Y2_win_Wheel)

        # 窗口位置改变事件
        self.bind("<Configure>", self.Win_Change)  # 绑定事件

    # ____________________________________________________________________________________________________________
    # 编译
    def BianYi(self):
        # 编译文本先清空
        self.Text_BianYi.delete(1.0, END)

        self.Text_BianYi.insert(END, allconfig['Str_BianYi'])
        hua = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        hua.Hua_BianYi()

    # ____________________________________________________________________________________________________________
    # 设置 设计UI窗口参数
    def Set_KouZhuan(self):
        ck = SetCK_D(self)


    # ____________________________________________________________________________________________________________
    def UI_Ban(self, value):
        Len = len(allconfig['XuanZhong'])
        self.UI_2_QuanJu()
        if Len != 0:
            self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
            self.a.UI_Ban_Design()
            # print('UI_Ban')

    def UI_Ban_Btn_OK(self):
        Len = len(allconfig['XuanZhong'])
        self.UI_2_QuanJu()
        if Len != 0:
            self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
            self.a.UI_Ban_Design()

    # ____________________________________________________________________________________________________________
    # 窗口位置改变
    def Win_Change(self, event):
        allconfig['win_X'] = self.winfo_x()
        allconfig['win_Y'] = self.winfo_y()

    # ____________________________________________________________________________________________________________
    # 全局 to UI
    def QuanJu_2_UI(self):
        # 上属性框部件设置
        self.lab_ControlType.set(allconfig['lab_ControlType'])
        self.ent_ControlName.set(allconfig['ent_ControlName'])
        self.ent_X0.set(allconfig['ent_X0'])
        self.ent_Y0.set(allconfig['ent_Y0'])
        self.ent_width.set(allconfig['ent_width'])
        self.combt_background.set(allconfig['combt_background'])
        self.ent_container.set(allconfig['ent_container'])

        if allconfig['ent_height'] != "":
            self.ent_height.set(allconfig['ent_height'])
        else:
            self.ent_height.set(0)

        if allconfig['ent_length'] != "":
            self.ent_length.set(allconfig['ent_length'])
        else:
            self.ent_length.set(0)

        if allconfig['ent_fontSize'] != "":
            self.ent_fontSize.set(allconfig['ent_fontSize'])
        else:
            self.ent_fontSize.set(0)

        if allconfig['combt_fontType'] != "":
            self.combt_fontType.set(allconfig['combt_fontType'])
        else:
            self.combt_fontType.set("")

        if allconfig['combt_foreground'] != "":
            self.combt_foreground.set(allconfig['combt_foreground'])
        else:
            self.combt_foreground.set(0)

        if allconfig['combt_anchor'] != "":
            self.combt_anchor.set(allconfig['combt_anchor'])
        else:
            self.combt_anchor.set("")

        if allconfig['combt_justify'] != "":
            self.combt_justify.set(allconfig['combt_justify'])
        else:
            self.combt_justify.set("")

        if allconfig['ent_text'] != "":
            self.ent_text.set(allconfig['ent_text'])
        else:
            self.ent_text.set("")

        if allconfig['combt_state'] != "":
            self.combt_state.set(allconfig['combt_state'])
        else:
            self.combt_state.set("")

        if allconfig['combt_relief'] != "":
            self.combt_relief.set(allconfig['combt_relief'])
        else:
            self.combt_relief.set("")

        if allconfig['combt_highlightcolor'] != "":
            self.combt_highlightcolor.set(allconfig['combt_highlightcolor'])
        else:
            self.combt_highlightcolor.set("")

        if allconfig['combt_highlightbackground'] != "":
            self.combt_highlightbackground.set(allconfig['combt_highlightbackground'])
        else:
            self.combt_highlightbackground.set("")

        if allconfig['combt_bitmap'] != "":
            self.combt_bitmap.set(allconfig['combt_bitmap'])
        else:
            self.combt_bitmap.set("")

        if allconfig['ent_image'] != "":
            self.ent_image.set(allconfig['ent_image'])
        else:
            self.ent_image.set("")

        if allconfig['combt_padx'] != "":
            self.combt_padx.set(allconfig['combt_padx'])
        else:
            self.combt_padx.set(0)

        if allconfig['combt_pady'] != "":
            self.combt_pady.set(allconfig['combt_pady'])
        else:
            self.combt_pady.set(0)

        if allconfig['combt_takefocus'] != "":
            self.combt_takefocus.set(allconfig['combt_takefocus'])
        else:
            self.combt_takefocus.set("")

        if allconfig['combt_cursor'] != "":
            self.combt_cursor.set(allconfig['combt_cursor'])
        else:
            self.combt_cursor.set("")

        if allconfig['ent_command'] != "":
            self.ent_command.set(allconfig['ent_command'])
        else:
            self.ent_command.set("")

    # ____________________________________________________________________________________________________________
    # 全局 to UI
    def UI_2_QuanJu(self):
        # 上属性框部件设置
        allconfig['lab_ControlType'] = self.lab_ControlType.get()
        allconfig['ent_ControlName'] = self.ent_ControlName.get()
        allconfig['ent_X0'] = self.ent_X0.get()
        allconfig['ent_Y0']= self.ent_Y0.get()
        allconfig['ent_width'] = self.ent_width.get()
        allconfig['ent_height'] = self.ent_height.get()
        allconfig['ent_length'] = self.ent_length.get()
        allconfig['ent_fontSize'] = self.ent_fontSize.get()
        allconfig['combt_fontType'] = self.combt_fontType.get()
        allconfig['combt_foreground'] = self.combt_foreground.get()
        allconfig['combt_background'] = self.combt_background.get()
        allconfig['combt_anchor'] = self.combt_anchor.get()
        allconfig['combt_justify'] = self.combt_justify.get()
        allconfig['ent_text'] = self.ent_text.get()
        allconfig['combt_state'] = self.combt_state.get()
        allconfig['combt_relief'] = self.combt_relief.get()
        allconfig['combt_highlightcolor'] = self.combt_highlightcolor.get()
        allconfig['combt_highlightbackground'] = self.combt_highlightbackground.get()
        allconfig['combt_bitmap'] = self.combt_bitmap.get()
        allconfig['ent_image'] = self.ent_image.get()
        allconfig['combt_padx'] = self.combt_padx.get()
        allconfig['combt_pady'] = self.combt_pady.get()
        allconfig['combt_takefocus'] = self.combt_takefocus.get()
        allconfig['combt_cursor'] = self.combt_cursor.get()
        allconfig['ent_container'] = self.ent_container.get()
        allconfig['ent_command'] = self.ent_command.get()

    # ____________________________________________________________________________________________________________
    def BianJi_OK(self):
        allconfig['each_YouJian'] = 'OK'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.OK()


    def BianJi_Move(self):
        allconfig['each_YouJian'] = 'Move'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Move()


    def BianJi_Delete(self):
        allconfig['each_YouJian'] = 'Delete'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Delete()


    def BianJi_Design(self):
        self.BianYi_Text_Design()
        allconfig['each_YouJian'] = 'Design'
        self.QuanJu_2_UI()


    def BianJi_Cancel(self):
        allconfig['each_YouJian'] = 'Cancel'
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Cancel()

    # ____________________________________________________________________________________________________________
    # 属性框处理函数
    # 滚动处理
    def Y1_win_Wheel(self, event):
        i = self.Scal_Y1.get()
        if event.delta > 0:  # 滚轮上滚
            i = i - 10
            print('i= ', i)
            self.Scal_Y1.set(i)
        else:  # 滚轮下滚
            i = i + 10
            print('i= ', i)
            self.Scal_Y1.set(i)

    def Y2_win_Wheel(self, event):
        i = self.Scal_Y2.get()
        if event.delta > 0:  # 滚轮上滚
            i = i - 5
            self.Scal_Y2.set(i)
        else:  # 滚轮下滚
            i = i + 5
            self.Scal_Y2.set(i)

    # 添加前景色
    def More_foreground(self):
        a = Choose_Color()
        b = a.Color_Choose()
        allconfig['combt_foreground'] = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加背景色
    def More_background(self):
        a = Choose_Color()
        b = a.Color_Choose()
        allconfig['combt_background'] = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 highlightcolor
    def More_highlightcolor(self):
        a = Choose_Color()
        b = a.Color_Choose()
        allconfig['combt_highlightcolor'] = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 highlightbackground
    def More_highlightbackground(self):
        a = Choose_Color()
        b = a.Color_Choose()
        allconfig['combt_highlightbackground'] = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 bitmap
    def More_bitmap(self):
        a = Get_File_Name_XBM()
        b = a.Get_Name()
        allconfig['combt_bitmap'] = b
        self.QuanJu_2_UI()

    # 添加 image
    def More_image(self):
        a = Get_File_Name_GIF()
        b = a.Get_Name()
        allconfig['ent_image'] = b
        self.QuanJu_2_UI()

    # 打开事件 button_press_1
    def SJ_button_press_1(self):
        # def SJ_Dict(self, str_SJ):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_1")

    # 打开事件 button_release_1
    def SJ_button_release_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_release_1")

    # 打开事件 button_press_right_1
    def SJ_button_press_right_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_right_1")

    def SJ_button_press_left_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_left_2")

    def SJ_button_press_right_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_right_2")

    def SJ_button_press_middle_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_middle_1")

    def SJ_button_press_middle_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_middle_2")

    def SJ_button_press_left_move(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_left_move")

    def SJ_cursor_enter(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("cursor_enter")

    def SJ_cursor_leave(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("cursor_leave")

    def SJ_get_key_focus(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("get_key_focus")

    def SJ_lose_key_focus(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("lose_key_focus")

    def SJ_press_a_key(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("press_a_key")

    def SJ_press_enter_key(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("press_enter_key")

    def SJ_when_control_change(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("when_control_change")

    def SJ_control_mouseWheel(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("control_mouseWheel")

    def SJ_shift_mouseWheel(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("shift_mouseWheel")

    # ____________________________________________________________________________________________________________
    # 属性框展开函数
    def V_P_Scal_Y1(self, value):
        self.PanedF_Canvas_Y1.place(x=48, y=0-int(value)*10)


    def V_P_Scal_Y2(self, value):
        self.PanedF_Canvas_Y2.place(x=48, y=0-int(value)*10)


    def ShuXing_Zhan(self):
        if allconfig['flag_ShuXing_Tan'] == FALSE:
            self.Btn_ShuXing_Text.set('=>')
            self.PanedWin_X1.place(x=1196, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, after=self.PanedWin_Y1)
            allconfig['flag_ShuXing_Tan'] = TRUE
            self.Btn_Update.place(x=1420, y=26)
        else:
            self.Btn_ShuXing_Text.set('<=')
            self.PanedWin_X1.place(x=2000, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
            allconfig['flag_ShuXing_Tan'] = FALSE
            self.Btn_Update.place(x=2000, y=26)

    # ____________________________________________________________________________________________________________
    # 编译文本框展开函数
    def BianYi_Text(self):
        if allconfig['flag_BianYi_Text'] == FALSE:
            self.Tv_BianYi_Text.set('Hide')
            self.PanedWin_X1.place(x=60, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
            allconfig['flag_BianYi_Text'] = TRUE
            self.Btn_Update.place(x=1420, y=26)

        elif allconfig['flag_BianYi_Text'] == TRUE:
            self.Tv_BianYi_Text.set('Text')
            self.PanedWin_X1.place(x=2000, y=50)
            allconfig['flag_BianYi_Text'] = FALSE
            self.Btn_Update.place(x=2000, y=26)

    def BianYi_Text_Design(self):
        self.Tv_BianYi_Text.set('Hide')
        self.PanedWin_X1.place(x=60, y=50)
        self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
        self.Btn_Update.place(x=1420, y=26)
        allconfig['flag_BianYi_Text'] = TRUE

    # ____________________________________________________________________________________________________________
    # Canvas 隐藏函数
    def Canva_Hide(self):
        if allconfig['flag_Canva_Hide'] == FALSE:
            self.Tv_Canva_Hide.set('Hide')
            self.canva.place(x=allconfig['canva_X'], y=allconfig['canva_Y'])
            allconfig['flag_Canva_Hide'] = TRUE

        elif allconfig['flag_Canva_Hide'] == TRUE:
            self.Tv_Canva_Hide.set('Paint')
            self.canva.place(x=2000, y=50)
            allconfig['flag_Canva_Hide'] = FALSE

    # ____________________________________________________________________________________________________________
    # Text 背景颜色设定函数

    def BianYi_Color_White(self):
        self.Text_BianYi.config(fg='black', bg='white', insertbackground='black')

    def BianYi_Color_Black(self):
        self.Text_BianYi.config(fg='white', bg='black', insertbackground='white')

    def BianYi_Color_Green(self):
        self.Text_BianYi.config(fg='white', bg='green', insertbackground='white')

    def BianYi_Color_YangPiZhi(self):
        self.Text_BianYi.config(fg='black', bg='LemonChiffon', insertbackground='black')


    # ____________________________________________________________________________________________________________
    # Text 字体大小调节函数
    def Text_font(self, value):
        Font=('Consolas',str(value))
        self.Text_BianYi.config(font=Font)

    # Text_BianYi 滚轮事件
    def Text_Wheel(self, event):
        i = self.Sca_Text_front.get()
        if event.delta > 0:  # 滚轮上滚
            i = i + 1
            self.Sca_Text_front.set(i)
        else:  # 滚轮下滚
            i = i - 1
            self.Sca_Text_front.set(i)

    # ____________________________________________________________________________________________________________
    # 右键菜单
    def Button3_Press(self, event):
        self.New_kj_menu.post(event.x_root, event.y_root)  # 必须为 (event.x_root, event.y_root) 才精准出现在点击点

    # ____________________________________________________________________________________________________________
    def HuoQu_Canvas_ZuoBiao(self, event):
        allconfig['Event_GunLun_x']= event.x
        allconfig['Event_GunLun_y'] = event.y
     

    # ____________________________________________________________________________________________________________
    # 定义画布放伸缩函数
    def HuaBuFangDa_Y(self, value):
        allconfig['scal_Y_Zhi']  = value

        self.ZhuChuangKou_BianYan_ShanChu()

        allconfig['canva_H'] = self.fram_H + int(value)
        self.canva.config(width=allconfig['canva_W'], height=allconfig['canva_H'])
        self.ent_y.set(allconfig['canva_H'])
        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    def HuaBuFangDa_X(self, value):
        allconfig['scal_X_Zhi'] = value

        self.ZhuChuangKou_BianYan_ShanChu()

        allconfig['canva_W'] = self.fram_W + int(value)
        self.canva.config(width=allconfig['canva_W'], height=allconfig['canva_H'])
        self.ent_x.set(allconfig['canva_W'])
        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    # ____________________________________________________________________________________________________________
    # 转到窗口
    def ChuangKouZhuan(self):
        self.ZhuChuangKou_BianYan_ShanChu()

        self.ScZhi_X = int(self.ent_y.get()) - self.Yuan_canva_H  # ScZhi_X 为 X方向的范围条的值
        self.ScZhi_Y = int(self.ent_x.get()) - self.Yuan_canva_W  # ScZhi_Y 为 Y方向的范围条的值

        self.vy.set(self.ScZhi_X)  # vy is the value of Sca_Y
        self.vx.set(self.ScZhi_Y)  # vx is the value of Sca_X

        allconfig['canva_H'] = int(self.ent_y.get())
        allconfig['canva_W'] = int(self.ent_x.get())

        self.canva.config(width=allconfig['canva_W'], height=allconfig['canva_H'])

        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    # ____________________________________________________________________________________________________________
    # 复位窗口
    def FuWeiKouZhuan(self):
        # 定义画布复位
        allconfig['canva_X'] = 60
        allconfig['canva_Y']  = 50
        self.ZhuChuangKou_BianYan_ShanChu()
        self.canva.place(x=allconfig['canva_X'], y=allconfig['canva_Y'])  # 此句用于复位
        self.ZhuChuangKou_BianYan()

    # ____________________________________________________________________________________________________________
    # 隐藏窗口
    def YinCang(self):
        if self.flag_BuJian_YinCang == FALSE:
            self.flag_BuJian_YinCang= TRUE
            self.Btn_YinCang_Text.set('Show')
            D = -600
            self.Lab1.place(x=D, y=0)
            self.Lab2.place(x=D, y=0)
            self.Lab_CK_X_len.place(x=D, y=0)
            self.Lab_CK_Y_len.place(x=D, y=26)
            self.Lab_font_size.place(x=D, y=760)

            self.Btn_CK_ZhuanDao.place(x=D, y=0)
            self.Btn_CK_FuWei.place(x=D, y=0)
            self.GuDing.place(x=D, y=0)
            # 
            self.Btn_WangGe.place(x=D, y=746)
            self.Btn_BianYi.place(x=D, y=600)
            self.Btn_BianYi_FuZhi.place(x=D, y=650)
            self.Btn_BianYi_ShengCheng.place(x=D, y=700)
            self.Btn_BianYi_Text.place(x=D, y=746)
            self.Btn_Canva_Hide.place(x=D, y=746)
            self.Btn_BianYi_Color_White.place(x=D, y=746)
            self.Btn_BianYi_Color_Black.place(x=D, y=746)
            self.Btn_BianYi_Color_YangPiZhi.place(x=D, y=746)
            self.Btn_BianYi_Color_Green.place(x=D, y=746)
            self.Btn_CK_Set.place(x=D, y=26)
            # 

            self.Ent_X.place(x=D, y=0)
            self.Ent_Y.place(x=D, y=26)

            self.Sca_Y.place(x=D, y=40)
            self.Sca_X.place(x=D, y=0)
            self.Sca_Text_front.place(x=D, y=739)

        else:
            self.flag_BuJian_YinCang = FALSE
            self.Btn_YinCang_Text.set('Hide')
            self.Lab1.place(x=0, y=0)
            self.Lab2.place(x=60, y=0)
            self.Lab_CK_X_len.place(x=620, y=0)
            self.Lab_CK_Y_len.place(x=620, y=26)
            self.Lab_font_size.place(x=1250, y=760)

            self.Btn_CK_ZhuanDao.place(x=762, y=0)
            self.Btn_CK_FuWei.place(x=762, y=26)
            self.GuDing.place(x=0, y=746)
            # 
            self.Btn_WangGe.place(x=420, y=746)
            self.Btn_BianYi.place(x=6, y=600)
            self.Btn_BianYi_FuZhi.place(x=6, y=650)
            self.Btn_BianYi_ShengCheng.place(x=6, y=700)
            self.Btn_BianYi_Text.place(x=60, y=746)
            self.Btn_Canva_Hide.place(x=120, y=746)
            self.Btn_BianYi_Color_White.place(x=180, y=746)
            self.Btn_BianYi_Color_Black.place(x=240, y=746)
            self.Btn_BianYi_Color_YangPiZhi.place(x=300, y=746)
            self.Btn_BianYi_Color_Green.place(x=360, y=746)
            self.Btn_CK_Set.place(x=826, y=26)
            # 

            self.Ent_X.place(x=710, y=0)
            self.Ent_Y.place(x=710, y=26)

            self.Sca_Y.place(x=0, y=40)
            self.Sca_X.place(x=100, y=0)
            self.Sca_Text_front.place(x=1328, y=739)

    # ____________________________________________________________________________________________________________
    # 固定窗口
    def GuDingChuangKou(self):
        if allconfig['flag_CK_GuDing'] == FALSE:
            allconfig['flag_CK_GuDing'] = TRUE
            self.GuDing_Text.set('Unluck')
        else:
            allconfig['flag_CK_GuDing'] = FALSE
            self.GuDing_Text.set('Luck')

    # ____________________________________________________________________________________________________________
    # 网格开
    def WG_Kai(self):
        # 参数设定
        allconfig['WangGe_ShuMu_X']  = (allconfig['canva_H'] - self.bar_W) / allconfig['WangGe_KuanDu']
        allconfig['WangGe_ShuMu_Y'] = allconfig['canva_W'] / allconfig['WangGe_KuanDu']

        # 下面画网格
        for i in range(0, int(allconfig['WangGe_ShuMu_X']), 1):
            self.it_WangGe = self.canva.create_line(0, self.bar_W + allconfig['WangGe_KuanDu']  * i, allconfig['canva_W'],
                                               self.bar_W + allconfig['WangGe_KuanDu']  * i,
                                               fill=self.WangGe_YanSe, width=0.1)
            self.canva.itemconfig(self.it_WangGe, tags='WG')
            self.canva.lower(self.it_WangGe)

        for i in range(0, int(allconfig['WangGe_ShuMu_Y']), 1):
            self.it_WangGe = self.canva.create_line(allconfig['WangGe_KuanDu']  + allconfig['WangGe_KuanDu']  * i, self.bar_W,
                                               allconfig['WangGe_KuanDu']  + allconfig['WangGe_KuanDu']  * i, allconfig['canva_H'],
                                               fill=self.WangGe_YanSe, width=0.1)
            self.canva.itemconfig(self.it_WangGe, tags='WG')
            self.canva.lower(self.it_WangGe)

    # ____________________________________________________________________________________________________________
    # 网格关
    def WG_Gun(self):
        self.canva.delete('WG')  # 删除所有具有标签'WG'的项目

    # ____________________________________________________________________________________________________________
    # 启用网格
    def QiYong_WangGe(self):
        if self.flag_WangGe == FALSE:
            self.flag_WangGe = TRUE
            self.Btn_WG_Text.set('G_Off')
            self.WG_Kai()

        else:
            self.flag_WangGe = FALSE
            self.Btn_WG_Text.set('G_On')
            self.WG_Gun()

    # ____________________________________________________________________________________________________________
    # 画主窗口边沿
    def ZhuChuangKou_BianYan(self):
        # 画外边框
        self.it1 = self.canva.create_rectangle(2, allconfig['canva_H'] - 1, allconfig['canva_W'] - 1, 2)
        # 画标题栏框
        self.it2 = self.canva.create_rectangle(2, self.bar_W, allconfig['canva_W'] - 1, self.bar_W,
                                               fil=self.ChuangKou_BiaoTiLan_YanSe)
        # 画标题
        self.it_BiaoTi = self.canva.create_text(43, 16, text=self.BiaoTi_Text,
                                                font=('Consol', 11),
                                                fill=self.BiaoTi_Text_YanSe)

        # 画标题栏按钮
        self.it_BiaoTi_AnNiu_ZuiXiao = self.canva.create_text(allconfig['canva_W'] - 116, 16, text='—',
                                                              font=('Consol', 11),
                                                              fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_ZuiDa = self.canva.create_text(allconfig['canva_W'] - 70, 16, text='□',
                                                            font=('Consol', 11),
                                                            fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_GuanBi = self.canva.create_text(allconfig['canva_W'] - 28, 16, text='X',
                                                             font=('Helvetica', 11),
                                                             fill=self.BiaoTi_Text_YanSe)

    # ____________________________________________________________________________________________________________
    # 删除主窗口边沿
    def ZhuChuangKou_BianYan_ShanChu(self):
        if allconfig['flag_Menu_Kai'] == TRUE:
            self.canva.delete(self.it_Menu)

        self.canva.delete(self.it1)
        self.canva.delete(self.it2)
        self.canva.delete(self.it_BiaoTi)
        self.canva.delete(self.it_BiaoTi_AnNiu_ZuiXiao)
        self.canva.delete(self.it_BiaoTi_AnNiu_ZuiDa)
        self.canva.delete(self.it_BiaoTi_AnNiu_GuanBi)

    # ____________________________________________________________________________________________________________
    # 画布移动
    def HuaBu_YiDong(self):
        # 鼠标中键按下事件
        def paint1(event):
            self.x1 = event.x
            self.y1 = event.y
            self.flag_SongKai = FALSE
            self.canva.config(cursor='fleur')

        # 鼠标中键松开事件
        def paint2(event):
            self.flag_SongKai = TRUE
            self.canva.config(cursor='arrow')

        # 鼠标中键按下并移动事件
        def paint3(event):
            self.x2 = event.x
            self.y2 = event.y
            if self.flag_SongKai == FALSE:
                if allconfig['flag_CK_GuDing'] == FALSE:
                    self.canva.place(x=allconfig['canva_X'] + (self.x2 - self.x1), y=allconfig['canva_Y']  + (self.y2 - self.y1))
                    # 重新定义画布位置
                    allconfig['canva_X'] = allconfig['canva_X'] + (self.x2 - self.x1)
                    allconfig['canva_Y']  = allconfig['canva_Y']  + (self.y2 - self.y1)

        # 画布控件与鼠标左键进行绑定
        self.canva.bind("<ButtonPress-2>", paint1)  # 绑定鼠标按下事件
        self.canva.bind("<ButtonRelease - 2>", paint2)  # 绑定鼠标松开事件
        self.canva.bind("<B2-Motion>", paint3)  # 绑定鼠标移动事件


    # ____________________________________________________________________________________________________________
    # 主菜单功能函数定义
    def Hua_Button(self):
        allconfig['DangQian_KJ_name'] = 'Button ' + str(allconfig['button1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('button1')
        a.Hua_Button()


    def Hua_Canvas(self):
        allconfig['DangQian_KJ_name'] = 'Canvas ' + str(allconfig['canvas1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('canvas1')
        a.Hua_Canvas()


    def Hua_Checkbutton(self):
        allconfig['DangQian_KJ_name']  = 'Checkbutton ' + str(allconfig['checkbutton1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('checkbutton1')
        a.Hua_Checkbutton()


    def Hua_Combobox(self):
        allconfig['DangQian_KJ_name']  = 'Combobox ' + str(allconfig['combobox1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('combobox1')
        a.Hua_Combobox()


    def Hua_Entry(self):
        allconfig['DangQian_KJ_name']  = 'Entry ' + str(allconfig['entry1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('entry1')
        a.Hua_Entry()


    def Hua_Frame(self):
        allconfig['DangQian_KJ_name']  = 'Frame ' + str(allconfig['frame1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('frame1')
        a.Hua_Frame()


    def Hua_Label(self):
        allconfig['DangQian_KJ_name']  = 'Label ' + str(allconfig['label1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('label1')
        a.Hua_Label()


    def Hua_LabelFrame(self):
        allconfig['DangQian_KJ_name']  = 'LabelFrame ' + str(allconfig['labelFrame1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('labelFrame1')
        a.Hua_LabelFrame()


    def Hua_Listbox(self):
        allconfig['DangQian_KJ_name']  = 'Listbox ' + str(allconfig['listbox1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('listbox1')
        a.Hua_Listbox()


    def Hua_Menu(self):
        allconfig['DangQian_KJ_name']  = 'Menu ' + str(allconfig['menu1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('menu1')
        a.Hua_Menu()


    def Hua_Message(self):
        allconfig['DangQian_KJ_name']  = 'Message ' + str(allconfig['message1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('message1')
        a.Hua_Message()


    def Hua_PanedWindow(self):
        allconfig['DangQian_KJ_name']  = 'PanedWindow ' + str(allconfig['frame1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('panedWindow1')
        a.Hua_PanedWindow()


    def Hua_Radiobutton(self):
        allconfig['flag_RadBtn_Zu'] = FALSE
        allconfig['Radiobutton_i']  = 0
        allconfig['DangQian_KJ_name']  = 'Radiobutton ' + str(allconfig['radiobutton1_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('radiobutton1')
        a.Hua_Radiobutton()


    def Hua_Scale_X(self):
        allconfig['DangQian_KJ_name'] = 'Scale_X ' + str(allconfig['scale1_x_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('scale1_x')
        a.Hua_Scale_X()


    def Hua_Scale_Y(self):
        allconfig['DangQian_KJ_name']  = 'Scale_Y ' + str(allconfig['scale1_y_i'] + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('scale1_y')
        a.Hua_Scale_Y()


    def Hua_Spinbox(self):
        allconfig['DangQian_KJ_name']  = 'Spinbox ' + str(allconfig['spinbox1_i']   + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('spinbox1')
        a.Hua_Spinbox()


    def Hua_Text(self):
        allconfig['DangQian_KJ_name']  = 'Text ' + str(allconfig['text1_i']    + 1)
        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('text1')
        a.Hua_Text()


    def Hua_Toplevel(self):
        pass

    def Hua_tkMessageBox(self):
        pass


# ____________________________________________________________________________________________________________
# 画基本图形类
class Hua:
    def __init__(self, Canva_1, Menu_1, Text_1):
        self.Text_1 = Text_1
        self.BianJi_kj_menu = Menu_1
        self.canva = Canva_1
        self.front_BiLi = 20
        self.Text_YanSe = 'black'
        self.fill_YanSe = 'white'
        self.OutLine_YanSe = 'Aqua'
        self.Kuan_width = 2
        self.flag_WanCheng1 = FALSE
        self.flag_FuZuKuang = FALSE

        self.bg_Canvas_YanSe = 'LightCyan'
        self.bg_Entry_YanSe = 'Aqua'
        self.bg_Spinbox_YanSe = 'Aqua'
        self.bg_Listbox_YanSe = 'AquaMarine'

        self.bg_Canvas_YanSe = 'LightCyan'
        self.bg_Text_YanSe = 'LightCyan'

        self.list_name = StringVar()

        self.bar_W = allconfig['bar_W']
        self.Zi_Menu_Shu = 0


    # 
    def Hua_Button(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                 
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Button = Button(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10), width=7, height=1)
                self.it_Button.place(x=self.X0, y=self.Y0)
                # self.it_Button.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Button.config(width=W, height=H)

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 50
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Canvas(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                 
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Canva = Canvas(self.canva, bg=self.bg_Canvas_YanSe, width=100, height=80)
                self.it_Canva.place(x=self.X0, y=self.Y0)

                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=allconfig['DangQian_KJ_name'] , fill='DeepSkyBlue')

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                 
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Canva.config(width=W, height=H)

                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=allconfig['DangQian_KJ_name'] , fill='DeepSkyBlue')

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 80

                self.it_Canva.delete(self.it_Canva_name_Text)
                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=allconfig['DangQian_KJ_name'] , fill='DeepSkyBlue')
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Checkbutton(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                 
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Checkbutton = Checkbutton(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10),
                                                  width=12, height=1)

                self.it_Checkbutton.place(x=self.X0, y=self.Y0)

                self.it_Checkbutton.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.3)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Checkbutton.config(width=W, height=H)
                # self.it_Checkbutton.place(x=self.X1, y=self.Y1)

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 20
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Combobox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                list_name = StringVar()
                self.it_Combobox = ttk.Combobox(self.canva, text=list_name, font=('TkDefaultFont', 10),  width=12, height=2)
                self.it_Combobox["values"] = ('Combobox', 1)
                self.it_Combobox.current(0)
                self.it_Combobox.place(x=self.X0, y=self.Y0)
                self.it_Combobox.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.6)
                H = int(abs(self.Y1 - self.Y0)/15.26)

                self.it_Combobox.config(width=W, height=H)
                self.it_Combobox.place(x=self.X0, y=self.Y0)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 90
                    self.Y1 = self.Y0 + 5

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Entry(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                entry_Text = StringVar()
                entry_Text.set(allconfig['DangQian_KJ_name'] )
                self.it_Entry = Entry(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10), width=10, bg=self.bg_Entry_YanSe)
                self.it_Entry.place(x=self.X0, y=self.Y0)
                self.it_Entry.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)

                self.it_Entry.config(width=W)
                self.it_Entry.place(x=self.X0, y=self.Y0)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 70
                    self.Y1 = self.Y0 + 20

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Frame(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Frame = Frame(self.canva,  width=100, height=60)
                self.it_Frame.place(x=self.X0, y=self.Y0)
                self.it_Frame.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Frame.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 60
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Label(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Label = Label(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10), width=0, height=0)
                self.it_Label.place(x=self.X0, y=self.Y0)
                self.it_Label.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.Text = allconfig['DangQian_KJ_name'] 

                self.X1 = event.x
                self.Y1 = event.y
                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Label.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 40
                    self.Y1 = self.Y0 + 10

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_LabelFrame(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y

                self.canva.config(cursor='crosshair')

                # LabelFrame 无 textvariable 属性
                self.it_LabelFrame = LabelFrame(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10), width=100, height=60)
                self.it_LabelFrame.place(x=self.X0, y=self.Y0)
                self.it_LabelFrame.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.Text = allconfig['DangQian_KJ_name'] 

                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_LabelFrame.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 60
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Listbox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                # Listbox 无 textvariable 或 text 属性
                self.it_Listbox = Listbox(self.canva, bg=self.bg_Listbox_YanSe, font=('TkDefaultFont', 10), width=12, height=3)
                self.it_Listbox.place(x=self.X0, y=self.Y0)
                self.it_Listbox.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.Text = allconfig['DangQian_KJ_name'] 

                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/14)

                self.it_Listbox.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 60
                    self.Y1 = self.Y0 + 60
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    def Hua_Menu_Tuo(self):
        self.list_name.set('')
        self.btn_name.set('')
        self.it_ShuRu_Entry.place(x=3, y=2)
        self.it_List_ShuRu_Entry.place(x=180, y=2)

        def X_add():
            self.Ent_X = StringVar()

            if allconfig['zi_menu1_sum'] != 0:
                YinChang_List(allconfig['zi_menu1_num_i'])

            if self.btn_name.get() != '':  # Entry 空时用 '' 表示
                allconfig['zi_menu1_num_i']  = allconfig['zi_menu1_num_i']  + 1
                allconfig['zi_menu1_sum'] = allconfig['zi_menu1_sum']     + 1
                allconfig['DQ_ZhuMenu_ZiXiang_Num_i'] = allconfig['zi_menu1_num_i'] 

                self.Ent_X.set(self.btn_name.get())

                # ____________________________________________________________________________________________________________
                num = allconfig['zi_menu1_num_i']  # 华文琥珀  微软雅黑
                self.it_X_add_Btn_New = Button(self.frame, textvariable=self.Ent_X, relief=FLAT, height=1,
                                               font=('TkDefaultFont', 8), command=lambda: XianShi_ListBox(num_i=num))
                self.it_X_add_Btn_New.grid(row=1, column = allconfig['zi_menu1_num_i'] + 1)
                self.it_X_add_Btn_New.lift()

                width = int((self.it_X_add_Btn_New.winfo_reqwidth()))

                # ____________________________________________________________________________________________________________
                allconfig['DQ_Zong_Len'] = 0
                if allconfig['zi_menu1_num_i']  > 1:
                    for i in range(1, allconfig['zi_menu1_num_i'] , 1):
                        if i not in allconfig['Menu1_Delete_Num']:
                            len_name = "Len" + str(i)
                            allconfig['DQ_Zong_Len'] = allconfig['DQ_Zong_Len'] + allconfig['Menu1_Son_Len'][len_name][1]
                else:
                    allconfig['DQ_Zong_Len'] = 0

                self.it_Y_add_Listbox_new = Listbox(self.canva, bg='SystemButtonFace')
                self.it_Y_add_Listbox_new.place(x=3 + allconfig['DQ_Zong_Len'], y=self.bar_W + 20)  # 画布坐标是控件的 7 倍
                self.it_Y_add_Listbox_new.lift()

                len_name = "Len" + str(allconfig['zi_menu1_num_i'])
                allconfig['Menu1_Son_Len'][len_name] = (allconfig['zi_menu1_num_i'], width)
                # ____________________________________________________________________________________________________________
                # 设置字典
                # 0： self.it_X_add_Btn_New      菜单标题按钮
                # 1： allconfig['zi_menu1_num_i']                菜单标题按钮的 序号
                # 2： self.it_Y_add_Listbox_new  菜单标题按钮对应的下拉列表
                # 3： self.Ent_X.get()           菜单标题按钮的 输入标题

                D_Menu_Btn_name = 'Menu_Btn' + str(allconfig['zi_menu1_num_i'])
                allconfig['D_ZhuMenu'][D_Menu_Btn_name] = (self.it_X_add_Btn_New, allconfig['zi_menu1_num_i'] , self.it_Y_add_Listbox_new,
                                              self.Ent_X.get())

                # ____________________________________________________________________________________________________________
                # 录入代码
                Menubar = "Menubar"

                zi_menu_name = "zi_menu_name" + str(allconfig['zi_menu1_num_i'])
                allconfig['Menu1'][zi_menu_name] = (str(self.Ent_X.get()) + "_menu").strip()

                zi_menu_tearoff_name = "zi_menu_tearoff_name" + str(allconfig['zi_menu1_num_i'])
                zi_menu_add_cascade_name = "zi_menu_add_cascade_name" + str(allconfig['zi_menu1_num_i'])

                Menu_Code1 = str(allconfig['Menu1'][zi_menu_name]) + " = Menu(" + Menubar + ", tearoff=0)"
                Menu_Code2 = Menubar + ".add_cascade(label='" + str(self.Ent_X.get()) + "', menu=" + str(allconfig['Menu1'][zi_menu_name]) + ")"

                allconfig['Menu1'][zi_menu_tearoff_name] = (Menu_Code1, allconfig['zi_menu1_num_i'] )
                allconfig['Menu1'][zi_menu_add_cascade_name] = (Menu_Code2, allconfig['zi_menu1_num_i'] )

                print(allconfig['Menu1'][zi_menu_tearoff_name][0])
                print(allconfig['Menu1'][zi_menu_add_cascade_name][0])

                # ____________________________________________________________________________________________________________
                # 屏蔽之前的 List
                if allconfig['zi_menu1_num_i']  > 1:
                    for i in range(1, allconfig['zi_menu1_num_i'] , 1):
                        if i not in allconfig['Menu1_Delete_Num']:
                            a = allconfig['D_ZhuMenu']['Menu_Btn' + str(i)]
                            a[2].place(x=-600, y=self.bar_W + 30)

                # ____________________________________________________________________________________________________________
                # 清空以备下次输入
                self.btn_name.set('')

        def XianShi_ListBox(num_i):
            allconfig['DQ_ZhuMenu_ZiXiang_Num_i'] = num_i   # 定义当前按下的子按钮标号
            L = 0

            # len_name = "Len" + str(allconfig['zi_menu1_num_i'])
            # allconfig['Menu1_Son_Len'][len_name] = (allconfig['zi_menu1_num_i'], width)
            for i in range(1, num_i, 1):
                if i not in allconfig['Menu1_Delete_Num']:
                    len_name = "Len" + str(i)
                    L = L + allconfig['Menu1_Son_Len'][len_name][1]
                    print("L = ", L)

            name_menu = 'Menu_Btn' + str(num_i)

            print("num_i = ", num_i)

            a = allconfig['D_ZhuMenu'][name_menu]
            # 重新复位
            a[2].place(x=3 + L, y=self.bar_W + 20)  # 字典内的列表下表由 0 开始

            print("zi_menu1_sum = ", allconfig['zi_menu1_sum']    )

            for i_Num in range(1, allconfig['zi_menu1_num_i'] +1, 1):
                if (i_Num != num_i) and (i_Num not in allconfig['Menu1_Delete_Num']):
                    name1 = 'Menu_Btn' + str(i_Num)
                    a = allconfig['D_ZhuMenu'][name1]
                    a[2].place(x=-600, y=self.bar_W + 30)


        def X_delet():
            if allconfig['zi_menu1_sum'] != 0:
                if allconfig['DQ_ZhuMenu_ZiXiang_Num_i'] == allconfig['zi_menu1_sum']    :
                    allconfig['DQ_ZhuMenu_ZiXiang_Num_i'] = allconfig['DQ_ZhuMenu_ZiXiang_Num_i'] - 1

                # D_Menu_Btn_name = 'Menu_Btn' + str(allconfig['zi_menu1_num_i'])
                D_Menu_Btn_name = 'Menu_Btn' + str(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
                a = allconfig['D_ZhuMenu'][D_Menu_Btn_name]

                allconfig['Menu1_Delete_Num'].append(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])

                a[0].destroy()  # 0： self.it_X_add_Btn_New  菜单标题按钮
                a[2].destroy()  # 2： self.it_Y_add_Listbox_new  菜单标题按钮对应的下拉列表

                del allconfig['D_ZhuMenu'][D_Menu_Btn_name]
                allconfig['zi_menu1_sum'] = allconfig['zi_menu1_sum'] - 1


        def YinChang_List(i):
            if i not in allconfig['Menu1_Delete_Num']:
                name1 = 'Menu_Btn' + str(i)
                a = allconfig['D_ZhuMenu'][name1]
                a[2].place(x=-600, y=self.bar_W + 30)


        def YinChang_Entry():
            self.it_ShuRu_Entry.place(x=-600, y=0)
            self.it_List_ShuRu_Entry.place(x=-600, y=0)


        def YinChang_All():
            YinChang_List(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
            YinChang_Entry()


        def Y_add(flag):
            Str_Insert = ''

            if flag == "text":
                Str_Insert = allconfig['tap'] + str(self.list_name.get())
            elif flag == "separator":
                Str_Insert = '-----------------------------------------------------------------------------'

            if allconfig['zi_menu1_sum'] != 0:
                D_Menu_Btn_name = 'Menu_Btn' + str(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
                a = allconfig['D_ZhuMenu'][D_Menu_Btn_name]

                DQ_Listbox = a[2]
                zong = DQ_Listbox.size()

                if zong == 0:
                    DQ_Listbox.insert(END, Str_Insert)
                if zong > 0:
                    if a[2].curselection() == ():
                        DQ_Listbox.insert(END, Str_Insert)
                    else:
                        DQ_i = a[2].curselection()
                        DQ_Listbox.insert(DQ_i, Str_Insert)

                # ____________________________________________________________________________________________________________
                # 录入代码
                zi_menu_name = "zi_menu_name" + str(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
                Code_Insert = ''
                # ____________________________________________________________________________________________________________
                if flag == "text":
                    Code_Insert = str(allconfig['Menu1'][zi_menu_name]) + ".add_command(label='" + \
                                  str(self.list_name.get()) + "', command='')"
                elif flag == "separator":
                    Code_Insert = str(allconfig['Menu1'][zi_menu_name]) + ".add_separator()"

                # ____________________________________________________________________________________________________________

                if zong == 0:
                    menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(1)
                    allconfig['Menu1_ListCode'][menu_list_code_name] = (Code_Insert, allconfig['DQ_ZhuMenu_ZiXiang_Num_i'], 1)
                    print(Menu1_ListCode[menu_list_code_name][0])

                if zong > 0:
                    if a[2].curselection() == ():
                        menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(zong + 1)
                        allconfig['Menu1_ListCode'][menu_list_code_name] = (Code_Insert, allconfig['DQ_ZhuMenu_ZiXiang_Num_i'], zong + 1)
                        print(Menu1_ListCode[menu_list_code_name][0])

                    else:
                        # 按下后当前选定选项向后偏移一个
                        A = a[2].curselection()  # a[3].curselection() 是一个单值元组 为 (索引值,)
                        DQ_Listbox_i = A[0]   # A[0] 从 0 开始

                        # for 循环重新排列大于 int(DQ_Listbox_i) 项对应代码
                        # listbox 可以 get() 不能 set()
                        # *****************************************************************************************
                        D = {}  # 备用记录字典
                        for i in range(1, zong+1, 1):  # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
                            name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                            D[str(i)] = allconfig['Menu1_ListCode'][name]

                        for i in range(int(DQ_Listbox_i)+1, zong+2, 1):
                            name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                            allconfig['Menu1_ListCode'][name] = D[str(i-1)]

                        # ____________________________________________________________________________________________________________
                        # 关键代码
                        menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(int(DQ_Listbox_i))
                        allconfig['Menu1_ListCode'][menu_list_code_name] = (Code_Insert, allconfig['zi_menu1_sum'], int(DQ_Listbox_i))

                        print(Menu1_ListCode[menu_list_code_name][0])
                        # ____________________________________________________________________________________________________________
                        for i in range(1, zong + 2, 1):
                            name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                            print("allconfig['Menu1'][name] = ", allconfig['Menu1'][name][0], 'i = ', i)

        # ____________________________________________________________________________________________________________
        def Y_delet():
            D_Menu_Btn_name = 'Menu_Btn' + str(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
            a = allconfig['D_ZhuMenu'][D_Menu_Btn_name]
            DQ_Listbox = a[2]
            zong = DQ_Listbox.size()

            if zong > 0:
                # 录入代码
                zi_menu_name = "zi_menu_name" + str(allconfig['DQ_ZhuMenu_ZiXiang_Num_i'])
                if zong == 0:
                    DQ_Listbox.delete(END)

                    menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(zong)
                    del allconfig['Menu1_ListCode'][menu_list_code_name]

                if zong > 0:
                    if a[2].curselection() == ():
                        DQ_Listbox.delete(END)

                        menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(zong)
                        del allconfig['Menu1_ListCode'][menu_list_code_name]
                        print("del allconfig['Menu1'][menu_list_code_name] **************************")

                    else:
                        DQ_i = a[2].curselection()  # a[3].curselection() 是一个单值元组 为 (索引值,)
                        DQ_Listbox_i = DQ_i[0]  # A[0] 从 0 开始
                        DQ_Listbox.delete(DQ_i)  # 删除选定列表项

                        print('D = {}  # 备用记录字典')
                        D = {}  # 备用记录字典
                        # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
                        for i in range(1, zong + 1, 1):
                            name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                            D[str(i)] = allconfig['Menu1_ListCode'][name]

                        for i in range(int(DQ_Listbox_i)+1, zong, 1):
                            name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                            allconfig['Menu1_ListCode'][name] = D[str(i + 1)]

                        # ____________________________________________________________________________________________________________
                        # 关键代码
                        menu_list_code_name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(zong)
                        del allconfig['Menu1_ListCode'][menu_list_code_name]
                        # ____________________________________________________________________________________________________________

                for i in range(1, zong, 1):
                    name = str(allconfig['Menu1'][zi_menu_name]) + "_list_" + str(i)
                    print("allconfig['Menu1'][name] = ", allconfig['Menu1_ListCode'][name], 'i = ', i)

        # ____________________________________________________________________________________________________________
        Font = ('TkDefaultFont', 8)
        if self.YiCi == FALSE:
            self.it_Y_add_Btn = Button(self.frame, text='+Y', width=3, bg='yellow', fg='blue',
                                       font=Font, command=lambda: Y_add(flag="text"))

            self.it_Y_delet_Btn = Button(self.frame, text='-Y', width=3, bg='red', fg='white',
                                       font=Font,  command=Y_delet)

            self.it_X_add_Btn = Button(self.frame, text='+X', width=3, bg='yellow', fg='blue',
                                       font=Font, command=X_add)

            self.it_X_delet_Btn = Button(self.frame, text='-X', width=3, bg='red', fg='white',
                                       font=Font,  command=X_delet)

            self.Separator_Btn = Button(self.frame, text='----', width=3, bg='lightblue', fg='white',
                                       font=Font, command=lambda: Y_add(flag="separator"))

            self.YinCang_Btn = Button(self.frame, text='C', width=3, bg='blue', fg='white',
                                       font=Font, command=YinChang_All)
            self.YiCi = TRUE

        self.it_X_add_Btn.grid(row=1, column=1001)
        self.it_X_delet_Btn.grid(row=1, column=1002)
        self.it_Y_add_Btn.grid(row=1, column=1003)
        self.it_Y_delet_Btn.grid(row=1, column=1005)
        self.Separator_Btn.grid(row=1, column=1004)
        self.YinCang_Btn.grid(row=1, column=1006)

        self.it_X_add_Btn.lift()
        self.it_X_delet_Btn.lift()
        self.it_Y_add_Btn.lift()
        self.it_Y_delet_Btn.lift()
        self.YinCang_Btn.lift()
        self.Separator_Btn.lift()
        # self.it_Y_add_Btn.place(x=3, y=self.bar_W + 2 + 28)

    def Hua_Menu(self):
        if self.flag_WanCheng1 == FALSE:
            def paint_AnXia(event):
                self.YiCi = FALSE
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                if allconfig['flag_Menu_Kai'] == FALSE:
                    self.frame = Frame(self.canva, width=380, height=28)
                    self.frame.place(x=3, y=self.bar_W + 2)

                    self.btn_name = StringVar()
                    self.btn_name.set('Menu title input')

                    self.list_name = StringVar()
                    self.list_name.set('Title list input')

                    self.it_ShuRu_Entry = Entry(self.canva, textvariable=self.btn_name, font=('微软雅黑', 10),
                                                bg='DeepSkyBlue', width=20)

                    self.it_List_ShuRu_Entry = Entry(self.canva, textvariable=self.list_name, font=('微软雅黑', 10),
                                                bg='LightBlue', width=20)

                    self.it_Button_Menu = Button(self.frame, text='Edit', width=6, bg='LightGreen',
                                                 font=('TkDefaultFont', 8), command=self.Hua_Menu_Tuo)  # 此处调用函数时，不要加()，加()后，是调用+执行

                    self.it_Button_Menu.grid(row=1, column=100)
                    self.it_ShuRu_Entry.place(x=3, y=2)
                    self.it_List_ShuRu_Entry.place(x=180, y=2)

                    self.it_Button_Menu.lift()
                    allconfig['flag_Menu_Kai'] = TRUE


            def paint_YiDong(event):
                self.Text = allconfig['DangQian_KJ_name'] 


            def paint_ShiFang(event):
                self.X0 = 0
                self.Y0 = 0
                self.X1 = 0
                self.Y1 = 0
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Hua_Message(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                # 再引入 tkinter.messagebox 后，Message定义前面要加上 tk. ，避免冲突
                self.it_Message = tk.Message(self.canva, text=allconfig['DangQian_KJ_name'] , font=('TkDefaultFont', 10), width=100)
                self.it_Message.place(x=self.X0, y=self.Y0)
                self.it_Message.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y
                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                # H = int(abs(self.Y1 - self.Y0))  # Message 无 height属性
                self.it_Message.config(width=W)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 80
                    self.Y1 = self.Y0 + 10
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Hua_PanedWindow(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_PanedWindow = PanedWindow(self.canva, width=100, height=60)
                self.it_PanedWindow.place(x=self.X0, y=self.Y0)
                self.it_PanedWindow.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_PanedWindow.config(width=W, height=H)


            def paint_ShiFang(event):
                self.X1 = self.X0 + 100
                self.Y1 = self.Y0 + 65

                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()


            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Hua_Radiobutton(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                if allconfig['flag_RadBtn_Zu'] == FALSE:
                    self.varInt = IntVar()
                    self.varInt.set(0)
                    allconfig['flag_RadBtn_Zu'] = TRUE


                print('varInt = ', self.varInt)
                self.it_Radiobutton = Radiobutton(self.canva, variable=self.varInt, text='Radiobutton',
                                                  font=('TkDefaultFont', 10), value= allconfig['Radiobutton_i'])

                self.it_Radiobutton.place(x=self.X0, y=self.Y0)
                self.it_Radiobutton.lower()

                print("allconfig['Radiobutton_i'] = ",  allconfig['Radiobutton_i'])
                allconfig['Radiobutton_i']  = allconfig['Radiobutton_i']  + 1

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.6)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Radiobutton.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 90
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________

    def Hua_Scale_X(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Scale_X = Scale(self.canva, orient=HORIZONTAL, font=('TkDefaultFont', 10))
                self.it_Scale_X.place(x=self.X0, y=self.Y0)
                self.it_Scale_X.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Scale_X.config(width=H-23, length=W)

                # ******************************************************************************************
                if self.flag_FuZuKuang == TRUE:
                    self.canva.itemconfig(self.it_Kuan, tags='Hua_Kuang_ing')
                # ******************************************************************************************

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 40
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________

    def Hua_Scale_Y(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Scale_Y = Scale(self.canva, font=('TkDefaultFont', 10))
                self.it_Scale_Y.place(x=self.X0, y=self.Y0)
                self.it_Scale_Y.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Scale_Y.config(width=W-26, length=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 50
                    self.Y1 = self.Y0 + 100
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________

    def Hua_Spinbox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                 

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Spinbox = Spinbox(self.canva, values=(allconfig['DangQian_KJ_name'] , 1, 2, 3), font=('TkDefaultFont', 10),
                                          bg=self.bg_Spinbox_YanSe)
                self.it_Spinbox.place(x=self.X0, y=self.Y0)
                self.it_Spinbox.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.2)
                # H = int(abs(self.Y1 - self.Y0))

                self.it_Spinbox.config(width=W)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 200
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________

    def Hua_Text(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                 

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Text = Text(self.canva, bg=self.bg_Text_YanSe, font=('TkDefaultFont', 10), width=20, height=6)
                self.it_Text.insert(END, allconfig['DangQian_KJ_name'] )
                self.it_Text.place(x=self.X0, y=self.Y0)
                self.it_Text.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Text.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 145
                    self.Y1 = self.Y0 + 80
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    # 完成后
    def WanCheng(self):
        self.flag_WanCheng1 = TRUE

        def paint_AnXia(event):
            self.Yanse_HuiFu()  # 每次按下颜色都要恢复到原来的状态

            allconfig['XuanZhong'].clear()
            allconfig['XuanZhong_sum'] = 0

            allconfig['Event_Canvas_x'] = event.x
            allconfig['Event_Canvas_y'] = event.y

            allconfig['XuanKuang_X0'] = event.x
            allconfig['XuanKuang_Y0'] = event.y

            self.Yanse_HuiFu()


        def paint_YiDong(event):
            allconfig['flag_TanChuan_BianJian'] = TRUE
            allconfig['XuanKuang_X1'] = event.x
            allconfig['XuanKuang_Y1'] = event.y

            self.canva.delete('Xuan_Kuang_ing')

            self.it_Kuan1 = self.canva.create_line(allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y0'], fill='DeepSkyBlue', width=2)
            self.it_Kuan2 = self.canva.create_line(allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y1'], fill='DeepSkyBlue', width=2)
            self.it_Kuan3 = self.canva.create_line(allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y1'], allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y1'], fill='DeepSkyBlue', width=2)
            self.it_Kuan4 = self.canva.create_line(allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y1'], fill='DeepSkyBlue', width=2)

            # ******************************************************************************************
            self.canva.itemconfig(self.it_Kuan1, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan2, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan3, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan4, tags='Xuan_Kuang_ing')

        def paint_ShiFang(event):
            if allconfig['zi_menu1_sum'] == 0:
                allconfig['Distance'] = allconfig['bar_W']
            else:
                allconfig['Distance'] = allconfig['bar_W'] + allconfig['bar_menu_W']

            # ____________________________________________________________________________________________________________
            allconfig['XuanKuang_X1'] = event.x
            allconfig['XuanKuang_Y1'] = event.y

            allconfig['XuanKuang_Y0'] = allconfig['XuanKuang_Y0'] - allconfig['Distance']
            allconfig['XuanKuang_Y1'] = allconfig['XuanKuang_Y1'] - allconfig['Distance']

            self.canva.delete('Xuan_Kuang_ing')

            # for 循环逐个判断
            for i in range(1, allconfig['button1_i'] + 1, 1):
                if i not in allconfig['Button1_List_Num']:
                    # BuJian_ChuLi(self, i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_Lei, allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y1']):
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Button', 'button', allconfig['Button1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'], allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['canvas1_i'] + 1, 1):
                if i not in allconfig['Canvas1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Canvas', 'canvas', allconfig['Canvas1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['checkbutton1_i'] + 1, 1):
                if i not in allconfig['Checkbutton1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Checkbutton', 'checkbutton', allconfig['Checkbutton1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['combobox1_i'] + 1, 1):
                if i not in allconfig['Combobox1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Combobox', 'combobox', allconfig['Combobox1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['entry1_i'] + 1, 1):
                if i not in allconfig['Entry1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Entry', 'entry', allconfig['Entry1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['frame1_i'] + 1, 1):
                if i not in allconfig['Frame1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Frame', 'frame', allconfig['Frame1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['label1_i'] + 1, 1):
                if i not in allconfig['Label1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Label', 'label', allconfig['Label1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['labelFrame1_i'] + 1, 1):
                if i not in allconfig['LabelFrame1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'LabelFrame', 'labelFrame', allconfig['LabelFrame1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['listbox1_i'] + 1, 1):
                if i not in allconfig['Listbox1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Listbox', 'listbox', allconfig['Listbox1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['message1_i'] + 1, 1):
                if i not in allconfig['Message1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Message', 'message', allconfig['Message1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['panedWindow1_i'] + 1, 1):
                if i not in allconfig['PanedWindow1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'PanedWindow', 'panedWindow', allconfig['PanedWindow1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['radiobutton1_i'] + 1, 1):
                if i not in allconfig['Radiobutton1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Radiobutton', 'radiobutton', allconfig['Radiobutton1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['scale1_x_i'] + 1, 1):
                if i not in allconfig['Scale1_List_Num_X']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Scale_X', 'scale_x', allconfig['Scale1_X'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['scale1_y_i'] + 1, 1):
                if i not in allconfig['Scale1_List_Num_Y']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Scale_Y', 'scale_y', allconfig['Scale1_Y'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['spinbox1_i'] + 1, 1):
                if i not in allconfig['Spinbox1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Spinbox', 'spinbox', allconfig['Spinbox1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            for i in range(1, allconfig['text1_i'] + 1, 1):
                if i not in allconfig['Text1_List_Num']:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Text', 'text', allconfig['Text1'], allconfig['XuanKuang_X0'], allconfig['XuanKuang_Y0'], allconfig['XuanKuang_X1'],
                                           allconfig['XuanKuang_Y1'])

            # ____________________________________________________________________________________________________________
            self.Design()
            self.TanChuang()


        self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
        self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
        self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def TanChuang(self):
        if allconfig['flag_TanChuan_BianJian'] == TRUE:
            self.BianJi_kj_menu.post(allconfig['XuanKuang_X1']+allconfig['canva_X']+allconfig['win_X'], allconfig['XuanKuang_Y1']+allconfig['canva_Y']+allconfig['win_Y'])
            allconfig['flag_TanChuan_BianJian'] = FALSE


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def OK(self):
        allconfig['flag_ZuJian_Move'] = FALSE
        print("OK, allconfig['flag_ZuJian_Move'] = ", allconfig['flag_ZuJian_Move'])
        self.WanCheng()
        self.Yanse_HuiFu()
        self.Clear_XuanZhong()


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Design(self):
        # Design_bujian(self, XuanZhong_Object):
        design_buJian = Design_BuJian()
        Len = len(allconfig['XuanZhong'])
        if Len == 1:
            name = "XuanZhong" + str(1)
            a = allconfig['XuanZhong'][name]
            design_buJian.Design_bujian(a)


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def UI_Ban_Design(self):
        Len = len(allconfig['XuanZhong'])
        if Len == 1:
            name = "XuanZhong" + str(1)
            a = allconfig['XuanZhong'][name]

            BuJian_LeiXing_DaXie = a[1]
            BuJian_LeiXing_XiaoXie = a[2]
            BuJian_NO_i = a[3]
            BuJian_Lei = a[4]

            # name = "XuanZhong" + str(XuanZhong_sum)
            # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])
            design_new = Design_New()
            design_new.BuJian_New(BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei)

            # name
            # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
            # BuJian_Lei[KJ_name] = allconfig['ent_ControlName']
            sj_chu_li = SJ_ChuLi()
            sj_chu_li.SJ_New(BuJian_LeiXing_XiaoXie, BuJian_NO_i, BuJian_Lei)


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Move(self):
        Len = len(allconfig['XuanZhong'])
        # name = "XuanZhong" + str(XuanZhong_sum)
        # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])

        if 1:
        # if allconfig['flag_ZuJian_Move'] == TRUE:
            # 鼠标左键按下事件
            def paint1(event):
                self.ZuJian_x1 = event.x
                self.ZuJian_y1 = event.y
                self.canva.config(cursor='fleur')
                self.Line = self.canva.create_line(self.ZuJian_x1, self.ZuJian_y1, self.ZuJian_x1, self.ZuJian_y1,
                                                   fill="DeepSkyBlue", width=1.6)

            # 鼠标左键按下并移动事件
            def paint2(event):
                self.ZuJian_x2 = event.x
                self.ZuJian_y2 = event.y

                self.Move_X = self.ZuJian_x2 - self.ZuJian_x1
                self.Move_Y = self.ZuJian_y2 - self.ZuJian_y1

                # 绘制移动基线
                self.canva.coords(self.Line, self.ZuJian_x1, self.ZuJian_y1, self.ZuJian_x2, self.ZuJian_y2)

                # ____________________________________________________________________________________________________________
                for i in range(1, Len + 1, 1):
                    name = "XuanZhong" + str(i)
                    a = allconfig['XuanZhong'][name]
                    if a[1] == 'Button':
                        num_i = a[3]
                        KJ = 'Button' + str(a[3])
                        name_coords = 'button_coords' + str(num_i)
                        a = allconfig['Button1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Button1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Canvas':
                        num_i = a[3]
                        KJ = 'Canvas' + str(a[3])
                        name_coords = 'canvas_coords' + str(num_i)
                        a = allconfig['Canvas1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Canvas1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Checkbutton':
                        num_i = a[3]
                        KJ = 'Checkbutton' + str(a[3])
                        name_coords = 'checkbutton_coords' + str(num_i)
                        a = allconfig['Checkbutton1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Checkbutton1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Combobox':
                        num_i = a[3]
                        KJ = 'Combobox' + str(a[3])
                        name_coords = 'combobox_coords' + str(num_i)
                        a = allconfig['Combobox1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Combobox1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Entry':
                        num_i = a[3]
                        KJ = 'Entry' + str(a[3])
                        name_coords = 'entry_coords' + str(num_i)
                        a = allconfig['Entry1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Entry1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Frame':
                        num_i = a[3]
                        KJ = 'Frame' + str(a[3])
                        name_coords = 'frame_coords' + str(num_i)
                        a = allconfig['Frame1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Frame1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Label':
                        num_i = a[3]
                        KJ = 'Label' + str(a[3])
                        name_coords = 'label_coords' + str(num_i)
                        a = allconfig['Label1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Label1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'LabelFrame':
                        num_i = a[3]
                        KJ = 'LabelFrame' + str(a[3])
                        name_coords = 'labelFrame_coords' + str(num_i)
                        a = allconfig['LabelFrame1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['LabelFrame1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Listbox':
                        num_i = a[3]
                        KJ = 'Listbox' + str(a[3])
                        name_coords = 'listbox_coords' + str(num_i)
                        a = allconfig['Listbox1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Listbox1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Message':
                        num_i = a[3]
                        KJ = 'Message' + str(a[3])
                        name_coords = 'message_coords' + str(num_i)
                        a = allconfig['Message1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Message1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'PanedWindow':
                        num_i = a[3]
                        KJ = 'PanedWindow' + str(a[3])
                        name_coords = 'panedWindow_coords' + str(num_i)
                        a = allconfig['PanedWindow1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['PanedWindow1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Radiobutton':
                        num_i = a[3]
                        KJ = 'Radiobutton' + str(a[3])
                        name_coords = 'radiobutton_coords' + str(num_i)
                        a = allconfig['Radiobutton1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Radiobutton1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Scale_X':
                        num_i = a[3]
                        KJ = 'Scale_X' + str(a[3])
                        name_coords = 'scale_x_coords' + str(num_i)
                        a = allconfig['Scale1_X'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Scale1_X'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Scale_Y':
                        num_i = a[3]
                        KJ = 'Scale_Y' + str(a[3])
                        name_coords = 'scale_y_coords' + str(num_i)
                        a = allconfig['Scale1_Y'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Scale1_Y'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Spinbox':
                        num_i = a[3]
                        KJ = 'Spinbox' + str(a[3])
                        name_coords = 'spinbox_coords' + str(num_i)
                        a = allconfig['Spinbox1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Spinbox1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Text':
                        num_i = a[3]
                        KJ = 'Text' + str(a[3])
                        name_coords = 'text_coords' + str(num_i)
                        a = allconfig['Text1'][name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        allconfig['Text1'][KJ].place(x=X, y=Y)
            # ____________________________________________________________________________________________________________

            # 鼠标左键松开事件
            def paint3(event):
                self.ZuJian_x2 = event.x
                self.ZuJian_y2 = event.y

                self.canva.delete(self.Line)
                self.canva.config(cursor='arrow')
                self.BianJi_kj_menu.post(self.ZuJian_x2 + allconfig['canva_X'] + allconfig['win_X'], self.ZuJian_y2 + allconfig['canva_Y']  + allconfig['win_Y'])

                # ____________________________________________________________________________________________________________
                for i in range(1, Len + 1, 1):
                    name = "XuanZhong" + str(i)
                    a = allconfig['XuanZhong'][name]
                    if a[1] == 'Button':
                        num_i = a[3]
                        KJ = 'Button' + str(a[3])
                        name_coords = 'button_coords' + str(num_i)
                        a = allconfig['Button1'][name_coords]

                        # name_coords = 'button_coords' + str(BuJian_NO_i)
                        # Zhi = (self.X0, self.Y0, self.X1, self.Y1, BuJian_NO_i)

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Button1'][name_coords] = Zhi
                        # allconfig['Button1'][KJ].place(x=X, y=Y)

                    elif a[1] == 'Canvas':
                        num_i = a[3]
                        KJ = 'Canvas' + str(a[3])
                        name_coords = 'canvas_coords' + str(num_i)
                        a = allconfig['Canvas1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Canvas1'][name_coords] = Zhi

                    elif a[1] == 'Checkbutton':
                        num_i = a[3]
                        KJ = 'Checkbutton' + str(a[3])
                        name_coords = 'checkbutton_coords' + str(num_i)
                        a = allconfig['Checkbutton1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Checkbutton1'][name_coords] = Zhi

                    elif a[1] == 'Combobox':
                        num_i = a[3]
                        KJ = 'Combobox' + str(a[3])
                        name_coords = 'combobox_coords' + str(num_i)
                        a = allconfig['Combobox1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Combobox1'][name_coords] = Zhi

                    elif a[1] == 'Entry':
                        num_i = a[3]
                        KJ = 'Entry' + str(a[3])
                        name_coords = 'entry_coords' + str(num_i)
                        a = allconfig['Entry1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Entry1'][name_coords] = Zhi

                    elif a[1] == 'Frame':
                        num_i = a[3]
                        KJ = 'Frame' + str(a[3])
                        name_coords = 'frame_coords' + str(num_i)
                        a = allconfig['Frame1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Entry1'][name_coords] = Zhi



                    elif a[1] == 'Label':
                        num_i = a[3]
                        KJ = 'Label' + str(a[3])
                        name_coords = 'label_coords' + str(num_i)
                        a = allconfig['Label1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Label1'][name_coords] = Zhi


                    elif a[1] == 'LabelFrame':
                        num_i = a[3]
                        KJ = 'LabelFrame' + str(a[3])
                        name_coords = 'labelFrame_coords' + str(num_i)
                        a = allconfig['LabelFrame1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['LabelFrame1'][name_coords] = Zhi


                    elif a[1] == 'Listbox':
                        num_i = a[3]
                        KJ = 'Listbox' + str(a[3])
                        name_coords = 'listbox_coords' + str(num_i)
                        a = allconfig['Listbox1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Listbox1'][name_coords] = Zhi


                    elif a[1] == 'Message':
                        num_i = a[3]
                        KJ = 'Message' + str(a[3])
                        name_coords = 'message_coords' + str(num_i)
                        a = allconfig['Message1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Message1'][name_coords] = Zhi


                    elif a[1] == 'PanedWindow':
                        num_i = a[3]
                        KJ = 'PanedWindow' + str(a[3])
                        name_coords = 'panedWindow_coords' + str(num_i)
                        a = allconfig['PanedWindow1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['PanedWindow1'][name_coords] = Zhi


                    elif a[1] == 'Radiobutton':
                        num_i = a[3]
                        KJ = 'Radiobutton' + str(a[3])
                        name_coords = 'radiobutton_coords' + str(num_i)
                        a = allconfig['Radiobutton1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Radiobutton1'][name_coords] = Zhi


                    elif a[1] == 'Scale_X':
                        num_i = a[3]
                        KJ = 'Scale_X' + str(a[3])
                        name_coords = 'scale_x_coords' + str(num_i)
                        a = allconfig['Scale1_X'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Scale1_X'][name_coords] = Zhi


                    elif a[1] == 'Scale_Y':
                        num_i = a[3]
                        KJ = 'Scale_Y' + str(a[3])
                        name_coords = 'scale_y_coords' + str(num_i)
                        a = allconfig['Scale1_Y'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Scale1_Y'][name_coords] = Zhi


                    elif a[1] == 'Spinbox':
                        num_i = a[3]
                        KJ = 'Spinbox' + str(a[3])
                        name_coords = 'spinbox_coords' + str(num_i)
                        a = allconfig['Spinbox1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Spinbox1'][name_coords] = Zhi


                    elif a[1] == 'Text':
                        num_i = a[3]
                        KJ = 'Text' + str(a[3])
                        name_coords = 'text_coords' + str(num_i)
                        a = allconfig['Text1'][name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        allconfig['Text1'][name_coords] = Zhi

                        print('Text1 = \n', allconfig['Text1'][KJ])
                        print('Text1_coords = \n', allconfig['Text1'][name_coords])
                # ____________________________________________________________________________________________________________

            # 画布控件与鼠标左键进行绑定
            self.canva.bind("<ButtonPress-1>", paint1)  # 绑定鼠标按下事件
            self.canva.bind("<B1-Motion>", paint2)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonRelease-1>", paint3)  # 绑定鼠标松开事件


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Delete(self):
        if askyesno('Delete', 'Is going to delete Selected?'):
            Len = len(allconfig['XuanZhong'])

            for i in range(1, Len + 1, 1):
                name = "XuanZhong" + str(i)
                a = allconfig['XuanZhong'][name]

                XuanZhong_Object = a
                delete_buJian = Delete_BuJian()
                delete_buJian.Delete(XuanZhong_Object)

            # 清空选中
            self.Clear_XuanZhong()

        # 如果不清空则恢复原来颜色
        else:
            self.Yanse_HuiFu()

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Cancel(self):
        self.Yanse_HuiFu()

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Clear_XuanZhong(self):
        allconfig['XuanZhong_sum'] = 0
        allconfig['XuanZhong'].clear()

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Yanse_HuiFu(self):
        # name = "XuanZhong" + str(XuanZhong_sum)
        # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])

        Len = len(allconfig['XuanZhong'])
        if len != 0:
            for i in range(1, Len + 1, 1):
                name = "XuanZhong" + str(i)
                a = allconfig['XuanZhong'][name]

                BuJian_Lei = a[4]
                BuJian_LeiXing_DaXie = a[1]
                BuJian_LeiXing_XiaoXie = a[2]
                Num_i = a[3]

                # Color_Restore(self, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i):
                color_handle = Color_Handle()
                color_handle.Color_Restore(BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i)

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    # 设置控件标志
    def Set_KJBZ(self, str):
        allconfig['KJBZ'] = str


    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    def Hua_BianYi(self):
        if allconfig['ck_name'] != "":
            str_code = allconfig['tap'] + allconfig['tap'] + "# Control Define" + "\n\n"
            self.Text_1.insert(END, str_code)

        # Menu
        if allconfig['zi_menu1_sum'] != 0:
            str_code = allconfig['tap'] + allconfig['tap'] + "# Menu Define" + "\n"
            self.Text_1.insert(END, str_code)

            menu_str = Menu_Str()
            str_Menu = menu_str.Menu_Str()
            self.Text_1.insert(END, str_Menu)

        if allconfig['ck_name'] != "":
            str_code = allconfig['tap'] + allconfig['tap'] + "# Other Control Define" + "\n\n"
            self.Text_1.insert(END, str_code)

        # for 循环逐个判断
        for i in range(1, allconfig['button1_i'] + 1, 1):
            if i not in allconfig['Button1_List_Num']:
                KJ = 'Button' + str(i)
                # Record_Code(self, BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
                dictionary = Dictionary()

                print(f"{allconfig['Button1'] = }")
                print(f"{allconfig = }")

                dictionary.Record_Code(allconfig['Button1'][KJ], allconfig['Button1'], 'Button', 'button', i)

                name_Code = 'button' + '_Code' + str(i)
                str_code = allconfig['Button1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['canvas1_i'] + 1, 1):
            if i not in allconfig['Canvas1_List_Num']:
                KJ = 'Canvas' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Canvas1'][KJ], allconfig['Canvas1'], 'Canvas', 'canvas', i)

                name_Code = 'canvas' + '_Code' + str(i)
                str_code = allconfig['Canvas1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['checkbutton1_i'] + 1, 1):
            if i not in allconfig['Checkbutton1_List_Num']:
                KJ = 'Checkbutton' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Checkbutton1'][KJ], allconfig['Checkbutton1'], 'Checkbutton', 'checkbutton', i)

                name_Code = 'checkbutton' + '_Code' + str(i)
                str_code = allconfig['Checkbutton1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['combobox1_i'] + 1, 1):
            if i not in allconfig['Combobox1_List_Num']:
                KJ = 'Combobox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Combobox1'][KJ], allconfig['Combobox1'], 'ttk.Combobox', 'combobox', i)

                name_Code = 'combobox' + '_Code' + str(i)
                str_code = allconfig['Combobox1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['entry1_i'] + 1, 1):
            if i not in allconfig['Entry1_List_Num']:
                KJ = 'Entry' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Entry1'][KJ], allconfig['Entry1'], 'Entry', 'entry', i)

                name_Code = 'entry' + '_Code' + str(i)
                str_code = allconfig['Entry1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['frame1_i'] + 1, 1):
            if i not in allconfig['Frame1_List_Num']:
                KJ = 'Frame' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Frame1'][KJ], allconfig['Frame1'], 'Frame', 'frame', i)

                name_Code = 'frame' + '_Code' + str(i)
                str_code = allconfig['Frame1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['label1_i'] + 1, 1):
            if i not in allconfig['Label1_List_Num']:
                KJ = 'Label' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Label1'][KJ], allconfig['Label1'], 'Label', 'label', i)

                name_Code = 'label' + '_Code' + str(i)
                str_code = allconfig['Label1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['labelFrame1_i'] + 1, 1):
            if i not in allconfig['LabelFrame1_List_Num']:
                KJ = 'LabelFrame' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['LabelFrame1'][KJ], allconfig['LabelFrame1'], 'LabelFrame', 'labelFrame', i)

                name_Code = 'labelFrame' + '_Code' + str(i)
                str_code = allconfig['LabelFrame1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['listbox1_i'] + 1, 1):
            if i not in allconfig['Listbox1_List_Num']:
                KJ = 'Listbox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Listbox1'][KJ], allconfig['Listbox1'], 'Listbox', 'listbox', i)

                name_Code = 'listbox' + '_Code' + str(i)
                str_code = allconfig['Listbox1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['message1_i'] + 1, 1):
            if i not in allconfig['Message1_List_Num']:
                KJ = 'Message' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Message1'][KJ], allconfig['Message1'], 'tk.Message', 'message', i)

                name_Code = 'message' + '_Code' + str(i)
                str_code = allconfig['Message1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['panedWindow1_i'] + 1, 1):
            if i not in allconfig['PanedWindow1_List_Num']:
                KJ = 'PanedWindow' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['PanedWindow1'][KJ], allconfig['PanedWindow1'], 'PanedWindow', 'panedWindow', i)

                name_Code = 'panedWindow' + '_Code' + str(i)
                str_code = allconfig['PanedWindow1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['radiobutton1_i'] + 1, 1):
            if i not in allconfig['Radiobutton1_List_Num']:
                KJ = 'Radiobutton' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Radiobutton1'][KJ], allconfig['Radiobutton1'], 'Radiobutton', 'radiobutton', i)

                name_Code = 'radiobutton' + '_Code' + str(i)
                str_code = allconfig['Radiobutton1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['scale1_x_i'] + 1, 1):
            if i not in allconfig['Scale1_List_Num_X']:
                KJ = 'Scale_X' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Scale1_X'][KJ], allconfig['Scale1_X'], 'Scale_X', 'scale_x', i)

                name_Code = 'scale_x' + '_Code' + str(i)
                str_code = allconfig['Scale1_X'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['scale1_y_i'] + 1, 1):
            if i not in allconfig['Scale1_List_Num_Y']:
                KJ = 'Scale_Y' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Scale1_Y'][KJ], allconfig['Scale1_Y'], 'Scale_Y', 'scale_y', i)

                name_Code = 'scale_y' + '_Code' + str(i)
                str_code = allconfig['Scale1_Y'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['spinbox1_i'] + 1, 1):
            if i not in allconfig['Spinbox1_List_Num']:
                KJ = 'Spinbox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(allconfig['Spinbox1'][KJ], allconfig['Spinbox1'], 'Spinbox', 'spinbox', i)

                name_Code = 'spinbox' + '_Code' + str(i)
                str_code = allconfig['Spinbox1'][name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, allconfig['text1_i'] + 1, 1):
            if i not in allconfig['Text1_List_Num']:
                KJ = 'Text' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Text1[KJ], allconfig['Text1'], 'Text', 'text', i)

                name_Code = 'text' + '_Code' + str(i)
                str_code = allconfig['Text1'][name_Code]
                self.Text_1.insert(END, str_code)

        if allconfig['ck_name'] != "":
            event_code = allconfig['tap'] + allconfig['tap'] + "# Event Define" + "\n\n"
            self.Text_1.insert(END, event_code)

        # def Judge_If_Delete(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        sj_chu_li = SJ_ChuLi()
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_1'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_release_1'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_right_1'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_left_2'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_right_2'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_middle_1'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_middle_2'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_button_press_left_move'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_cursor_enter'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_cursor_leave'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_get_key_focus'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_lose_key_focus'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_press_a_key'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_press_enter_key'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_when_control_change'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_press_space_key'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_shift_mouseWheel'], self.Text_1)
        sj_chu_li.SJ_Bian_Yi(allconfig['SJ_press_combinatorial_key'], self.Text_1)

        # 结尾
        if allconfig['ck_name'] != "":
            self.Text_1.insert(END, allconfig['Str_BianYi_End'])

    # ____________________________________________________________________________________________________________
    # ____________________________________________________________________________________________________________
    # 录入字典
    def LuRu_Dict(self):
        # ____________________________________________________________________________________________________________
        if allconfig['zi_menu1_sum'] == 0:
            allconfig['Distance'] = allconfig['bar_W']
        else:
            allconfig['Distance'] = allconfig['bar_W'] + allconfig['bar_menu_W']

        self.Y0 = self.Y0 - allconfig['Distance']
        self.Y1 = self.Y1 - allconfig['Distance']
        # ____________________________________________________________________________________________________________

        if allconfig['KJBZ'] == 'button1':
            allconfig['button1_i'] = allconfig['button1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Button ' + str(allconfig['button1_i'])
            self.it_Button.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['button1_i']

            # Record_Dict(self, BuJian, BuJian_Lei, BuJian_NO_i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie,
            #             self_X0, self_Y0, self_X1, self_Y1):
            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Button, allconfig['Button1'], BuJian_NO_i, 'Button', 'button',
                        self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'canvas1':
            allconfig['canvas1_i'] = allconfig['canvas1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Canvas ' + str(allconfig['canvas1_i'])
            BuJian_NO_i = allconfig['canvas1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Canva, allconfig['Canvas1'], BuJian_NO_i, 'Canvas', 'canvas',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'checkbutton1':
            allconfig['checkbutton1_i'] = allconfig['checkbutton1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Checkbutton ' + str(allconfig['checkbutton1_i'])
            self.it_Checkbutton.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['checkbutton1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Checkbutton, allconfig['Checkbutton1'], BuJian_NO_i, 'Checkbutton', 'checkbutton',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________

        elif allconfig['KJBZ'] == 'combobox1':
            allconfig['combobox1_i'] = allconfig['combobox1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Combobox ' + str(allconfig['combobox1_i'] )

            self.it_Combobox["values"] = ('Combobox', allconfig['DangQian_KJ_name'] )
            self.it_Combobox.current(1)
            BuJian_NO_i = allconfig['combobox1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Combobox, allconfig['Combobox1'], BuJian_NO_i, 'Combobox', 'combobox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'entry1':
            allconfig['entry1_i'] = allconfig['entry1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Entry ' + str(allconfig['entry1_i'])
            # self.it_Entry.config(text=allconfig['DangQian_KJ_name'] )
            self.it_Entry.insert(1, allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['entry1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Entry, allconfig['Entry1'], BuJian_NO_i, 'Entry', 'entry',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'frame1':
            allconfig['frame1_i'] = allconfig['frame1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Frame ' + str(allconfig['frame1_i'] + 1)
            BuJian_NO_i = allconfig['frame1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Frame, allconfig['Frame1'], BuJian_NO_i, 'Frame', 'frame',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________

        elif allconfig['KJBZ'] == 'label1':
            allconfig['label1_i'] = allconfig['label1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Label ' + str(allconfig['label1_i'] + 1)
            self.it_Label.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['label1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Label, allconfig['Label1'], BuJian_NO_i, 'Label', 'label',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________

        elif allconfig['KJBZ'] == 'labelFrame1':
            allconfig['labelFrame1_i'] = allconfig['labelFrame1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'LabelFrame ' + str(allconfig['labelFrame1_i'] + 1)
            self.it_LabelFrame.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['labelFrame1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_LabelFrame, allconfig['LabelFrame1'], BuJian_NO_i, 'LabelFrame', 'labelFrame',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________

        elif allconfig['KJBZ'] == 'listbox1':
            allconfig['listbox1_i'] = allconfig['listbox1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Listbox ' + str(allconfig['listbox1_i'] + 1)
            BuJian_NO_i = allconfig['listbox1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Listbox, allconfig['Listbox1'], BuJian_NO_i, 'Listbox', 'listbox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'menu1':
            menu1_i = menu1_i + 1
            allconfig['DangQian_KJ_name']  = 'Menu ' + str(allconfig['menu1_i'] + 1)

       # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'message1':
            allconfig['message1_i'] = allconfig['message1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Message ' + str(allconfig['message1_i'])
            self.it_Message.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['message1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Message, allconfig['Message1'], BuJian_NO_i, 'Message', 'message',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'panedWindow1':
            allconfig['panedWindow1_i'] = allconfig['panedWindow1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'PanedWindow ' + str(allconfig['message1_i'] + 1)
            BuJian_NO_i = allconfig['panedWindow1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_PanedWindow, allconfig['PanedWindow1'], BuJian_NO_i, 'PanedWindow', 'panedWindow',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'radiobutton1':
            allconfig['radiobutton1_i'] = allconfig['radiobutton1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Radiobutton ' + str(allconfig['radiobutton1_i'])
            self.it_Radiobutton.config(text=allconfig['DangQian_KJ_name'] )
            BuJian_NO_i = allconfig['radiobutton1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Radiobutton, allconfig['Radiobutton1'], BuJian_NO_i, 'Radiobutton', 'radiobutton',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'scale1_x':
            allconfig['scale1_x_i'] = allconfig['scale1_x_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Scale_X ' + str(allconfig['scale1_x_i'] + 1)
            BuJian_NO_i = allconfig['scale1_x_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Scale_X, allconfig['Scale1_X'], BuJian_NO_i, 'Scale_X', 'scale_x',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'scale1_y':
            allconfig['scale1_y_i'] = allconfig['scale1_y_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Scale_Y ' + str(allconfig['scale1_y_i'] + 1)
            BuJian_NO_i = allconfig['scale1_y_i']
            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Scale_Y, allconfig['Scale1_Y'], BuJian_NO_i, 'Scale_Y', 'scale_y',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________

        elif allconfig['KJBZ'] == 'scrollbar1_x':
            allconfig['scrollbar1_i']  = allconfig['scrollbar1_x_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Scrollbar_X ' + str(allconfig['scrollbar1_i']  + 1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'scrollbar1_y':
            allconfig['scrollbar1_i']  = allconfig['scrollbar1_y_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Scrollbar_Y ' + str(allconfig['scrollbar1_i']  + 1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'text1':
            allconfig['text1_i'] = allconfig['text1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Text ' + str(allconfig['text1_i']    + 1)
            BuJian_NO_i = allconfig['text1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Text, allconfig['Text1'], BuJian_NO_i, 'Text', 'text',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'spinbox1':
            allconfig['spinbox1_i'] = allconfig['spinbox1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Spinbox ' + str(allconfig['spinbox1_i'] + 1)
            BuJian_NO_i = allconfig['spinbox1_i']

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Spinbox, allconfig['Spinbox1'], BuJian_NO_i, 'Spinbox', 'spinbox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'toplevel1':
            allconfig['toplevel1_i'] = allconfig['toplevel1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'Toplevel ' + str(allconfig['toplevel1_i'] + 1)

        # ____________________________________________________________________________________________________________
        elif allconfig['KJBZ'] == 'tkMessageBox1':
            allconfig['tkMessageBox1_i'] = allconfig['tkMessageBox1_i'] + 1
            allconfig['DangQian_KJ_name']  = 'tkMessageBox1_i ' + str(allconfig['tkMessageBox1_i'] + 1)

        # ____________________________________________________________________________________________________________


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 字符串处理类
class Str_ChuLi:
    def FenDuan(self, str1):
        self.str = str(str1)
        L = len(self.str)
        for i in range(1, L, 1):
            if self.str[i] == ' ':
                self.falg_FenDuan = True
                self.a = self.str[0:i]
                self.ab = self.str[i:L]
                break
            else:
                self.falg_FenDuan = False

        if self.falg_FenDuan == True:
            L = len(self.ab)
            for i in range(1, L + 1, 1):
                if self.ab[i] != ' ':
                    self.b = self.ab[i:L]
                    break
            print(self.a)
            print(self.b)
            return (self.a, self.b)
        else:
            return (self.str, '')

# ____________________________________________________________________________________________________________
# 颜色选择框类
class Choose_Color:
    def Color_Choose(self):
        col = tkinter.colorchooser.askcolor(color='green', title="Choose the Colour")
        print(col)
        return col

# ____________________________________________________________________________________________________________
# 获取文件名类
class Get_File_Name_GIF:
    def Get_Name(self):
        file_name = tkinter.filedialog.askopenfilename(filetypes=[("*.gif", "gif")])
        return file_name

class Get_File_Name_XBM:
    def Get_Name(self):
        file_name = tkinter.filedialog.askopenfilename(filetypes=[("*.xbm", "xbm")])
        return file_name

# ____________________________________________________________________________________________________________
# Bitmap 图像处理类
class BitMap:
    def BitMap_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):
        name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
        list = (
        'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning')
        Zhi = allconfig['combt_bitmap']
        flag_bitmap_list = FALSE
        for i in list:
            if i == Zhi:
                flag_bitmap_list = TRUE
                BuJian.config(bitmap=Zhi)

        if (flag_bitmap_list == FALSE) and (Zhi != ''):
            bitmap_photo = tkinter.BitmapImage(file=Zhi)
            BuJian.config(bitmap=bitmap_photo)

        BuJian_Lei[name_bitmap] = "" + Zhi + ""

# ____________________________________________________________________________________________________________
# Image 图像处理类
class Image_ChuLi:
    def Image_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):
        name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
        Zhi = allconfig['ent_image']
        if Zhi != '':
            BuJian_Lei[name_image] = Zhi
            image_photo = PhotoImage(file=Zhi)
            BuJian.config(image=image_photo)
        elif Zhi == '':
            BuJian.config(image='')


# ____________________________________________________________________________________________________________
# 设计更新类
class Design_New:
    def BuJian_New(self, BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei):
        BuJian_NO_i = BuJian_NO_i
        allconfig['lab_ControlType'] = BuJian_LeiXing_DaXie
        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # ____________________________________________________________________________________________________________
        if allconfig['zi_menu1_sum'] == 0:
            allconfig['Distance'] = allconfig['bar_W']
        else:
            allconfig['Distance'] = allconfig['bar_W'] + allconfig['bar_menu_W']
        # ____________________________________________________________________________________________________________
        # 字典更新及设计窗口更新
        # name = "XuanZhong" + str(XuanZhong_sum)
        # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])

        judge = Judge_Property()

        # ____________________________________________________________________________________________________________
        # 通用属性 container, name, cusor, width, background, coords
        # container
        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        Zhi = allconfig['ent_container']
        BuJian_Lei[name_container] = Zhi

        # name
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ_name] = allconfig['ent_ControlName']
        judge_Property = Judge_Property()
        if (judge_Property.Is_In_text(BuJian_LeiXing_DaXie) == TRUE) and allconfig['ent_text'] == '':
            BuJian_Lei[KJ].config(text=allconfig['ent_ControlName'])

        # coords and width
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        Zhi = (allconfig['ent_X0'], allconfig['ent_Y0'], allconfig['ent_width'], allconfig['ent_height'], BuJian_NO_i)
        BuJian_Lei[name_coords] = Zhi

        BuJian_Lei[KJ].place(x=allconfig['ent_X0'], y=allconfig['ent_Y0'] + allconfig['Distance'])
        BuJian_Lei[KJ].config(width=int(allconfig['ent_width']))

        # cursor
        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        Zhi = allconfig['combt_cursor']
        BuJian_Lei[name_cursor] = Zhi
        BuJian_Lei[KJ].config(cursor=Zhi)

        # background
        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        Zhi = allconfig['combt_background']
        BuJian_Lei[name_background] = Zhi
        BuJian_Lei[KJ].config(background=Zhi)


        # ____________________________________________________________________________________________________________
        # 部分属性

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            Zhi = int(allconfig['ent_height'])
            BuJian_Lei[name_height] = Zhi
            BuJian_Lei[KJ].config(height=Zhi)

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            Zhi = int(allconfig['ent_length'])
            BuJian_Lei[name_length] = Zhi
            BuJian_Lei[KJ].config(length=Zhi)

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            Zhi = (str(allconfig['combt_fontType']), allconfig['ent_fontSize'])
            BuJian_Lei[name_font] = Zhi
            BuJian_Lei[KJ].config(font=Zhi)

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            Zhi = allconfig['combt_foreground']
            BuJian_Lei[name_foreground] = Zhi
            BuJian_Lei[KJ].config(foreground=Zhi)

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            Zhi = allconfig['combt_anchor']
            BuJian_Lei[name_anchor] = Zhi
            BuJian_Lei[KJ].config(anchor=Zhi)

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            Zhi = allconfig['combt_justify']
            BuJian_Lei[name_justify] = Zhi
            BuJian_Lei[KJ].config(justify=Zhi)

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            Zhi = allconfig['combt_state']
            BuJian_Lei[name_state] = Zhi
            BuJian_Lei[KJ].config(state=Zhi)

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            Zhi = allconfig['combt_relief']
            BuJian_Lei[name_relief] = Zhi
            BuJian_Lei[KJ].config(relief=Zhi)


        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            Zhi = allconfig['combt_highlightcolor']
            BuJian_Lei[name_highlightcolor] = Zhi
            BuJian_Lei[KJ].config(highlightcolor=Zhi)

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            Zhi = allconfig['combt_highlightbackground']
            BuJian_Lei[name_highlightbackground] = Zhi
            BuJian_Lei[KJ].config(highlightbackground=Zhi)


        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            a = BitMap()
            a.BitMap_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian_Lei[KJ])
            # BitMap_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            a = Image_ChuLi()
            a.Image_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian_Lei[KJ])
            # Image_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):

        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            Zhi = allconfig['combt_padx']
            BuJian_Lei[name_padx] = Zhi
            BuJian_Lei[KJ].config(padx=Zhi)

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            Zhi = allconfig['combt_pady']
            BuJian_Lei[name_pady] = Zhi
            BuJian_Lei[KJ].config(pady=Zhi)

        # text
        if (judge.Is_In_takefocus(BuJian_LeiXing_DaXie)) == TRUE and (allconfig['ent_text'] != ''):
            name_text = str(BuJian_LeiXing_XiaoXie) + '_text' + str(BuJian_NO_i)
            Zhi = allconfig['ent_text']
            BuJian_Lei[name_text] = Zhi
            BuJian_Lei[KJ].config(text=Zhi)

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            Zhi = allconfig['combt_takefocus']
            BuJian_Lei[name_takefocus] = Zhi
            BuJian_Lei[KJ].config(takefocus=Zhi)

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            Zhi = allconfig['ent_command']
            BuJian_Lei[name_command] = Zhi
            BuJian_Lei[KJ].config(command=Zhi)


# ____________________________________________________________________________________________________________

# 判断属性类
# 每个控件都有的属性 container, cusor, width, background
class Judge_Property:
    def Is_In_anchor(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'tk.Message', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_font(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message', 'Radiobutton',
                'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_bitmap(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_justify(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'Listbox', 'tk.Message', 'Radiobutton', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_image(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE



    def Is_In_height(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'PanedWindow', 'Radiobutton', 'Text')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_length(self, BuJian_LeiXing_DaXie):
        list = ('Scale_X', 'Scale_Y')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_foreground(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')

        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_padx_or_pady(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Frame', 'Label', 'LabelFrame', 'tk.Message', 'Radiobutton', 'Text')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_relief(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'tk.Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_text(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Entry', 'Label', 'LabelFrame', 'tk.Message', 'Radiobutton', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_state(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'Listbox',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_takefocus(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'tk.Message', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_highlightcolor_or_highlightbackground(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_command(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE

    def Is_In_orient(self, BuJian_LeiXing_DaXie):
        list = ('Scale_X', 'Scale_Y')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE

# ____________________________________________________________________________________________________________

# BuJian_New(self, BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei)
# 颜色恢复处理类
class Color_Handle:
    # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])
    def Color_Restore(self, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i):
        num_i = Num_i
        KJ = BuJian_LeiXing_DaXie + str(Num_i)

        if self.Judge_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = BuJian_LeiXing_XiaoXie + '_foreground' + str(num_i)
            BuJian_Lei[KJ].config(foreground=BuJian_Lei[name_foreground])

        if self.Judge_background(BuJian_LeiXing_DaXie) == TRUE:
            name_background = BuJian_LeiXing_XiaoXie + '_background' + str(num_i)
            BuJian_Lei[KJ].config(background=BuJian_Lei[name_background])

        if self.Judge_state(BuJian_LeiXing_DaXie) == TRUE:
            BuJian_Lei[KJ].configure(state='normal')

    # 判断是否具有 foreground or background or state
    def Judge_foreground(self, BuJian_LeiXing_DaXie):
        foreground_list = ('Button', 'Checkbutton', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                           'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox', 'Text')
        if BuJian_LeiXing_DaXie in foreground_list:
            return TRUE
        else:
            return FALSE

    def Judge_background(self, BuJian_LeiXing_DaXie):
        background_list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                           'tk.Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox', 'Text')
        if BuJian_LeiXing_DaXie in background_list:
            return TRUE
        else:
            return FALSE

    def Judge_state(self, BuJian_LeiXing_DaXie):   # 注意此处为颜色恢复
        state_list = ('Combobox')
        if BuJian_LeiXing_DaXie in state_list:
            return TRUE
        else:
            return FALSE

# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 完成后，选定处理类
class XuanDing:
    def BuJian_ChuLi(self, i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_Lei,
                     XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y1):
        name = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(i)
        a = BuJian_Lei[name]
        xx0 = a[0]
        yy0 = a[1]
        xx1 = a[2]
        yy1 = a[3]
        Num_i = a[4]

        if ((XuanKuang_X0 <= xx0) and (XuanKuang_Y0 <= yy0) and (XuanKuang_X1 >= xx1) and (XuanKuang_Y1 >= yy1)) \
                and (XuanKuang_X1 != allconfig['XuanKuang_X0']) and (XuanKuang_Y1 != allconfig['XuanKuang_Y0']):
            KJ = str(BuJian_LeiXing_DaXie) + str(i)

            color_handle = Color_Handle()

            if color_handle.Judge_foreground(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(foreground=allconfig['foreground_XiangMu_XuanDing'])
            if color_handle.Judge_background(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(background=allconfig['background_XiangMu_XuanDing'])
            if color_handle.Judge_state(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(state='disabled')

            allconfig['XuanZhong_sum'] = allconfig['XuanZhong_sum'] + 1
            name = "XuanZhong" + str(allconfig['XuanZhong_sum'])
            allconfig['XuanZhong'][name] = (BuJian_Lei[KJ], str(BuJian_LeiXing_DaXie), str(BuJian_LeiXing_XiaoXie), Num_i, BuJian_Lei)


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# Design 部件类
class Design_BuJian:
    def Design_bujian(self, XuanZhong_Object):
        a = XuanZhong_Object
        allconfig['lab_ControlType'] = a[1]
        BuJian_LeiXing_DaXie = a[1]
        BuJian_LeiXing_XiaoXie = a[2]
        BuJian_NO_i = a[3]
        BuJian_Lei = a[4]

        # 每个控件都有的属性 name, coords, container, cusor, width, background
        # ____________________________________________________________________________________________________________
        # ____________________________________________________________________________________________________________
        # 共有属性修改

        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        allconfig['ent_ControlName'] = BuJian_Lei[KJ_name]

        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        allconfig['ent_container'] = BuJian_Lei[name_container]

        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        allconfig['combt_cursor'] = BuJian_Lei[name_cursor]

        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        a = BuJian_Lei[name_coords]
        allconfig['ent_X0'] = a[0]
        allconfig['ent_Y0'] = a[1]

        name_width = str(BuJian_LeiXing_XiaoXie) + '_width' + str(BuJian_NO_i)
        allconfig['ent_width'] = BuJian_Lei[name_width]

        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        allconfig['combt_background'] = BuJian_Lei[name_background]

        # ____________________________________________________________________________________________________________
        # ____________________________________________________________________________________________________________
        # 部分属性
        judge = Judge_Property()

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            allconfig['ent_height'] = BuJian_Lei[name_height]

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            allconfig['ent_length'] = BuJian_Lei[name_length]

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            font = BuJian_Lei[name_font]
            allconfig['combt_fontType'] = font[0]
            allconfig['ent_fontSize'] = font[1]

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            allconfig['combt_foreground'] = BuJian_Lei[name_foreground]

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            allconfig['combt_anchor'] = BuJian_Lei[name_anchor]

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            allconfig['combt_justify'] = BuJian_Lei[name_justify]

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            allconfig['combt_state'] = BuJian_Lei[name_state]

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            allconfig['combt_relief'] = BuJian_Lei[name_relief]

        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            allconfig['combt_highlightcolor'] = BuJian_Lei[name_highlightcolor]

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            allconfig['combt_highlightbackground'] = BuJian_Lei[name_highlightbackground]

        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
            allconfig['combt_bitmap'] = BuJian_Lei[name_bitmap]

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
            allconfig['ent_image'] = BuJian_Lei[name_image]

        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            allconfig['combt_padx'] = BuJian_Lei[name_padx]

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            allconfig['combt_pady'] = BuJian_Lei[name_pady]

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            allconfig['combt_takefocus'] = BuJian_Lei[name_takefocus]

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            allconfig['ent_command'] = BuJian_Lei[name_command]


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# Delete 部件类
class Delete_BuJian:
    def Delete(self, XuanZhong_Object):
        # 记录各个部件类型删除的成员的 列表
        a = XuanZhong_Object
        BuJian_LeiXing_DaXie = a[1]
        BuJian_NO_i = a[3]
        BuJian_Lei = a[4]

        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        BuJian_Lei[KJ].destroy()

        if BuJian_LeiXing_DaXie == 'Button':
            allconfig['Button1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Canvas':
            allconfig['Canvas1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Checkbutton':
            allconfig['Checkbutton1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Combobox':
            allconfig['Combobox1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Entry':
            allconfig['Entry1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Frame':
            allconfig['Frame1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Label':
            allconfig['Label1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'LabelFrame':
            allconfig['LabelFrame1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Listbox':
            allconfig['Listbox1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Message':
            allconfig['Message1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            allconfig['PanedWindow1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            allconfig['PanedWindow1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Radiobutton':
            allconfig['Radiobutton1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Scale_X':
            allconfig['Scale1_List_Num_X'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Scale_Y':
            allconfig['Scale1_List_Num_Y'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            allconfig['PanedWindow1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Spinbox':
            allconfig['Spinbox1_List_Num'].append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Text':
            allconfig['Text1_List_Num'].append(BuJian_NO_i)

 # ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox', 'Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 录入字典类
class Dictionary:
    def Record_Dict(self, BuJian, BuJian_Lei, BuJian_NO_i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie,
                    self_X0, self_Y0, self_X1, self_Y1):
         
        X0 = self_X0
        Y0 = self_Y0
        X1 = self_X1
        Y1 = self_Y1

        allconfig['DangQian_KJ_name']  = str(BuJian_LeiXing_DaXie) + ' ' + str(BuJian_NO_i)

        # ____________________________________________________________________________________________________________
        # 将控件录入字典
        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ] = BuJian
        BuJian_Lei[KJ_name] = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # ____________________________________________________________________________________________________________
        # 具体参数录入
        # 通用属性
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        Zhi = (X0, Y0, X1, Y1, BuJian_NO_i)
        BuJian_Lei[name_coords] = Zhi

        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        Zhi = 'root'
        BuJian_Lei[name_container] = Zhi

        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        Zhi = BuJian.cget('cursor')
        BuJian_Lei[name_cursor] = Zhi

        name_width = str(BuJian_LeiXing_XiaoXie) + '_width' + str(BuJian_NO_i)
        Zhi = BuJian.cget('width')
        BuJian_Lei[name_width] = Zhi

        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        Zhi = BuJian.cget('background')
        BuJian_Lei[name_background] = Zhi

        # ____________________________________________________________________________________________________________
        # 部分属性
        judge = Judge_Property()

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            Zhi = BuJian.cget('length')
            BuJian_Lei[name_length] = Zhi

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            Zhi = BuJian.cget('height')
            BuJian_Lei[name_height] = Zhi

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            str1 = BuJian.cget('font')
            a = Str_ChuLi()
            b = a.FenDuan(str1)
            BuJian_Lei[name_font] = b

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            Zhi = BuJian.cget('foreground')
            BuJian_Lei[name_foreground] = Zhi

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            Zhi = BuJian.cget('anchor')
            BuJian_Lei[name_anchor] = Zhi

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            Zhi = BuJian.cget('justify')
            BuJian_Lei[name_justify] = Zhi

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            Zhi = BuJian.cget('state')
            BuJian_Lei[name_state] = Zhi

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            Zhi = BuJian.cget('relief')
            BuJian_Lei[name_relief] = Zhi

        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            Zhi = BuJian.cget('highlightcolor')
            BuJian_Lei[name_highlightcolor] = Zhi

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            Zhi = BuJian.cget('highlightbackground')
            BuJian_Lei[name_highlightbackground] = Zhi

        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
            Zhi = BuJian.cget('bitmap')
            BuJian_Lei[name_bitmap] = Zhi

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
            Zhi = BuJian.cget('image')
            BuJian_Lei[name_image] = Zhi

        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            Zhi = BuJian.cget('padx')
            BuJian_Lei[name_padx] = Zhi

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            Zhi = BuJian.cget('pady')
            BuJian_Lei[name_pady] = Zhi

        # text
        if judge.Is_In_text(BuJian_LeiXing_DaXie) == TRUE:
            name_text = str(BuJian_LeiXing_XiaoXie) + '_text' + str(BuJian_NO_i)
            Zhi = BuJian.cget('text')
            BuJian_Lei[name_text] = Zhi
            # 组件名显示
            BuJian.config(text=allconfig['DangQian_KJ_name'] )

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            Zhi = BuJian.cget('takefocus')
            BuJian_Lei[name_takefocus] = Zhi

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            Zhi = BuJian.cget('command')
            BuJian_Lei[name_command] = Zhi

        # orient
        if judge.Is_In_orient(BuJian_LeiXing_DaXie) == TRUE:
            name_orient = str(BuJian_LeiXing_XiaoXie) + '_orient' + str(BuJian_NO_i)
            Zhi = BuJian.cget('orient')
            BuJian_Lei[name_orient] = Zhi

        self.Record_Code(BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i)

        # ____________________________________________________________________________________________________________
        # ____________________________________________________________________________________________________________

    def Record_Code(self, BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        # 录入代码
        judge = Judge_Property()
        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ] = BuJian

        # global allconfig['ent_ControlName']
        # if allconfig['ent_ControlName'] != '':
        #     BuJian_Lei[KJ_name] = allconfig['ent_ControlName']
        # else:
        # BuJian_Lei[KJ_name] = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # 通用属性
        # name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)

        if BuJian.cget('cursor') != '':
            cursor_str = str(BuJian.cget('cursor'))
            cursor_str_head = "cursor='"
            cursor_str_tail = "', "
        else:
            cursor_str = ""
            cursor_str_head = ""
            cursor_str_tail = ""

        if BuJian.cget('background') != '':
            background_str = str(BuJian.cget('background'))
            background_str_head = "background='"
            background_str_tail = "', "
        else:
            background_str = ""
            background_str_head = ""
            background_str_tail = ""

        if BuJian.cget('width') != '':
            width_str = str(BuJian.cget('width'))
            width_str_head = "width="
            width_str_tail = ", "
        else:
            width_str = ""
            width_str_head = ""
            width_str_tail = ""

        # 部分属性
        # height
        height_str = ""
        height_str_head = ""
        height_str_tail = ""
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('height') != '':
                height_str = str(BuJian.cget('height'))
                height_str_head = "height="
                height_str_tail = ", "

        # length
        length_str = ""
        length_str_head = ""
        length_str_tail = ""
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('length') != '':
                length_str = str(BuJian.cget('length'))
                length_str_head = "length="
                length_str_tail = ", "

        # font
        font_str = ""
        font_str_head = ""
        font_str_tail = ""
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('font') != '':
                str2 = BuJian.cget('font')
                a = Str_ChuLi()
                b = a.FenDuan(str2)
                font_str = "('" + str(b[0]) + "', " + str(b[1]) + ")"
                font_str_head = "font="
                font_str_tail = ", "

        # foreground
        foreground_str = ""
        foreground_str_head = ""
        foreground_str_tail = ""
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('foreground') != '':
                foreground_str = str(BuJian.cget('foreground'))
                foreground_str_head = "foreground='"
                foreground_str_tail = "', "

        # anchor
        anchor_str = ""
        anchor_str_head = ""
        anchor_str_tail = ""
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('anchor') != '':
                anchor_str = str(BuJian.cget('anchor'))
                anchor_str_head = "anchor='"
                anchor_str_tail = "', "

        # justify
        justify_str = ""
        justify_str_head = ""
        justify_str_tail = ""
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('justify') != '':
                justify_str = str(BuJian.cget('justify'))
                justify_str_head = "justify='"
                justify_str_tail = "', "

        # state
        state_str = ""
        state_str_head = ""
        state_str_tail = ""
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('state') != '':
                state_str = str(BuJian.cget('state'))
                state_str_head = "state='"
                state_str_tail = "', "

        # relief
        relief_str = ""
        relief_str_head = ""
        relief_str_tail = ""
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('relief') != '':
                relief_str = str(BuJian.cget('relief'))
                relief_str_head = "relief='"
                relief_str_tail = "', "

        # highlightcolor and highlightbackground
        highlightcolor_str = ""
        highlightbackground_str = ""
        highlightcolor_str_head = ""
        highlightcolor_str_tail = ""
        highlightbackground_str_head = ""
        highlightbackground_str_tail = ""
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('highlightcolor') != '':
                highlightcolor_str = str(BuJian.cget('highlightcolor'))
                highlightcolor_str_head = "highlightcolor='"
                highlightcolor_str_tail = "', "

            if BuJian.cget('highlightbackground') != '':
                highlightbackground_str = str(BuJian.cget('highlightbackground'))
                highlightbackground_str_head = "highlightbackground='"
                highlightbackground_str_tail = "', "

        # bitmap
        bitmap_photo_str = ""
        bitmap_str_head = ""
        bitmap_str_tail = ""
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('bitmap') != '':
                bitmap_str = str(BuJian.cget('bitmap'))
                bitmap_photo_str = "PhotoImage(file='" + bitmap_str + "'), "
                bitmap_str_head = "bitmap="
                bitmap_str_tail = ", "

        # image
        image_photo_str = ""
        image_str_head = ""
        image_str_tail = ""
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('image') != '':
                image_str = str(BuJian.cget('image'))
                image_photo_str = "PhotoImage(file='" + image_str + "'), "
                image_str_head = "image="
                image_str_tail = ", "

        # padx and pady
        padx_str = ""
        pady_str = ""
        padx_str_head = ""
        padx_str_tail = ""
        pady_str_head = ""
        pady_str_tail = ""
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('padx') != '':
                padx_str = str(BuJian.cget('padx'))
                padx_str_head = "padx="
                padx_str_tail = ", "

            if BuJian.cget('pady') != '':
                pady_str = str(BuJian.cget('pady'))
                pady_str_head = "pady="
                pady_str_tail = ", "

        # text
        text_str = ""
        text_str_head = ""
        text_str_tail = ""
        if judge.Is_In_text(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('text') != '':
                text_str = str(BuJian.cget('text'))
                text_str_head = "text='"
                text_str_tail = "', "

        # takefocus
        takefocus_str = ""
        takefocus_str_head = ""
        takefocus_str_tail = ""
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('takefocus') != '':
                takefocus_str = str(BuJian.cget('takefocus'))
                takefocus_str_head = "takefocus='"
                takefocus_str_tail = "', "

        # command
        command_str = ""
        command_str_head = ""
        command_str_tail = ""
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('command') != '':
                command_str = str(BuJian.cget('command'))
                command_str_head = "command="
                command_str_tail = ""

        # orient
        orient_str = ""
        orient_str_head = ""
        orient_str_tail = ""
        if judge.Is_In_orient(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('orient') != '':
                orient_str = "'" + str(BuJian.cget('orient')) + "'"
                orient_str_head = "orient="
                orient_str_tail = ""

        Control_Lei = ""
        # 判断是否 Scale
        if (BuJian_LeiXing_DaXie == "Scale_X") or (BuJian_LeiXing_DaXie == "Scale_Y"):
            Control_Lei = "Scale"
        else:
            Control_Lei = str(BuJian_LeiXing_DaXie)

        # ____________________________________________________________________________________________________________
        # 生成编辑代码
        # + BuJian_Lei[name_container] + ", " \
        Code1 = BuJian_Lei[KJ_name] + " = " + Control_Lei + "(" \
                + anchor_str_head + anchor_str + anchor_str_tail \
                + cursor_str_head + cursor_str + cursor_str_tail \
                + font_str_head + font_str + font_str_tail \
                + bitmap_str_head + bitmap_photo_str + bitmap_str_tail \
                + justify_str_head + justify_str + justify_str_tail \
                + image_str_head + image_photo_str + image_str_tail \
                + width_str_head + width_str + width_str_tail \
                + height_str_head + height_str + height_str_tail \
                + length_str_head + length_str + length_str_tail \
                + foreground_str_head + foreground_str + foreground_str_tail \
                + background_str_head + background_str + background_str_tail \
                + padx_str_head + padx_str + padx_str_tail \
                + pady_str_head + pady_str + pady_str_tail \
                + relief_str_head + relief_str + relief_str_tail \
                + text_str_head + text_str + text_str_tail \
                + state_str_head + state_str + state_str_tail \
                + takefocus_str_head + takefocus_str + takefocus_str_tail \
                + highlightcolor_str_head + highlightcolor_str + highlightcolor_str_tail \
                + highlightbackground_str_head + highlightbackground_str + highlightbackground_str_tail \
                + orient_str_head + orient_str + orient_str_tail \
                + command_str_head + command_str + command_str_tail + ")"

        ZuJianZB = BuJian_Lei[name_coords]
        Code2 = BuJian_Lei[KJ_name] + ".place(x=" + str(ZuJianZB[0]) + ", " + "y=" + str(ZuJianZB[1]) + ')'

        # 代码录入字典**********************************
        name_Code = str(BuJian_LeiXing_XiaoXie) + '_Code' + str(BuJian_NO_i)
        BuJian_Lei[name_Code] = "    " + "    " + Code1 + "\n" + "    " + "    " + Code2 + '\n\n'

        print(BuJian_Lei[name_Code])

# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 紧耦合模式
# 窗口设置类
class SetCK_D(Toplevel):
    def __init__(self, Parent):
        super().__init__()
        self.title('Win Setup')
        
        

        self.Parent = Parent  # 显式地保留父窗口
        self.Propertys("-topmost", -1)
        self.focus_set()

        w = 800
        h = 500
        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)
        self.resizable(width=False, height=False)

        # 参数设置
        self.Tv_ck_width = canva_W
        self.Tv_ck_height = canva_H

        self.Font = ('Consol', '12')

        self.Set_UI()

    def Set_UI(self):
        self.JG_x = 210
        # ____________________________________________________________________________________________________________

        self.Lab_ck_name = Label(self, text='Interface Name', font=self.Font)
        self.Lab_ck_name.place(x=0, y=6)

        self.Tv_ck_name = StringVar()
        self.Ent_ck_name = Entry(self, textvariable=self.Tv_ck_name, font=self.Font, width=25)
        self.Ent_ck_name.place(x=self.JG_x, y=6)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_width = Label(self, text='Interface Width', font=self.Font)
        self.Lab_ck_width.place(x=0, y=6 + 40)

        self.Lab_ck_width = Label(self, text=self.Tv_ck_width, font=self.Font, width=25, bg='DeepSkyBlue')
        self.Lab_ck_width.place(x=self.JG_x, y=6 + 40)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_height = Label(self, text='Interface Height', font=self.Font)
        self.Lab_ck_height.place(x=0, y=6 + 80)

        self.Lab_ck_height = Label(self, text=self.Tv_ck_height, font=self.Font, width=25, bg='DeepSkyBlue')
        self.Lab_ck_height.place(x=self.JG_x, y=6 + 80)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_init_x = Label(self, text='Initial X coordinate', font=self.Font)
        self.Lab_ck_init_x.place(x=0, y=120)

        self.Tv_ck_init_x = StringVar()
        self.Ent_ck_init_x = Entry(self, textvariable=self.Tv_ck_init_x, font=self.Font, width=25)
        self.Ent_ck_init_x.place(x=self.JG_x, y=120)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_init_y = Label(self, text='Initial Y coordinate', font=self.Font)
        self.Lab_ck_init_y.place(x=0, y=160)

        self.Tv_ck_init_y = StringVar()
        self.Ent_ck_init_y = Entry(self, textvariable=self.Tv_ck_init_y, font=self.Font, width=25)
        self.Ent_ck_init_y.place(x=self.JG_x, y=160)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_width_not_change = Label(self, text='Is width not changeable', font=self.Font)
        self.Lab_ck_is_width_not_change.place(x=0, y=200)

        self.Tv_ck_is_width_not_change = IntVar()
        self.Rad_ck_is_width_not_change1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_width_not_change, value=1)
        self.Rad_ck_is_width_not_change2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_width_not_change, value=2)

        self.Rad_ck_is_width_not_change1.place(x=self.JG_x + 30, y=200)
        self.Rad_ck_is_width_not_change2.place(x=self.JG_x + 120, y=200)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_height_not_change = Label(self, text='Is height not changeable', font=self.Font)
        self.Lab_ck_is_height_not_change.place(x=0, y=240)

        self.Tv_ck_is_height_not_change = IntVar()
        self.Rad_ck_is_height_not_change1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_height_not_change, value=1)
        self.Rad_ck_is_height_not_change2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_height_not_change, value=2)

        self.Rad_ck_is_height_not_change1.place(x=self.JG_x + 30, y=240)
        self.Rad_ck_is_height_not_change2.place(x=self.JG_x + 120, y=240)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_minsize = Label(self, text='Is minsize interface', font=self.Font)
        self.Lab_ck_is_minsize.place(x=0, y=280)

        self.Lab_ck_is_minsize = Label(self, text='X', font=self.Font)
        self.Lab_ck_is_minsize.place(x=160 + 70, y=320)

        self.Tv_ck_is_minsize = IntVar()
        self.Rad_ck_is_minsize1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_minsize, value=1)
        self.Rad_ck_is_minsize2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_minsize, value=2)

        self.Rad_ck_is_minsize1.place(x=self.JG_x + 30, y=280)
        self.Rad_ck_is_minsize2.place(x=self.JG_x + 120, y=280)

        self.Tv_ck_init_minsize_w = StringVar()
        self.Ent_ck_init_minsize_w = Entry(self, textvariable=self.Tv_ck_init_minsize_w, font=self.Font, width=18)
        self.Ent_ck_init_minsize_w.place(x=6 + 70, y=320)

        self.Tv_ck_init_minsize_h = StringVar()
        self.Ent_ck_init_minsize_h = Entry(self, textvariable=self.Tv_ck_init_minsize_h, font=self.Font, width=18)
        self.Ent_ck_init_minsize_h.place(x=180 + 70, y=320)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_maxsize = Label(self, text='Is maxsize interface', font=self.Font)
        self.Lab_ck_is_maxsize.place(x=0, y=360)

        self.Lab_ck_is_maxsize = Label(self, text='X', font=self.Font)
        self.Lab_ck_is_maxsize.place(x=160 + 70, y=400)

        self.Tv_ck_is_maxsize = IntVar()
        self.Rad_ck_is_maxsize1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_maxsize, value=1)
        self.Rad_ck_is_maxsize2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_maxsize, value=2)

        self.Rad_ck_is_maxsize1.place(x=self.JG_x + 30, y=360)
        self.Rad_ck_is_maxsize2.place(x=self.JG_x + 120, y=360)

        self.Tv_ck_init_maxsize_w = StringVar()
        self.Ent_ck_init_maxsize_w = Entry(self, textvariable=self.Tv_ck_init_maxsize_w, font=self.Font, width=18)
        self.Ent_ck_init_maxsize_w.place(x=6 + 70, y=400)

        self.Tv_ck_init_maxsize_h = StringVar()
        self.Ent_ck_init_maxsize_h = Entry(self, textvariable=self.Tv_ck_init_maxsize_h, font=self.Font, width=18)
        self.Ent_ck_init_maxsize_h.place(x=180 + 70, y=400)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_toolwindow = Label(self, text='Is interface toolwindow', font=self.Font)
        self.Lab_ck_is_toolwindow.place(x=0, y=440)

        self.Tv_ck_is_toolwindow = IntVar()
        self.Rad_ck_is_toolwindow1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_toolwindow, value=1)
        self.Rad_ck_is_toolwindow2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_toolwindow, value=2)

        self.Rad_ck_is_toolwindow1.place(x=self.JG_x + 30, y=440)
        self.Rad_ck_is_toolwindow2.place(x=self.JG_x + 120, y=440)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_topmost = Label(self, text='Is interface topmost', font=self.Font)
        self.Lab_ck_is_topmost.place(x=self.JG_x + 230, y=6)

        self.Tv_ck_is_topmost = IntVar()
        self.Rad_ck_is_topmost1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_topmost, value=1)
        self.Rad_ck_is_topmost2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_topmost, value=2)

        self.Rad_ck_is_topmost1.place(x=self.JG_x + 430, y=6)
        self.Rad_ck_is_topmost2.place(x=self.JG_x + 520, y=6)

        # ____________________________________________________________________________________________________________

        self.Lab_ck_is_zoomed = Label(self, text='Is  initial zoomed', font=self.Font)
        self.Lab_ck_is_zoomed.place(x=self.JG_x + 230, y=6 + 40)

        self.Tv_ck_is_zoomed = IntVar()
        self.Rad_ck_is_zoomed1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_zoomed, value=1)
        self.Rad_ck_is_zoomed2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_zoomed, value=2)

        self.Rad_ck_is_zoomed1.place(x=self.JG_x + 430, y=6 + 40)
        self.Rad_ck_is_zoomed2.place(x=self.JG_x + 520, y=6 + 40)

        # ____________________________________________________________________________________________________________
        # 窗口透明度

        self.Lab_ck_is_transparency = Label(self, text='Interface transparency', font=self.Font)
        self.Lab_ck_is_transparency.place(x=self.JG_x + 230, y=6 + 80)

        self.Tv_ck_is_transparency = IntVar()
        self.Rad_ck_is_transparency1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_transparency, value=1)
        self.Rad_ck_is_transparency2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_transparency, value=2)

        self.Rad_ck_is_transparency1.place(x=self.JG_x + 430, y=6 + 80)
        self.Rad_ck_is_transparency2.place(x=self.JG_x + 520, y=6 + 80)

        self.V_Scal_ck_is_transparency = DoubleVar()
        self.Scal_ck_is_transparency = Scale(self, from_=0, to=1, orient=HORIZONTAL,
                                             variable=self.V_Scal_ck_is_transparency,
                                             length=330, width=10, resolution=0.01)
        self.Scal_ck_is_transparency.place(x=self.JG_x + 230, y=6 + 110)

        # ____________________________________________________________________________________________________________
        # 窗口图标

        self.Lab_ck_set_icon = Label(self, text='Set interface icon', font=self.Font)
        self.Lab_ck_set_icon.place(x=self.JG_x + 230, y=6 + 160)

        self.Tv_ck_set_icon = StringVar()
        self.Ent_ck_set_icon = Entry(self, textvariable=self.Tv_ck_set_icon, font=self.Font, width=36)
        self.Ent_ck_set_icon.place(x=self.JG_x + 230, y=6 + 200)

        self.Btn_ck_set_icon = Button(self, text='...', font=('Consol', '10'), width=6, height=1,
                                      command=self.More_Icon)
        self.Btn_ck_set_icon.place(x=self.JG_x + 530, y=6 + 196)

        # ____________________________________________________________________________________________________________
        # 窗口网格宽度

        self.Lab_ck_set_grid = Label(self, text='Set the grid width', font=self.Font)
        self.Lab_ck_set_grid.place(x=self.JG_x + 230, y=6 + 240)

        self.Tv_ck_set_grid = IntVar()
        self.Comb_ck_set_grid = ttk.Combobox(self, width=23, textvariable=self.Tv_ck_set_grid)

        self.Comb_ck_set_grid['values'] = (10, 20, 30, 40, 50, 60)
        self.Comb_ck_set_grid.place(x=self.JG_x + 400, y=6 + 240)
        self.Comb_ck_set_grid.current(1)

        # ____________________________________________________________________________________________________________
        # ____________________________________________________________________________________________________________
        # 确定或取消键

        self.Lab_OK = Label(self, text='____________________________________________', font=('Consol', '16'))
        self.Lab_OK.place(x=self.JG_x + 230, y=6 + 280)

        self.Btn_ck_OK = Button(self, text='OK', font=('Consol', '13'), width=6, height=1, command=self.CK_OK)
        self.Btn_ck_OK.place(x=self.JG_x + 300, y=6 + 450)

        self.Btn_ck_Cancel = Button(self, text='Cancel', font=('Consol', '13'), width=6, height=1,
                                    command=self.CK_Cancel)
        self.Btn_ck_Cancel.place(x=self.JG_x + 430, y=6 + 450)

    def More_Icon(self):
        w = 800
        h = 500
        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2 + 600, (S_height - h) / 2 - 30)
        self.geometry(size)

        get_more_icon = Get_File_Name_GIF()
        icon = get_more_icon.Get_Name()
        self.Tv_ck_set_icon.set(icon)

        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)


    def CK_OK(self):
        allconfig['ck_name'] = self.Ent_ck_name.get()
        allconfig['ck_name'] = self.Tv_ck_init_x.get()
        allconfig['ck_init_y'] = self.Tv_ck_init_y.get()
        allconfig['ck_is_width_not_change'] = self.Tv_ck_is_width_not_change.get()
        allconfig['ck_is_height_not_change'] = self.Tv_ck_is_height_not_change.get()
        allconfig['ck_is_minsize'] = self.Tv_ck_is_minsize.get()
        allconfig['ck_init_minsize_w'] = self.Tv_ck_init_minsize_w.get()
        allconfig['ck_init_minsize_h'] = self.Tv_ck_init_minsize_h.get()
        allconfig['ck_is_maxsize'] = self.Tv_ck_is_maxsize.get()
        allconfig['ck_init_maxsize_w'] = self.Tv_ck_init_maxsize_w.get()
        allconfig['ck_init_maxsize_h'] = self.Tv_ck_init_maxsize_h.get()
        allconfig['ck_is_toolwindow'] = self.Tv_ck_is_toolwindow.get()
        allconfig['ck_is_topmost'] = self.Tv_ck_is_topmost.get()
        allconfig['ck_is_zoomed'] = self.Tv_ck_is_zoomed.get()
        allconfig['ck_is_transparency'] = self.Tv_ck_is_transparency.get()
        allconfig['ck_scal_transparency'] = self.V_Scal_ck_is_transparency.get()
        allconfig['ck_set_icon'] = self.Tv_ck_set_icon.get()
        allconfig['ck_set_grid'] = self.Tv_ck_set_grid.get()

        line_next = "\n"

        Str_Import = "# Use the PyUI to Design UI"\
        + """
# © JY.Lin 
from tkinter import *
from tkinter import ttk  # (when you want to use ttk)
from tkinter.scrolledtext import ScrolledText  # (when you want to use scrolledtext)
from tkinter.messagebox import *  # (when you want to use messagebox)
import tkinter.colorchooser  # (when you want to use colorchooser)
import tkinter.filedialog  # (when you want to use filedialog)
import tkinter as tk  # (when you want to use the short-call)
""" \

        if self.Ent_ck_name.get() == '':
            allconfig['ck_name'] = "PyUI"
        # self.title('PyUI')
        Str_Main_CK = "class " + str(allconfig['ck_name']) + "(Tk):" + line_next \
                      + allconfig['tap'] + "def __init__(self): " + line_next \
                      + allconfig['tap'] + allconfig['tap'] + "super().__init__() " + line_next\
                      + allconfig['tap'] + allconfig['tap'] + "self.title(\"" + str(allconfig['ck_name']) + "\")" + line_next

        if allconfig['ck_name'] == '':
            allconfig['ck_name'] = 0
        if allconfig['ck_init_y'] == 0:
            allconfig['ck_init_y'] = 0

        # ____________________________________________________________________________________________________________
        if allconfig['zi_menu1_sum'] == 0:
            allconfig['Distance'] = allconfig['bar_W']
        else:
            allconfig['Distance'] = allconfig['bar_W'] + allconfig['bar_menu_W']
        # ____________________________________________________________________________________________________________

        Str_Coords = allconfig['tap'] + allconfig['tap'] + "S_width = self.winfo_screenwidth()" + line_next \
                     + allconfig['tap'] + allconfig['tap'] + "S_height = self.winfo_screenwidth()" + line_next \
                     + allconfig['tap'] + allconfig['tap'] + "Size = '%dx%d+%d+%d' % (" + str(allconfig['canva_W']) + ", " + str(allconfig['canva_W']-allconfig['Distance']) + ", " + "(S_width - " + str(allconfig['canva_W']) + ") /2, "\
                     + "(S_height - " + str(allconfig['canva_W']-allconfig['Distance']) + ") /2)" + line_next \
                     + allconfig['tap'] + allconfig['tap'] + "self.geometry(Size)" + line_next

        Str_width_height_change = ''

        if allconfig['ck_is_width_not_change'] == 1:
            if allconfig['ck_is_height_not_change'] == 1:
                pass
            elif allconfig['ck_is_height_not_change'] == 2:
                Str_width_height_change = allconfig['tap'] + allconfig['tap'] + "self.resizable(width=TRUE, height=False)" + line_next

        elif allconfig['ck_is_width_not_change'] == 2:
            if allconfig['ck_is_height_not_change'] == 1:
                Str_width_height_change = allconfig['tap'] + allconfig['tap'] + "self.resizable(width=False, height=TRUE)" + line_next

            elif allconfig['ck_is_height_not_change'] == 2:
                Str_width_height_change = allconfig['tap'] + allconfig['tap'] + "self.resizable(width=False, height=False)" + line_next


        if allconfig['ck_is_minsize'] == 1:
            Str_Min_Size = allconfig['tap'] + allconfig['tap'] + "Min_W = " + str(ck_init_minsize_w) + line_next \
                           + allconfig['tap'] + allconfig['tap'] + "Min_H = " + str(ck_init_minsize_h) + line_next \
                           + allconfig['tap'] + allconfig['tap'] + "self.minsize(Min_W, Min_H)" + line_next
        else:
            Str_Min_Size = ""


        if allconfig['ck_is_maxsize'] == 1:
            Str_Max_Size = allconfig['tap'] + allconfig['tap'] + "Max_W = " + str(ck_init_maxsize_w) + line_next\
                         + allconfig['tap'] + allconfig['tap'] + "Max_H = " + str(ck_init_maxsize_h) + line_next\
                         + allconfig['tap'] + allconfig['tap'] + "self.maxsize(Max_W, Max_H)" + line_next
        else:
            Str_Max_Size = ""


        if allconfig['ck_is_toolwindow'] == 1:
            Str_is_toolwindow = allconfig['tap'] + allconfig['tap'] + "self.Propertys(\"-toolwindow\", 1)" + line_next
        else:
            Str_is_toolwindow = ''


        if allconfig['ck_is_topmost'] == 1:
            Str_is_topmost = allconfig['tap'] + allconfig['tap'] + "self.Propertys(\"-topmost\", 1)" + line_next
        else:
            Str_is_topmost = ''


        if allconfig['ck_is_zoomed'] == 1:
            Str_is_zoomed = allconfig['tap'] + allconfig['tap'] + "self.state(\"zoomed\")" + line_next
        else:
            Str_is_zoomed = ''


        if allconfig['ck_is_transparency'] == 1:
            Str_is_transparency = allconfig['tap'] + allconfig['tap'] + "self.Propertys(\"-alpha\", " + str(ck_scal_transparency) + ")" + line_next
        else:
            Str_is_transparency = ''


        if allconfig['ck_set_icon'] == 1:
            Str_set_icon = allconfig['tap'] + allconfig['tap'] + "self.iconbitmap('" + str(ck_set_icon) + "')" + line_next
        else:
            Str_set_icon = ''

        allconfig['WangGe_KuanDu']  = int(ck_set_grid)

        Str_set_UI = allconfig['tap'] + allconfig['tap'] + "self.SetUI()" + line_next

        Str_def_UI = allconfig['tap'] + "def SetUI(self):" + line_next

        # 编译汇总
        allconfig['Str_BianYi'] = Str_Import + line_next + Str_Main_CK + Str_Coords + Str_width_height_change  \
                     + Str_Min_Size + Str_Max_Size + Str_is_toolwindow + Str_is_topmost + Str_is_zoomed \
                     + Str_is_transparency + Str_set_icon + Str_set_UI + line_next + Str_def_UI

        allconfig['Str_BianYi_End'] = line_next \
                         + "if __name__ == '__main__':" + line_next \
                         + allconfig['tap'] + "PyPa = " + str(allconfig['ck_name']) + "()" + line_next \
                         + allconfig['tap'] + "PyPa.SetUI()" + line_next \
                         + allconfig['tap'] + "PyPa.mainloop()" + line_next
        self.destroy()


    def CK_Cancel(self):
        self.destroy()




# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# name = "XuanZhong" + str(XuanZhong_sum)
# allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])
class SJ_Dictionary:
    def SJ_Dict(self, str_SJ):
        if allconfig['XuanZhong_sum'] == 1:
            # name = "XuanZhong" + str(XuanZhong_sum)
            # allconfig['XuanZhong'][name] = (allconfig['Button1'][KJ], 'Button', 'button', Num_i, allconfig['Button1'])
            # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
            # BuJian_Lei[KJ] = BuJian
            # 控件.bind('<事件代码>', event_handler)

            name = "XuanZhong" + str(1)

            xuan = allconfig['XuanZhong'][name]
            BuJian_LeiXing_XiaoXie = xuan[2]
            BuJian_NO_i = xuan[3]
            BuJian_Lei = xuan[4]
            if str_SJ == "button_press_1":
                SJ_code = "1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_1'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)

                # a = allconfig['SJ_button_press_1'][KJ_name]
                # print(str(a[0]))


            elif str_SJ == "button_release_1":
                SJ_code = "ButtonRelease-1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_release_1'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_right_1":
                SJ_code = "3"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_right_1'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_left_2":
                SJ_code = "Double-1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_left_2'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_right_2":
                SJ_code = "Double-3"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_right_2'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_middle_1":
                SJ_code = "2"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_middle_1'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_middle_2":
                SJ_code = "	Double-2"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_middle_2'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)



            elif str_SJ == "button_press_left_move":
                SJ_code = "	B1-Motion"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_button_press_left_move'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "cursor_enter":
                SJ_code = "Enter"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_cursor_enter'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "cursor_leave":
                SJ_code = "Leave"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_cursor_leave[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "get_key_focus":
                SJ_code = "FocusIn"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_get_key_focus'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "lose_key_focus":
                SJ_code = "FocusOut"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_lose_key_focus'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "press_a_key":
                SJ_code = "Key"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_press_a_key'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "press_enter_key":
                SJ_code = "Return"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_press_enter_key'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "when_control_change":
                SJ_code = "Configure"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_when_control_change'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "control_mouseWheel":
                SJ_code = "Control-MouseWheel"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_shift_mouseWheel'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "shift_mouseWheel":
                SJ_code = "Shift-MouseWheel"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                allconfig['SJ_shift_mouseWheel'][KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 判断类
class Judge:
    def Judge_If_Delete(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        if BuJian_LeiXing_XiaoXie == "button":
            if BuJian_NO_i in allconfig['Button1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "canvas":
            if BuJian_NO_i in allconfig['Canvas1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "checkbutton":
            if BuJian_NO_i in allconfig['Checkbutton1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "combobox":
            if BuJian_NO_i in allconfig['Combobox1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "entry":
            if BuJian_NO_i in allconfig['Entry1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "frame":
            if BuJian_NO_i in allconfig['Frame1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "label":
            if BuJian_NO_i in allconfig['Label1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "labelFrame":
            if BuJian_NO_i in allconfig['LabelFrame1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "listbox":
            if BuJian_NO_i in allconfig['Listbox1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "menu":
            if BuJian_NO_i in allconfig['Menu1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "message":
            if BuJian_NO_i in allconfig['Message1_List_Num']:
                return TRUE
            else:
                return FALSE


        if BuJian_LeiXing_XiaoXie == "panedWindow":
            if BuJian_NO_i in allconfig['PanedWindow1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "radiobutton":
            if BuJian_NO_i in allconfig['Radiobutton1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "scale_x":
            if BuJian_NO_i in allconfig['Scale1_List_Num_X']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "scale_y":
            if BuJian_NO_i in allconfig['Scale1_List_Num_Y']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "spinbox":
            if BuJian_NO_i in allconfig['Spinbox1_List_Num']:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "text":
            if BuJian_NO_i in allconfig['Text1_List_Num']:
                return TRUE
            else:
                return FALSE

# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# 事件处理类
class SJ_ChuLi:
    def SJ_Bian_Yi(self, SJ_Dictionary, Text_1):
        judge = Judge()
        allconfig['tap'] = "    "
        for i in SJ_Dictionary:
            a = SJ_Dictionary[i]
            sj_code = allconfig['tap'] + allconfig['tap'] + a[0] + a[1] + "\n"
            BuJian_LeiXing_XiaoXie = a[2]
            BuJian_NO_i = a[3]
            if judge.Judge_If_Delete(BuJian_LeiXing_XiaoXie, BuJian_NO_i) == FALSE:
                Text_1.insert(END, sj_code)

    # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
    # BuJian_Lei[KJ_name]
    def SJ_New(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i, BuJian_Lei):
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        SJ_Dictionary_Zong = (allconfig['SJ_button_press_1'],
            allconfig['SJ_button_release_1'],
            allconfig['SJ_button_press_right_1'],
            allconfig['SJ_button_press_left_2'],
            allconfig['SJ_button_press_right_2'],
            allconfig['SJ_button_press_middle_1'],
            allconfig['SJ_button_press_middle_2'],
            allconfig['SJ_button_press_left_move'],
            allconfig['SJ_cursor_enter'],
            allconfig['SJ_cursor_leave'],
            allconfig['SJ_get_key_focus'],
            allconfig['SJ_lose_key_focus'],
            allconfig['SJ_press_a_key'],
            allconfig['SJ_press_enter_key'],
            allconfig['SJ_when_control_change'],
            allconfig['SJ_press_space_key'],
            allconfig['SJ_shift_mouseWheel'],
            allconfig['SJ_press_combinatorial_key'])

        for SJ_Dictionary in SJ_Dictionary_Zong:
            for i in SJ_Dictionary:
                a = SJ_Dictionary[i]
                SJ_LeiXing_XiaoXie = a[2]
                SJ_NO_i = a[3]
                if SJ_LeiXing_XiaoXie == BuJian_LeiXing_XiaoXie:
                    if SJ_NO_i == BuJian_NO_i:
                        SJ_Dictionary[i] = (BuJian_Lei[KJ_name], a[1], a[2], a[3])


# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________
# menu string 生成类
class Menu_Str:
    def Menu_Str(self):
        allconfig['Str_Menu'] = ""
        str_bar = allconfig['tap'] + allconfig['tap'] + "Menubar = Menu(self)" + "\n"

        # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
        for i in range(1, allconfig['zi_menu1_sum']    +1, 1):
            zi_menu_tearoff_name = "zi_menu_tearoff_name" + str(i)
            zi_menu_add_cascade_name = "zi_menu_add_cascade_name" + str(i)
            tearoff = allconfig['Menu1'][zi_menu_tearoff_name]
            add_cascade = allconfig['Menu1'][zi_menu_add_cascade_name]

            Code_tearoff = allconfig['tap'] + allconfig['tap'] + tearoff[0] + "\n"
            Code_add_cascade = allconfig['tap'] + allconfig['tap'] + add_cascade[0]
            Str_list = ""

            for mlist_j in allconfig['Menu1_ListCode']:
                # allconfig['Menu1_ListCode'][menu_list_code_name] = (Code, allconfig['zi_menu1_sum'], zong+1)
                menu_list = allconfig['Menu1_ListCode'][mlist_j]
                if i == menu_list[1]:
                    Str_list = Str_list + allconfig['tap'] + allconfig['tap'] + menu_list[0] + "\n"

            Str_son_menu = Code_tearoff + Str_list + Code_add_cascade

            allconfig['Str_Menu'] = allconfig['Str_Menu'] + Str_son_menu + "\n"

        Str_Conifg = "\n" + allconfig['tap'] + allconfig['tap'] + "self.config(menu=Menubar)" + "\n\n"

        allconfig['Str_Menu'] = str_bar + "\n" + allconfig['Str_Menu'] + Str_Conifg

        return allconfig['Str_Menu']

# ____________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________


if __name__ == '__main__':
    PypA = PyUI()
    PypA.HuaBu_YiDong()

    PypA.mainloop()










