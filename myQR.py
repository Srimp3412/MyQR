import pyqrcode
import PySimpleGUI as sg

sg.theme('Dark Brown')

# 画面設定
def main():
    main_layout = [ [sg.Text('MyQR')],
                    [sg.Text('自分用のQRコードを作成できます。\nご利用になる目的に応じてボタンをクリックしてください。')],
                    [sg.Button('URLをQRに', key='urlQR'), sg.Button('まとめてQRに', key='mixQR'), sg.Button('文章をQRに', key='textQR')]]

    return sg.Window('MyOR', main_layout, size=(450, 250))



def url_main():
    frame1 = sg.Frame('', [
        [sg.Text('URLを入力してください')],
        [sg.InputText('', key='url')],
        [sg.Text('QRコードの色')],
        [sg.Text('シンボルの形')],
        [sg.Text('セルの形')],
        [sg.Button('メイン画面に戻る', key='back')]
    ], size=(270,250))
    frame2 = sg.Frame('', [], size=(180,250))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-URL', url_layout, size=(450, 250))

def mix_main():
    frame1 = sg.Frame('', [
        [sg.Text('最大5つのURLをまとめることができます')],
        [sg.Combo(('タイトル1','タイトル2','タイトル3','タイトル4','タイトル5'), size=(10,1), key='titleID'), sg.InputText('', key='title')],
        [sg.Text('URLを入力してください')],
        [sg.InputText('', key='url')],
        [sg.Text('QRコードの色')],
        [sg.Text('シンボルの形')],
        [sg.Text('セルの形')],
        [sg.Button('メイン画面に戻る', key='back')]
    ], size=(270,250))
    frame2 = sg.Frame('', [], size=(180,250))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-Mix', url_layout, size=(450, 250))

def text_main():
    frame1 = sg.Frame('', [
        [sg.Text('テキストを入力してください')],
        [sg.Multiline(font=('Arial',11),size=(270,5),key='text')],
        [sg.Text('QRコードの色')],
        [sg.Text('シンボルの形')],
        [sg.Text('セルの形')],
        [sg.Button('メイン画面に戻る', key='back')]
    ], size=(270,250))
    frame2 = sg.Frame('', [], size=(180,250))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-Text', url_layout, size=(450, 250))


# 初期画面
window = main()

# イベント
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # main画面で押されたボタンに応じて画面遷移
    # 前の画面は閉じる
    if event == 'urlQR':
        window.close()
        window = url_main()
    
    if event == 'mixQR':
        window.close()
        window = mix_main()

    if event == 'textQR':
        window.close()
        window = text_main()

    if event == 'back':
        window.close()
        window = main()
window.close()