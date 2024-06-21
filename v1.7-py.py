#mPythonType:0
from mpython import *

TeamA = None

TA_games = None

TeamB = None

TB_games = None

import time

import math
oled.fill(0)
TeamA = 0
TA_games = 0
TeamB = 0
TB_games = 0
oled.DispChar(str('感谢使用液林写的bug'), 0, 0, 1)
oled.DispChar(str('计分板 v1.7'), 0, 16, 1)
oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
oled.show()
while True:
    while not (touchpad_p.is_pressed() or touchpad_n.is_pressed()):
        oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
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
    while not (math.fabs(TeamA - TeamB) >= 2 and (TeamA >= 11 or TeamB >= 11)):
        if touchpad_t.is_pressed():
            time.sleep(0.3)
            if touchpad_t.is_pressed():
                TeamA = TeamA + 1
        if touchpad_p.is_pressed():
            time.sleep(0.3)
            if touchpad_p.is_pressed():
                TeamA = TeamA + -1
        if touchpad_h.is_pressed():
            time.sleep(0.3)
            if touchpad_h.is_pressed():
                TeamB = TeamB + 1
        if touchpad_n.is_pressed():
            time.sleep(0.3)
            if touchpad_n.is_pressed():
                TeamB = TeamB + -1
        oled.fill(0)
        oled.DispChar(str(str('teamA  ') + str((str(TeamA)))), 0, 0, 1)
        oled.DispChar(str(str('teamB  ') + str((str(TeamB)))), 0, 16, 1)
        oled.show()
    if TeamA > TeamB:
        oled.fill(0)
        oled.DispChar(str('TeamA wins!'), 0, 0, 1)
        oled.show()
        TA_games = TA_games + 1
        oled.fill(0)
        oled.DispChar(str(str('A ') + str((str(TA_games)))), 0, 16, 1)
        oled.DispChar(str(str('B ') + str((str(TB_games)))), 0, 32, 1)
        oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
        oled.show()
    else:
        oled.fill(0)
        oled.DispChar(str('TeamB wins!'), 0, 0, 1)
        oled.show()
        TB_games = TB_games + 1
        oled.fill(0)
        oled.DispChar(str(str('A ') + str((str(TA_games)))), 0, 16, 1)
        oled.DispChar(str(str('B ') + str((str(TB_games)))), 0, 32, 1)
        oled.DispChar(str('按P开始,N清空'), 0, 48, 1)
        oled.show()
