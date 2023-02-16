import pyqrcode as qr
import PySimpleGUI as sg

# それぞれのファイルをimport
import urlQR
import mixQR
import textQR

# メイン画面設定
# それぞれの画面設定は各ファイルに記載
def main():
    main_layout = [ [sg.Text('MyQR', font=('Arial',15))],
                    [sg.Text('自分用のQRコードを作成できます。\nご利用になる目的に応じてボタンをクリックしてください。')],
                    [sg.Button('URLをQRに', key='urlQR'), sg.Button('まとめてQRに', key='mixQR'), sg.Button('文章をQRに', key='textQR')]]

    return sg.Window('MyOR', main_layout, size=(500, 300))

# 初期画面
sg.theme('Dark Brown')
window = main()




# QRコード作成関数
def makeQR(code):
    qr_img = qr.make(str(code))
    return qr_img

# イベント
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

    elif event == 'back_btn':
        window.close()
        window = main()
    
    if event == 'color':
        color = values['color']

    if event == 'qr_size':
        size = values['qr_size']
        if size=="大":
            num = 15
        elif size=="中":
            num = 10
        else:
            num = 6
        
    # QRコード作成・保存（ダウンロード）
    if event == 'make_url':
        code = values['url']
        print(color)
        print(num)
        urlQR.make_url(code, color, num)
        window['qrimg'].update('urlQR.png')

    if event == 'make_text':
        text = values['text']
        textQR.make_text(text, color, num)
        window['qrimg'].update('textQR.png')
window.close()