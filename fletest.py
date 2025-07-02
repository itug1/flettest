import flet as ft
import csv
import os
import tkinter as tk
from tkinter import ttk
import random
import time

csvpath = os.getcwd()
print(csvpath)
csvpath2 = csvpath+r"/hamu.csv"
print(csvpath2)
csvpath2 = r"C:\Python\hamugo\hamu.csv"
with open(csvpath2, encoding="shift-jis") as file:
    lsts = list(csv.reader(file))
s = 0
CONTAINER_HEIGHT=900
CONTAINER_WIDTH=540

    #print(lsts)

#def main(page: ft.Page):
    
#    t= ft.Text(value="hello",color="red")   #txtコントロール（t）
#    page.controls.append(t)                #tをページに追加
#    page.update()                           #ページを更新

#ft.app(target=main)

def main(page: ft.Page):
#イベント
    def sort_1(e):
        i = 0
        while i <= 264:
            print(i)
            print(f"読み{lsts[i]}")
            i+=1
            print(f"意味{lsts[i]}")
            i+=1
    def rot(e):
        if page.theme == ft.Theme(color_scheme_seed="orange"):
            page.theme = ft.Theme(color_scheme_seed="red")
        elif page.theme == ft.Theme(color_scheme_seed="red"):
            page.theme = ft.Theme(color_scheme_seed="purple")
        elif page.theme == ft.Theme(color_scheme_seed="purple"):
            page.theme = ft.Theme(color_scheme_seed="blue")
        elif page.theme == ft.Theme(color_scheme_seed="blue"):
            page.theme = ft.Theme(color_scheme_seed="green")
        elif page.theme == ft.Theme(color_scheme_seed="green"):
            page.theme = ft.Theme(color_scheme_seed="orange")
        page.update()
    def lod(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            text_q.color="#000000"
            text_a.color="#000000"
        else:
            page.theme_mode = "dark"
            text_q.color="#FFFFFF"
            text_a.color="#FFFFFF"
        page.update()
    def show_ans(e):
        if text_a.visible:
            text_a.visible=False
        else:
            text_a.visible=True
        page.update()
    def show_nex(e):
        if page.theme_mode == "dark":
            text_q.color="#FFFFFF"
            text_a.color="#FFFFFF"
        elif page.theme_mode == "light":
            text_q.color="#000000"
            text_a.color="#000000"
        text_a.visible=False
        butt_a.disabled=False
        butt_n.disabled=False
        RNG = random.randint(0,131)
        RNG2 = random.randint(1,65)
        text_q.value=f"{lsts[RNG][1]}"
        text_a.value=f"{lsts[RNG][2]}"
        if (RNG == 131) or (RNG2 == 65) :
            print(RNG,RNG2)
            text_a.visible=True
            text_q.value="・・・"
            text_a.value="・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・"
            butt_a.disabled=True
            text_q.color="#B90000"
            text_a.color="#B90000"
        page.update()

#pageのプロパティ
    page.title                      = "Cール"
    page.window.center()
    page.window.width               = 576
    page.window.height              = 1024
    page.window.minimizable         = False
    page.window.maximizable         = False
    page.window.resizable           = False
    page.window.opacity             = 0.97
    page.theme                      = ft.Theme(color_scheme_seed="orange")
    page.theme_mode                 = "dark"

#Control追加

    dt_cols     = []
    for col in ["単語","意味","単語","意味"]:
        dt_cols.append(ft.DataColumn(ft.Text(col)))
    dt_rows     = []
    i = 0
    while True:
        dt_rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(lsts[i][1])),
            ft.DataCell(ft.Text(lsts[i][2])),
            ft.DataCell(ft.Text(lsts[i+1][1])),
            ft.DataCell(ft.Text(lsts[i+1][2])),
            ]))
        i+=2
        if i==132:
            break
    datatable   = ft.DataTable(
        columns = dt_cols,
        rows    = dt_rows,
        divider_thickness=2,
        vertical_lines=ft.border.BorderSide(1,"#42464d2f"),        
    )
    listview    = ft.ListView([datatable],expand=0, spacing=0, padding=0)
    row= ft.Row([
        ft.Container(
            content=listview,
            border=ft.border.all(1),
            height=CONTAINER_HEIGHT,
            width=CONTAINER_WIDTH,
        ),
    ],
    scroll="auto"
    )
    tatesen     = ft.Container(
        bgcolor         = "#42464d",
        border_radius   = ft.border_radius.all(30),
        height          = 900,
        width           = 2,
        top             = 0,
        left            = 255,
    )
    stack = ft.Stack([
        row,tatesen
    ])
################################################################tab2
    dt_cols2     = []
    for col2 in ["単語","意味","単語","意味"]:
        dt_cols2.append(ft.DataColumn(ft.Text(col2)))
    dt_rows2     = []
    i = 132
    while True:
        dt_rows2.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(lsts[i][1])),
            ft.DataCell(ft.Text(lsts[i][2])),
            ft.DataCell(ft.Text(lsts[i+1][1])),
            ft.DataCell(ft.Text(lsts[i+1][2])),
            ]))
        i+=2
        if i==264:
            break
    datatable2   = ft.DataTable(
        columns = dt_cols2,
        rows    = dt_rows2,
        divider_thickness=2,
        vertical_lines=ft.border.BorderSide(1,"#42464d2f"),        
    )
    listview2    = ft.ListView([datatable2],expand=0, spacing=0, padding=0)
    row2= ft.Row([
        ft.Container(
            content=listview2,
            border=ft.border.all(1),
            height=CONTAINER_HEIGHT,
            width=CONTAINER_WIDTH,
        ),
    ],
    scroll="auto"
    )
    tatesen2     = ft.Container(
        bgcolor         = "#42464d",
        border_radius   = ft.border_radius.all(30),
        height          = 900,
        width           = 2,
        top             = 0,
        left            = 265,
    )    
    stack2 = ft.Stack([
        row2,tatesen2
    ])
#########################################################################tab3
    butt_rot = ft.IconButton(icon=ft.Icons.COLOR_LENS,on_click=rot, icon_size=20,top=0,left=450)
    butt_lod = ft.IconButton(icon=ft.Icons.WB_TWILIGHT,on_click=lod, icon_size=20,top=0,left=500)
    text_q      = ft.Text("ハム語帳",size=84,color="#FFFFFF",
                          top=120)
    text_a      = ft.Text("ああああああ",size=40,visible=False,color="#FFFFFF",
                          top=240)
    butt_a      = ft.Button("答へ",height=50,width=540,on_click=show_ans,
                            top=360)
    butt_n      = ft.Button("次え",height=50,width=540,on_click=show_nex,
                            top=480)
    stack3 = ft.Stack([
        text_q,text_a,butt_a,butt_n,butt_lod,butt_rot
    ])
#pageに追加
    t1 = ft.Column(
        [
            stack,
        ]
    )
    t2 = ft.Column(
        [
            stack2,
        ]
    )
    t3 = ft.Column(
        [
           stack3 
        ]
    )
    tab1 = ft.Tab(text="単語順",content=t1)
    tab2 = ft.Tab(text="意味順",content=t2)
    tab3 = ft.Tab(text="あ",content=t3)
    t=ft.Tabs(
        selected_index=2,
        indicator_thickness=10,
        animation_duration=400,
        indicator_tab_size=False,
        tabs=[tab1,tab2,tab3],
        expand=0
    )
    page.add(
        t
    )

ft.app(target=main)