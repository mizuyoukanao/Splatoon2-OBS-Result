from tkinter import ttk
import tkinter
import os
import requests
import json

url = "https://app.splatoon2.nintendo.net/api/results"
cookies = {"iksm_session" : "ここにキーを入力"}
obstext = "ここにOBSで表示するtxt(utf-8)のPATHを入力"

root = tkinter.Tk()
root.title(u"リザルト更新ウィンドウ")
root.geometry("300x300")

def Updateresult(event):
    r = requests.get(url, cookies=cookies)
    jsondata = json.loads(r.text)
    with open(obstext, 'a', encoding="utf-8") as f:
        if jsondata["results"][0]["my_team_result"]["key"] == "victory":
            winlose = "\nWIN!   "
        elif jsondata["results"][0]["my_team_result"]["key"] == "defeat":
            winlose = "\nLose...   "
        kcount = jsondata["results"][0]["player_result"]["kill_count"]
        acount = jsondata["results"][0]["player_result"]["assist_count"]
        dcount = jsondata["results"][0]["player_result"]["death_count"]
        scount = jsondata["results"][0]["player_result"]["special_count"]
        f.write(winlose + str(kcount) + ("(") + str(acount) + (")") + ("キル") + str(dcount) + ("デス") + str(scount) + ("スペシャル"))

Button = tkinter.Button(text=u'リザルト更新', width=50)
Button.bind("<Button-1>",Updateresult)
Button.pack()

root.mainloop()