import qrcode
import PySimpleGUI as sg

def text_main():
    frame1 = sg.Frame('', [
        [sg.Text('テキストを入力してください')],
        [sg.Multiline(font=('Arial',11),size=(270,6),key='text')],
        [sg.Text('- 基本設定 -')],
        [sg.Text('・QRコードの色'), sg.Combo(("Red", "Blue", "Pink", "Green", "Black"), default_value="未選択", size=(8,1), key='color', enable_events=True)],
        [sg.Text('・大きさ '), sg.Combo(("大","中","小"), default_value="未選択", size=(8,1), key='qr_size', enable_events=True)],
        [sg.Button('メイン画面に戻る', key='back_btn')]
    ], size=(270,330))
    frame2 = sg.Frame('', [
        [sg.Image(size=(210,220), key= 'qrimg')],
        [sg.Button('作成', size=(24,1), key='make_text')],
        [sg.Button('ダウンロード\n(PNG形式)', size=(24,2),key='download_text')]
], size=(250,330))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-Text', url_layout, size=(520, 330))

# QRコード作成
def make_text(text, color, num):
        qr = qrcode.QRCode(
            version=num,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=8
        )
        qr.add_data(text)
        qr.make()
        img = qr.make_image(fill_color=color, back_color="white")
        img.save('textQR.png')