## 【お願い】このファイルを実行して、お使いください。

# モジュールをimport
import pyqrcode as qr
import PySimpleGUI as sg
import shutil
import os
from tkinter import messagebox

# それぞれのファイルをimport
import urlQR
import mixQR
import textQR

# メイン画面設定　※それぞれの画面設定は各ファイルに記載
def main():
    main_layout = [ [sg.Text('MyQR', font=('Arial',15))],
                    [sg.Text('自分用のQRコードを作成できます。\nご利用になる目的に応じてボタンをクリックしてください。')],
                    [sg.Button('URLをQRに', image_filename="", key='urlQR'), sg.Button('まとめてQRに', key='mixQR'), sg.Button('文章をQRに', key='textQR')],
                ]

    return sg.Window('MyOR', main_layout, size=(500, 330))

# 初期画面
sg.theme('LightGrey1')
window = main()

# イベント処理
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # 押されたボタンに応じて画面遷移
    # 前の画面は閉じる
    if event == 'urlQR':
        window.close()
        window = urlQR.url_main()
    
    elif event == 'mixQR':
        window.close()
        window = mixQR.mix_main()

    elif event == 'textQR':
        window.close()
        window = textQR.text_main()
    #「戻る」ボタン
    elif event == 'back_btn':
        window.close()
        window = main()

    #「QRコードの色」指定
    if event == 'color':
        color = values['color']

    #「QRコードの大きさ」指定
    if event == 'qr_size':
        size = values['qr_size']
        if size=="大":
            num = 15
        elif size=="中":
            num = 10
        else:
            num = 5
    
    ## QRコード作成
    # urlQRコード作成
    if event == 'make_url':
        code = values['url']
        # URL、色、大きさの情報をurlQRのmake_urlメソッドに渡す
        urlQR.make_url(code, color, num)
        # 生成されたQRコードをアプリ画面上に表示する
        window['qrimg'].update('urlQR.png')

    # textQRコード作成
    if event == 'make_text':
        text = values['text']
        # テキスト、色、大きさの情報をtextQRのmake_urlメソッドに渡す
        textQR.make_text(text, color, num)
        # 生成されたQRコードをアプリ画面上に表示する
        window['qrimg'].update('textQR.png')
    
    # mixQRコード作成
    if event == 'make_mix':
        # 入力されたURLを取得
        code1 = values['url1']
        code2 = values['url2']
        code3 = values['url3']
        # 3つのURL、色、大きさの情報をmixQRのmake_urlメソッドに渡す
        mixQR.make_mix(code1, code2, code3, color, num)
        # 生成されたQRコードをアプリ画面上に表示する
        window['qrimg'].update('mixQR.png')
    
    ## QRコードをダウンロードディレクトリに保存する
    #ダウンロードパス取得
    download_path = os.path.expanduser("~/Downloads")
    
    # urlQRコード保存
    if event == 'download_url':
        # 保存先までのpathを指定する
        file_path = os.path.join(download_path, "urlQR.png")
        # png形式でQRコードを保存
        shutil.copyfile("urlQR.png", file_path)
        # ユーザーに保存したことを伝える
        messagebox.showinfo('確認','QRを保存しました。')
    
    # mixQRコード保存
    if event == 'download_mix':
        # 保存先までのpathを指定する
        file_path = os.path.join(download_path, "mixQR.png")
        # png形式でQRコードを保存
        shutil.copyfile("mixQR.png", file_path)
        # ユーザーに保存したことを伝える
        messagebox.showinfo('確認','QRを保存しました。')
    
    # textQRコード保存
    if event == 'download_text':
        # 保存先までのpathを指定する
        file_path = os.path.join(download_path, "textQR.png")
        # png形式でQRコードを保存
        shutil.copyfile("textQR.png", file_path)
        # ユーザーに保存したことを伝える
        messagebox.showinfo('確認','QRを保存しました。')

window.close()