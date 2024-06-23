#mPythonType:0
from mpython import *

TeamA = None

TA_games = None

TeamB = None

TB_games = None

touchtime = None

canceled = None

import time

import math
oled.fill(0)
TeamA = 0
TA_games = 0
TeamB = 0
TB_games = 0
touchtime = 0.1
oled.DispChar(str('感谢使用液林写的bug'), 0, 0, 1)
oled.DispChar(str('计分板 v2.0'), 0, 16, 1)
oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
oled.show()
while True:
    canceled = 0
    while not (touchpad_p.is_pressed() or touchpad_n.is_pressed()):
        oled.DispChar(str('按P开始,N清空并开始'), 0, 48, 1)
    TeamA = 0
    TeamB = 0
    oled.fill(0)
    if touchpad_n.is_pressed():
        oled.DispChar(str('比分归零'), 0, 0, 1)
        TA_games = 0
        TB_games = 0
        oled.show()
    time.sleep(0.5)
    oled.fill(0)
    oled.DispChar(str('开始记分！'), 0, 0, 1)
    oled.show()
    time.sleep(0.5)
    # 已决胜负
    while not (math.fabs(TeamA - TeamB) >= 2 and (TeamA >= 11 or TeamB >= 11) or canceled == 1):
        if TeamA < 0 or TeamB < 0:
            oled.fill(0)
            oled.DispChar(str('有队伍低于零分，本局无效'), 0, 0, 1, True)
            oled.show()
            time.sleep(0.7)
            canceled = 1
        if touchpad_t.is_pressed():
            time.sleep(touchtime)
            if touchpad_t.is_pressed():
                TeamA = TeamA + 1
        if touchpad_p.is_pressed():
            time.sleep(touchtime)
            if touchpad_p.is_pressed():
                TeamA = TeamA + -1
        if touchpad_h.is_pressed():
            time.sleep(touchtime)
            if touchpad_h.is_pressed():
                TeamB = TeamB + 1
        if touchpad_n.is_pressed():
            time.sleep(touchtime)
            if touchpad_n.is_pressed():
                TeamB = TeamB + -1
        if button_a.is_pressed() or button_b.is_pressed():
            canceled = 1
        oled.fill(0)
        oled.DispChar(str(str('teamA  ') + str((str(TeamA)))), 0, 0, 1)
        oled.DispChar(str(str('teamB  ') + str((str(TeamB)))), 0, 16, 1)
        oled.DispChar(str('按 A 或 B 取消本局'), 0, 48, 1)
        oled.show()
    if canceled == 0:
        if TeamA > TeamB:
            oled.fill(0)
            oled.DispChar(str('TeamA wins!'), 0, 0, 1)
            oled.show()
            TA_games = TA_games + 1
            time.sleep(0.5)
            oled.fill(0)
            oled.DispChar(str(str('A ') + str((str(TA_games)))), 0, 16, 1)
            oled.DispChar(str(str('B ') + str((str(TB_games)))), 0, 32, 1)
            oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
            oled.show()
        if TeamA < TeamB:
            oled.fill(0)
            oled.DispChar(str('TeamB wins!'), 0, 0, 1)
            oled.show()
            TB_games = TB_games + 1
            time.sleep(0.5)
            oled.fill(0)
            oled.DispChar(str(str('A ') + str((str(TA_games)))), 0, 16, 1)
            oled.DispChar(str(str('B ') + str((str(TB_games)))), 0, 32, 1)
            oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
            oled.show()
    if canceled == 1:
        oled.fill(0)
        oled.DispChar(str('本局取消'), 0, 0, 1)
        oled.show()
        canceled = 0
        time.sleep(0.5)
        oled.fill(0)
        oled.DispChar(str(str('A ') + str((str(TA_games)))), 0, 16, 1)
        oled.DispChar(str(str('B ') + str((str(TB_games)))), 0, 32, 1)
        oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
        oled.show()

button_a.is_pressed()
