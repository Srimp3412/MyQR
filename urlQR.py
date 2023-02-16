import qrcode
import PySimpleGUI as sg

# 画面設定
def url_main():
    frame1 = sg.Frame('', [
        [sg.Text('URLを入力してください')],
        [sg.InputText('', key='url')],
        [sg.Text('- 基本設定 -')],
        [sg.Text('QRコードの色'), sg.Combo(("Red", "Blue", "Pink", "Green", "Black"), size=(7,1), key='color', enable_events=True)],
        [sg.Text('大きさ '), sg.Combo(("大","中","小"), size=(5, 1), key='qr_size', enable_events=True)],
        [sg.Button('メイン画面に戻る', key='back_btn')]
    ], size=(270,300))
    frame2 = sg.Frame('', [
        [sg.Image(size=(210,210), key= 'qrimg')],
        [sg.Button('作成', size=(22,1), key='make_url')],
        [sg.Button('ダウンロード\n(PNG形式)', size=(22,2),key='download')]
    ], size=(250,300))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-URL', url_layout, size=(520, 350))



# QRコード作成
def make_url(code, color, num):
        qr = qrcode.QRCode(
            version=num,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=8
        )
        qr.add_data(code)
        qr.make()
        img = qr.make_image(fill_color=color, back_color="white")
        img.save('urlQR.png')