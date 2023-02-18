import qrcode
import PySimpleGUI as sg

def mix_main():
    frame1 = sg.Frame('', [
        [sg.Text('3つまでのURLをまとめることができます')],
        [sg.Text('タイトル1')],
        [sg.Text('URL'), sg.InputText('', key='url1')],
        [sg.Text('タイトル2')],
        [sg.Text('URL'), sg.InputText('', key='url2')],
        [sg.Text('タイトル3')],
        [sg.Text('URL'), sg.InputText('', key='url3')],
        [sg.Text('- 基本設定 -')],
        [sg.Text('QRコードの色'), sg.Combo(("Red", "Blue", "Pink", "Green", "Black"), size=(7,1), key='color', enable_events=True)],
        [sg.Text('大きさ '), sg.Combo(("大","中","小"), size=(5, 1), key='qr_size', enable_events=True)],
        [sg.Button('メイン画面に戻る', key='back_btn')]
    ], size=(270,300))
    frame2 = sg.Frame('', [
        [sg.Image(size=(210,210), key= 'qrimg')],
        [sg.Button('作成', size=(22,1), key='make_mix')],
        [sg.Button('ダウンロード\n(PNG形式)', size=(22,2),key='download')]
    ], size=(250,300))
    url_layout =  [[frame1,frame2]]

    return sg.Window('MyQR-Mix', url_layout, size=(520, 350))

# QRコード作成
def make_mix(code1, code2, code3, color, num):
        qr = qrcode.QRCode(
            version=num,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=8
        )
        mix = 'タイトル１\n'+code1+'\nタイトル2\n'+code2+'\nタイトル3\n'+code3
        qr.add_data(mix)
        qr.make()
        img = qr.make_image(fill_color=color, back_color="white")
        img.save('mixQR.png')
