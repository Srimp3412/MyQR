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

# メイン画面設定
# それぞれの画面設定は各ファイルに記載
def main():
    main_layout = [ [sg.Text('MyQR', font=('Arial',15))],
                    [sg.Text('自分用のQRコードを作成できます。\nご利用になる目的に応じてボタンをクリックしてください。')],
                    [sg.Button('URLをQRに', image_filename="", key='urlQR'), sg.Button('まとめてQRに', key='mixQR'), sg.Button('文章をQRに', key='textQR')],
                    [sg.Text('（注意）\n「まとめてQR」、「文章をQR」で生成したQRコードは\n読み取るアプリによって結果が大きく異なります。\nあらかじめご了承ください。')]]

    return sg.Window('MyOR', main_layout, size=(500, 330))

# 初期画面
sg.theme('LightGrey1')
window = main()

# イベント処理
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # main画面で押されたボタンに応じて画面遷移
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
            num = 6
    
    ## QRコード作成
    # urlQRコード作成
    if event == 'make_url':
        code = values['url']
        urlQR.make_url(code, color, num)
        window['qrimg'].update('urlQR.png')

    # textQRコード作成
    if event == 'make_text':
        text = values['text']
        textQR.make_text(text, color, num)
        window['qrimg'].update('textQR.png')
    
    # mixQRコード作成
    if event == 'make_mix':
        code1 = values['url1']
        code2 = values['url2']
        code3 = values['url3']
        mixQR.make_mix(code1, code2, code3, color, num)
        window['qrimg'].update('mixQR.png')
    
    ## QRコードをダウンロードディレクトリに保存する
    # urlQRコード保存
    if event == 'download_url':
        download_path = os.path.expanduser("~/Downloads")
        file_path = os.path.join(download_path, "urlQR.png")
        shutil.copyfile("urlQR.png", file_path)
        messagebox.showinfo('確認','QRを保存しました。')
    
    # mixQRコード保存
    if event == 'download_mix':
        download_path = os.path.expanduser("~/Downloads")
        file_path = os.path.join(download_path, "mixQR.png")
        shutil.copyfile("mixQR.png", file_path)
        messagebox.showinfo('確認','QRを保存しました。')
    
    # textQRコード保存
    if event == 'download_text':
        download_path = os.path.expanduser("~/Downloads")
        file_path = os.path.join(download_path, "textQR.png")
        shutil.copyfile("textQR.png", file_path)
        messagebox.showinfo('確認','QRを保存しました。')

window.close()