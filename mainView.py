import tkinter as tk
from tkinter import messagebox
import mainViewController
import threading
import pandas as pd


def message_send_callback(button):
    messagebox.showinfo('done', '処理が完了しました')
    button.configure(state=tk.ACTIVE)


def csv_import(mail_el, password_el, id_el, message_el):
    df = pd.read_csv('data.csv')
    mail_el.insert(tk.END, df['mail'][0])
    password_el.insert(tk.END, df['pass'][0])
    id_el.insert(tk.END, df['target'][0])
    message_el.insert(tk.END, df['message'][0])


def message_send(mail, password, id, message, button, callback):
    button.configure(state=tk.DISABLED)
    thread1 = threading.Thread(
        target=mainViewController.send_message, args=(mail, password, id, message, callback))
    thread1.start()


def build_view():
    # ウインドウの作成
    root = tk.Tk()
    root.title("Python GUI")
    root.geometry("360x140")

    # メールアドレス
    input_mail_label = tk.Label(text="メールアドレス")
    input_mail_label.grid(row=1, column=1, padx=10,)

    # メールアドレス入力欄の作成
    input_mail = tk.Entry(width=40)
    input_mail.grid(row=1, column=2)

    # パスワード
    input_pass_label = tk.Label(text="パスワード")
    input_pass_label.grid(row=2, column=1, padx=10,)

    # パスワード入力欄の作成
    input_pass = tk.Entry(width=40)
    input_pass.grid(row=2, column=2)

    # 送信先ID
    input_id_label = tk.Label(text="送信先ID")
    input_id_label.grid(row=3, column=1, padx=10,)

    # 送信先ID入力欄の作成
    input_id = tk.Entry(width=40)
    input_id.grid(row=3, column=2)

    # メッセージ
    input_message_label = tk.Label(text="メッセージ")
    input_message_label.grid(row=4, column=1, padx=10,)

    # メッセージ入力欄の作成
    input_message = tk.Entry(width=40)
    input_message.grid(row=4, column=2)

    # 送信ボタンの作成
    send_button = tk.Button(
        text="送信",
        command=lambda: message_send(
            input_mail.get(), input_pass.get(), input_id.get(), input_message.get(), send_button, lambda: message_send_callback(send_button)),
    )
    send_button.place(x=10, y=100)

    # CSV インポートボタンの作成
    csv_button = tk.Button(
        text="CSV インポート",
        command=lambda: csv_import(
            input_mail, input_pass, input_id, input_message),
    )
    csv_button.place(x=50, y=100)

    # ウインドウの描画
    root.mainloop()


if __name__ == '__main__':
    build_view()
