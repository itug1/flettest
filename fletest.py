import flet as ft

#def main(page: ft.Page):
    
#    t= ft.Text(value="hello",color="red")   #txtコントロール（t）
#    page.controls.append(t)                #tをページに追加
#    page.update()                           #ページを更新

#ft.app(target=main)

def main(page: ft.Page):


#イベントを追加
    def btn_click(e):
        line.controls.append(ft.Text(f"URL   : {URL.value}\nSerial: {Serial.value}", font_family="Consolas"))
        URL.value       = ""
        Serial.value    = ""
        Button.disabled = True
        page.update()

    def submit1(e):
        Serial.focus()

    def submit2(e):
        Button.focus()

    def long_click(e):
        Button.text     = "♡"
        page.update()

    def change(e):
        Button.disabled = False
        page.update()
        

#pageのプロパティ
    page.title              = "CSPサービス開始のご案内ツール"
    page.window.center()
    page.window.width       = 480
    page.window.height      = 360
    page.window.minimizable = False
    page.window.maximizable = False
    page.window.resizable   = False
    page.window.opacity     = 0.97

#Control追加
    URL     = ft.TextField(
        label       ="URL",
        autofocus   =True,
        on_submit   = submit1,
        on_change   = change,
        )
    
    Serial  = ft.TextField(
        label       ="SerialNumber (option)",
        on_submit   =submit2,
        on_change   = change,
        )
    
    line    = ft.Column(
        width       = 460,
        height      = 120,
        scroll      = ft.ScrollMode.ALWAYS,
        auto_scroll = True
        )
    
    Button  = ft.ElevatedButton(
        text            = "Go",
        on_click        = btn_click,
        on_long_press   = long_click,        
        width           = 460
    )
    
#pageに追加

    page.add(
        URL,
        Serial,
        Button,
        line,
    )

ft.app(target=main)