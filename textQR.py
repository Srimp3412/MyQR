import pyqrcode as qr
import PySimpleGUI as sg

def text_main():
    frame1 = sg.Frame('', [
        [sg.Text('テキストを入力してください')],
        [sg.Multiline(font=('Arial',11),size=(270,4),key='text')],
        [sg.Text('- 基本設定 -')],
        [sg.Text('QRコードの色'), sg.Combo(("Red", "Blue", "Pink", "Green", "Black"), size=(7,1), key='color')],
        [sg.Text('シンボル'), sg.Combo(("四角","丸"), size=(4, 1), key='symbol'),sg.Text('セル'), sg.Combo(("四角","丸"), size=(4, 1), key='cell')],
        [sg.Button('メイン画面に戻る', key='back')]
    ], size=(270,250))
    frame2 = sg.Frame('', [
    [sg.Canvas(size=(145,145), background_color='white', key= '-canvas-')],
    [sg.Button('作成', size=(15,1), key='make')],
    [sg.Button('ダウンロード\n(PNG形式)', size=(15,2),key='download')]
], size=(180,250))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-Text', url_layout, size=(450, 250))