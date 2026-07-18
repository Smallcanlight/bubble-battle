# -*- coding: utf-8 -*-
"""
泡泡大作戰 Bubble Battle
=======================
一款「水球對戰」類型遊戲(玩法向經典水球對戰遊戲致敬,美術為原創圖形)。

玩法:
  - 放置水球,水球倒數後炸出十字水柱
  - 被水柱噴到不會直接死,而是被「困在大水泡裡」!
  - 被困住時:倒數結束會爆掉(死亡)、被其他玩家碰到會被戳破(死亡)
  - 手上有「針」的話,被困時再按一次放球鍵即可自救脫困
  - 打破箱子有機率掉道具

道具:
  💧 水球+1   : 可同時放置的水球數量 +1
  🧪 藥水     : 水柱威力(射程) +1
  ⚡ 溜冰鞋   : 移動速度提升
  📌 針       : 被困住時可自救一次(可囤數支)

模式(標題畫面全面按鈕化,滑鼠點選;數字鍵/I/N 快捷鍵仍可用):
  本機遊戲:單人 vs 電腦×1~3、雙人對戰、雙人+電腦×2、三人、四人(同一鍵盤)
  佔地大作戰:水柱染地成隊色(橘vs青),陣亡 10 秒復活,時間到比佔地多寡
  感染大作戰:開場 3 秒隨機一人感染爆發;生存者被泡爆 3 秒後復活成感染者
    (綠光、移速+15%、威力+1、死亡只會復活);有人撐到時間結束生存者就贏
  水球足球 4v4:專屬球場、左右球門;持球者減速、被泡爆才掉球、5 秒復活;
    進球有歡呼與橫幅,慶祝後重新開球,時間到比進球數(荒野亂鬥式規則致敬)
  章魚王討伐:1P+電腦隊友 / 雙人合作
  連線房間:最多 8 人同場!建立房間者為房主。
    房主可設定電腦強度(初級/中級/高級/專家):影響反應速度、丟彈頻率、
    技能使用率、被困自救速度;初級還會偶爾遲疑。
      房間大廳有 8 個玩家格位(含準備狀態、房主皇冠),房主可:
      點空位加入/移除電腦、切換模式(大亂鬥/章魚王)、挑選地圖、按「開始遊戲」。
      加入方輸入房主畫面顯示的 IP,進房後按「準備!」;全員準備後房主才能開始。
      對戰結束由房主按「返回房間」帶大家回大廳再戰。
      兩台以上裝置需在同一網路:同 Wi-Fi、手機/平板熱點、或藍牙 PAN 皆可。
      房主是 P1;加入方各自分到 P2~P8。連線房間內所有真人玩家
      一律使用同一套鍵位:方向鍵移動、空白鍵放球/用針。
      道具採「雙槽制」(顯示在全螢幕右側黑邊):撿到的主動道具依序填入
      優先槽與備用槽(各一個、最多兩個),X 使用優先槽、Z 對調兩槽,
      兩槽皆滿時地上的主動道具撿不起來。

章魚王討伐(合作 Boss 戰,忠實原作怪物模式規則):
  - 全員同隊,用水柱轟章魚王把血條打空即獲勝;碰到怪物立即死亡(光盾可防)
  - 章魚王會瞄準玩家丟水球(紅色落點預警)、講狠話後施放全場彈幕、召喚追人的小章魚
  - 小章魚可以被水柱炸死,也會被水球擋路
  - 被困在泡泡裡時怪物打不到你,隊友碰你一下即可救援
  - 血量剩 30% 進入紅血狂暴:移動加速、彈幕加量、小章魚變多變快

地圖(共 32 張,選完模式後點選;「?」卡片=每場開局隨機):
  1 青青草原(經典棋盤)      2 黃沙綠洲(對稱亂石、開闊)
  3 冰晶湖(稀疏地形、移速+18%) 4 熔岩洞窟(十字牆、道具豐富)
  5 幽暗森林(箱子超多)       6 齒輪工廠(橫向廠房牆)
  7 陽光沙灘(中央競技場)     8 夜色迷宮(棒倒法迷宮)
  -- 機關地圖(場地互動:加速履帶/泥沼/大砲/傳送門) --
  9 星光跑道(上下雙向履帶)   10 泥沼濕地(減速泥潭遍布)
  11 砲彈要塞(四門大砲互射)  12 幻境之門(雙色傳送門)
  13 工廠生產線(縱向履帶)    14 火山口(泥漿護城河)
  15 雪原滑道(高速+環場履帶) 16 混沌樂園(履帶+泥沼+砲+門全上)
  -- 風景地圖(造景 + 環境粒子:櫻花瓣/雪/楓葉/螢火/火星/氣泡) --
  17 櫻花庭園(櫻樹鳥居+傳送門)  18 楓紅山莊(楓樹小屋+履帶大砲)
  19 雪夜小鎮(雪屋雪人+冰面)    20 沙漠遺跡(仙人掌+四向砲+流沙)
  21 螢火之森(大樹蘑菇+迷宮)    22 海底王宮(珊瑚水晶+洋流履帶)
  23 熔岩工房(紅晶岩石+岩漿池)  24 天空棧道(雲上棧道+全機關)
  -- 進階風景地圖(新機關:彈跳墊=朝面向彈飛 2 格、開關門=切換鐵閘) --
  25 和風溫泉(蒸氣湯池+跳石)    26 幽靈古堡(開關城門+鬼火)
  27 糖果樂園(糖霜冰面+彈跳墊)  28 廢棄礦坑(礦車履帶+礦門開關)
  29 竹林小徑(四角彈跳+竹風)    30 星空天文台(雙色傳送門+冰面)
  31 海賊灣(四向砲戰+跳板)      32 終焉鐘樓(六種機關全數登場)

背景音樂:在遊戲同資料夾建立 music/ 並放入音檔(M 鍵靜音):
  title.* → 開始畫面   room.* → 連線房間   battle01.*、battle02.*… → 對戰隨機播放

道具(標題畫面按 I 開道具圖鑑;連線房間可切換道具池:普通 16 種 / 擴充 20 種):
  能力:水球+1 / 藥水(威力+1) / 溜冰鞋(加速) / 大力藥丸(威力全滿) / 紅色惡魔(速度全滿)
  自保:針(困住自救) / 無敵光盾(短暫無敵) / 隱形衣(隱形) / 泡泡雷達(顯示爆炸範圍)
  攻擊:飛鏢(遠距引爆水球) / 拳套(丟水球,可越牆、出界繞回) / 運動鞋(踢水球滑行)
  坐騎:烏龜(慢但擋一次) / 貓頭鷹(略快、擋一次) / 飛碟(快、飛越箱子、不能撿道具)
  詛咒:惡魔面具(反向操作或亂放水球)
  擴充(原創設計):鉤爪(勾牆位移) / 飛彈(直線爆破) / 磁力槍(吸人吸球) / 冰凍槍(定身)
  ※ 主動道具(飛鏢/鉤爪/飛彈/磁力/冰凍)共用「手持道具槽」:
    同種可疊 3 個,撿到不同種會替換,按使用鍵發動。

角色(連線房間進場前選擇,24 隻原創角色,技能鍵 C、冷卻制,面板在右側黑邊):
  神射手(長距投籃:拋 4 格無視障礙) 足球明星(香蕉球:直走 2 格後轉彎)
  工程師(X 型炸藥:對角線爆炸)     劍客(居合斬:斬箱/引爆且不波及自己那側)
  忍者(瞬身:穿牆位移 3 格)        醫護兵(急救:淨化+護盾,可救被困隊友)
  守護者(築牆:5 秒臨時石牆)       時空行者(回溯:回到 3 秒前的位置)
  氣旋使(颶風掌:擊退身邊敵人與水球) 砲手(震撼彈:炸箱+震退暈眩敵人)
  獵人(捕獸夾:半隱形陷阱定身敵人)  蠻牛(衝撞:直衝 4 格推開沿路敵人)
  幻影師(換位術:與自己的水球換位)  冰霜使(霜華綻放:凍結兩格內敵人)
  水靈(漣漪足跡:水漬讓敵人濕身緩速) 節奏使(狂想加速:自己與隊友加速)
  士官長(空襲信標:預警後轟炸直線)   海盜船長(掠奪之手:偷敵人的道具)
  電光使(雷光疾馳:高速且穿過水球)   爆破專家(遙控水雷:再按 C 引爆)
  釣客(精準甩竿:釣回直線上的道具)   園丁(快速種樹:種 3 個木箱)
  氣球商人(限時特賣:短暫+1球+1力)  力士(震地踏:震退+引信剩0.4秒)

操作(最多 4 人同鍵盤):
  P1: W A S D 移動,空白鍵 放球/用針,左Ctrl 或 E 使用道具
  P2: 方向鍵 移動,Enter 放球/用針,右Ctrl 使用道具
  P3: I J K L 移動,O 放球/用針,P 使用道具
  P4: 數字鍵盤 8 4 5 6 移動,數字鍵盤 0 放球/用針,數字鍵盤 + 使用道具
  (電腦玩家會自動行動:躲水柱、開路、撿道具、圍攻與用針自救)

  R 重新開始同地圖,M 更換地圖,Esc 回選單

需求: Python 3.8+ 與 pygame  (pip install pygame)
執行: python bubble_battle.py
"""

import json
import math
import os
import threading
import time
import random
import socket
import sys
from collections import deque

os.environ.setdefault("SDL_ACCELEROMETER_AS_JOYSTICK", "0")
import pygame



# ----------------------------------------------------------------------
# 內建背景音樂:原創曲目,啟動後於背景執行緒合成(陽光台式流行 chiptune 風)
# music/ 資料夾有對應檔案時以玩家的檔案優先
# ----------------------------------------------------------------------
SYNTH_BGM_VOLUME = 0.42

# 足球模式:專屬球場、持球減速、進球慶祝
BALL_SLOW = 0.65         # 持球者移速倍率
SHOOT_SPEED = 13.0       # 射門球速(格/秒)
SHOOT_RANGE = 6          # 射門最遠距離(格)
GOAL_PAUSE = 2.5         # 進球慶祝秒數(之後重新開球)
SOCCER_RESPAWN = 5.0     # 足球模式復活秒數
SOCCER_MAP = dict(
    zh="水球競技場", en="Splash Stadium", layout="soccer",
    soft=0.30, drop=0.55, speed=1.0,
    colors=dict(fa=(96, 168, 96), fb=(88, 158, 90),
                hard=(120, 126, 140), hard_dark=(84, 90, 104),
                hard_top=(154, 160, 174),
                soft=(196, 160, 116), soft_dark=(150, 116, 78),
                soft_light=(230, 196, 152)))
GOAL_ROWS = (5, 6, 7)    # 球門開口(左右邊界)

# 佔地模式隊色(避開警告紅與水柱藍):橘隊 vs 青隊
TURF_COLS = ((255, 176, 36), (45, 205, 190))
TURF_ZH = ("橘隊", "青隊")
TURF_EN = ("ORANGE", "TEAL")


def _midi_hz(n):
    return 440.0 * (2.0 ** ((n - 69) / 12.0))


def _render_song(sr, bpm, bars, voices):
    """迷你音序器:voices = [(wave, vol, notes)],notes = [(拍, 長, MIDI)]。

    wave: sine / pulse / tri / kick / hat / snare。回傳 int16 位元組(單聲道)。
    """
    spb = 60.0 / bpm                       # 每拍秒數
    total = int(sr * bars * 4 * spb) + sr // 10
    buf = [0.0] * total
    tau = 2 * math.pi
    rng = random.Random(4242)
    for wave, vol, notes in voices:
        for (beat, durb, midi) in notes:
            f = _midi_hz(midi) if midi is not None else 0.0
            start = int(beat * spb * sr)
            n = int(durb * spb * sr)
            for i in range(n):
                if ANDROID and (i & 4095) == 0:
                    time.sleep(0.002)     # 讓出 GIL,別餓死主迴圈
                t = i / sr
                # 包絡:快起 + 收尾釋放
                env = min(1.0, t / 0.012) * min(1.0, (n - i) / (sr * 0.05))
                if wave == "sine":
                    v = math.sin(tau * f * t)
                elif wave == "tri":
                    ph = (f * t) % 1.0
                    v = 4 * abs(ph - 0.5) - 1
                elif wave == "pulse":
                    v = 1.0 if (f * t) % 1.0 < 0.3 else -1.0
                    v *= 0.8
                elif wave == "kick":
                    fk = 120 - 75 * min(1.0, t / 0.09)
                    v = math.sin(tau * fk * t) * math.exp(-t * 18)
                elif wave == "hat":
                    v = (rng.random() * 2 - 1) * math.exp(-t * 60)
                elif wave == "snare":
                    v = ((rng.random() * 2 - 1) * 0.7
                         + math.sin(tau * 190 * t) * 0.3) * math.exp(-t * 24)
                else:
                    v = 0.0
                j = start + i
                if j < total:
                    buf[j] += v * vol * env
    import array
    out = array.array("h")
    for v in buf:
        out.append(int(max(-1.0, min(1.0, v * 0.8)) * 30000))
    return out


def _bar_notes(prog, pattern, base_beat=0.0):
    """把和弦進行(每小節一組音)套進節奏樣板,產生 notes。"""
    notes = []
    for bar, chord in enumerate(prog):
        for (b, d, deg) in pattern:
            notes.append((base_beat + bar * 4 + b, d, chord[deg % len(chord)]))
    return notes


def compose_bgm(sr):
    """回傳 {名稱: int16 bytes} 的四首原創曲。"""
    songs = {}
    # 和弦(MIDI):C=60。三和弦以 [根, 三, 五, 高八根] 表示
    def tri(root, minor=False):
        return [root, root + (3 if minor else 4), root + 7, root + 12]
    C, G, Am, F = tri(48), tri(43), tri(45, True), tri(41)
    Em, Dm = tri(40, True), tri(38, True)

    # ---- 標題〈果醬日和〉120 BPM,8 小節 ----
    prog = [C, G, Am, F, C, G, F, C]
    bass = _bar_notes(prog, [(0, 0.9, 0), (1, 0.9, 0), (2, 0.9, 2), (3, 0.9, 0)])
    stabs = _bar_notes([[n + 12 for n in ch] for ch in prog],
                       [(0.5, 0.35, 0), (0.5, 0.35, 1), (0.5, 0.35, 2),
                        (1.5, 0.35, 0), (1.5, 0.35, 1), (1.5, 0.35, 2),
                        (2.5, 0.35, 0), (2.5, 0.35, 1), (2.5, 0.35, 2),
                        (3.5, 0.35, 0), (3.5, 0.35, 1), (3.5, 0.35, 2)])
    melody = []
    lines = [
        [(0, 1, 76), (1, 0.5, 79), (1.5, 0.5, 81), (2, 1, 79), (3, 1, 76)],
        [(0, 1.5, 74), (1.5, 0.5, 71), (2, 1, 74), (3, 1, 79)],
        [(0, 1, 81), (1, 0.5, 79), (1.5, 0.5, 76), (2, 2, 72)],
        [(0, 1, 74), (1, 1, 72), (2, 1.5, 69), (3.5, 0.5, 72)],
        [(0, 1, 76), (1, 0.5, 79), (1.5, 0.5, 84), (2, 1, 81), (3, 1, 79)],
        [(0, 0.5, 74), (0.5, 0.5, 76), (1, 1, 79), (2, 2, 74)],
        [(0, 1, 72), (1, 0.5, 74), (1.5, 0.5, 76), (2, 1, 77), (3, 1, 74)],
        [(0, 2.5, 72), (3, 1, 67)],
    ]
    for bar, ln in enumerate(lines):
        melody += [(bar * 4 + b, d, m) for (b, d, m) in ln]
    drums_k = [(bar * 4 + b, 0.3, None) for bar in range(8) for b in (0, 2)]
    drums_h = [(bar * 4 + b, 0.12, None) for bar in range(8)
               for b in (0.5, 1.5, 2.5, 3.5)]
    songs["title"] = _render_song(sr, 120, 8, [
        ("tri", 0.30, bass), ("pulse", 0.10, stabs), ("pulse", 0.17, melody),
        ("kick", 0.5, drums_k), ("hat", 0.16, drums_h)])

    # ---- 房間〈等待果實〉92 BPM,8 小節(輕鬆) ----
    prog = [Am, F, C, G, Am, F, G, C]
    bass = _bar_notes(prog, [(0, 1.8, 0), (2, 1.8, 2)])
    pad = _bar_notes([[n + 12 for n in ch] for ch in prog],
                     [(0, 3.6, 0), (0, 3.6, 1), (0, 3.6, 2)])
    lines = [
        [(0, 1.5, 76), (2, 1.5, 74)],
        [(0, 1, 72), (1.5, 1, 74), (3, 1, 76)],
        [(0, 2, 79), (2.5, 1, 76)],
        [(0, 1.5, 74), (2, 2, 71)],
        [(0, 1.5, 76), (2, 1, 81), (3, 1, 79)],
        [(0, 2, 77), (2.5, 1, 76)],
        [(0, 1, 74), (1.5, 1, 76), (3, 1, 74)],
        [(0, 3, 72)],
    ]
    melody = [(bar * 4 + b, d, m) for bar, ln in enumerate(lines)
              for (b, d, m) in ln]
    songs["room"] = _render_song(sr, 92, 8, [
        ("tri", 0.26, bass), ("sine", 0.07, pad), ("sine", 0.20, melody)])

    # ---- 戰鬥一〈衝吧水球〉138 BPM ----
    prog = [C, G, Am, F, C, G, F, G]
    bass = _bar_notes(prog, [(b, 0.45, 0 if b % 1 == 0 else 2)
                             for b in [x * 0.5 for x in range(8)]])
    stabs = _bar_notes([[n + 12 for n in ch] for ch in prog],
                       [(0.5, 0.3, 1), (1.5, 0.3, 1), (2.5, 0.3, 1), (3.5, 0.3, 1),
                        (0.5, 0.3, 2), (1.5, 0.3, 2), (2.5, 0.3, 2), (3.5, 0.3, 2)])
    lines = [
        [(0, 0.5, 79), (0.5, 0.5, 81), (1, 0.5, 84), (2, 0.5, 81), (2.5, 0.5, 79), (3, 1, 76)],
        [(0, 0.5, 74), (0.5, 0.5, 76), (1, 1, 79), (2, 0.5, 76), (2.5, 0.5, 74), (3, 1, 71)],
        [(0, 0.5, 81), (0.5, 0.5, 84), (1, 0.5, 81), (1.5, 0.5, 79), (2, 1, 76), (3, 1, 72)],
        [(0, 0.5, 74), (0.5, 0.5, 77), (1, 1, 81), (2, 1.5, 79), (3.5, 0.5, 76)],
        [(0, 0.5, 79), (0.5, 0.5, 81), (1, 0.5, 84), (2, 0.5, 86), (2.5, 0.5, 84), (3, 1, 81)],
        [(0, 1, 79), (1, 0.5, 76), (1.5, 0.5, 74), (2, 1, 79), (3, 1, 74)],
        [(0, 0.5, 77), (0.5, 0.5, 81), (1, 1, 84), (2, 1, 81), (3, 0.5, 77), (3.5, 0.5, 81)],
        [(0, 0.5, 79), (0.5, 0.5, 83), (1, 1, 86), (2, 2, 84)],
    ]
    melody = [(bar * 4 + b, d, m) for bar, ln in enumerate(lines)
              for (b, d, m) in ln]
    drums_k = [(bar * 4 + b, 0.3, None) for bar in range(8) for b in (0, 1, 2, 3)]
    drums_s = [(bar * 4 + b, 0.2, None) for bar in range(8) for b in (1, 3)]
    drums_h = [(bar * 4 + b, 0.1, None) for bar in range(8)
               for b in [x * 0.5 for x in range(8)]]
    songs["battle1"] = _render_song(sr, 138, 8, [
        ("tri", 0.30, bass), ("pulse", 0.08, stabs), ("pulse", 0.16, melody),
        ("kick", 0.5, drums_k), ("snare", 0.24, drums_s), ("hat", 0.12, drums_h)])

    # ---- 戰鬥二〈水球亂鬥〉144 BPM(F-G-Em-Am) ----
    prog = [F, G, Em, Am, F, G, C, C]
    bass = _bar_notes(prog, [(b, 0.45, 0) for b in [x * 0.5 for x in range(8)]])
    stabs = _bar_notes([[n + 12 for n in ch] for ch in prog],
                       [(0.5, 0.28, 0), (1.5, 0.28, 1), (2.5, 0.28, 2), (3.5, 0.28, 1)])
    lines = [
        [(0, 0.5, 81), (0.5, 0.5, 84), (1, 1, 81), (2, 0.5, 79), (2.5, 0.5, 77), (3, 1, 74)],
        [(0, 0.5, 79), (0.5, 0.5, 83), (1, 1, 79), (2, 1, 74), (3, 1, 71)],
        [(0, 1, 76), (1, 0.5, 79), (1.5, 0.5, 76), (2, 1, 71), (3, 1, 67)],
        [(0, 0.5, 72), (0.5, 0.5, 76), (1, 1, 81), (2, 2, 79)],
        [(0, 0.5, 81), (0.5, 0.5, 84), (1, 1, 86), (2, 1, 84), (3, 1, 81)],
        [(0, 0.5, 83), (0.5, 0.5, 86), (1, 1, 83), (2, 1, 79), (3, 1, 74)],
        [(0, 0.5, 76), (0.5, 0.5, 79), (1, 0.5, 84), (1.5, 0.5, 79), (2, 1, 76), (3, 1, 72)],
        [(0, 1.5, 72), (2, 2, 72)],
    ]
    melody = [(bar * 4 + b, d, m) for bar, ln in enumerate(lines)
              for (b, d, m) in ln]
    songs["battle2"] = _render_song(sr, 144, 8, [
        ("tri", 0.30, bass), ("pulse", 0.08, stabs), ("pulse", 0.16, melody),
        ("kick", 0.5, drums_k), ("snare", 0.24, drums_s), ("hat", 0.12, drums_h)])
    return songs


# ----------------------------------------------------------------------
# 背景音樂:讀取程式旁的 music/ 資料夾(檔案由玩家自行提供)
#   title.*             → 開始畫面與各選單
#   room.*              → 連線房間/大廳
#   battle01.* 02.* ... → 對戰中隨機播放(數量不限)
#   支援 ogg / mp3 / wav / flac;缺檔時安靜跳過。遊戲中按 M 靜音。
# ----------------------------------------------------------------------
MUSIC_VOLUME = 0.6


class MusicBox:
    def __init__(self):
        self.enabled = False
        self.current = None          # 目前播放的群組名稱
        self.cur_src = None          # "file" 或 "synth"
        self.muted = False
        self.tracks = {"title": [], "room": [], "battle": []}
        self.synth = {}              # 內建原創曲(背景執行緒烘焙)
        self.chan = None
        try:
            pygame.mixer.init()
            self.enabled = True
        except pygame.error:
            return
        try:
            self.chan = pygame.mixer.Channel(6)
        except pygame.error:
            self.chan = None
        threading.Thread(target=self._bake_synth, daemon=True).start()
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "music")
        if os.path.isdir(base):
            for fn in sorted(os.listdir(base)):
                low = fn.lower()
                if not low.endswith((".ogg", ".mp3", ".wav", ".flac")):
                    continue
                path = os.path.join(base, fn)
                if low.startswith("title"):
                    self.tracks["title"].append(path)
                elif low.startswith("room"):
                    self.tracks["room"].append(path)
                elif low.startswith("battle"):
                    self.tracks["battle"].append(path)

    def _bake_synth(self):
        """背景合成內建原創曲(音樂檔缺席時的預設 BGM)。"""
        init = pygame.mixer.get_init()
        if not init:
            return
        sr, _, channels = init[0], init[1], init[2]
        synth_sr = sr // 2 if ANDROID else sr
        try:
            raw = compose_bgm(synth_sr)
        except Exception:
            return
        import array
        if synth_sr != sr:
            up = {}
            for name, mono in raw.items():
                m = array.array("h")
                m.frombytes(mono)
                dup = array.array("h")
                for k2, v in enumerate(m):
                    if ANDROID and (k2 & 8191) == 0:
                        time.sleep(0.001)
                    dup.append(v)
                    dup.append(v)          # 樣本複製 ×2 升頻
                up[name] = dup.tobytes()
            raw = up
        for name, mono in raw.items():
            if channels > 1:
                inter = array.array("h")
                for k3, v in enumerate(mono):
                    if ANDROID and (k3 & 8191) == 0:
                        time.sleep(0.001)
                    for _ in range(channels):
                        inter.append(v)
                data = inter
            else:
                data = mono
            try:
                self.synth[name] = pygame.mixer.Sound(buffer=data.tobytes())
            except pygame.error:
                return
        # 若目前群組正等著內建曲,烘焙完成後立即補播
        if self.cur_src == "synth" and self.current:
            grp = self.current
            self.current = None
            self.play(grp)

    def _synth_for(self, group):
        if group == "battle":
            names = [n for n in ("battle1", "battle2") if n in self.synth]
            return self.synth[random.choice(names)] if names else None
        return self.synth.get(group)

    def play(self, group):
        """切換音樂群組:玩家的檔案優先,缺席時用內建原創曲。"""
        if not self.enabled:
            return
        if self.current == group:
            return
        pool = self.tracks.get(group) or []
        if pool:
            if self.chan is not None:
                self.chan.stop()
            path = random.choice(pool)
            try:
                pygame.mixer.music.fadeout(200)
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(0.0 if self.muted
                                              else MUSIC_VOLUME)
                pygame.mixer.music.play(-1, fade_ms=400)
                self.current = group
                self.cur_src = "file"
            except pygame.error:
                self.current = None
            return
        # 內建原創曲
        try:
            pygame.mixer.music.fadeout(200)
        except pygame.error:
            pass
        snd = self._synth_for(group)
        self.current = group
        self.cur_src = "synth"
        if self.chan is not None:
            self.chan.stop()
            if snd is not None:
                self.chan.set_volume(0.0 if self.muted else SYNTH_BGM_VOLUME)
                self.chan.play(snd, loops=-1, fade_ms=300)

    def toggle_mute(self):
        self.muted = not self.muted
        if self.enabled:
            try:
                pygame.mixer.music.set_volume(0.0 if self.muted
                                              else MUSIC_VOLUME)
            except pygame.error:
                pass
            if self.chan is not None:
                self.chan.set_volume(0.0 if self.muted
                                     else SYNTH_BGM_VOLUME)




# ----------------------------------------------------------------------
# 音效:啟動時以純程式合成(原創波形,無需外部檔案)
# ----------------------------------------------------------------------
SFX_VOLUME = 0.5

# 積分模式:名次分數表(第 1~8 名;並列取區塊墊底名次的分數)
PLACE_POINTS = [10, 7, 5, 4, 3, 1, 0, 0]


def placement_points(statuses):
    """依 (alive, death_t) 清單計算每人得分(順序對應輸入)。

    活著者並列第一;陣亡者死得越晚名次越高、death_t 相同視為並列。
    並列 m 人自名次 k 起,全部拿第 k+m-1 名的分數。
    """
    n = len(statuses)
    table = (PLACE_POINTS + [0] * n)[:n]
    keyed = []
    for ix, (alive, dt_) in enumerate(statuses):
        key = (0, 0.0) if alive else (1, -(dt_ if dt_ is not None else 0.0))
        keyed.append((key, ix))
    keyed.sort(key=lambda x: x[0])
    pts = [0] * n
    i = 0
    while i < n:
        j = i
        while j < n and keyed[j][0] == keyed[i][0]:
            j += 1
        val = table[min(j - 1, n - 1)]
        for k in range(i, j):
            pts[keyed[k][1]] = val
        i = j
    return pts


class Sfx:
    def __init__(self):
        self.enabled = False
        self.muted = False
        self.sounds = {}
        init = pygame.mixer.get_init()
        if not init:
            try:
                pygame.mixer.init()
                init = pygame.mixer.get_init()
            except pygame.error:
                return
        if not init:
            return
        self.sr, _, self.channels = init[0], init[1], init[2]
        if ANDROID:
            threading.Thread(target=self._build_all, daemon=True).start()
        else:
            self._build_all()

    def _build_all(self):
        rng = random.Random(20260714)

        def pack(samples):
            """浮點樣本 → int16 位元組(依混音器聲道數交錯)。"""
            import array
            out = array.array("h")
            for j, v in enumerate(samples):
                if ANDROID and (j & 4095) == 0:
                    time.sleep(0.001)     # 讓出 GIL
                s = int(max(-1.0, min(1.0, v)) * 30000)
                for _ in range(self.channels):
                    out.append(s)
            return pygame.mixer.Sound(buffer=out.tobytes())

        sr = self.sr

        def build(dur, fn):
            n = int(sr * dur)
            return pack(fn(i / sr, i) for i in range(n))

        # 水柱爆炸:水花轟濺 + 咕嚕氣泡串 + 低頻水湧
        bubbles_sched = [(0.03 + rng.random() * 0.05, 480 + rng.random() * 160),
                         (0.12 + rng.random() * 0.05, 340 + rng.random() * 120),
                         (0.22 + rng.random() * 0.06, 240 + rng.random() * 90),
                         (0.32 + rng.random() * 0.06, 180 + rng.random() * 70)]

        def _explode(t, i):
            atk = min(1.0, t / 0.012)
            splash = (rng.random() * 2 - 1) * math.exp(-t * 5.5) * 0.5 * atk
            gurgle = 0.72 + 0.28 * math.sin(2 * math.pi * 11 * t) \
                * math.sin(2 * math.pi * 4 * t)
            bub = 0.0
            for (bt, bf) in bubbles_sched:
                if bt <= t < bt + 0.09:
                    tt = t - bt
                    bub += math.sin(2 * math.pi * (bf - 150 * tt / 0.09) * tt) \
                        * math.exp(-tt * 26) * 0.45
            surge = math.sin(2 * math.pi * (95 - 55 * min(1, t * 2.2)) * t) \
                * math.exp(-t * 8) * 0.5
            return splash * gurgle + bub + surge
        self.sounds["explode"] = build(0.55, _explode)

        # 戳破:水滴「啵嚕」(頻率先揚後落,像水珠落水)
        def _pop(t, i):
            if t < 0.028:
                f = 380 + (980 - 380) * (t / 0.028)
            else:
                f = 980 - (980 - 230) * min(1.0, (t - 0.028) / 0.075)
            body = math.sin(2 * math.pi * f * t) * math.exp(-t * 24) * 0.85
            blub = math.sin(2 * math.pi * 165 * t) * math.exp(-t * 34) * 0.32
            return body + blub
        self.sounds["pop"] = build(0.13, _pop)

        # 被泡住:上揚顫音「咕嚕」
        def _trap(t, i):
            f = 180 + 340 * (t / 0.28) + 30 * math.sin(2 * math.pi * 24 * t)
            env = min(1.0, t * 30) * math.exp(-t * 6)
            return math.sin(2 * math.pi * f * t) * env * 0.7
        self.sounds["trap"] = build(0.28, _trap)

        # 場地攻擊警報:雙音交替鳴笛
        def _alarm(t, i):
            f = 760 if int(t / 0.16) % 2 == 0 else 540
            sq = 1.0 if math.sin(2 * math.pi * f * t) >= 0 else -1.0
            edge = min(1.0, t * 20, (1.0 - t) * 20)
            return sq * 0.28 * edge
        self.sounds["alarm"] = build(1.0, _alarm)

        # 放水球:輕柔「噗通」
        def _place(t, i):
            f = 330 - 140 * min(1.0, t / 0.08)
            return math.sin(2 * math.pi * f * t) * math.exp(-t * 30) * 0.5
        self.sounds["place"] = build(0.09, _place)

        # 撿道具:兩段上行叮聲
        def _item(t, i):
            if t < 0.08:
                f, tt = 660, t
            else:
                f, tt = 990, t - 0.08
            return math.sin(2 * math.pi * f * t) * math.exp(-tt * 22) * 0.45
        self.sounds["item"] = build(0.18, _item)

        # 進球歡呼:人群聲浪(噪音湧起 + 高頻口哨)
        def _cheer(t, i):
            d = 1.2
            swell = min(1.0, t / 0.18) * math.exp(-max(0.0, t - 0.55) * 3.2)
            crowd = (rng.random() * 2 - 1) * swell * 0.5
            roar = 0.7 + 0.3 * math.sin(2 * math.pi * 6.5 * t)
            wh = 0.0
            for (wt, wf) in ((0.15, 1450), (0.45, 1650)):
                if wt <= t < wt + 0.22:
                    tt = t - wt
                    wh += math.sin(2 * math.pi * (wf + 300 * tt) * t) \
                        * math.exp(-tt * 9) * 0.18
            return crowd * roar + wh
        self.sounds["cheer"] = build(1.2, _cheer)

        # 技能施放:掃頻嗖聲
        def _skill(t, i):
            d = 0.2
            n = (rng.random() * 2 - 1) * (t / d) * (1 - t / d) * 1.1
            chirp = math.sin(2 * math.pi * (300 + 2600 * t) * t) * 0.35 \
                * math.exp(-t * 5)
            return n * 0.5 + chirp
        self.sounds["skill"] = build(0.2, _skill)

        # 連殺播報:階梯式音階(雙殺2音…五連殺5音+號角)
        NOTES = [523.25, 659.25, 783.99, 987.77, 1174.66]
        for n in range(2, 6):
            seq = NOTES[:n]
            gapd = 0.11
            durn = gapd * n + 0.35

            def _mk(seq=seq, gapd=gapd, n=n):
                def _f(t, i):
                    v = 0.0
                    for k2, f2 in enumerate(seq):
                        st2 = k2 * gapd
                        if st2 <= t < st2 + 0.22:
                            tt = t - st2
                            v += (1.0 if math.sin(2 * math.pi * f2 * t) >= 0
                                  else -1.0) * 0.22 * math.exp(-tt * 9)
                    if n >= 5 and t >= gapd * n:      # 五殺:號角尾音
                        tt = t - gapd * n
                        v += math.sin(2 * math.pi * 1046.5 * t) \
                            * math.exp(-tt * 4) * 0.3
                        v += (rng.random() * 2 - 1) * math.exp(-tt * 8) * 0.2
                    return v
                return _f
            self.sounds["dk%d" % n] = build(durn, _mk())

        for snd in self.sounds.values():
            snd.set_volume(SFX_VOLUME)
        self.enabled = True

    def play(self, name):
        if self.enabled and not self.muted and name in self.sounds:
            self.sounds[name].play()

    def toggle_mute(self):
        self.muted = not self.muted


class SfxDetector:
    """觀察遊戲狀態變化來觸發音效(主機與客戶端共用同一套邏輯)。"""
    def __init__(self):
        self.gid = None

    def _baseline(self, g):
        self.gid = id(g)
        self.blast_keys = set(g.blasts.keys())
        self.trapped = {p.id: p.trapped for p in g.players}
        self.n_hazards = len(getattr(g, "hazards", []))
        self.n_strikes = len(getattr(g, "strikes", []))
        self.n_bubbles = len(g.bubbles)
        self.item_keys = set(g.items.keys())
        self.skill_cd = {p.id: p.skill_cd for p in g.players}
        self.scores = tuple(getattr(g, "scores", (0, 0)))
        self.feed_n = len(getattr(g, "feed", []))
        self.feed_seen = {id(fe) for fe in getattr(g, "feed", [])}

    def tick(self, g, sfx):
        if g is None or sfx is None or not sfx.enabled:
            return
        if id(g) != self.gid:
            self._baseline(g)
            return
        events = []
        bk = set(g.blasts.keys())
        if bk - self.blast_keys:
            events.append("explode")
        for p in g.players:
            was = self.trapped.get(p.id, False)
            if p.trapped and not was:
                events.append("trap")
            elif was and not p.trapped and p.alive:
                events.append("pop")
            if p.skill_cd > self.skill_cd.get(p.id, 0.0) + 0.5:
                events.append("skill")
        nh = len(getattr(g, "hazards", []))
        ns = len(getattr(g, "strikes", []))
        if nh > self.n_hazards or ns > self.n_strikes:
            events.append("alarm")
        if len(g.bubbles) > self.n_bubbles:
            events.append("place")
        ik = set(g.items.keys())
        if self.item_keys - ik and not (bk - self.blast_keys):
            events.append("item")
        if tuple(getattr(g, "scores", (0, 0))) > self.scores:
            events.append("cheer")
        for fe in getattr(g, "feed", []):
            if id(fe) not in self.feed_seen and fe.get("m", 0) >= 2:
                events.append("dk%d" % min(5, fe["m"]))
        self._baseline(g)
        for name in events[:3]:      # 每幀最多 3 個音效,避免轟炸
            sfx.play(name)


_TEXT_CACHE = {}


def render_text(size, text, color):
    """帶快取的文字渲染(HUD/名牌每幀重複字串直接命中)。"""
    key = (size, text, color)
    surf = _TEXT_CACHE.get(key)
    if surf is None:
        if len(_TEXT_CACHE) > 800:
            _TEXT_CACHE.clear()
        surf = get_font(size).render(text, True, color)
        _TEXT_CACHE[key] = surf
    return surf


def music_group_for(state):
    """依畫面狀態決定音樂群組。"""
    if state in ("game", "net_game"):
        return "battle"
    if state in ("room_menu", "name_entry", "char_sel",
                 "net_join", "room_host", "room_client"):
        return "room"
    return "title"


# ----------------------------------------------------------------------
# 常數設定
# ----------------------------------------------------------------------
TILE = 48                      # 每格像素
COLS, ROWS = 15, 13            # 地圖大小(含外牆)
HUD_H = 68                     # 底部資訊列高度
SCREEN_W = COLS * TILE
SCREEN_H = ROWS * TILE + HUD_H
FPS = 60

FLOOR, SOFT, HARD = 0, 1, 2   # 地板 / 可破壞箱子 / 不可破壞磚

BUBBLE_FUSE = 3.0             # 水球引信秒數
BLAST_TIME = 0.55             # 水柱停留秒數
TRAP_TIME = 6.0               # 被困住的存活倒數
TRAP_GRACE = 0.8              # 剛被困住的短暫無敵(避免同一發水柱連續判定)
ITEM_DROP_RATE = 0.60         # 箱子掉道具機率

HITBOX = TILE * 0.60          # 玩家碰撞盒(比一格小,轉彎較滑順)

# 對戰/組隊的殘局機制:限時 + 場地崩塌(原作靠時間限制逼和,系列作用縮圈)
MATCH_TIME = 120.0            # 每局時間(秒),時間到平手
SD_START = 45.0               # 剩餘秒數低於此值 → 外圈磚塊開始落下
SD_INTERVAL = 0.45            # 每隔幾秒落下一塊
SD_WARN = 1.0                 # 落下前的紅色預警秒數

# 終局狂熱(最後 45 秒的四階段加壓)
FEVER_FUSE = 2.1              # 狂熱期間新水球的引信秒數
FEVER_SPEED = 1.12            # 狂熱期間全員移速倍率
RAIN_START = 30.0             # 剩餘秒數低於此值 → 道具雨
RAIN_EVERY = 2.0              # 道具雨間隔
SD_FAST_AT = 18.0             # 剩餘秒數低於此值 → 崩塌加速
SD_FAST_INTERVAL = 0.26       # 加速後的落石間隔
FINAL_AT = 10.0               # 剩餘秒數低於此值 → 全員威力 +1

# 場地攻擊事件(對戰/組隊):轟炸機空襲、企鵝衝鋒,攻擊前紅色驚嘆號預警
HAZARD_FIRST = 5.0            # 開場多久後開始第一次場地攻擊
HAZARD_EVERY = (4.0, 7.0)    # 之後每隔幾秒一次(隨機區間)
HAZARD_WARN = 1.3             # 驚嘆號預警秒數

DIRS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

# ----------------------------------------------------------------------
# 地圖定義(8 張,各有配色 / 地形產生器 / 參數)
#   layout: checker=經典棋盤柱  airy=稀疏柱  rocks=對稱亂石  cross=十字牆
#           rows=橫向廠房牆  arena=中央競技場  maze=棒倒法迷宮
#   soft: 箱子密度   drop: 道具掉落率   speed: 全體移速倍率
# ----------------------------------------------------------------------
MAPS = [
    dict(zh="青青草原", en="Grassland", layout="checker", soft=0.72, drop=0.60, speed=1.0,
         colors=dict(fa=(168, 212, 120), fb=(156, 202, 110),
                     hard=(110, 116, 126), hard_dark=(82, 88, 98), hard_top=(140, 146, 156),
                     soft=(196, 140, 78), soft_dark=(150, 100, 52), soft_light=(224, 176, 116))),
    dict(zh="黃沙綠洲", en="Desert", layout="rocks", soft=0.55, drop=0.60, speed=1.0,
         colors=dict(fa=(232, 208, 150), fb=(224, 198, 138),
                     hard=(158, 120, 86), hard_dark=(118, 86, 58), hard_top=(190, 152, 110),
                     soft=(172, 120, 64), soft_dark=(128, 86, 42), soft_light=(206, 158, 98))),
    dict(zh="冰晶湖", en="Frozen Lake", layout="airy", soft=0.62, drop=0.60, speed=1.18,
         colors=dict(fa=(208, 232, 244), fb=(194, 222, 238),
                     hard=(128, 158, 190), hard_dark=(92, 122, 154), hard_top=(168, 198, 224),
                     soft=(148, 202, 234), soft_dark=(102, 158, 198), soft_light=(210, 240, 252))),
    dict(zh="熔岩洞窟", en="Lava Cave", layout="cross", soft=0.65, drop=0.72, speed=1.0,
         colors=dict(fa=(96, 74, 70), fb=(88, 66, 62),
                     hard=(60, 50, 58), hard_dark=(36, 28, 36), hard_top=(94, 82, 92),
                     soft=(176, 92, 52), soft_dark=(124, 58, 30), soft_light=(232, 144, 72))),
    dict(zh="幽暗森林", en="Deep Forest", layout="checker", soft=0.88, drop=0.55, speed=1.0,
         colors=dict(fa=(96, 138, 84), fb=(86, 128, 76),
                     hard=(98, 106, 96), hard_dark=(70, 78, 68), hard_top=(130, 138, 126),
                     soft=(138, 102, 58), soft_dark=(98, 68, 36), soft_light=(178, 140, 90))),
    dict(zh="齒輪工廠", en="Gear Factory", layout="rows", soft=0.60, drop=0.60, speed=1.0,
         colors=dict(fa=(176, 180, 188), fb=(164, 168, 176),
                     hard=(92, 98, 110), hard_dark=(60, 66, 78), hard_top=(128, 134, 146),
                     soft=(208, 164, 60), soft_dark=(150, 112, 32), soft_light=(236, 200, 110))),
    dict(zh="陽光沙灘", en="Sunny Beach", layout="arena", soft=0.55, drop=0.65, speed=1.0,
         open_center=True,
         colors=dict(fa=(244, 226, 180), fb=(236, 216, 168),
                     hard=(140, 128, 116), hard_dark=(104, 94, 84), hard_top=(176, 164, 150),
                     soft=(196, 140, 78), soft_dark=(148, 98, 50), soft_light=(226, 178, 116))),
    dict(zh="夜色迷宮", en="Night Maze", layout="maze", soft=0.50, drop=0.65, speed=1.0,
         colors=dict(fa=(88, 84, 122), fb=(80, 76, 112),
                     hard=(54, 50, 86), hard_dark=(34, 30, 60), hard_top=(110, 104, 152),
                     soft=(148, 106, 152), soft_dark=(106, 70, 112), soft_light=(192, 152, 198))),
    # ---- 機關地圖(場地互動:履帶/泥沼/大砲/傳送門,原創設計) ----
    dict(zh="星光跑道", en="Star Speedway", layout="rows", soft=0.55, drop=0.62, speed=1.0,
         colors=dict(fa=(70, 66, 110), fb=(62, 58, 100),
                     hard=(44, 42, 78), hard_dark=(28, 26, 54), hard_top=(96, 92, 140),
                     soft=(120, 110, 190), soft_dark=(84, 76, 140), soft_light=(164, 154, 226)),
         feat=[("belt", 3, c, 1, 0) for c in range(2, 13)]
              + [("belt", 9, c, -1, 0) for c in range(2, 13)]),
    dict(zh="泥沼濕地", en="Murky Marsh", layout="rocks", soft=0.62, drop=0.62, speed=1.0,
         colors=dict(fa=(126, 150, 96), fb=(116, 140, 88),
                     hard=(86, 96, 66), hard_dark=(58, 68, 44), hard_top=(112, 124, 90),
                     soft=(150, 116, 70), soft_dark=(108, 80, 46), soft_light=(186, 150, 100)),
         feat=[("mud", r, c) for (r, c) in
               ((2, 4), (2, 10), (4, 7), (6, 3), (6, 11),
                (8, 7), (10, 4), (10, 10), (5, 5), (7, 9))]),
    dict(zh="砲彈要塞", en="Cannon Keep", layout="cross", soft=0.60, drop=0.65, speed=1.0,
         colors=dict(fa=(180, 172, 158), fb=(170, 162, 148),
                     hard=(110, 104, 96), hard_dark=(78, 74, 66), hard_top=(142, 136, 126),
                     soft=(150, 108, 78), soft_dark=(108, 74, 50), soft_light=(188, 146, 112)),
         feat=[("cannon", 6, 1, 1, 0, 5), ("cannon", 6, 13, -1, 0, 5),
               ("cannon", 1, 7, 0, 1, 4), ("cannon", 11, 7, 0, -1, 4)]),
    dict(zh="幻境之門", en="Portal Haven", layout="airy", soft=0.58, drop=0.65, speed=1.0,
         colors=dict(fa=(110, 92, 148), fb=(100, 84, 136),
                     hard=(70, 56, 104), hard_dark=(46, 36, 72), hard_top=(140, 120, 180),
                     soft=(168, 120, 190), soft_dark=(122, 82, 142), soft_light=(206, 164, 224)),
         feat=[("portal", 2, 2, 0), ("portal", 10, 12, 0),
               ("portal", 2, 12, 1), ("portal", 10, 2, 1)]),
    dict(zh="工廠生產線", en="Assembly Lines", layout="checker", soft=0.60, drop=0.62, speed=1.0,
         colors=dict(fa=(148, 154, 166), fb=(138, 144, 156),
                     hard=(92, 98, 110), hard_dark=(64, 70, 80), hard_top=(120, 126, 138),
                     soft=(186, 140, 84), soft_dark=(140, 100, 56), soft_light=(220, 176, 120)),
         feat=[("belt", r, 3, 0, 1) for r in range(2, 11)]
              + [("belt", r, 11, 0, -1) for r in range(2, 11)]),
    dict(zh="火山口", en="Crater Rim", layout="arena", soft=0.58, drop=0.65, speed=1.0,
         colors=dict(fa=(150, 84, 62), fb=(140, 76, 56),
                     hard=(90, 46, 38), hard_dark=(60, 28, 24), hard_top=(122, 66, 52),
                     soft=(198, 120, 60), soft_dark=(150, 84, 38), soft_light=(232, 162, 96)),
         feat=[("cannon", 3, 7, 0, 1, 5), ("cannon", 9, 7, 0, -1, 5),
               ("mud", 6, 5), ("mud", 6, 9), ("mud", 4, 7), ("mud", 8, 7)]),
    dict(zh="雪原滑道", en="Frost Run", layout="airy", soft=0.55, drop=0.62, speed=1.12,
         colors=dict(fa=(226, 238, 248), fb=(214, 228, 242),
                     hard=(150, 174, 202), hard_dark=(110, 134, 164), hard_top=(190, 212, 236),
                     soft=(170, 210, 238), soft_dark=(124, 168, 202), soft_light=(224, 246, 254)),
         feat=[("belt", 1, c, 1, 0) for c in range(3, 12)]
              + [("belt", 11, c, -1, 0) for c in range(3, 12)]),
    dict(zh="混沌樂園", en="Chaos Park", layout="arena", soft=0.58, drop=0.68, speed=1.0,
         colors=dict(fa=(238, 190, 160), fb=(230, 180, 150),
                     hard=(150, 96, 120), hard_dark=(110, 64, 88), hard_top=(184, 128, 152),
                     soft=(120, 170, 200), soft_dark=(80, 124, 154), soft_light=(164, 210, 234)),
         feat=[("portal", 1, 7, 0), ("portal", 11, 7, 0),
               ("belt", 6, 2, 1, 0), ("belt", 6, 3, 1, 0), ("belt", 6, 4, 1, 0),
               ("belt", 6, 10, -1, 0), ("belt", 6, 11, -1, 0), ("belt", 6, 12, -1, 0),
               ("mud", 3, 3), ("mud", 3, 11), ("mud", 9, 3), ("mud", 9, 11),
               ("cannon", 6, 7, 0, -1, 4)]),
    # ---- 風景地圖(豐富造景 + 環境粒子 + 機關組合,原創設計) ----
    dict(zh="櫻花庭園", en="Sakura Garden", layout="checker", soft=0.62, drop=0.64,
         speed=1.0, ambient="petals",
         colors=dict(fa=(206, 226, 168), fb=(196, 216, 158),
                     hard=(150, 128, 118), hard_dark=(110, 90, 84), hard_top=(184, 160, 148),
                     soft=(226, 184, 150), soft_dark=(178, 136, 104), soft_light=(248, 216, 184)),
         deco=[("sakura", 2, 2), ("sakura", 2, 12), ("sakura", 10, 2), ("sakura", 10, 12),
               ("sakura", 4, 6), ("sakura", 8, 8), ("lantern", 2, 6), ("lantern", 10, 8),
               ("torii", 6, 7), ("flower", 3, 3), ("flower", 3, 11), ("flower", 9, 3),
               ("flower", 9, 11), ("flower", 5, 7), ("flower", 7, 7)],
         feat=[("portal", 3, 7, 0), ("portal", 9, 7, 0),
               ("mud", 6, 4), ("mud", 6, 10)]),
    dict(zh="楓紅山莊", en="Maple Lodge", layout="rocks", soft=0.60, drop=0.64,
         speed=1.0, ambient="leaves",
         colors=dict(fa=(214, 186, 132), fb=(204, 176, 124),
                     hard=(134, 100, 74), hard_dark=(96, 68, 50), hard_top=(168, 130, 96),
                     soft=(196, 148, 96), soft_dark=(150, 106, 62), soft_light=(230, 186, 132)),
         deco=[("maple", 2, 3), ("maple", 2, 11), ("maple", 10, 3), ("maple", 10, 11),
               ("house", 2, 7), ("house", 10, 7), ("rock", 6, 3), ("rock", 6, 11),
               ("grass", 4, 5), ("grass", 8, 9), ("grass", 4, 9), ("grass", 8, 5)],
         feat=[("belt", 6, 5, 1, 0), ("belt", 6, 6, 1, 0), ("belt", 6, 7, 1, 0),
               ("belt", 6, 8, 1, 0), ("belt", 6, 9, 1, 0),
               ("cannon", 4, 2, 1, 0, 10), ("cannon", 8, 12, -1, 0, 10)]),
    dict(zh="雪夜小鎮", en="Snowy Town", layout="rows", soft=0.60, drop=0.64,
         speed=1.0, ambient="snow",
         colors=dict(fa=(206, 220, 238), fb=(196, 210, 230),
                     hard=(116, 132, 162), hard_dark=(82, 96, 124), hard_top=(150, 168, 198),
                     soft=(172, 190, 216), soft_dark=(124, 142, 172), soft_light=(222, 236, 250)),
         deco=[("house_snow", 2, 2), ("house_snow", 2, 12), ("house_snow", 10, 2),
               ("house_snow", 10, 12), ("house_snow", 2, 7),
               ("pine", 4, 4), ("pine", 4, 10), ("pine", 8, 4), ("pine", 8, 10),
               ("snowman", 6, 2), ("snowman", 6, 12),
               ("pebble", 5, 7), ("pebble", 7, 6)],
         feat=[("ice", 6, 5), ("ice", 6, 6), ("ice", 6, 7), ("ice", 6, 8), ("ice", 6, 9),
               ("portal", 3, 7, 0), ("portal", 9, 7, 0)]),
    dict(zh="沙漠遺跡", en="Desert Ruins", layout="cross", soft=0.58, drop=0.66,
         speed=1.0,
         colors=dict(fa=(232, 208, 150), fb=(222, 198, 142),
                     hard=(176, 142, 96), hard_dark=(132, 102, 66), hard_top=(208, 174, 124),
                     soft=(206, 168, 112), soft_dark=(160, 124, 76), soft_light=(240, 208, 156)),
         deco=[("cactus", 2, 3), ("cactus", 2, 11), ("cactus", 10, 3), ("cactus", 10, 11),
               ("rock", 4, 2), ("rock", 8, 12), ("rock", 6, 4), ("rock", 6, 10),
               ("pebble", 3, 7), ("pebble", 9, 7), ("pebble", 5, 5), ("pebble", 7, 9)],
         feat=[("cannon", 2, 7, 0, 1, 8), ("cannon", 10, 7, 0, -1, 8),
               ("mud", 4, 5), ("mud", 4, 9), ("mud", 8, 5), ("mud", 8, 9)]),
    dict(zh="螢火之森", en="Firefly Woods", layout="maze", soft=0.52, drop=0.66,
         speed=1.0, ambient="fireflies",
         colors=dict(fa=(96, 122, 92), fb=(88, 114, 86),
                     hard=(62, 82, 66), hard_dark=(42, 58, 46), hard_top=(88, 112, 90),
                     soft=(134, 112, 84), soft_dark=(96, 78, 56), soft_light=(174, 150, 116)),
         deco=[("tree", 2, 4), ("tree", 2, 10), ("tree", 10, 4), ("tree", 10, 10),
               ("mushroom", 4, 2), ("mushroom", 8, 12),
               ("grass", 3, 7), ("grass", 9, 7), ("grass", 6, 5), ("grass", 6, 9)],
         feat=[("mud", 6, 4), ("mud", 6, 10),
               ("portal", 3, 3, 0), ("portal", 9, 11, 0)]),
    dict(zh="海底王宮", en="Coral Palace", layout="airy", soft=0.58, drop=0.66,
         speed=1.0, ambient="bubbles",
         colors=dict(fa=(74, 128, 158), fb=(68, 120, 150),
                     hard=(46, 84, 116), hard_dark=(30, 60, 88), hard_top=(70, 112, 146),
                     soft=(188, 138, 104), soft_dark=(142, 96, 66), soft_light=(224, 178, 140)),
         deco=[("coral", 2, 3), ("coral", 2, 11), ("coral", 10, 3), ("coral", 10, 11),
               ("coral", 6, 3), ("coral", 6, 11), ("crystal", 2, 7), ("crystal", 10, 7),
               ("shell", 4, 5), ("shell", 8, 9), ("shell", 5, 7), ("shell", 7, 7)],
         feat=[("belt", 3, 4, 0, 1), ("belt", 4, 4, 0, 1), ("belt", 5, 4, 0, 1),
               ("belt", 7, 10, 0, -1), ("belt", 8, 10, 0, -1), ("belt", 9, 10, 0, -1)]),
    dict(zh="熔岩工房", en="Magma Forge", layout="arena", soft=0.58, drop=0.68,
         speed=1.0, ambient="embers",
         colors=dict(fa=(96, 62, 58), fb=(88, 56, 52),
                     hard=(66, 42, 44), hard_dark=(44, 26, 30), hard_top=(96, 62, 60),
                     soft=(150, 92, 62), soft_dark=(110, 62, 40), soft_light=(196, 134, 92)),
         deco=[("crystal_red", 2, 2), ("crystal_red", 2, 12), ("crystal_red", 10, 2),
               ("crystal_red", 10, 12), ("rock", 2, 7), ("rock", 10, 7),
               ("pebble", 4, 4), ("pebble", 8, 10)],
         feat=[("mud", 4, 4), ("mud", 4, 10), ("mud", 8, 4), ("mud", 8, 10),
               ("cannon", 3, 2, 1, 0, 10), ("cannon", 9, 12, -1, 0, 10),
               ("belt", 6, 6, 1, 0), ("belt", 6, 7, 1, 0), ("belt", 6, 8, 1, 0)]),
    dict(zh="天空棧道", en="Sky Walk", layout="airy", soft=0.52, drop=0.68,
         speed=1.05, ambient="snow",
         colors=dict(fa=(198, 222, 244), fb=(188, 214, 238),
                     hard=(150, 172, 204), hard_dark=(112, 134, 168), hard_top=(186, 208, 236),
                     soft=(216, 226, 244), soft_dark=(164, 178, 206), soft_light=(244, 250, 255)),
         deco=[("crystal", 2, 4), ("crystal", 2, 10), ("crystal", 10, 4), ("crystal", 10, 10),
               ("lantern", 6, 7), ("flower", 3, 7), ("flower", 9, 7),
               ("flower", 6, 4), ("flower", 6, 10)],
         feat=[("belt", 2, 6, 1, 0), ("belt", 2, 7, 1, 0), ("belt", 2, 8, 1, 0),
               ("belt", 10, 6, -1, 0), ("belt", 10, 7, -1, 0), ("belt", 10, 8, -1, 0),
               ("ice", 6, 6), ("ice", 6, 8),
               ("portal", 5, 2, 0), ("portal", 7, 12, 0)]),
    # ---- 進階風景地圖(彈跳墊/開關門新機關 + 更豐富造景) ----
    dict(zh="和風溫泉", en="Hot Spring Inn", layout="checker", soft=0.60, drop=0.66,
         speed=1.0, ambient="steam",
         colors=dict(fa=(182, 200, 176), fb=(172, 190, 168),
                     hard=(128, 112, 100), hard_dark=(92, 78, 70), hard_top=(162, 144, 128),
                     soft=(214, 176, 138), soft_dark=(166, 128, 92), soft_light=(244, 210, 172)),
         deco=[("house", 2, 2), ("house", 2, 12), ("torii", 2, 7),
               ("lantern", 6, 3), ("lantern", 6, 11), ("rock", 10, 2), ("rock", 10, 12),
               ("bamboo", 10, 7), ("flower", 3, 5), ("flower", 3, 9),
               ("pebble", 9, 5), ("pebble", 9, 9)],
         feat=[("mud", 5, 6), ("mud", 5, 8), ("mud", 7, 6), ("mud", 7, 8),
               ("spring", 3, 7), ("spring", 9, 7),
               ("portal", 6, 2, 0), ("portal", 6, 12, 0)]),
    dict(zh="幽靈古堡", en="Haunted Keep", layout="maze", soft=0.52, drop=0.66,
         speed=1.0, ambient="fireflies",
         colors=dict(fa=(104, 100, 126), fb=(96, 92, 118),
                     hard=(66, 62, 88), hard_dark=(44, 40, 62), hard_top=(94, 88, 118),
                     soft=(140, 118, 150), soft_dark=(100, 80, 110), soft_light=(182, 158, 194)),
         deco=[("lantern", 2, 4), ("lantern", 2, 10), ("lantern", 10, 4), ("lantern", 10, 10),
               ("crystal", 6, 3), ("crystal", 6, 11), ("rock", 2, 7), ("rock", 10, 7),
               ("pebble", 5, 7), ("pebble", 7, 7)],
         feat=[("switch", 3, 7, 0), ("switch", 9, 7, 0),
               ("gate", 6, 6, 0), ("gate", 6, 7, 0), ("gate", 6, 8, 0),
               ("portal", 5, 2, 0), ("portal", 7, 12, 0)]),
    dict(zh="糖果樂園", en="Candy Land", layout="arena", soft=0.60, drop=0.70,
         speed=1.0, ambient="petals",
         colors=dict(fa=(244, 208, 224), fb=(236, 198, 216),
                     hard=(196, 130, 170), hard_dark=(150, 92, 128), hard_top=(226, 166, 202),
                     soft=(240, 190, 150), soft_dark=(196, 142, 100), soft_light=(255, 226, 190)),
         deco=[("mushroom", 2, 2), ("mushroom", 2, 12), ("mushroom", 10, 2),
               ("mushroom", 10, 12), ("crystal", 2, 7), ("crystal_red", 10, 7),
               ("flower", 4, 4), ("flower", 4, 10), ("flower", 8, 4), ("flower", 8, 10)],
         feat=[("belt", 6, 3, 0, -1), ("belt", 6, 11, 0, 1),
               ("ice", 3, 7), ("ice", 9, 7),
               ("spring", 6, 5), ("spring", 6, 9)]),
    dict(zh="廢棄礦坑", en="Old Mine", layout="rows", soft=0.62, drop=0.68,
         speed=1.0, ambient="embers",
         colors=dict(fa=(140, 122, 104), fb=(132, 114, 98),
                     hard=(92, 78, 66), hard_dark=(64, 52, 44), hard_top=(122, 104, 88),
                     soft=(158, 126, 88), soft_dark=(116, 90, 60), soft_light=(196, 162, 120)),
         deco=[("rock", 2, 2), ("rock", 2, 12), ("rock", 10, 2), ("rock", 10, 12),
               ("crystal", 4, 6), ("crystal_red", 8, 8), ("lantern", 2, 7), ("lantern", 10, 7),
               ("pebble", 5, 5), ("pebble", 7, 9)],
         feat=[("belt", 4, 4, 1, 0), ("belt", 4, 5, 1, 0), ("belt", 4, 6, 1, 0),
               ("belt", 8, 8, -1, 0), ("belt", 8, 9, -1, 0), ("belt", 8, 10, -1, 0),
               ("switch", 6, 3, 0), ("switch", 6, 11, 0),
               ("gate", 6, 6, 0), ("gate", 6, 8, 0),
               ("cannon", 2, 4, 0, 1, 8)]),
    dict(zh="竹林小徑", en="Bamboo Path", layout="airy", soft=0.58, drop=0.66,
         speed=1.0, ambient="leaves",
         colors=dict(fa=(168, 196, 140), fb=(158, 186, 132),
                     hard=(104, 128, 88), hard_dark=(74, 94, 62), hard_top=(134, 160, 112),
                     soft=(186, 158, 112), soft_dark=(140, 114, 74), soft_light=(222, 196, 150)),
         deco=[("bamboo", 2, 3), ("bamboo", 2, 11), ("bamboo", 10, 3), ("bamboo", 10, 11),
               ("bamboo", 6, 5), ("bamboo", 6, 9), ("rock", 2, 7), ("rock", 10, 7),
               ("grass", 4, 6), ("grass", 8, 8), ("grass", 4, 8), ("grass", 8, 6),
               ("flower", 6, 7)],
         feat=[("spring", 3, 3), ("spring", 3, 11), ("spring", 9, 3), ("spring", 9, 11),
               ("mud", 5, 7), ("mud", 7, 7)]),
    dict(zh="星空天文台", en="Star Observatory", layout="airy", soft=0.54, drop=0.68,
         speed=1.0, ambient="fireflies",
         colors=dict(fa=(64, 72, 112), fb=(58, 66, 104),
                     hard=(44, 50, 84), hard_dark=(28, 32, 58), hard_top=(70, 78, 118),
                     soft=(122, 108, 150), soft_dark=(86, 74, 110), soft_light=(164, 148, 192)),
         deco=[("crystal", 2, 3), ("crystal", 2, 11), ("crystal", 10, 3), ("crystal", 10, 11),
               ("lantern", 6, 7), ("rock", 2, 7), ("rock", 10, 7),
               ("pebble", 4, 5), ("pebble", 8, 9)],
         feat=[("portal", 3, 3, 0), ("portal", 9, 11, 0),
               ("portal", 3, 11, 1), ("portal", 9, 3, 1),
               ("ice", 6, 5), ("ice", 6, 7), ("ice", 6, 9)]),
    dict(zh="海賊灣", en="Pirate Cove", layout="rocks", soft=0.60, drop=0.70,
         speed=1.0, ambient="bubbles",
         colors=dict(fa=(216, 196, 152), fb=(206, 186, 144),
                     hard=(120, 104, 82), hard_dark=(86, 72, 56), hard_top=(152, 134, 106),
                     soft=(178, 134, 92), soft_dark=(132, 96, 62), soft_light=(214, 174, 128)),
         deco=[("house", 2, 7), ("rock", 2, 3), ("rock", 10, 11),
               ("coral", 10, 3), ("coral", 2, 11), ("coral", 10, 7),
               ("shell", 4, 5), ("shell", 8, 9), ("shell", 6, 7), ("pebble", 4, 9)],
         feat=[("cannon", 3, 2, 1, 0, 10), ("cannon", 9, 12, -1, 0, 10),
               ("cannon", 2, 10, 0, 1, 8), ("cannon", 10, 4, 0, -1, 8),
               ("spring", 6, 4), ("spring", 6, 10),
               ("mud", 5, 7), ("mud", 7, 7)]),
    dict(zh="終焉鐘樓", en="Clock Tower", layout="cross", soft=0.56, drop=0.70,
         speed=1.0, ambient="embers",
         colors=dict(fa=(112, 96, 92), fb=(104, 88, 86),
                     hard=(74, 60, 62), hard_dark=(50, 38, 42), hard_top=(104, 86, 86),
                     soft=(150, 116, 94), soft_dark=(110, 82, 64), soft_light=(192, 156, 128)),
         deco=[("crystal_red", 2, 2), ("crystal_red", 10, 12), ("lantern", 2, 12),
               ("lantern", 10, 2), ("rock", 4, 2), ("rock", 8, 12),
               ("torii", 2, 7), ("pebble", 5, 5), ("pebble", 7, 9)],
         feat=[("switch", 6, 2, 0), ("switch", 6, 12, 0),
               ("gate", 5, 7, 0), ("gate", 7, 7, 0),
               ("spring", 3, 4), ("spring", 9, 10),
               ("belt", 10, 6, 1, 0), ("belt", 10, 7, 1, 0), ("belt", 10, 8, 1, 0),
               ("portal", 3, 10, 0), ("portal", 9, 4, 0),
               ("ice", 6, 6), ("ice", 6, 8)]),
]


# ----------------------------------------------------------------------
# 章魚王 Boss 模式(合作討伐)
# ----------------------------------------------------------------------
BOSS_MAP = dict(zh="深海王座", en="Abyss Throne", drop=0.70, speed=1.0,
                colors=dict(fa=(70, 110, 150), fb=(64, 102, 142),
                            hard=(40, 60, 92), hard_dark=(24, 40, 64), hard_top=(66, 92, 128),
                            soft=(196, 122, 90), soft_dark=(140, 82, 56), soft_light=(232, 162, 120)))

BOSS_HP = 24                 # 「普通」難度的章魚王血量(每次爆炸命中 -1)
BOSS_IFRAME = 0.45           # 受擊無敵幀(同一發爆炸只算 1 滴血)
BOSS_ENRAGE_AT = 0.3         # 血量低於 30% 進入紅血狂暴
BOSS_ZONE_ROWS = (1, 6)      # Boss 活動的開闊區(列範圍)

# 章魚王難度(hp=基礎血量 per=每多一位玩家加血 atk=攻擊間隔倍率(小=快)
#   pw/epw=水球威力(平常/狂暴) toss=丟球數 cap/ecap=小章魚上限
#   bar/ebar=彈幕數 msp=小章魚速度 bsp=Boss移速倍率 needles=玩家自帶針 drop=道具率)
BOSS_DIFFS = [
    dict(zh="簡單", en="Easy", hp=18, per=4, atk=1.3, pw=2, epw=2, toss=2,
         cap=1, ecap=2, bar=6, ebar=8, msp=1.7, bsp=0.85, needles=3, drop=0.78),
    dict(zh="普通", en="Normal", hp=24, per=6, atk=1.0, pw=2, epw=3, toss=2,
         cap=2, ecap=3, bar=8, ebar=10, msp=2.0, bsp=1.0, needles=2, drop=0.70),
    dict(zh="困難", en="Hard", hp=32, per=7, atk=0.8, pw=3, epw=3, toss=3,
         cap=3, ecap=4, bar=10, ebar=13, msp=2.3, bsp=1.15, needles=2, drop=0.65),
    dict(zh="地獄", en="Nightmare", hp=40, per=8, atk=0.62, pw=3, epw=4, toss=4,
         cap=3, ecap=5, bar=12, ebar=16, msp=2.6, bsp=1.3, needles=1, drop=0.62),
]
BOSS_STARTS = [(ROWS - 2, 1), (ROWS - 2, COLS - 2), (ROWS - 2, 3),
               (ROWS - 2, COLS - 4), (ROWS - 2, 5), (ROWS - 2, COLS - 6),
               (ROWS - 2, 7), (ROWS - 3, 1)]

# 台詞為本遊戲原創
BOSS_TAUNTS_BARRAGE = [("接招!水彈狂潮!", "Taste my bubble storm!"),
                       ("淹沒吧,小鬼們!", "Drown, little pests!")]
BOSS_TAUNTS_MISC = [("咕嚕嚕……好癢啊!", "Blub blub... that tickles!"),
                    ("就這點程度嗎?", "Is that all you've got?"),
                    ("我的海域不歡迎你們!", "You're not welcome in my sea!")]
BOSS_TAUNT_ENRAGE = ("氣死我了!!", "Now I'm ANGRY!!")


def build_boss_grid():
    """章魚王競技場:上半部開闊(Boss 區),下半部箱子與少數柱子。"""
    grid = [[FLOOR] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            if r in (0, ROWS - 1) or c in (0, COLS - 1):
                grid[r][c] = HARD
    for (r, c) in ((8, 3), (8, 11), (10, 5), (10, 9)):
        grid[r][c] = HARD
    for r in range(7, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] == FLOOR and random.random() < 0.45:
                grid[r][c] = SOFT
    # 清出所有玩家的重生區(下排,含向上的逃生走道)
    for (sr, sc) in BOSS_STARTS:
        for (r, c) in ((sr, sc), (sr - 1, sc), (sr - 2, sc),
                       (sr, sc + 1), (sr, sc - 1)):
            if 0 < r < ROWS - 1 and 0 < c < COLS - 1:
                grid[r][c] = FLOOR
    return grid


def _spawns_connected(grid):
    """確認四個出生點在(忽略箱子的)硬牆地形下互通。"""
    start = SPAWNS[0]
    seen = {start}
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dy, c + dx
            if (0 <= rr < ROWS and 0 <= cc < COLS
                    and grid[rr][cc] != HARD and (rr, cc) not in seen):
                seen.add((rr, cc))
                q.append((rr, cc))
    return all(s in seen for s in SPAWNS)


def build_grid(cfg, rng=random):
    """依地圖設定產生地形;硬牆佈局會做連通性檢查,確保四個出生點互通。"""
    kind = cfg["layout"]
    if kind == "soccer":
        # 足球場:對稱柱 + 稀疏箱,左右邊界開球門
        grid = [[FLOOR] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1):
                    grid[r][c] = HARD
        for (r, c) in ((3, 4), (3, 10), (9, 4), (9, 10),
                       (6, 3), (6, 11)):
            grid[r][c] = HARD
        for (r, c) in ((2, 6), (2, 8), (10, 6), (10, 8),
                       (4, 7), (8, 7), (5, 4), (5, 10),
                       (7, 4), (7, 10), (3, 2), (3, 12),
                       (9, 2), (9, 12)):
            grid[r][c] = SOFT
        for r in GOAL_ROWS:          # 球門開口
            grid[r][0] = FLOOR
            grid[r][COLS - 1] = FLOOR
        return grid
    grid = None
    for _ in range(60):
        grid = [[FLOOR] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1):
                    grid[r][c] = HARD

        def pillar_all():
            for r in range(2, ROWS - 1, 2):
                for c in range(2, COLS - 1, 2):
                    grid[r][c] = HARD

        if kind == "checker":
            pillar_all()
        elif kind == "airy":                    # 稀疏柱,較空曠
            for r in range(2, ROWS - 1, 2):
                for c in range(2, COLS - 1, 2):
                    if rng.random() < 0.68:
                        grid[r][c] = HARD
        elif kind == "rocks":                   # 四向對稱亂石
            placed = 0
            while placed < 14:
                r = rng.randint(2, ROWS - 3)
                c = rng.randint(2, COLS - 3)
                pts = {(r, c), (r, COLS - 1 - c),
                       (ROWS - 1 - r, c), (ROWS - 1 - r, COLS - 1 - c)}
                for rr, cc in pts:
                    grid[rr][cc] = HARD
                placed += len(pts)
        elif kind == "cross":                   # 棋盤柱 + 十字牆(留缺口)
            pillar_all()
            midr, midc = ROWS // 2, COLS // 2
            for c in range(1, COLS - 1):
                if c not in (3, 5, 9, 11):
                    grid[midr][c] = HARD
            for r in range(1, ROWS - 1):
                if r not in (3, 5, 7, 9):
                    grid[r][midc] = HARD
        elif kind == "rows":                    # 橫向廠房牆,隨機開門
            for r in (3, 6, 9):
                for c in range(1, COLS - 1):
                    grid[r][c] = HARD
                for c in rng.sample(range(2, COLS - 2), 4):
                    grid[r][c] = FLOOR
        elif kind == "arena":                   # 中央開闊競技場
            midr, midc = ROWS // 2, COLS // 2
            for r in range(2, ROWS - 1, 2):
                for c in range(2, COLS - 1, 2):
                    if abs(r - midr) > 2 or abs(c - midc) > 3:
                        grid[r][c] = HARD
        elif kind == "maze":                    # 棒倒法迷宮
            pillar_all()
            for r in range(2, ROWS - 1, 2):
                for c in range(2, COLS - 1, 2):
                    dx, dy = rng.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
                    rr, cc = r + dy, c + dx
                    if 0 < rr < ROWS - 1 and 0 < cc < COLS - 1:
                        grid[rr][cc] = HARD

        # 清出四個角落重生區(硬牆也清)
        for (sr, sc) in SPAWNS:
            for (r, c) in ((sr, sc), (sr + 1, sc), (sr - 1, sc),
                           (sr, sc + 1), (sr, sc - 1)):
                if 0 < r < ROWS - 1 and 0 < c < COLS - 1:
                    grid[r][c] = FLOOR

        if _spawns_connected(grid):
            break

    # 放箱子
    midr, midc = ROWS // 2, COLS // 2
    open_center = cfg.get("open_center", False)
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] != FLOOR:
                continue
            if open_center and abs(r - midr) <= 2 and abs(c - midc) <= 3:
                continue        # 競技場中央保持空曠
            if rng.random() < cfg["soft"]:
                grid[r][c] = SOFT

    # 重生區不放箱子
    for (sr, sc) in SPAWNS:
        for (r, c) in ((sr, sc), (sr + 1, sc), (sr - 1, sc),
                       (sr, sc + 1), (sr, sc - 1)):
            if 0 < r < ROWS - 1 and 0 < c < COLS - 1 and grid[r][c] == SOFT:
                grid[r][c] = FLOOR

    # 場地機關格(履帶/泥沼/冰面/大砲/傳送門)保持空地
    for spec in cfg.get("feat", []):
        r, c = spec[1], spec[2]
        if 0 < r < ROWS - 1 and 0 < c < COLS - 1:
            grid[r][c] = FLOOR

    # 場景造景:實體造景佔用硬磚格,花草類保持地板淨空
    for (kind, r, c) in cfg.get("deco", []):
        if not (0 < r < ROWS - 1 and 0 < c < COLS - 1):
            continue
        grid[r][c] = HARD if kind in DECO_SOLID else FLOOR
    # 保險絲:造景硬磚若與隨機牆型組合封死出生點,逐一降級直到連通
    if cfg.get("deco") and not _spawns_connected(grid):
        for (kind, r, c) in cfg["deco"]:
            if kind in DECO_SOLID and grid[r][c] == HARD:
                grid[r][c] = FLOOR
                if _spawns_connected(grid):
                    break
    return grid

# 顏色
C_FLOOR_A = (168, 212, 120)
C_FLOOR_B = (156, 202, 110)
C_HARD = (110, 116, 126)
C_HARD_DARK = (82, 88, 98)
C_SOFT = (196, 140, 78)
C_SOFT_DARK = (150, 100, 52)
C_SOFT_LIGHT = (224, 176, 116)
C_WATER = (120, 190, 255)
C_WATER_CORE = (225, 245, 255)
C_BUBBLE = (140, 200, 255)
C_HUD = (36, 40, 52)
C_TEXT = (240, 240, 240)

MAX_PLAYERS = 8

PLAYER_COLORS = [
    (235, 80, 80),    # P1 紅
    (80, 130, 240),   # P2 藍
    (170, 90, 220),   # P3 紫
    (245, 160, 50),   # P4 橘
    (60, 190, 170),   # P5 青
    (240, 120, 180),  # P6 粉
    (120, 200, 80),   # P7 綠
    (250, 210, 70),   # P8 黃
]

# ----------------------------------------------------------------------
# 道具總表(16 種)
#   weight: 出現機率權重   desc: 圖鑑說明(自寫)
# ----------------------------------------------------------------------
ITEM_DEFS = {
    "bubble":   dict(zh="水球",     en="Bubble",     weight=20,
                     dz=["可同時放置的水球數量 +1"],
                     de=["Max bubbles you can place +1"]),
    "potion":   dict(zh="藥水",     en="Potion",     weight=20,
                     dz=["水柱威力(射程)+1"],
                     de=["Blast power (range) +1"]),
    "shoe":     dict(zh="溜冰鞋",   en="Roller",     weight=13,
                     dz=["移動速度提升"],
                     de=["Move speed up"]),
    "ultra":    dict(zh="大力藥丸", en="Ultra",      weight=3,
                     dz=["水球威力立刻升到最大!"],
                     de=["Blast power instantly MAXED!"]),
    "reddevil": dict(zh="紅色惡魔", en="Red Devil",  weight=3,
                     dz=["移動速度立刻升到最大!"],
                     de=["Move speed instantly MAXED!"]),
    "needle":   dict(zh="針",       en="Needle",     weight=8,
                     dz=["被困在泡泡裡時,按放球鍵", "刺破泡泡自救"],
                     de=["While trapped, press your bomb", "key to pop free"]),
    "dart":     dict(zh="飛鏢",     en="Dart",       weight=6,
                     dz=["按使用鍵朝面向射出,", "引爆直線上第一顆水球"],
                     de=["Press USE key to shoot; detonates", "the first bubble in a line"]),
    "glove":    dict(zh="拳套",     en="Glove",      weight=5,
                     dz=["站在水球上按放球鍵把它丟出去,", "可飛越障礙,出界會繞到對面"],
                     de=["Stand on a bubble + bomb key to", "throw it; flies over walls, wraps"]),
    "kick":     dict(zh="運動鞋",   en="Kick Shoes", weight=5,
                     dz=["朝水球走過去就能把它踢出去,", "一路滑到撞上東西為止"],
                     de=["Walk into a bubble to kick it;", "slides until it hits something"]),
    "turtle":   dict(zh="烏龜",     en="Turtle",     weight=5,
                     dz=["坐騎:速度變慢,", "但能替你擋下一次水柱"],
                     de=["Mount: slow, but absorbs", "one water blast for you"]),
    "owl":      dict(zh="貓頭鷹",   en="Owl",        weight=4,
                     dz=["坐騎:速度略增,", "並能替你擋下一次水柱"],
                     de=["Mount: a bit faster, absorbs", "one water blast for you"]),
    "ufo":      dict(zh="飛碟",     en="UFO",        weight=3,
                     dz=["坐騎:高速、可飛越箱子,", "但騎乘時撿不到道具"],
                     de=["Mount: fast, flies over boxes,", "but can't pick up items"]),
    "ghost":    dict(zh="隱形衣",   en="Ghost",      weight=4,
                     dz=["短時間隱形,只剩淡淡影子,", "電腦也不會鎖定你"],
                     de=["Turn near-invisible for a while;", "CPUs won't target you"]),
    "shield":   dict(zh="無敵光盾", en="Shield",     weight=3,
                     dz=["短時間無敵,", "水柱完全傷不到你"],
                     de=["Brief invincibility;", "water blasts can't touch you"]),
    "radar":    dict(zh="泡泡雷達", en="Radar",      weight=4,
                     dz=["短時間顯示全場水球的", "爆炸範圍(紅色區域)"],
                     de=["Shows every bubble's blast", "range for a while (red zones)"]),
    "devil":    dict(zh="惡魔面具", en="Devil Mask", weight=6,
                     dz=["中咒!一段時間反向操作", "或是不受控地亂放水球"],
                     de=["Cursed! Reversed controls or", "uncontrollably dropping bubbles"]),
    # ---- 擴充道具(擴充模式限定,原創設計) ----
    "hook":     dict(zh="鉤爪", en="Grapple Hook", weight=6, ext=True,
                     dz=["朝面向射出鉤爪,勾住牆或箱子", "把自己快速拉過去(位移神器)"],
                     de=["Fires at walls/boxes ahead and", "yanks you to them. Mobility!"]),
    "missile":  dict(zh="飛彈", en="Missile", weight=5, ext=True,
                     dz=["朝面向發射,撞到牆、箱子、", "水球或玩家就爆出十字水柱"],
                     de=["Flies ahead; explodes in a cross", "on walls, boxes, bubbles, players"]),
    "magnet":   dict(zh="磁力槍", en="Magnet Gun", weight=5, ext=True,
                     dz=["把直線上第一個玩家或水球", "吸到自己面前(光盾可擋)"],
                     de=["Pulls the first player or bubble", "in a line to you (shield blocks)"]),
    "freeze":   dict(zh="冰凍槍", en="Freeze Ray", weight=5, ext=True,
                     dz=["直線冰凍第一個敵人約 2 秒,", "動彈不得也不能放球"],
                     de=["Freezes the first enemy hit for", "~2s: no moving, no bombing"]),
}
ITEM_ORDER = list(ITEM_DEFS.keys())
ITEM_WEIGHTS = [ITEM_DEFS[k]["weight"] for k in ITEM_ORDER]

# 主動道具(佔用手持道具槽,按使用鍵發動;同種可疊 3 個,撿新種類會替換)
ACTIVE_KINDS = {"dart", "hook", "missile", "magnet", "freeze"}
ITEM_CHAR = {"dart": ("鏢", "D"), "hook": ("鉤", "H"), "missile": ("彈", "M"),
             "magnet": ("磁", "G"), "freeze": ("冰", "F")}


# ----------------------------------------------------------------------
# 角色(8 隻,原創設計;連線房間進場前選擇,技能鍵 C,冷卻制)
# ----------------------------------------------------------------------
CHAR_DEFS = [
    dict(key="hoop", zh="神射手", en="Hoopster", skill_zh="長距投籃",
         skill_en="Long Shot", cd=5.0,
         dz=["把水球拋投到前方 4 格,", "無視中間所有障礙"],
         de=["Lob a bubble 4 tiles ahead,", "flying over all obstacles"]),
    dict(key="strike", zh="足球明星", en="Striker", skill_zh="香蕉球",
         skill_en="Banana Kick", cd=6.0,
         dz=["踢出前進 2 格後轉彎的", "曲線水球(短引信)"],
         de=["Kick a bubble that curves", "after 2 tiles (short fuse)"]),
    dict(key="engineer", zh="工程師", en="Engineer", skill_zh="X 型炸藥",
         skill_en="X-Charge", cd=7.0,
         dz=["放置特殊水球,", "爆炸呈對角線 X 字形"],
         de=["Place a special bubble that", "explodes in an X pattern"]),
    dict(key="sword", zh="劍客", en="Swordsman", skill_zh="居合斬",
         skill_en="Iai Slash", cd=3.5,
         dz=["斬碎面前的箱子或引爆水球,", "爆炸不會朝自己這側延伸"],
         de=["Slash the box/bubble ahead;", "the blast spares your side"]),
    dict(key="ninja", zh="忍者", en="Ninja", skill_zh="瞬身",
         skill_en="Blink", cd=7.0,
         dz=["向前瞬移最多 3 格,", "可穿過牆、箱子與水球"],
         de=["Blink up to 3 tiles ahead,", "through walls, boxes, bubbles"]),
    dict(key="medic", zh="醫護兵", en="Medic", skill_zh="急救",
         skill_en="First Aid", cd=9.0,
         dz=["淨化自身詛咒並獲得短護盾;", "合作/組隊可救 4 格內被困隊友"],
         de=["Cleanse curses + brief shield;", "frees trapped allies within 4"]),
    dict(key="guard", zh="守護者", en="Guardian", skill_zh="築牆",
         skill_en="Wall Up", cd=8.0,
         dz=["在面前築起一道臨時石牆", "(5 秒),可阻擋水柱與企鵝"],
         de=["Raise a temporary stone wall", "ahead (5s); blocks blasts"]),
    dict(key="chrono", zh="時空行者", en="Chrono", skill_zh="回溯",
         skill_en="Rewind", cd=8.0,
         dz=["瞬間回到自己", "3 秒前所在的位置"],
         de=["Teleport back to where you", "were 3 seconds ago"]),
    dict(key="cyclone", zh="氣旋使", en="Cyclone", skill_zh="颶風掌",
         skill_en="Gale Palm", cd=7.0,
         dz=["把身邊的敵人全部轟退兩格,", "鄰接的水球也會被踢飛"],
         de=["Blast nearby foes 2 tiles away;", "adjacent bubbles get kicked"]),
    dict(key="mortar", zh="砲手", en="Mortar", skill_zh="迫擊砲",
         skill_en="Mortar Shot", cd=6.0,
         dz=["朝前方 3 格轟出震撼彈:炸箱、", "引爆水球,震退並暈眩敵人"],
         de=["Lob a concussion shell: smash", "boxes, daze & knock foes back"]),
    dict(key="trapper", zh="獵人", en="Trapper", skill_zh="捕獸夾",
         skill_en="Snare Trap", cd=8.0,
         dz=["在腳下佈半隱形陷阱(12秒),", "敵人踩到定身 1.5 秒"],
         de=["Plant a faint trap (12s);", "enemies stepping in are rooted"]),
    dict(key="bull", zh="蠻牛", en="Bull", skill_zh="蠻牛衝撞",
         skill_en="Rampage", cd=7.0,
         dz=["向前猛衝最多 4 格,", "撞到的人被推開並暈眩"],
         de=["Charge up to 4 tiles;", "victims are shoved and dazed"]),
    dict(key="phantom", zh="幻影師", en="Phantom", skill_zh="換位術",
         skill_en="Switcheroo", cd=6.0,
         dz=["與面前直線上自己最近的", "水球交換位置(可穿牆)"],
         de=["Swap places with your nearest", "bubble ahead (through walls)"]),
    dict(key="frost", zh="冰霜使", en="Frost", skill_zh="霜華綻放",
         skill_en="Frost Nova", cd=9.0,
         dz=["周圍兩格內的所有敵人", "凍結 1.2 秒(光盾可擋)"],
         de=["Freeze all foes within 2 tiles", "for 1.2s (shield blocks it)"]),
    dict(key="ripple", zh="水靈", en="Ripple", skill_zh="漣漪足跡",
         skill_en="Wake Trail", cd=9.0,
         dz=["2.5 秒內走過的路留下水漬,", "敵人踩到濕身減速 2.2 秒"],
         de=["Leave a water trail for 2.5s;", "foes touching it get slowed"]),
    dict(key="tempo", zh="節奏使", en="Tempo", skill_zh="狂想加速",
         skill_en="Uptempo", cd=8.0,
         dz=["自己與身旁的隊友", "移動速度 x1.6 共 2.5 秒"],
         de=["You and adjacent allies gain", "x1.6 move speed for 2.5s"]),
    dict(key="sarge", zh="士官長", en="Sarge", skill_zh="空襲信標",
         skill_en="Air Strike", cd=9.0,
         dz=["標記前方直線 3 格,一秒後", "水彈轟炸(紅色預警可閃)"],
         de=["Mark 3 tiles ahead; after 1s", "they get bombed (dodgeable)"]),
    dict(key="corsair", zh="海盜船長", en="Corsair", skill_zh="掠奪之手",
         skill_en="Plunder", cd=8.0,
         dz=["偷走身邊敵人的優先槽道具", "佔為己有(光盾可擋)"],
         de=["Steal an adjacent foe's item", "for yourself (shield blocks)"]),
    dict(key="volt", zh="電光使", en="Volt", skill_zh="雷光疾馳",
         skill_en="Volt Rush", cd=7.0,
         dz=["1.4 秒內移速 x2,", "並可直接穿過水球"],
         de=["x2 speed for 1.4s and pass", "straight through bubbles"]),
    dict(key="boomer", zh="爆破專家", en="Boomer", skill_zh="遙控水雷",
         skill_en="Remote Mine", cd=4.0,
         dz=["放置遙控水球(8 秒內有效),", "再按一次 C 隨時引爆"],
         de=["Place a remote bubble (8s);", "press C again to detonate"]),
    dict(key="angler", zh="釣客", en="Angler", skill_zh="精準甩竿",
         skill_en="Cast Line", cd=5.0,
         dz=["把面前直線 4 格內", "最近的道具釣回來"],
         de=["Reel in the nearest item", "within 4 tiles ahead"]),
    dict(key="gardener", zh="園丁", en="Gardener", skill_zh="快速種樹",
         skill_en="Overgrowth", cd=8.0,
         dz=["前方直線種出 3 個木箱", "(不掉道具),改造地形"],
         de=["Grow 3 boxes in a line ahead", "(no item drops); shape terrain"]),
    dict(key="vendor", zh="氣球商人", en="Vendor", skill_zh="限時特賣",
         skill_en="Flash Sale", cd=12.0,
         dz=["水球 +1、威力 +1,", "持續 6 秒後恢復"],
         de=["+1 bubble & +1 power", "for 6 seconds"]),
    dict(key="sumo", zh="力士", en="Sumo", skill_zh="震地踏",
         skill_en="Quake Stomp", cd=7.0,
         dz=["震退身邊敵人,兩格內的", "水球引信全部剩 0.4 秒"],
         de=["Shove nearby foes; bubbles", "within 2 tiles fuse to 0.4s"]),
]


def draw_char_icon(s, cx, cy, ch_ix, color, rad=14):
    """角色頭像(原創簡易造型):玩家色圓身 + 職業配件。"""
    pygame.draw.circle(s, color, (cx, cy), rad)
    dark = tuple(max(0, v - 60) for v in color)
    pygame.draw.circle(s, dark, (cx, cy), rad, 2)
    for dd in (-rad // 3, rad // 3):
        pygame.draw.circle(s, (255, 255, 255), (cx + dd, cy - 2), rad // 4 + 1)
        pygame.draw.circle(s, (30, 30, 40), (cx + dd, cy - 2), rad // 8 + 1)
    key = CHAR_DEFS[ch_ix]["key"] if ch_ix is not None else None
    if key == "hoop":       # 髮帶 + 籃球
        pygame.draw.rect(s, (240, 120, 40), (cx - rad, cy - rad + 2, rad * 2, 4))
        pygame.draw.circle(s, (235, 130, 50), (cx + rad - 2, cy + rad - 2), rad // 2)
        pygame.draw.line(s, (120, 60, 20), (cx + rad - 2 - rad // 2, cy + rad - 2),
                         (cx + rad - 2 + rad // 2, cy + rad - 2), 1)
    elif key == "strike":   # 足球
        pygame.draw.circle(s, (245, 245, 245), (cx - rad + 2, cy + rad - 2), rad // 2)
        pygame.draw.circle(s, (40, 40, 50), (cx - rad + 2, cy + rad - 2), rad // 5)
    elif key == "engineer":  # 工程帽
        pygame.draw.rect(s, (250, 200, 60), (cx - rad + 2, cy - rad - 2, rad * 2 - 4, rad // 2 + 3),
                         border_radius=4)
        pygame.draw.rect(s, (250, 200, 60), (cx - rad - 2, cy - rad // 2 - 2, rad * 2 + 4, 3))
    elif key == "sword":    # 武士刀
        pygame.draw.line(s, (210, 215, 225), (cx + rad - 4, cy + rad),
                         (cx + rad + 6, cy - rad - 4), 3)
        pygame.draw.line(s, (120, 80, 50), (cx + rad - 6, cy + rad + 3),
                         (cx + rad - 2, cy + rad - 2), 4)
    elif key == "ninja":    # 面罩
        pygame.draw.rect(s, (50, 55, 75), (cx - rad, cy - rad // 2 - 4, rad * 2, rad // 2 + 2))
        pygame.draw.line(s, (200, 60, 60), (cx + rad - 2, cy - rad // 2),
                         (cx + rad + 6, cy - rad // 2 + 4), 2)
    elif key == "medic":    # 十字臂章
        pygame.draw.circle(s, (255, 255, 255), (cx - rad + 3, cy + rad - 4), rad // 2)
        cr = rad // 3
        pygame.draw.rect(s, (220, 60, 60), (cx - rad + 3 - cr, cy + rad - 4 - 1, cr * 2, 3))
        pygame.draw.rect(s, (220, 60, 60), (cx - rad + 2, cy + rad - 4 - cr, 3, cr * 2))
    elif key == "guard":    # 小盾牌
        pts = [(cx + rad - 2, cy), (cx + rad + 5, cy + 3), (cx + rad + 5, cy + 9),
               (cx + rad - 2, cy + 13), (cx + rad - 9, cy + 9), (cx + rad - 9, cy + 3)]
        pygame.draw.polygon(s, (90, 160, 240), pts)
        pygame.draw.polygon(s, (40, 90, 170), pts, 1)
    elif key == "chrono":   # 時鐘
        pygame.draw.circle(s, (250, 245, 220), (cx - rad + 3, cy - rad + 3), rad // 2)
        pygame.draw.line(s, (60, 60, 80), (cx - rad + 3, cy - rad + 3),
                         (cx - rad + 3, cy - rad - 1), 2)
        pygame.draw.line(s, (60, 60, 80), (cx - rad + 3, cy - rad + 3),
                         (cx - rad + 6, cy - rad + 3), 2)
    elif key == "cyclone":  # 旋風紋
        for k in range(3):
            pygame.draw.arc(s, (200, 240, 255),
                            (cx + rad - 10 - k * 3, cy + rad - 10 - k * 3,
                             14 + k * 6, 14 + k * 6),
                            0.5 + k, 2.6 + k, 2)
    elif key == "mortar":   # 鋼盔 + 砲彈
        pygame.draw.arc(s, (110, 120, 90), (cx - rad, cy - rad - 4, rad * 2, rad + 6),
                        3.14, 6.28, 5)
        pygame.draw.ellipse(s, (70, 74, 84), (cx + rad - 8, cy + rad - 6, 14, 9))
    elif key == "trapper":  # 捕獸夾
        jx, jy = cx - rad + 2, cy + rad - 3
        pygame.draw.circle(s, (180, 186, 200), (jx, jy), 7, 2)
        for a in range(6):
            ang = a * 1.05
            pygame.draw.line(s, (180, 186, 200),
                             (jx + int(7 * math.cos(ang)), jy + int(7 * math.sin(ang))),
                             (jx + int(10 * math.cos(ang)), jy + int(10 * math.sin(ang))), 2)
    elif key == "bull":     # 牛角
        for sgn in (-1, 1):
            pygame.draw.arc(s, (235, 225, 205),
                            (cx + sgn * rad - 8, cy - rad - 6, 16, 16),
                            (0.3 if sgn > 0 else 1.6), (1.5 if sgn > 0 else 2.9), 4)
    elif key == "phantom":  # 半面具
        pygame.draw.polygon(s, (240, 240, 250),
                            [(cx, cy - rad + 2), (cx + rad - 1, cy - rad + 4),
                             (cx + rad - 3, cy + 4), (cx, cy + 2)])
        pygame.draw.circle(s, (40, 40, 60), (cx + rad // 2, cy - 2), 2)
    elif key == "frost":    # 雪花
        fx, fy = cx - rad + 3, cy - rad + 3
        for a in range(6):
            ang = a * 1.047
            pygame.draw.line(s, (210, 240, 255), (fx, fy),
                             (fx + int(8 * math.cos(ang)), fy + int(8 * math.sin(ang))), 2)
    elif key == "ripple":   # 水滴 + 漣漪
        pygame.draw.circle(s, (150, 210, 250), (cx - rad + 3, cy + rad - 4), 5)
        pygame.draw.circle(s, (150, 210, 250), (cx - rad + 3, cy + rad - 4), 9, 1)
    elif key == "tempo":    # 音符
        nx, ny = cx + rad - 4, cy - rad + 6
        pygame.draw.circle(s, (255, 235, 150), (nx - 3, ny + 8), 4)
        pygame.draw.line(s, (255, 235, 150), (nx + 1, ny + 8), (nx + 1, ny - 6), 2)
        pygame.draw.line(s, (255, 235, 150), (nx + 1, ny - 6), (nx + 7, ny - 3), 2)
    elif key == "sarge":    # 軍帽 + 肩章
        pygame.draw.rect(s, (90, 110, 70), (cx - rad + 1, cy - rad - 3, rad * 2 - 2, 6))
        pygame.draw.rect(s, (70, 88, 54), (cx - rad + 3, cy - rad + 2, rad * 2 - 6, 3))
        pygame.draw.line(s, (240, 210, 90), (cx + rad - 8, cy + rad - 6),
                         (cx + rad - 2, cy + rad - 9), 2)
        pygame.draw.line(s, (240, 210, 90), (cx + rad - 8, cy + rad - 2),
                         (cx + rad - 2, cy + rad - 5), 2)
    elif key == "corsair":  # 眼罩 + 金耳環
        pygame.draw.line(s, (30, 30, 40), (cx - rad, cy - rad // 2 - 3),
                         (cx + rad, cy - rad + 1), 2)
        pygame.draw.circle(s, (30, 30, 40), (cx + rad // 3, cy - 2), rad // 4 + 2)
        pygame.draw.circle(s, (250, 210, 90), (cx - rad + 1, cy + 4), 3, 2)
    elif key == "volt":     # 閃電紋
        pygame.draw.polygon(s, (255, 240, 120),
                            [(cx + rad - 2, cy - rad - 4), (cx + rad - 8, cy - 2),
                             (cx + rad - 3, cy - 2), (cx + rad - 10, cy + rad + 2),
                             (cx + rad + 2, cy - 5), (cx + rad - 3, cy - 5)])
    elif key == "boomer":   # 遙控器
        pygame.draw.rect(s, (200, 60, 60), (cx + rad - 8, cy + rad - 8, 12, 10),
                         border_radius=2)
        pygame.draw.line(s, (180, 186, 200), (cx + rad - 2, cy + rad - 8),
                         (cx + rad - 2, cy + rad - 16), 2)
        pygame.draw.circle(s, (255, 235, 130), (cx + rad - 2, cy + rad - 16), 2)
    elif key == "angler":   # 釣竿
        pygame.draw.line(s, (150, 110, 70), (cx - rad + 2, cy + rad + 2),
                         (cx + rad + 4, cy - rad - 4), 2)
        pygame.draw.line(s, (220, 226, 240), (cx + rad + 4, cy - rad - 4),
                         (cx + rad + 4, cy - 2), 1)
        pygame.draw.circle(s, (220, 226, 240), (cx + rad + 4, cy - 1), 2, 1)
    elif key == "gardener":  # 新芽
        gx, gy = cx - rad + 3, cy - rad + 4
        pygame.draw.line(s, (110, 180, 90), (gx, gy + 6), (gx, gy - 2), 2)
        pygame.draw.ellipse(s, (130, 200, 100), (gx - 7, gy - 6, 8, 5))
        pygame.draw.ellipse(s, (150, 215, 110), (gx - 1, gy - 7, 8, 5))
    elif key == "vendor":   # 氣球
        pygame.draw.ellipse(s, (250, 130, 150), (cx + rad - 8, cy - rad - 8, 11, 13))
        pygame.draw.line(s, (220, 226, 240), (cx + rad - 3, cy - rad + 5),
                         (cx + rad - 5, cy + 2), 1)
    elif key == "sumo":     # 髮髻 + 腰帶
        pygame.draw.circle(s, (40, 40, 50), (cx, cy - rad + 1), 4)
        pygame.draw.rect(s, (220, 220, 230), (cx - rad + 2, cy + rad - 7, rad * 2 - 4, 4))


def item_pool(ext):
    """回傳(種類清單, 權重清單)。ext=False 時排除擴充道具。"""
    kinds = [k for k in ITEM_ORDER if ext or not ITEM_DEFS[k].get("ext")]
    return kinds, [ITEM_DEFS[k]["weight"] for k in kinds]

# 效果秒數
GHOST_TIME = 10.0
SHIELD_TIME = 6.0
RADAR_TIME = 12.0
CURSE_TIME = 8.0
MOUNT_SPEED = {"turtle": 0.62, "owl": 1.15, "ufo": 1.35}
FIELD_SPAWN_EVERY = (2, 5)       # 場地隨機刷道具的間隔(秒,隨機區間)
FIELD_ITEM_CAP = 20               # 場上道具數量上限(含箱子掉的)

KEYMAPS = [
    {   # P1
        "dirs": {"up": pygame.K_w, "down": pygame.K_s,
                 "left": pygame.K_a, "right": pygame.K_d},
        "action": [pygame.K_SPACE],
        "use": [pygame.K_LCTRL, pygame.K_e],
        "skill": [pygame.K_q],
        "label": "WASD+Space",
    },
    {   # P2
        "dirs": {"up": pygame.K_UP, "down": pygame.K_DOWN,
                 "left": pygame.K_LEFT, "right": pygame.K_RIGHT},
        "action": [pygame.K_RETURN],
        "use": [pygame.K_RCTRL],
        "skill": [pygame.K_RSHIFT],
        "label": "Arrows+Enter",
    },
    {   # P3
        "dirs": {"up": pygame.K_i, "down": pygame.K_k,
                 "left": pygame.K_j, "right": pygame.K_l},
        "action": [pygame.K_o],
        "use": [pygame.K_p],
        "skill": [pygame.K_u],
        "label": "IJKL+O",
    },
    {   # P4
        "dirs": {"up": pygame.K_KP8, "down": pygame.K_KP5,
                 "left": pygame.K_KP4, "right": pygame.K_KP6},
        "action": [pygame.K_KP0, pygame.K_KP_ENTER],
        "use": [pygame.K_KP_PLUS, pygame.K_KP_PERIOD],
        "skill": [pygame.K_KP_MINUS],
        "label": "Numpad",
    },
]

# 連線房間專用鍵位:每位真人玩家(房主與加入者)都用同一套
NET_KEYMAP = {
    "dirs": {"up": pygame.K_UP, "down": pygame.K_DOWN,
             "left": pygame.K_LEFT, "right": pygame.K_RIGHT},
    "action": [pygame.K_SPACE],
    "use": [pygame.K_x],       # X 使用優先槽道具
    "swap": [pygame.K_z],      # Z 對調兩個道具槽
    "skill": [pygame.K_c],     # C 施放角色技能
}

# 電腦強度四級(房間可調;中級=原本的行為)
BOT_LEVELS = [
    dict(zh="初級", en="Easy",
         think=0.55, gadget=0.9, bomb_cd=1.7, rescue=1.2,
         act_p=0.45, err_p=0.28, soccer=0.30),
    dict(zh="中級", en="Normal",
         think=0.15, gadget=0.35, bomb_cd=1.0, rescue=0.5,
         act_p=1.0, err_p=0.0, soccer=0.15),
    dict(zh="高級", en="Hard",
         think=0.10, gadget=0.25, bomb_cd=0.75, rescue=0.35,
         act_p=1.0, err_p=0.0, soccer=0.12),
    dict(zh="專家", en="Expert",
         think=0.06, gadget=0.16, bomb_cd=0.5, rescue=0.18,
         act_p=1.0, err_p=0.0, soccer=0.10),
]

def is_real_pad(js):
    """過濾安卓的感應器假搖桿(加速度計等):沒有按鍵的不是手把。"""
    try:
        name = (js.get_name() or "").lower()
        if "accelerometer" in name or "sensor" in name:
            return False
        if js.get_numbuttons() == 0:
            return False
    except pygame.error:
        return False
    return True


def attach_local_input(game, tp, pads, touch, touch_ui):
    """本機玩家的輸入來源選擇:已綁手把者維持;有空閒手把先接手把;
    否則觸控;都沒有就清掉觸控殘留。鍵盤透過融合機制永遠可用。"""
    if tp is None:
        return
    used = {q.pad_iid for q in game.players if q is not tp}
    free = [i for i in pads if i not in used]
    if tp.pad_iid in pads:
        game.pads = pads                      # 已有實體手把:維持綁定
    elif free:
        game.pads = pads                      # 有空閒手把:優先用手把
        tp.pad_iid = free[0]
    elif touch_ui:
        game.pads["__touch__"] = touch        # 沒手把:退回觸控搖桿
        tp.pad_iid = "__touch__"
    elif tp.pad_iid == "__touch__":
        tp.pad_iid = None


def heal_pads(game, pads):
    """手把在安卓上常於首次輸入後重新註冊(instance id 改變)。
    把綁著失效 id 的玩家改接到現存的手把上。"""
    if game is None or not pads:
        return
    game.pads = pads
    used = {p.pad_iid for p in game.players}
    free = [i for i in pads if i not in used]
    for p in game.players:
        if (p.pad_iid is not None and p.pad_iid != "__touch__"
                and p.pad_iid not in pads and free):
            p.pad_iid = free.pop(0)


def window_to_logical(nx, ny, ww, wh, lw, lh):
    """把視窗正規化座標換算成邏輯畫面正規化座標(補償 SCALED 黑邊)。"""
    sc = min(ww / lw, wh / lh)
    ox = (ww - lw * sc) / 2.0
    oy = (wh - lh * sc) / 2.0
    return ((nx * ww - ox) / (sc * lw), (ny * wh - oy) / (sc * lh))


class TouchPad:
    """螢幕虛擬按鍵:左半螢幕拖曳=搖桿(相容 pad_dirs 介面),右下 ABXY。"""

    def __init__(self):
        self.stick_id = None
        self.origin = (0, 0)
        self.vec = (0.0, 0.0)
        self.actions = []          # "a"/"b"/"x"/"y"/"esc"
        self.btn_fingers = {}
        self.disp = (SCREEN_W, SCREEN_H)
        self.radius = 70
        self._cache = {}           # 繪製快取(效能)

    def _circle(self, key, r, col, alpha, ring):
        ck = (key, r, col, alpha, ring)
        surf = self._cache.get(ck)
        if surf is None:
            surf = pygame.Surface((r * 2 + 6,) * 2, pygame.SRCALPHA)
            pygame.draw.circle(surf, (*col, alpha), (r + 3,) * 2, r)
            pygame.draw.circle(surf, (*col, min(255, alpha + 90)),
                               (r + 3,) * 2, r, ring)
            if len(self._cache) > 40:
                self._cache.clear()
            self._cache[ck] = surf
        return surf

    def _buttons(self, w, h):
        r = int(min(w, h) * 0.062)
        cx, cy = w - int(r * 3.4), h - int(r * 3.2)
        return {"a": ((cx + int(r * 1.7), cy + int(r * 0.9)), int(r * 1.25)),
                "b": ((cx - int(r * 0.6), cy + int(r * 1.7)), r),
                "x": ((cx - int(r * 0.6), cy - int(r * 0.7)), r),
                "y": ((cx + int(r * 1.7), cy - int(r * 1.5)), r),
                "esc": ((int(r * 1.2), int(r * 1.1)), int(r * 0.9))}

    def handle(self, e, w, h):
        self.disp = (w, h)
        if e.type == pygame.FINGERDOWN:
            x, y = e.x * w, e.y * h
            for name, (c, r) in self._buttons(w, h).items():
                if math.hypot(x - c[0], y - c[1]) <= r * 1.25:
                    self.btn_fingers[e.finger_id] = name
                    self.actions.append(name)
                    return
            if x < w * 0.45 and self.stick_id is None:
                self.stick_id = e.finger_id
                self.origin = (x, y)
                self.vec = (0.0, 0.0)
        elif e.type == pygame.FINGERMOTION:
            if e.finger_id == self.stick_id:
                x, y = e.x * w, e.y * h
                dx = (x - self.origin[0]) / self.radius
                dy = (y - self.origin[1]) / self.radius
                m = math.hypot(dx, dy)
                if m > 1.0:
                    dx, dy = dx / m, dy / m
                self.vec = (dx, dy)
        elif e.type == pygame.FINGERUP:
            if e.finger_id == self.stick_id:
                self.stick_id = None
                self.vec = (0.0, 0.0)
            self.btn_fingers.pop(e.finger_id, None)

    def take(self):
        acts, self.actions = self.actions, []
        return acts

    # ---- 手把相容介面(給 pad_dirs 讀方向)----
    def get_numaxes(self):
        return 2

    def get_axis(self, i):
        return self.vec[0] if i == 0 else self.vec[1]

    def get_numhats(self):
        return 0

    def draw(self, surf, in_game):
        w, h = surf.get_size()
        if in_game and self.stick_id is not None:
            ox, oy = int(self.origin[0]), int(self.origin[1])
            base = self._circle("stick", self.radius + 2,
                                (255, 255, 255), 42, 3)
            surf.blit(base, (ox - self.radius - 5, oy - self.radius - 5))
            kx = ox + int(self.vec[0] * self.radius * 0.8)
            ky = oy + int(self.vec[1] * self.radius * 0.8)
            knob = self._circle("knob", 26, (255, 255, 255), 140, 2)
            surf.blit(knob, (kx - 29, ky - 29))
        labels = {"a": ("放球", (90, 180, 250)), "b": ("道具", (250, 190, 70)),
                  "x": ("技能", (190, 120, 250)), "y": ("換槽", (120, 220, 150)),
                  "esc": ("≡", (200, 208, 224))}
        show = ["esc"] + (["a", "b", "x", "y"] if in_game else [])
        for name in show:
            c, r = self._buttons(w, h)[name]
            zh, col = labels[name]
            bs = self._circle(name, r, col, 60, 3)
            surf.blit(bs, (c[0] - r - 3, c[1] - r - 3))
            lt = render_text(max(14, int(r * 0.5)), zh, (255, 255, 255))
            surf.blit(lt, lt.get_rect(center=c))


PAD_DEADZONE = 0.45


def pad_dirs(js):
    """讀取手把的方向輸入(左類比 + 十字鍵)。"""
    if js is None:
        return []
    dirs = set()
    try:
        ax = js.get_axis(0) if js.get_numaxes() > 0 else 0.0
        ay = js.get_axis(1) if js.get_numaxes() > 1 else 0.0
        if ax < -PAD_DEADZONE:
            dirs.add("left")
        elif ax > PAD_DEADZONE:
            dirs.add("right")
        if ay < -PAD_DEADZONE:
            dirs.add("up")
        elif ay > PAD_DEADZONE:
            dirs.add("down")
        if js.get_numhats() > 0:
            hx, hy = js.get_hat(0)
            if hx < 0:
                dirs.add("left")
            elif hx > 0:
                dirs.add("right")
            if hy > 0:
                dirs.add("up")
            elif hy < 0:
                dirs.add("down")
    except pygame.error:
        return []
    return list(dirs)


SPAWNS = [(1, 1), (ROWS - 2, COLS - 2), (1, COLS - 2), (ROWS - 2, 1),
          (1, COLS // 2), (ROWS - 2, COLS // 2),
          (ROWS // 2, 1), (ROWS // 2, COLS - 2)]


# ----------------------------------------------------------------------
# 字型(優先尋找中文字型,找不到就退回英文介面)
# ----------------------------------------------------------------------
_FONT_PATH = None
_HAS_CJK = False


ANDROID = ("ANDROID_ARGUMENT" in os.environ
           or "ANDROID_STORAGE" in os.environ
           or "P4A_BOOTSTRAP" in os.environ)


def _init_font():
    global _FONT_PATH, _HAS_CJK
    # Android:直接找系統 CJK 字型檔
    for fp in ("/system/fonts/NotoSansCJK-Regular.ttc",
               "/system/fonts/NotoSansCJKtc-Regular.otf",
               "/system/fonts/NotoSansTC-Regular.otf",
               "/system/fonts/DroidSansFallback.ttf"):
        if os.path.exists(fp):
            _FONT_PATH = fp
            _HAS_CJK = True
            return
    candidates = [
        "microsoftjhengheiui", "microsoftjhenghei", "msjh",
        "notosanscjktc", "notosanscjk", "notosanstc",
        "sourcehansanstc", "droidsansfallback", "simhei",
        "pingfangtc", "arialunicodems", "wenquanyimicrohei",
    ]
    for name in candidates:
        p = pygame.font.match_font(name)
        if p:
            _FONT_PATH = p
            _HAS_CJK = True
            return
    _FONT_PATH = None
    _HAS_CJK = False


_FONT_CACHE = {}


def get_font(size):
    f = _FONT_CACHE.get(size)
    if f is None:
        f = pygame.font.Font(_FONT_PATH, size)
        _FONT_CACHE[size] = f
    return f


def T(zh, en):
    """有中文字型就用中文,否則用英文。"""
    return zh if _HAS_CJK else en


# ----------------------------------------------------------------------
# 道具圖示(原創簡易圖形,遊戲內與圖鑑共用)
# ----------------------------------------------------------------------
def draw_item_icon(s, cx, cy, kind):
    if kind == "bubble":            # 水滴
        pygame.draw.circle(s, (70, 140, 255), (cx, cy + 2), 9)
        pygame.draw.polygon(s, (70, 140, 255),
                            [(cx, cy - 12), (cx - 7, cy), (cx + 7, cy)])
        pygame.draw.circle(s, (200, 230, 255), (cx - 3, cy), 3)
    elif kind == "potion":          # 紅藥水瓶
        pygame.draw.rect(s, (150, 90, 60), (cx - 3, cy - 13, 6, 6))
        pygame.draw.circle(s, (235, 70, 70), (cx, cy + 3), 9)
        pygame.draw.circle(s, (255, 160, 160), (cx - 3, cy), 3)
    elif kind == "shoe":            # 閃電(速度)
        pts = [(cx + 2, cy - 12), (cx - 7, cy + 2), (cx - 1, cy + 2),
               (cx - 3, cy + 12), (cx + 7, cy - 2), (cx + 1, cy - 2)]
        pygame.draw.polygon(s, (250, 200, 40), pts)
        pygame.draw.polygon(s, (200, 150, 20), pts, 2)
    elif kind == "ultra":           # 大力藥丸(膠囊)
        pygame.draw.circle(s, (235, 70, 70), (cx - 5, cy), 7)
        pygame.draw.circle(s, (255, 255, 255), (cx + 5, cy), 7)
        pygame.draw.rect(s, (235, 70, 70), (cx - 5, cy - 7, 5, 14))
        pygame.draw.rect(s, (255, 255, 255), (cx + 1, cy - 7, 5, 14))
        pygame.draw.circle(s, (120, 30, 30), (cx, cy), 12, 2)
    elif kind == "reddevil":        # 紅色惡魔(角)
        pygame.draw.circle(s, (220, 50, 50), (cx, cy + 2), 9)
        pygame.draw.polygon(s, (220, 50, 50),
                            [(cx - 9, cy - 4), (cx - 12, cy - 14), (cx - 4, cy - 8)])
        pygame.draw.polygon(s, (220, 50, 50),
                            [(cx + 9, cy - 4), (cx + 12, cy - 14), (cx + 4, cy - 8)])
        pygame.draw.circle(s, (255, 240, 120), (cx - 3, cy), 2)
        pygame.draw.circle(s, (255, 240, 120), (cx + 3, cy), 2)
    elif kind == "needle":          # 針
        pygame.draw.line(s, (120, 125, 135), (cx - 9, cy + 9), (cx + 8, cy - 8), 4)
        pygame.draw.circle(s, (235, 80, 80), (cx - 9, cy + 9), 4)
        pygame.draw.line(s, (235, 235, 245), (cx + 3, cy - 3), (cx + 9, cy - 9), 2)
    elif kind == "dart":            # 飛鏢(箭形)
        pygame.draw.polygon(s, (90, 96, 108),
                            [(cx + 11, cy - 11), (cx + 3, cy - 8), (cx + 8, cy - 3)])
        pygame.draw.line(s, (150, 156, 168), (cx + 7, cy - 7), (cx - 7, cy + 7), 4)
        pygame.draw.polygon(s, (235, 90, 90),
                            [(cx - 5, cy + 5), (cx - 12, cy + 6), (cx - 6, cy + 12)])
    elif kind == "glove":           # 拳套
        pygame.draw.circle(s, (230, 70, 70), (cx + 1, cy - 2), 9)
        pygame.draw.rect(s, (230, 70, 70), (cx - 9, cy - 4, 8, 10), border_radius=3)
        pygame.draw.rect(s, (250, 220, 220), (cx - 10, cy + 5, 10, 5), border_radius=2)
        pygame.draw.circle(s, (160, 30, 30), (cx + 1, cy - 2), 9, 2)
    elif kind == "kick":            # 運動鞋
        pygame.draw.polygon(s, (250, 250, 250),
                            [(cx - 11, cy - 6), (cx - 3, cy - 6), (cx + 4, cy),
                             (cx + 11, cy + 2), (cx + 11, cy + 7), (cx - 11, cy + 7)])
        pygame.draw.rect(s, (70, 120, 220), (cx - 11, cy + 5, 22, 4))
        pygame.draw.line(s, (150, 150, 160), (cx - 6, cy - 4), (cx - 2, cy), 2)
    elif kind == "turtle":          # 烏龜殼
        pygame.draw.circle(s, (90, 170, 90), (cx, cy), 10)
        pygame.draw.circle(s, (50, 120, 50), (cx, cy), 10, 2)
        pygame.draw.line(s, (50, 120, 50), (cx - 8, cy), (cx + 8, cy), 2)
        pygame.draw.line(s, (50, 120, 50), (cx - 4, cy - 8), (cx - 4, cy + 8), 2)
        pygame.draw.line(s, (50, 120, 50), (cx + 4, cy - 8), (cx + 4, cy + 8), 2)
        pygame.draw.circle(s, (120, 200, 120), (cx + 12, cy - 2), 4)   # 頭
    elif kind == "owl":             # 貓頭鷹
        pygame.draw.circle(s, (150, 110, 70), (cx, cy + 1), 10)
        pygame.draw.polygon(s, (150, 110, 70),
                            [(cx - 8, cy - 6), (cx - 10, cy - 13), (cx - 3, cy - 9)])
        pygame.draw.polygon(s, (150, 110, 70),
                            [(cx + 8, cy - 6), (cx + 10, cy - 13), (cx + 3, cy - 9)])
        for dd in (-4, 4):
            pygame.draw.circle(s, (255, 245, 220), (cx + dd, cy - 2), 4)
            pygame.draw.circle(s, (40, 30, 20), (cx + dd, cy - 2), 2)
        pygame.draw.polygon(s, (240, 180, 60),
                            [(cx - 2, cy + 2), (cx + 2, cy + 2), (cx, cy + 6)])
    elif kind == "ufo":             # 飛碟
        pygame.draw.ellipse(s, (150, 156, 170), (cx - 12, cy - 1, 24, 9))
        pygame.draw.ellipse(s, (100, 106, 120), (cx - 12, cy - 1, 24, 9), 2)
        pygame.draw.circle(s, (140, 210, 250), (cx, cy - 3), 6)
        for dd in (-7, 0, 7):
            pygame.draw.circle(s, (255, 230, 120), (cx + dd, cy + 4), 2)
    elif kind == "ghost":           # 隱形衣(幽靈)
        pygame.draw.circle(s, (240, 240, 250), (cx, cy - 2), 9)
        pygame.draw.rect(s, (240, 240, 250), (cx - 9, cy - 2, 18, 9))
        for dd in (-6, 0, 6):
            pygame.draw.circle(s, (240, 240, 250), (cx + dd, cy + 7), 3)
        for dd in (-4, 4):
            pygame.draw.circle(s, (70, 70, 90), (cx + dd, cy - 3), 2)
    elif kind == "shield":          # 無敵光盾
        pts = [(cx, cy - 11), (cx + 9, cy - 7), (cx + 9, cy + 2),
               (cx, cy + 11), (cx - 9, cy + 2), (cx - 9, cy - 7)]
        pygame.draw.polygon(s, (90, 160, 240), pts)
        pygame.draw.polygon(s, (40, 90, 170), pts, 2)
        pygame.draw.line(s, (220, 240, 255), (cx, cy - 7), (cx, cy + 7), 3)
    elif kind == "radar":           # 泡泡雷達
        pygame.draw.circle(s, (60, 160, 90), (cx, cy), 10)
        pygame.draw.circle(s, (30, 100, 55), (cx, cy), 10, 2)
        pygame.draw.circle(s, (150, 240, 170), (cx, cy), 5, 1)
        pygame.draw.line(s, (200, 255, 210), (cx, cy), (cx + 7, cy - 7), 2)
        pygame.draw.circle(s, (255, 90, 90), (cx - 4, cy + 4), 2)
    elif kind == "hook":            # 鉤爪
        pygame.draw.line(s, (130, 136, 148), (cx - 10, cy + 10), (cx + 3, cy - 3), 4)
        pygame.draw.arc(s, (90, 96, 108), (cx - 2, cy - 12, 16, 16),
                        math.pi * 0.2, math.pi * 1.35, 4)
        pygame.draw.circle(s, (200, 205, 215), (cx - 10, cy + 10), 3)
    elif kind == "missile":         # 飛彈
        pygame.draw.polygon(s, (210, 70, 70),
                            [(cx + 11, cy), (cx + 4, cy - 5), (cx + 4, cy + 5)])
        pygame.draw.rect(s, (160, 166, 178), (cx - 7, cy - 4, 12, 8),
                         border_radius=3)
        pygame.draw.polygon(s, (120, 126, 138),
                            [(cx - 7, cy - 4), (cx - 12, cy - 8), (cx - 9, cy)])
        pygame.draw.polygon(s, (120, 126, 138),
                            [(cx - 7, cy + 4), (cx - 12, cy + 8), (cx - 9, cy)])
        pygame.draw.circle(s, (255, 190, 80), (cx - 10, cy), 3)
    elif kind == "magnet":          # 磁力槍(馬蹄磁鐵)
        pygame.draw.arc(s, (210, 60, 60), (cx - 10, cy - 10, 20, 20),
                        math.pi * 0.95, math.pi * 2.05, 6)
        pygame.draw.rect(s, (230, 230, 240), (cx - 10, cy + 2, 6, 8))
        pygame.draw.rect(s, (230, 230, 240), (cx + 4, cy + 2, 6, 8))
        for dd in (-14, 14):
            pygame.draw.line(s, (150, 200, 255), (cx + dd, cy - 2),
                             (cx + dd // 2, cy + 6), 2)
    elif kind == "freeze":          # 冰凍槍(雪花)
        for ang in range(0, 180, 60):
            a = math.radians(ang)
            dx2, dy2 = math.cos(a) * 11, math.sin(a) * 11
            pygame.draw.line(s, (120, 190, 240),
                             (cx - dx2, cy - dy2), (cx + dx2, cy + dy2), 3)
        pygame.draw.circle(s, (220, 245, 255), (cx, cy), 4)
    elif kind == "devil":           # 惡魔面具
        pygame.draw.circle(s, (140, 70, 190), (cx, cy + 1), 9)
        pygame.draw.polygon(s, (140, 70, 190),
                            [(cx - 8, cy - 4), (cx - 11, cy - 13), (cx - 3, cy - 8)])
        pygame.draw.polygon(s, (140, 70, 190),
                            [(cx + 8, cy - 4), (cx + 11, cy - 13), (cx + 3, cy - 8)])
        pygame.draw.line(s, (255, 220, 90), (cx - 6, cy - 2), (cx - 2, cy), 2)
        pygame.draw.line(s, (255, 220, 90), (cx + 6, cy - 2), (cx + 2, cy), 2)
        pygame.draw.arc(s, (255, 220, 90), (cx - 5, cy + 2, 10, 6), math.pi, 2 * math.pi, 2)


def draw_item_icon_scaled(s, cx, cy, kind, scale=1.0):
    """把道具圖示縮放後畫在 (cx, cy)(HUD 小圖示用)。"""
    if scale >= 0.99:
        draw_item_icon(s, cx, cy, kind)
        return
    size = 34
    tmp = pygame.Surface((size, size), pygame.SRCALPHA)
    draw_item_icon(tmp, size // 2, size // 2, kind)
    sz = max(8, int(size * scale))
    tmp = pygame.transform.smoothscale(tmp, (sz, sz))
    s.blit(tmp, (cx - sz // 2, cy - sz // 2))


# ----------------------------------------------------------------------
# 遊戲物件
# ----------------------------------------------------------------------
class Bubble:
    """放置在地上的水球。"""

    def __init__(self, r, c, owner, power):
        self.r, self.c = r, c
        self.owner = owner
        self.power = power
        self.timer = BUBBLE_FUSE
        # 放置瞬間站在上面的玩家可以走出去,離開後就變成障礙
        self.riders = set()
        # 被踢出去時的滑行狀態
        self.slide = None       # (dx, dy) 或 None
        self.slide_t = 0.0
        self.xshape = False     # 工程師:對角線 X 型爆炸
        self.curve = None       # 足球明星:曲線球狀態 {"steps":n,"turned":bool}
        self.belt_t = 0.0       # 履帶運送的累計時間
        self.remote = False     # 爆破專家:遙控水雷


class Player:
    def __init__(self, pid, r, c, is_bot=False):
        self.id = pid
        self.color = PLAYER_COLORS[pid]
        self.x = c * TILE + TILE / 2.0
        self.y = r * TILE + TILE / 2.0
        self.spawn = (r, c)
        self.is_bot = is_bot
        self.bot = None          # 由 Game 建立
        self.bot_dir = None      # 電腦這一幀想走的方向
        self.is_remote = False   # 網路連線的遠端玩家
        self.remote_dirs = []    # 遠端玩家目前按住的方向
        self.use_net_keys = False  # 連線房主:改用方向鍵+空白鍵
        self.team = None         # 組隊戰:0=紅隊 1=藍隊;None=個人戰

        # 能力值(水球數 / 威力 / 速度 / 針)
        self.max_bubbles = 1
        self.power = 1
        self.speed = 3.4          # 每秒移動格數
        self.needles = 0

        # 新道具狀態
        self.item_kind = None     # 手持道具槽(本機模式):dart/hook/...
        self.item_count = 0       # 手持道具數量(本機模式,同種可疊上限 3)
        self.slot_a = None        # 連線雙槽制:備用槽(左)
        self.slot_b = None        # 連線雙槽制:優先槽(右,X 鍵使用)
        self.has_glove = False    # 拳套:可丟水球
        self.has_kick = False     # 運動鞋:可踢水球
        self.mount = None         # 坐騎: turtle / owl / ufo
        self.ghost_t = 0.0        # 隱形剩餘秒數
        self.shield_t = 0.0       # 無敵剩餘秒數
        self.radar_t = 0.0        # 雷達剩餘秒數
        self.curse_t = 0.0        # 惡魔面具詛咒剩餘秒數
        self.curse_kind = None    # reverse=反向操作 / auto=亂放水球
        self.curse_drop_t = 0.0
        self.kick_cd = 0.0
        self.hook_to = None       # 鉤爪:飛行目標 (x, y)
        self.frozen_t = 0.0       # 被冰凍剩餘秒數
        self.feat_cd = 0.0        # 場地機關(大砲/傳送門)個人冷卻
        self.char = None          # 角色編號(連線房間選擇;None=無技能)
        self.skill_cd = 0.0       # 技能冷卻剩餘秒數
        self.pos_hist = deque(maxlen=36)   # 時空行者:位置歷史(每 0.1 秒)
        self.want_dirs = []       # 本幀的移動意圖(履帶讓路判斷用)
        self.name = "P%d" % (pid + 1)   # 顯示名稱(連線房間可自訂)
        self.death_t = None       # 陣亡時刻(名次計分用;None=存活)
        self.daze_t = 0.0         # 暈眩剩餘秒數(星星繞頭,非冰凍)
        self.respawn_t = 0.0      # 佔地/感染模式:復活倒數
        self.infected = False     # 感染模式:是否為感染者
        self.infect_t = None      # 被感染的時刻(名次計分用)
        self._to_infect = False   # 復活時轉為感染者
        self.last_stand = False   # 感染模式:最後的生存者覺醒
        self.pad_iid = None       # 藍牙/USB 手把的 instance id
        self.last_hit_by = None   # 最後困住我的人(擊殺歸屬)
        self.env_tag = None       # 環境兇手(酷企鵝/轟炸機/落石…)
        self.streak = 0           # 連殺數(死亡歸零)
        self.multi_n = 0          # 短窗口連殺(雙殺/三殺…)
        self.multi_t = 0.0        # 連殺窗口倒數
        self.trail_t = 0.0        # 水靈:漣漪足跡剩餘秒數
        self.wet_t = 0.0          # 濕身緩速剩餘秒數(水漬)
        self.volt_t = 0.0         # 電光使:疾馳剩餘秒數
        self.surge_t = 0.0        # 氣球商人:限時特賣剩餘秒數
        self.haste_t = 0.0        # 節奏使:加速剩餘秒數
        self.last_trail = None    # 水靈:上次留下水漬的格子

        self.alive = True
        self.trapped = False
        self.trap_timer = 0.0
        self.trap_elapsed = 0.0
        self.facing = "down"
        self.axis = "y"
        self.anim = random.random() * 10

    # ---- 座標輔助 ----
    def col(self):
        return int(self.x // TILE)

    def row(self):
        return int(self.y // TILE)

    def tile(self):
        return (self.row(), self.col())

    # ---- 移動 ----
    def step(self, d, sp, game):
        """朝方向 d 走一步;回傳是否有實際位移。"""
        dx, dy = DIRS[d]
        half = HITBOX / 2

        if dx != 0:
            # 水平移動:先把 y 對齊該列中心(轉角輔助)
            ty = self.row() * TILE + TILE / 2
            if abs(self.y - ty) > 0.5:
                old = self.y
                self.y += max(-sp, min(sp, ty - self.y))
                return abs(self.y - old) > 0.01
            self.y = ty
            old = self.x
            nx = self.x + dx * sp
            lead = nx + dx * half
            c_now = int(self.x // TILE)
            c_new = int(lead // TILE)
            if c_new != c_now and not game.passable(self.row(), c_new, self):
                self.maybe_kick(game, self.row(), c_new, dx, 0)
                boundary = c_now * TILE + (TILE if dx > 0 else 0)
                nx = boundary - dx * half
            self.x = nx
            return abs(self.x - old) > 0.01
        else:
            tx = self.col() * TILE + TILE / 2
            if abs(self.x - tx) > 0.5:
                old = self.x
                self.x += max(-sp, min(sp, tx - self.x))
                return abs(self.x - old) > 0.01
            self.x = tx
            old = self.y
            ny = self.y + dy * sp
            lead = ny + dy * half
            r_now = int(self.y // TILE)
            r_new = int(lead // TILE)
            if r_new != r_now and not game.passable(r_new, self.col(), self):
                self.maybe_kick(game, r_new, self.col(), 0, dy)
                boundary = r_now * TILE + (TILE if dy > 0 else 0)
                ny = boundary - dy * half
            self.y = ny
            return abs(self.y - old) > 0.01

    def maybe_kick(self, game, r, c, dx, dy):
        """運動鞋:走向水球時把它踢出去。"""
        if not self.has_kick or self.trapped or self.kick_cd > 0:
            return
        if not (0 <= r < ROWS and 0 <= c < COLS) or game.grid[r][c] != FLOOR:
            return
        b = game.bubble_at(r, c)
        if b is not None and self.id not in b.riders:
            game.kick_bubble(b, dx, dy)
            self.kick_cd = 0.35

    def update_move(self, keys, dt, game):
        if not self.alive:
            return
        # 被冰凍或暈眩:動彈不得
        if self.frozen_t > 0 or self.daze_t > 0:
            return
        # 鉤爪飛行中:高速滑向目標,無視輸入
        if self.hook_to is not None:
            hx, hy = self.hook_to
            sp = 16.0 * TILE * dt
            dx, dy = hx - self.x, hy - self.y
            dist = math.hypot(dx, dy)
            if dist <= sp or dist < 2:
                self.x, self.y = hx, hy
                self.hook_to = None
            else:
                self.x += dx / dist * sp
                self.y += dy / dist * sp
            return
        sp = self.speed * TILE * dt * game.map_cfg.get("speed", 1.0)
        sp *= MOUNT_SPEED.get(self.mount, 1.0)
        spec = game.terrain.get(self.tile())
        if spec is not None and spec[0] == "mud":
            sp *= 0.55            # 泥沼:大幅減速
        elif spec is not None and spec[0] == "ice":
            sp *= 1.35            # 冰面:局部加速
        if self.haste_t > 0:
            sp *= 1.6             # 節奏使:狂想加速
        if self.wet_t > 0:
            sp *= 0.6             # 濕身:水漬緩速
        if self.infected:
            nz = sum(1 for q in game.players if q.infected)
            total = max(1, len(game.players))
            if nz <= 1:
                sp *= 1.18        # 孤狼期:最快
            elif nz <= total / 3:
                sp *= 1.12
            elif nz <= total / 2:
                sp *= 1.06        # 鬼群壯大 → 優勢遞減
        if getattr(self, "last_stand", False) and not self.infected:
            sp *= 1.15            # 最後的生存者:覺醒加速
        if (game.soccer and game.ball is not None
                and game.ball["carrier"] == self.id):
            sp *= BALL_SLOW       # 持球者:跑速變慢
        if self.volt_t > 0:
            sp *= 2.0             # 電光使:雷光疾馳
        if game.match_left is not None and game.match_left <= SD_START:
            sp *= FEVER_SPEED     # 終局狂熱:全員加速
        if self.trapped:
            sp *= 0.28   # 被困住只能緩慢漂移

        if self.is_bot:
            pressed = [self.bot_dir] if self.bot_dir else []
        elif self.is_remote:
            pressed = list(self.remote_dirs)
        elif self.pad_iid is not None:
            pressed = pad_dirs(game.pads.get(self.pad_iid))
            if not pressed and self.id < len(game.keymaps):
                km2 = game.keymaps[self.id].get("dirs", {})
                pressed = [d for d in ("up", "down", "left", "right")
                           if d in km2 and keys[km2[d]]]
        elif self.use_net_keys:
            km = NET_KEYMAP["dirs"]   # 連線房間:方向鍵+空白鍵
            pressed = [d for d in ("up", "down", "left", "right") if keys[km[d]]]
        elif self.id >= len(game.keymaps):
            pressed = []          # 沒有對應鍵盤鍵位(連線房間才會有 P5~P8)
        else:
            km = game.keymaps[self.id]["dirs"]
            pressed = [d for d in ("up", "down", "left", "right")
                       if d in km and keys[km[d]]]
        # 惡魔面具:反向操作(電腦不受此類詛咒)
        if not self.is_bot and self.curse_t > 0 and self.curse_kind == "reverse":
            flip = {"up": "down", "down": "up", "left": "right", "right": "left"}
            pressed = [flip[d] for d in pressed]
        self.want_dirs = pressed      # 供場地機關判斷玩家意圖
        if not pressed:
            return

        def axis_of(d):
            return "x" if d in ("left", "right") else "y"

        # 優先嘗試「換軸」的方向,轉彎手感較好;被擋住就退回另一方向
        pressed.sort(key=lambda d: axis_of(d) == self.axis)
        for d in pressed:
            if self.step(d, sp, game):
                self.facing = d
                self.axis = axis_of(d)
                break


# ----------------------------------------------------------------------
# 電腦 AI
# ----------------------------------------------------------------------
def predicted_blast(game, r0, c0, power, xshape=False):
    """預測在 (r0,c0) 以指定威力爆炸時,水柱會覆蓋的格子。"""
    tiles = {(r0, c0)}
    dirs4 = (((1, 1), (-1, -1), (1, -1), (-1, 1)) if xshape
             else ((1, 0), (-1, 0), (0, 1), (0, -1)))
    for dx, dy in dirs4:
        for i in range(1, power + 1):
            r, c = r0 + dy * i, c0 + dx * i
            if not (0 <= r < ROWS and 0 <= c < COLS):
                break
            t = game.grid[r][c]
            if t == HARD:
                break
            tiles.add((r, c))
            if t == SOFT or game.bubble_at(r, c) is not None:
                break
    return tiles


def bfs_path(start, goal_fn, walkable_fn, limit=400):
    """回傳從 start 到第一個符合 goal_fn 的格子的路徑(不含起點);找不到回傳 None。"""
    q = deque([start])
    prev = {start: None}
    while q:
        cur = q.popleft()
        if goal_fn(cur):
            path = []
            while cur != start:
                path.append(cur)
                cur = prev[cur]
            path.reverse()
            return path
        if len(prev) > limit:
            break
        r, c = cur
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nt = (r + dy, c + dx)
            if nt in prev or not walkable_fn(nt):
                continue
            prev[nt] = cur
            q.append(nt)
    return None


class Bot:
    """電腦玩家:躲水柱 → 戳破被困敵人 → 攻擊 → 撿道具 → 炸箱子 → 追擊。"""

    def __init__(self, player):
        self.p = player
        self.path = []
        self.think_timer = 0.0
        self.bomb_cd = 0.0
        self.want_bomb = False

    # ---- 環境評估 ----
    def danger_map(self, game):
        danger = set(game.blasts.keys())
        for b in game.bubbles:
            danger |= predicted_blast(game, b.r, b.c, b.power, b.xshape)
        danger |= set(game.falling.keys())   # 場地崩塌:落石預警格
        # 場地攻擊:預警格 / 轟炸落點 / 企鵝前方路徑
        for hz in game.hazards:
            if hz["state"] == "warn" or hz["kind"] == "plane":
                for t in hz.get("tiles", []):
                    tt = (t[0], t[1])
                    danger |= predicted_blast(game, tt[0], tt[1], 1) \
                        if hz["kind"] == "plane" else {tt}
            if hz["kind"] == "penguin" and hz["state"] == "go":
                pr, pc = int(hz["y"] // TILE), int(hz["x"] // TILE)
                for i in range(6):
                    danger.add((pr + hz["vy"] * i, pc + hz["vx"] * i))
        # 飛彈:目前位置與前方數格
        for ms in game.missiles:
            mr, mc = int(ms["y"] // TILE), int(ms["x"] // TILE)
            for i in range(4):
                danger.add((mr + ms["dy"] * i, mc + ms["dx"] * i))
        if game.boss is not None:
            # 章魚王本體(外擴一圈)
            for (r, c) in game.boss.footprint():
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        danger.add((r + dr, c + dc))
            # 小章魚與其周圍兩格(會追人,保持距離)
            for mn in game.minions:
                mr, mc = mn.tile()
                for dr in (-2, -1, 0, 1, 2):
                    for dc in (-2, -1, 0, 1, 2):
                        danger.add((mr + dr, mc + dc))
            # 落點預警(預估威力 3 的十字)
            for m in game.incoming:
                danger |= predicted_blast(game, m[0], m[1], 3)
        return danger

    def walk_normal(self, game):
        p = self.p
        def f(t):
            return game.passable(t[0], t[1], p)
        return f

    def walk_safe(self, game, danger):
        p = self.p
        def f(t):
            return game.passable(t[0], t[1], p) and t not in danger
        return f

    def enemy_in_range(self, game):
        """攻擊目標是否貼身,或在同列/同行、威力範圍內且中間無阻擋。"""
        p = self.p
        r, c = p.tile()
        if game.boss is not None:
            targets = set(game.boss.footprint())
            targets |= {mn.tile() for mn in game.minions}
        else:
            targets = set()
            for q in game.players:
                if q is p or not q.alive:
                    continue
                if q.ghost_t > 0:          # 隱形衣:電腦看不到
                    continue
                if q.team is not None and q.team == p.team:
                    continue               # 組隊戰:不打隊友
                targets.add(q.tile())
        for (qr, qc) in targets:
            if abs(qr - r) + abs(qc - c) <= 1:
                return True
            if qr == r and abs(qc - c) <= p.power:
                lo, hi = sorted((qc, c))
                if all(game.grid[r][cc] == FLOOR and game.bubble_at(r, cc) is None
                       for cc in range(lo + 1, hi)):
                    return True
            if qc == c and abs(qr - r) <= p.power:
                lo, hi = sorted((qr, r))
                if all(game.grid[rr][c] == FLOOR and game.bubble_at(rr, c) is None
                       for rr in range(lo + 1, hi)):
                    return True
        return False

    def can_bomb_safely(self, game, danger):
        """模擬在腳下放球後,是否存在一條不長的逃生路徑。"""
        p = self.p
        me = p.tile()
        myblast = predicted_blast(game, me[0], me[1], p.power)
        # 絕不誤炸被困的隊友(Boss 全員同隊;組隊戰看隊伍)
        for q in game.players:
            if q is p or not q.alive or not q.trapped:
                continue
            mate = (game.boss is not None
                    or (q.team is not None and q.team == p.team))
            if mate and q.tile() in myblast:
                return False
        new_danger = danger | myblast

        def walk(t):
            r, c = t
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return False
            if game.grid[r][c] != FLOOR:
                return False
            b = game.bubble_at(r, c)
            if b is not None and t != me:   # 自己剛放的那顆可以站著離開
                return False
            return t not in game.blasts     # 逃生途中不要穿越現存水柱

        path = bfs_path(me, lambda t: t not in new_danger, walk, limit=200)
        return path is not None and len(path) <= 7

    # ---- 決策 ----
    def think(self, game):
        p = self.p
        me = p.tile()
        danger = self.danger_map(game)
        self.want_bomb = False
        walk_any = self.walk_normal(game)
        walk_safe = self.walk_safe(game, danger)

        # 1. 腳下危險 → 逃到最近安全格(優先走完全安全的路線)
        if me in danger:
            # 被小章魚追上來時,放一顆水球擋路(牠繞路或被炸),然後跑
            if (game.boss is not None
                    and game.active_bubbles(p) == 0 and self.bomb_cd <= 0
                    and game.grid[me[0]][me[1]] == FLOOR
                    and game.bubble_at(*me) is None
                    and any(abs(mn.tile()[0] - me[0]) + abs(mn.tile()[1] - me[1]) <= 2
                            for mn in game.minions)
                    and self.can_bomb_safely(game, danger)):
                self.want_bomb = True
            path = bfs_path(me, lambda t: t not in danger, walk_safe)
            if path is None:
                path = bfs_path(me, lambda t: t not in danger, walk_any)
            self.path = path or []
            return

        # 偶爾發呆一下,讓電腦不至於完美到打不贏
        if random.random() < 0.06:
            self.path = []
            return

        # 2. 有被困住的玩家 → 隊友救援(Boss/組隊);敵人衝去戳破
        mate_goals = {q.tile() for q in game.players
                      if q.alive and q.trapped and q is not p
                      and (game.boss is not None
                           or (q.team is not None and q.team == p.team))}
        foe_goals = {q.tile() for q in game.players
                     if q.alive and q.trapped and q is not p
                     and not (game.boss is not None
                              or (q.team is not None and q.team == p.team))}
        if mate_goals:
            # 救人要緊:只避開現存水柱,預測危險區允許快速穿越
            def walk_rescue(t):
                return game.passable(t[0], t[1], p) and t not in game.blasts
            path = bfs_path(me, lambda t: t in mate_goals, walk_rescue)
            if path is not None:
                self.path = path
                return
        if foe_goals:
            path = bfs_path(me, lambda t: t in foe_goals, walk_safe)
            if path is not None:
                self.path = path
                return

        if game.boss is not None:
            # Boss 模式:場上還有自己的水球就不再放,避免被自己的連環水柱困殺
            can_bomb = (game.active_bubbles(p) == 0 and self.bomb_cd <= 0)
        else:
            can_bomb = (game.active_bubbles(p) < p.max_bubbles and self.bomb_cd <= 0)

        # 3. 敵人在射程內 → 放球攻擊(先確認自己逃得掉)
        if can_bomb and self.enemy_in_range(game) and self.can_bomb_safely(game, danger):
            self.want_bomb = True
            self.path = []
            return

        # 4. 撿道具(避開惡魔面具;騎飛碟時撿不到就不去撿)
        if game.items and p.mount != "ufo":
            good = {t for t, k in game.items.items() if k != "devil"}
            path = bfs_path(me, lambda t: t in good, walk_safe)
            if path is not None and len(path) <= 18:
                self.path = path
                return

        # 5. 走到箱子旁邊放球開路
        def near_soft(t):
            r, c = t
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dy, c + dx
                if 0 <= rr < ROWS and 0 <= cc < COLS and game.grid[rr][cc] == SOFT:
                    return True
            return False

        if can_bomb:
            path = bfs_path(me, near_soft, walk_safe)
            if path is not None:
                if len(path) == 0:
                    if self.can_bomb_safely(game, danger):
                        self.want_bomb = True
                        self.path = []
                        return
                else:
                    self.path = path
                    return

        # 6. 朝目標逼近
        if game.boss is not None:
            # Boss 模式:走到能瞄準章魚王/小章魚的安全射擊位
            targets = set(game.boss.footprint()) | {mn.tile() for mn in game.minions}
            spots = set()
            for (tr, tc) in targets:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    for i in range(2, max(2, p.power) + 1):
                        r2, c2 = tr + dy * i, tc + dx * i
                        if not (0 <= r2 < ROWS and 0 <= c2 < COLS):
                            break
                        if game.grid[r2][c2] != FLOOR:
                            break
                        if (r2, c2) not in danger:
                            spots.add((r2, c2))
            if spots:
                path = bfs_path(me, lambda t: t in spots, walk_safe)
                if path is not None:
                    self.path = path[:6]
                    return
            self.path = []
            return

        # 對戰模式:朝最近的敵人靠近(看不到隱形的人,不追隊友)
        enemy_goals = {q.tile() for q in game.players
                       if q.alive and q is not p and q.ghost_t <= 0
                       and not (q.team is not None and q.team == p.team)}
        if enemy_goals:
            path = bfs_path(me, lambda t: t in enemy_goals, walk_safe)
            if path is not None:
                self.path = path[:6]
                return

        self.path = []

    # ---- 每幀輸出:方向 + 是否放球 ----
    def drive(self, game, dt):
        p = self.p
        self.think_timer -= dt
        self.bomb_cd -= dt
        if self.think_timer <= 0:
            self.think_timer = game.blv["think"] * (1.0 + random.random() * 0.6)
            self.think(game)

        while self.path and p.tile() == self.path[0]:
            self.path.pop(0)

        if not self.path:
            return None
        tr, tc = self.path[0]
        r, c = p.tile()
        if tc > c:
            return "right"
        if tc < c:
            return "left"
        if tr > r:
            return "down"
        if tr < r:
            return "up"
        return None


class Boss:
    """章魚王:3×3 大型 Boss。丟水球、彈幕、召喚小章魚,紅血狂暴。"""

    def __init__(self, diff_ix=1, num_players=2):
        self.diff_ix = diff_ix % len(BOSS_DIFFS)
        self.cfg = BOSS_DIFFS[self.diff_ix]
        self.cx = 7 * TILE + TILE / 2.0
        self.cy = 3 * TILE + TILE / 2.0
        self.tx, self.ty = self.cx, self.cy
        self.hp = self.cfg["hp"] + self.cfg["per"] * max(0, num_players - 2)
        self.max_hp = self.hp
        self.iframe = 0.0
        self.flash = 0.0
        self.state = "move"          # move / pause / barrage
        self.state_t = 0.0
        self.attack_cd = 4.5         # 開場緩衝,讓玩家先站穩腳步
        self.barrage_left = 0
        self.barrage_t = 0.0
        self.taunt = None
        self.taunt_t = 0.0
        self.said_enrage = False
        self.anim = 0.0

    def enraged(self):
        return self.hp <= self.max_hp * BOSS_ENRAGE_AT

    def center_tile(self):
        return (int(self.cy // TILE), int(self.cx // TILE))

    def footprint(self):
        cr, cc = self.center_tile()
        return {(cr + dr, cc + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)}

    def rect(self):
        return pygame.Rect(int(self.cx - TILE * 1.5), int(self.cy - TILE * 1.5),
                           TILE * 3, TILE * 3)

    def say(self, pair, dur=1.6):
        self.taunt = T(pair[0], pair[1])
        self.taunt_t = dur

    def new_target(self):
        r = random.randint(BOSS_ZONE_ROWS[0] + 1, BOSS_ZONE_ROWS[1] - 1)
        c = random.randint(2, COLS - 3)
        self.tx = c * TILE + TILE / 2.0
        self.ty = r * TILE + TILE / 2.0

    def update(self, game, dt):
        self.anim += dt
        self.iframe = max(0.0, self.iframe - dt)
        self.flash = max(0.0, self.flash - dt)
        self.taunt_t = max(0.0, self.taunt_t - dt)
        enr = self.enraged()
        if enr and not self.said_enrage:      # 進入紅血:狂暴宣告
            self.said_enrage = True
            self.say(BOSS_TAUNT_ENRAGE, 2.0)

        if self.state == "barrage":
            # 彈幕:定住不動,連續往全場丟
            self.state_t -= dt
            self.barrage_t -= dt
            if self.barrage_t <= 0 and self.barrage_left > 0:
                self.barrage_left -= 1
                self.barrage_t = 0.13
                r = random.randint(1, ROWS - 2)
                c = random.randint(1, COLS - 2)
                if game.grid[r][c] == FLOOR:
                    game.incoming.append([r, c, 0.75])
            if self.state_t <= 0 and self.barrage_left <= 0:
                self.state = "move"
                self.attack_cd = (2.6 if enr else 4.2) * self.cfg["atk"]
            return

        if self.state == "pause":             # 丟完水球的收招硬直
            self.state_t -= dt
            if self.state_t <= 0:
                self.state = "move"
            return

        # 移動
        sp = (74 if enr else 42) * self.cfg["bsp"] * dt
        dx, dy = self.tx - self.cx, self.ty - self.cy
        dist = math.hypot(dx, dy)
        if dist < 4:
            self.new_target()
        else:
            self.cx += dx / dist * min(sp, dist)
            self.cy += dy / dist * min(sp, dist)

        # 攻擊排程
        self.attack_cd -= dt
        if self.attack_cd > 0:
            return
        roll = random.random()
        cap = self.cfg["ecap"] if enr else self.cfg["cap"]
        if roll < 0.22 and len(game.minions) < cap:
            # 召喚小章魚
            n = 2 if enr else 1
            for _ in range(n):
                if len(game.minions) >= cap:
                    break
                spots = [(r, c) for r in (1, 2) for c in range(2, COLS - 2)
                         if game.grid[r][c] == FLOOR and (r, c) not in self.footprint()]
                if spots:
                    r, c = random.choice(spots)
                    game.minions.append(Minion(r, c))
                    game.effects.append(dict(kind="ring", x=c * TILE + TILE // 2,
                                             y=r * TILE + TILE // 2, t=0.4, t0=0.4))
            self.say(random.choice(BOSS_TAUNTS_MISC))
            self.attack_cd = (2.4 if enr else 3.4) * self.cfg["atk"]
        elif roll < 0.42:
            # 彈幕(先講狠話再開砸)
            self.state = "barrage"
            self.barrage_left = self.cfg["ebar"] if enr else self.cfg["bar"]
            self.barrage_t = 1.05           # 前搖:狠話時間可以先跑位
            self.state_t = 3.4
            self.say(random.choice(BOSS_TAUNTS_BARRAGE), 1.4)
        else:
            # 瞄準玩家丟水球(紅色預警後落下)
            n = self.cfg["toss"] + (1 if enr else 0)
            alive = [q for q in game.players if q.alive and not q.trapped]
            for _ in range(n):
                if not alive:
                    break
                q = random.choice(alive)
                r = max(1, min(ROWS - 2, q.tile()[0] + random.randint(-2, 2)))
                c = max(1, min(COLS - 2, q.tile()[1] + random.randint(-2, 2)))
                if game.grid[r][c] == FLOOR:
                    game.incoming.append([r, c, 0.95])
            self.state = "pause"
            self.state_t = 0.6
            self.attack_cd = (2.3 if enr else 3.4) * self.cfg["atk"]


class Minion:
    """小章魚:會追人的分身,碰到就死(被困者除外),可被水柱炸死。"""

    def __init__(self, r, c):
        self.x = c * TILE + TILE / 2.0
        self.y = r * TILE + TILE / 2.0
        self.path = []
        self.think = 0.0
        self.anim = random.random() * 10

    def tile(self):
        return (int(self.y // TILE), int(self.x // TILE))

    def update(self, game, dt):
        self.anim += dt
        self.think -= dt
        if self.think <= 0:
            self.think = 0.45
            targets = {q.tile() for q in game.players
                       if q.alive and not q.trapped and q.ghost_t <= 0}
            if targets:
                def walk(t):
                    r, c = t
                    return (0 <= r < ROWS and 0 <= c < COLS
                            and game.grid[r][c] == FLOOR
                            and game.bubble_at(r, c) is None)
                self.path = bfs_path(self.tile(), lambda t: t in targets, walk) or []
        while self.path and self.tile() == self.path[0]:
            self.path.pop(0)
        if not self.path:
            return
        base = game.boss.cfg["msp"] if game.boss else 2.0
        speed = base * (1.3 if (game.boss and game.boss.enraged()) else 1.0)
        sp = speed * TILE * dt
        tr, tc = self.path[0]
        tx = tc * TILE + TILE / 2.0
        ty = tr * TILE + TILE / 2.0
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.x += dx / dist * min(sp, dist)
            self.y += dy / dist * min(sp, dist)


# ----------------------------------------------------------------------
# 主遊戲
# ----------------------------------------------------------------------




# ----------------------------------------------------------------------
# 2.5D 像素美術:依地圖配色預先烘焙貼圖(地板/箱子/磚塊/陰影/暗角)
# ----------------------------------------------------------------------
BLOCK_DEPTH = 12   # 方塊前立面高度(2.5D 視角深度)


def _grad_v(surf, rect, top, bottom):
    x, y, w, h = rect
    for i in range(h):
        k = i / max(1, h - 1)
        col = tuple(int(top[j] + (bottom[j] - top[j]) * k) for j in range(3))
        pygame.draw.line(surf, col, (x, y + i), (x + w - 1, y + i))


def _lit(c, d):
    return tuple(min(255, v + d) for v in c)


def _dim(c, d):
    return tuple(max(0, v - d) for v in c)


def build_tile_art(cfg):
    """為單張地圖烘焙 2.5D 貼圖組(每局一次,繪製迴圈只做 blit)。"""
    col = cfg["colors"]
    rng = random.Random(sum(col["fa"]) * 7 + sum(col["hard"]))
    art = {}

    # 地板:受光漸層 + 像素噪點
    for key in ("fa", "fb"):
        base = col[key]
        t = pygame.Surface((TILE, TILE))
        _grad_v(t, (0, 0, TILE, TILE), _lit(base, 10), _dim(base, 9))
        for _ in range(12):
            px, py = rng.randrange(TILE), rng.randrange(TILE)
            t.set_at((px, py), _lit(base, 16) if rng.random() < 0.5
                     else _dim(base, 13))
        art[key] = t

    d = BLOCK_DEPTH
    # 硬磚:頂面受光 + 前立面磚縫
    hard = pygame.Surface((TILE, TILE))
    _grad_v(hard, (0, 0, TILE, TILE - d), _lit(col["hard"], 20), col["hard"])
    _grad_v(hard, (0, TILE - d, TILE, d), col["hard_dark"],
            _dim(col["hard_dark"], 24))
    pygame.draw.rect(hard, col["hard_top"],
                     (4, 4, TILE - 8, TILE - d - 8), border_radius=4)
    _grad_v(hard, (5, 5, TILE - 10, 6), _lit(col["hard_top"], 26),
            col["hard_top"])
    pygame.draw.rect(hard, _dim(col["hard"], 10),
                     (4, 4, TILE - 8, TILE - d - 8), 1, border_radius=4)
    pygame.draw.line(hard, _lit(col["hard_top"], 34), (2, 1), (TILE - 3, 1), 2)
    for bx in (TILE // 3, 2 * TILE // 3):
        pygame.draw.line(hard, _dim(col["hard_dark"], 26),
                         (bx, TILE - d + 2), (bx, TILE - 2), 1)
    pygame.draw.line(hard, _dim(col["hard_dark"], 34),
                     (0, TILE - 1), (TILE - 1, TILE - 1), 1)
    art["hard"] = hard

    # 箱子:頂面木板 + 前立面板縫
    soft = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
    th = TILE - d
    _grad_v(soft, (2, 2, TILE - 4, th - 2), _lit(col["soft"], 16), col["soft"])
    _grad_v(soft, (2, th, TILE - 4, d - 2), col["soft_dark"],
            _dim(col["soft_dark"], 22))
    pygame.draw.line(soft, col["soft_light"], (6, 7), (TILE - 7, 7), 3)
    pygame.draw.line(soft, _dim(col["soft"], 18),
                     (6, th // 2 + 4), (TILE - 7, th // 2 + 4), 2)
    pygame.draw.line(soft, _dim(col["soft"], 12),
                     (TILE // 2, 4), (TILE // 2, th - 2), 1)
    pygame.draw.line(soft, _dim(col["soft_dark"], 26),
                     (TILE // 2, th + 1), (TILE // 2, TILE - 3), 1)
    pygame.draw.rect(soft, col["soft_dark"], (2, 2, TILE - 4, TILE - 4), 2,
                     border_radius=6)
    pygame.draw.line(soft, _lit(col["soft_light"], 12), (6, 3), (16, 3), 2)
    art["soft"] = soft

    # 方塊投在下一格地板的柔影
    sh = pygame.Surface((TILE, d), pygame.SRCALPHA)
    for i in range(d):
        a = int(66 * (1 - i / d))
        pygame.draw.line(sh, (10, 14, 24, a), (0, i), (TILE - 1, i))
    art["shadow"] = sh

    # 場景暗角(柔和聚光感):只烘焙四條邊緣長條,省下中央的透明混合
    edge = 44
    H = ROWS * TILE
    top = pygame.Surface((SCREEN_W, edge), pygame.SRCALPHA)
    for i in range(edge):
        a = int(36 * (1 - i / edge) ** 1.5)
        pygame.draw.line(top, (8, 10, 20, a), (0, i), (SCREEN_W - 1, i))
    bot = pygame.transform.flip(top, False, True)
    left = pygame.Surface((edge, H), pygame.SRCALPHA)
    for i in range(edge):
        a = int(36 * (1 - i / edge) ** 1.5)
        pygame.draw.line(left, (8, 10, 20, a), (i, 0), (i, H - 1))
    right = pygame.transform.flip(left, True, False)
    art["vin_strips"] = ((top, (0, 0)), (bot, (0, H - edge)),
                         (left, (0, 0)), (right, (SCREEN_W - edge, 0)))

    # 佔地模式:兩隊的漆面(全不透明,深淺斑點保留潑漆質感)
    for key, base in (("paint0", TURF_COLS[0]), ("paint1", TURF_COLS[1])):
        pt = pygame.Surface((TILE, TILE))
        prng = random.Random(sum(base))
        _grad_v(pt, (0, 0, TILE, TILE), _lit(base, 12), _dim(base, 10))
        for _ in range(7):
            bx = prng.randrange(3, TILE - 3)
            by = prng.randrange(3, TILE - 3)
            pygame.draw.circle(pt, _dim(base, 26), (bx, by), prng.randint(3, 8))
        for _ in range(5):
            bx = prng.randrange(3, TILE - 3)
            by = prng.randrange(3, TILE - 3)
            pygame.draw.circle(pt, _lit(base, 30), (bx, by), prng.randint(2, 4))
        pygame.draw.rect(pt, _dim(base, 34), (0, 0, TILE, TILE), 1)
        art[key] = pt

    # 實體腳下的柔和橢圓影
    for key, w in (("sh_ent", 30), ("sh_item", 22)):
        es = pygame.Surface((w, w // 2 + 2), pygame.SRCALPHA)
        pygame.draw.ellipse(es, (10, 14, 24, 70), (0, 0, w, w // 2))
        art[key] = es
    return art




# ----------------------------------------------------------------------
# 場景造景(原創像素風):實體造景佔用硬磚格,花草類點綴地板
# ----------------------------------------------------------------------
DECO_SOLID = {"tree", "sakura", "maple", "pine", "house", "house_snow",
              "lantern", "torii", "rock", "cactus", "snowman", "coral",
              "crystal", "crystal_red", "mushroom", "bamboo"}
DECO_FLOOR = {"flower", "grass", "shell", "pebble"}


def draw_char_gear(s, ci, x, y, rad, facing, t):
    """依角色編號在頭上畫專屬配件,遊戲內一眼認出是哪隻。"""
    top = y - rad + 2
    if ci == 0:      # 神射手:綠頭帶+羽毛
        pygame.draw.rect(s, (70, 150, 80), (x - rad + 2, top - 2, rad*2 - 4, 6),
                         border_radius=3)
        pygame.draw.ellipse(s, (240, 240, 220), (x + rad - 8, top - 14, 6, 16))
    elif ci == 1:    # 足球明星:頭頂小足球
        pygame.draw.circle(s, (250, 250, 255), (x, top - 8), 7)
        pygame.draw.circle(s, (50, 54, 66), (x, top - 8), 7, 1)
        for a2 in (0.5, 2.6, 4.7):
            pygame.draw.circle(s, (50, 54, 66),
                               (int(x + 3.5*math.cos(a2)),
                                int(top - 8 + 3.5*math.sin(a2))), 2)
    elif ci == 2:    # 工程師:黃色安全帽
        pygame.draw.ellipse(s, (240, 190, 40), (x - rad + 3, top - 12,
                                                rad*2 - 6, 14))
        pygame.draw.rect(s, (240, 190, 40), (x - rad, top - 1, rad*2, 4),
                         border_radius=2)
        pygame.draw.line(s, (190, 140, 20), (x, top - 12), (x, top + 1), 2)
    elif ci == 3:    # 劍客:髮髻+背後刀柄
        pygame.draw.circle(s, (60, 50, 46), (x, top - 8), 6)
        pygame.draw.rect(s, (120, 90, 60), (x - rad - 6, y - 6, 8, 4))
        pygame.draw.circle(s, (200, 170, 90), (x - rad - 6, y - 4), 3)
    elif ci == 4:    # 忍者:藏藍頭巾+飄帶
        pygame.draw.rect(s, (44, 56, 96), (x - rad + 1, top - 4, rad*2 - 2, 8),
                         border_radius=4)
        wav = int(3 * math.sin(t * 6))
        pygame.draw.polygon(s, (44, 56, 96),
                            [(x + rad - 2, top), (x + rad + 12, top - 4 + wav),
                             (x + rad + 10, top + 4 + wav)])
    elif ci == 5:    # 醫護兵:白帽紅十字
        pygame.draw.rect(s, (245, 245, 250), (x - 10, top - 12, 20, 12),
                         border_radius=3)
        pygame.draw.rect(s, (220, 60, 60), (x - 2, top - 10, 4, 8))
        pygame.draw.rect(s, (220, 60, 60), (x - 6, top - 8, 12, 4))
    elif ci == 6:    # 守護者:銀灰頭盔+頂冠
        pygame.draw.ellipse(s, (150, 158, 172), (x - rad + 2, top - 10,
                                                 rad*2 - 4, 14))
        pygame.draw.rect(s, (120, 128, 142), (x - 2, top - 16, 4, 8))
    elif ci == 7:    # 時空行者:懸浮時鐘環
        cy2 = top - 12 + int(2 * math.sin(t * 3))
        pygame.draw.circle(s, (140, 200, 230), (x, cy2), 8, 2)
        ang = t * 2.5
        pygame.draw.line(s, (140, 200, 230), (x, cy2),
                         (int(x + 5*math.cos(ang)), int(cy2 + 5*math.sin(ang))), 2)
    elif ci == 8:    # 氣旋使:頭頂小旋風
        for k in range(3):
            r2 = 3 + k * 3
            a0 = t * 5 + k
            pygame.draw.arc(s, (170, 220, 240),
                            (x - r2, top - 12 - k*2 - r2//2, r2*2, r2),
                            a0, a0 + 4.2, 2)
    elif ci == 9:    # 砲手:軍綠貝雷帽(斜戴)
        pygame.draw.ellipse(s, (90, 110, 70), (x - rad + 1, top - 9,
                                               rad*2 - 8, 11))
        pygame.draw.circle(s, (70, 88, 54), (x + rad - 9, top - 4), 3)
    elif ci == 10:   # 獵人:寬簷帽
        pygame.draw.ellipse(s, (140, 100, 60), (x - rad - 4, top - 4,
                                                rad*2 + 8, 8))
        pygame.draw.ellipse(s, (120, 84, 48), (x - 9, top - 12, 18, 11))
    elif ci == 11:   # 蠻牛:牛角
        for sg in (-1, 1):
            pygame.draw.polygon(s, (230, 220, 200),
                                [(x + sg*(rad - 5), top + 2),
                                 (x + sg*(rad + 7), top - 8),
                                 (x + sg*(rad - 1), top - 2)])
    elif ci == 12:   # 幻影師:紫色魔術帽
        pygame.draw.ellipse(s, (90, 60, 140), (x - rad + 1, top - 3,
                                               rad*2 - 2, 7))
        pygame.draw.rect(s, (110, 74, 168), (x - 8, top - 17, 16, 15),
                         border_radius=2)
        pygame.draw.rect(s, (200, 170, 240), (x - 8, top - 7, 16, 3))
    elif ci == 13:   # 冰霜使:冰晶頭冠
        for dx2, h2 in ((-8, 8), (0, 12), (8, 8)):
            pygame.draw.polygon(s, (180, 225, 250),
                                [(x + dx2 - 3, top), (x + dx2, top - h2),
                                 (x + dx2 + 3, top)])
    elif ci == 14:   # 水靈:水滴呆毛
        drop = top - 8 + int(2 * math.sin(t * 4))
        pygame.draw.circle(s, (110, 190, 240), (x, drop), 5)
        pygame.draw.polygon(s, (110, 190, 240),
                            [(x - 4, drop - 2), (x, drop - 12), (x + 4, drop - 2)])
    elif ci == 15:   # 節奏使:耳機
        pygame.draw.arc(s, (250, 120, 170), (x - rad - 2, top - 8,
                                             rad*2 + 4, rad + 8), 0.4, 2.75, 3)
        for sg in (-1, 1):
            pygame.draw.circle(s, (250, 120, 170), (x + sg*(rad - 1), y - 4), 5)
    elif ci == 16:   # 士官長:軍帽
        pygame.draw.rect(s, (80, 96, 62), (x - rad + 2, top - 10, rad*2 - 4, 9),
                         border_radius=3)
        pygame.draw.rect(s, (56, 70, 44), (x - rad + 1, top - 2, rad*2 - 2, 4))
        pygame.draw.circle(s, (220, 200, 90), (x, top - 6), 2)
    elif ci == 17:   # 海盜船長:三角帽
        pygame.draw.polygon(s, (60, 46, 40),
                            [(x - rad - 5, top), (x, top - 14), (x + rad + 5, top)])
        pygame.draw.circle(s, (240, 240, 240), (x, top - 6), 3)
    elif ci == 18:   # 電光使:閃電呆毛
        pygame.draw.polygon(s, (255, 224, 60),
                            [(x - 2, top - 16), (x + 5, top - 8), (x + 1, top - 8),
                             (x + 4, top), (x - 4, top - 6), (x, top - 6)])
    elif ci == 19:   # 爆破專家:紅色爆破盔+引線
        pygame.draw.ellipse(s, (190, 70, 60), (x - rad + 2, top - 11,
                                               rad*2 - 4, 13))
        sp = top - 14 + int(1.5 * math.sin(t * 10))
        pygame.draw.line(s, (120, 90, 60), (x, top - 10), (x + 3, sp), 2)
        pygame.draw.circle(s, (255, 200, 80), (x + 3, sp), 2)
    elif ci == 20:   # 釣客:漁夫帽+魚鉤
        pygame.draw.ellipse(s, (120, 140, 110), (x - rad - 2, top - 4,
                                                 rad*2 + 4, 7))
        pygame.draw.ellipse(s, (104, 122, 96), (x - 8, top - 11, 16, 9))
        hy = y - 2 + int(2 * math.sin(t * 3))
        pygame.draw.line(s, (200, 208, 220), (x + rad + 2, top - 2),
                         (x + rad + 8, hy), 1)
        pygame.draw.arc(s, (220, 226, 236), (x + rad + 5, hy, 7, 7), 3.0, 6.0, 2)
    elif ci == 21:   # 園丁:草帽+小花
        pygame.draw.ellipse(s, (222, 196, 120), (x - rad - 3, top - 4,
                                                 rad*2 + 6, 8))
        pygame.draw.ellipse(s, (206, 178, 100), (x - 9, top - 11, 18, 10))
        for a2 in range(5):
            an = a2 * 1.256
            pygame.draw.circle(s, (250, 150, 190),
                               (int(x + 8 + 3*math.cos(an)),
                                int(top - 10 + 3*math.sin(an))), 2)
        pygame.draw.circle(s, (255, 220, 90), (x + 8, top - 10), 2)
    elif ci == 22:   # 氣球商人:綁著小氣球
        bx2 = x + rad - 2 + int(2 * math.sin(t * 2.2))
        by2 = top - 18 + int(2 * math.sin(t * 3.1))
        pygame.draw.line(s, (180, 188, 200), (x + rad - 4, top), (bx2, by2 + 6), 1)
        pygame.draw.ellipse(s, (255, 120, 120), (bx2 - 5, by2 - 6, 10, 12))
    elif ci == 23:   # 力士:髮髻+紅頭帶
        pygame.draw.rect(s, (210, 70, 60), (x - rad + 2, top - 2, rad*2 - 4, 5),
                         border_radius=2)
        pygame.draw.circle(s, (50, 42, 40), (x, top - 8), 7)
        pygame.draw.circle(s, (70, 58, 54), (x, top - 8), 7, 2)


MULTI_LABELS = {2: ("雙殺!", "DOUBLE KILL!"), 3: ("三殺!", "TRIPLE KILL!"),
                4: ("四殺!", "QUADRA KILL!"), 5: ("五連殺!!", "PENTA KILL!!")}
ENV_KILLERS = {"penguin": (("酷企鵝", "Penguin"), (150, 220, 250)),
               "plane": (("轟炸機", "Bomber"), (200, 206, 220)),
               "cannonball": (("砲彈", "Cannonball"), (190, 196, 210)),
               "fall": (("落石", "Falling block"), (200, 180, 150)),
               "boss": (("章魚王", "Octopus King"), (230, 130, 200)),
               "minion": (("章魚小兵", "Octo-minion"), (200, 150, 230))}


def draw_feed(surf, g, x0, y0, max_w=None):
    """即時戰況欄(擊殺播報 + 連殺),可畫在全螢幕左側黑邊。"""
    fy = y0
    for fe in g.feed:
        alpha = max(0, min(255, int(fe["t"] / 5.0 * 340)))
        killer = next((q for q in g.players if q.id == fe["k"]), None)
        victim = next((q for q in g.players if q.id == fe["v"]), None)
        if victim is None:
            continue
        vname = ("CPU%d" % (victim.id + 1)) if victim.is_bot \
            else victim.name[:6]
        parts = []
        if fe["m"] >= 2:
            mz = MULTI_LABELS[min(5, fe["m"])]
            parts.append((T(*mz), (255, 214, 90)))
        if killer is not None:
            kname = ("CPU%d" % (killer.id + 1)) if killer.is_bot \
                else killer.name[:6]
            parts.append((kname, killer.color))
            parts.append((T(" 泡爆了 ", " popped "), (225, 232, 244)))
            parts.append((vname, victim.color))
            if fe["s"] >= 3:
                parts.append((T("(%d連殺中)" % fe["s"],
                                " (%d streak)" % fe["s"]),
                              (255, 190, 120)))
        elif fe.get("e") in ENV_KILLERS:
            (zh_en, ecol) = ENV_KILLERS[fe["e"]]
            parts.append((T(*zh_en), ecol))
            parts.append((T(" 擊殺了 ", " killed "), (225, 232, 244)))
            parts.append((vname, victim.color))
        else:
            parts.append((vname, victim.color))
            parts.append((T(" 被場地淘汰", " eliminated by arena"),
                          (200, 208, 224)))
        surfs = [render_text(19, txt, col) for (txt, col) in parts]
        tw = sum(sf.get_width() for sf in surfs)
        row = pygame.Surface((tw + 18, 28), pygame.SRCALPHA)
        pygame.draw.rect(row, (12, 18, 30, min(190, alpha)),
                         row.get_rect(), border_radius=9)
        rx2 = 9
        for sf in surfs:
            row.blit(sf, (rx2, 3))
            rx2 += sf.get_width()
        if max_w is not None and row.get_width() > max_w:
            row = row.subsurface((0, 0, max_w, row.get_height())).copy()
        row.set_alpha(alpha)
        surf.blit(row, (x0, fy))
        fy += 31


def draw_deco(s, kind, x, y, t):
    """在 (x,y) 格繪製造景(頂部可探出格子上緣,更有立體感)。"""
    cx = x + TILE // 2
    sway = math.sin(t * 1.6 + x * 0.05) * 2
    if kind in ("tree", "sakura", "maple", "pine"):
        pygame.draw.rect(s, (108, 76, 48), (cx - 5, y + TILE - 22, 10, 20))
        pygame.draw.rect(s, (86, 58, 36), (cx - 5, y + TILE - 22, 10, 20), 1)
        if kind == "pine":
            cols = ((36, 96, 66), (48, 120, 82), (70, 148, 100))
            for i, w in enumerate((22, 17, 11)):
                yy = y + TILE - 26 - i * 11
                pygame.draw.polygon(s, cols[i],
                                    [(cx - w + sway, yy + 12),
                                     (cx + w + sway, yy + 12),
                                     (cx + sway, yy - 6)])
            return
        pal = {"tree": ((52, 118, 62), (76, 150, 84), (108, 182, 110)),
               "sakura": ((214, 130, 168), (236, 164, 196), (250, 204, 222)),
               "maple": ((178, 84, 44), (214, 118, 54), (240, 160, 76))}[kind]
        for (ddx, ddy, rr, ci) in ((-11, -12, 11, 0), (11, -12, 11, 0),
                                   (0, -22, 13, 1), (-7, -17, 9, 2),
                                   (8, -18, 8, 2)):
            pygame.draw.circle(s, pal[ci],
                               (int(cx + ddx + sway), y + TILE - 20 + ddy), rr)
        if kind == "sakura":
            rng = random.Random(x * 3 + y)
            for _ in range(5):
                pygame.draw.circle(s, (255, 240, 248),
                                   (cx + rng.randint(-13, 13) + int(sway),
                                    y + TILE - 34 + rng.randint(-10, 8)), 1)
    elif kind in ("house", "house_snow"):
        pygame.draw.rect(s, (238, 224, 196), (x + 7, y + 16, TILE - 14, TILE - 22))
        pygame.draw.rect(s, (170, 150, 120), (x + 7, y + 16, TILE - 14, TILE - 22), 1)
        roof = (208, 92, 74) if kind == "house" else (120, 130, 156)
        pygame.draw.polygon(s, roof, [(x + 3, y + 18), (x + TILE - 3, y + 18),
                                      (x + TILE - 9, y + 2), (x + 9, y + 2)])
        pygame.draw.polygon(s, tuple(max(0, v - 40) for v in roof),
                            [(x + 3, y + 18), (x + TILE - 3, y + 18),
                             (x + TILE - 9, y + 2), (x + 9, y + 2)], 1)
        if kind == "house_snow":
            pygame.draw.polygon(s, (244, 250, 255),
                                [(x + 5, y + 14), (x + TILE - 5, y + 14),
                                 (x + TILE - 10, y + 4), (x + 10, y + 4)])
        pygame.draw.rect(s, (124, 90, 60), (cx - 5, y + TILE - 18, 10, 12))
        win = (255, 226, 130)
        pygame.draw.rect(s, win, (x + 11, y + 24, 8, 8))
        pygame.draw.rect(s, (150, 130, 100), (x + 11, y + 24, 8, 8), 1)
    elif kind == "lantern":
        pygame.draw.rect(s, (150, 154, 166), (cx - 4, y + TILE - 16, 8, 14))
        pygame.draw.rect(s, (168, 172, 184), (cx - 9, y + 14, 18, 12),
                         border_radius=3)
        glow = 200 + int(40 * math.sin(t * 3 + x))
        pygame.draw.rect(s, (255, glow, 120), (cx - 5, y + 17, 10, 6))
        pygame.draw.polygon(s, (120, 124, 136),
                            [(cx - 12, y + 14), (cx + 12, y + 14), (cx, y + 5)])
    elif kind == "torii":
        red = (196, 70, 58)
        for px in (x + 9, x + TILE - 13):
            pygame.draw.rect(s, red, (px, y + 8, 5, TILE - 12))
        pygame.draw.rect(s, red, (x + 2, y + 6, TILE - 4, 5))
        pygame.draw.rect(s, (150, 48, 40), (x + 5, y + 14, TILE - 10, 4))
        pygame.draw.rect(s, (150, 48, 40), (x + 2, y + 6, TILE - 4, 5), 1)
    elif kind == "rock":
        pygame.draw.ellipse(s, (140, 140, 152), (x + 5, y + 12, TILE - 10, TILE - 18))
        pygame.draw.ellipse(s, (170, 170, 182), (x + 10, y + 8, TILE - 24, 16))
        pygame.draw.ellipse(s, (104, 104, 118), (x + 5, y + 12, TILE - 10, TILE - 18), 2)
    elif kind == "cactus":
        g = (92, 158, 84)
        pygame.draw.rect(s, g, (cx - 5, y + 8, 10, TILE - 14), border_radius=5)
        pygame.draw.rect(s, g, (cx - 15, y + 16, 8, 12), border_radius=4)
        pygame.draw.rect(s, g, (cx + 7, y + 12, 8, 14), border_radius=4)
        rng = random.Random(x + y * 5)
        for _ in range(7):
            pygame.draw.circle(s, (210, 232, 190),
                               (cx + rng.randint(-4, 4),
                                y + 12 + rng.randint(0, TILE - 22)), 1)
    elif kind == "snowman":
        pygame.draw.circle(s, (246, 250, 255), (cx, y + TILE - 14), 12)
        pygame.draw.circle(s, (250, 252, 255), (cx, y + 16), 9)
        for c2 in ((246, 250, 255), (250, 252, 255)):
            pass
        pygame.draw.circle(s, (210, 222, 236), (cx, y + TILE - 14), 12, 1)
        pygame.draw.circle(s, (30, 34, 44), (cx - 3, y + 14), 1)
        pygame.draw.circle(s, (30, 34, 44), (cx + 3, y + 14), 1)
        pygame.draw.polygon(s, (240, 140, 60),
                            [(cx, y + 17), (cx + 7, y + 19), (cx, y + 20)])
        pygame.draw.line(s, (110, 80, 50), (cx - 9, y + 24), (cx - 17, y + 18), 2)
        pygame.draw.line(s, (110, 80, 50), (cx + 9, y + 24), (cx + 17, y + 18), 2)
    elif kind == "coral":
        for (ddx, col) in ((-10, (238, 120, 130)), (0, (250, 160, 110)),
                           (10, (232, 104, 150))):
            bx = cx + ddx
            pygame.draw.line(s, col, (bx, y + TILE - 6), (bx, y + 18), 4)
            pygame.draw.line(s, col, (bx, y + 26), (bx - 6, y + 16), 3)
            pygame.draw.line(s, col, (bx, y + 24), (bx + 6, y + 14), 3)
    elif kind in ("crystal", "crystal_red"):
        col = (120, 220, 230) if kind == "crystal" else (240, 110, 100)
        lit = tuple(min(255, v + 40) for v in col)
        for (ddx, h, w) in ((-9, 22, 7), (2, 32, 9), (12, 18, 6)):
            bx = cx + ddx
            base = y + TILE - 6
            pygame.draw.polygon(s, col, [(bx - w // 2, base), (bx + w // 2, base),
                                         (bx, base - h)])
            pygame.draw.line(s, lit, (bx, base - h), (bx - 1, base - 4), 2)
    elif kind == "bamboo":
        for (ddx, h) in ((-11, TILE + 4), (0, TILE + 12), (11, TILE - 2)):
            bx = cx + ddx + int(sway * 0.7)
            top = y + TILE - h
            pygame.draw.rect(s, (118, 176, 96), (bx - 3, top, 6, h))
            pygame.draw.rect(s, (92, 148, 74), (bx - 3, top, 6, h), 1)
            for seg in range(1, h // 14 + 1):
                pygame.draw.line(s, (80, 132, 64),
                                 (bx - 3, y + TILE - seg * 14),
                                 (bx + 3, y + TILE - seg * 14), 2)
            pygame.draw.line(s, (140, 196, 116), (bx, top),
                             (bx + 8 + int(sway), top - 6), 2)
            pygame.draw.ellipse(s, (150, 206, 124),
                                (bx + 5 + int(sway), top - 10, 9, 5))
    elif kind == "mushroom":
        pygame.draw.rect(s, (240, 232, 214), (cx - 4, y + 22, 8, TILE - 28),
                         border_radius=3)
        pygame.draw.ellipse(s, (210, 76, 70), (cx - 14, y + 8, 28, 18))
        for (ddx, ddy) in ((-7, 5), (2, 3), (7, 8)):
            pygame.draw.circle(s, (250, 240, 235), (cx + ddx, y + 8 + ddy), 2)
    elif kind == "flower":
        rng = random.Random(x * 11 + y * 3)
        for _ in range(3):
            fx2 = x + 8 + rng.randrange(TILE - 16)
            fy2 = y + 8 + rng.randrange(TILE - 16)
            col = rng.choice(((250, 170, 190), (255, 220, 130), (190, 170, 250)))
            for a in range(5):
                ang = a * 1.257
                pygame.draw.circle(s, col, (int(fx2 + 3 * math.cos(ang)),
                                            int(fy2 + 3 * math.sin(ang))), 2)
            pygame.draw.circle(s, (255, 250, 210), (fx2, fy2), 2)
    elif kind == "grass":
        rng = random.Random(x * 7 + y)
        for _ in range(4):
            gx = x + 6 + rng.randrange(TILE - 12)
            gy = y + TILE - 8 - rng.randrange(10)
            for ddx in (-3, 0, 3):
                pygame.draw.line(s, (96, 160, 84), (gx, gy),
                                 (gx + ddx + int(sway), gy - 7), 1)
    elif kind == "shell":
        pygame.draw.circle(s, (246, 222, 196), (cx, y + TILE - 12), 7)
        pygame.draw.circle(s, (216, 182, 150), (cx, y + TILE - 12), 7, 1)
        for a in range(3):
            pygame.draw.line(s, (216, 182, 150), (cx, y + TILE - 12),
                             (cx + int(6 * math.cos(1.2 + a * 0.5)),
                              y + TILE - 12 - int(6 * math.sin(1.2 + a * 0.5))), 1)
    elif kind == "pebble":
        rng = random.Random(x + y * 13)
        for _ in range(3):
            pygame.draw.circle(s, (176, 172, 168),
                               (x + 8 + rng.randrange(TILE - 16),
                                y + 10 + rng.randrange(TILE - 18)),
                               rng.randint(2, 4))


def draw_ambient(s, kind, t):
    """環境粒子(無狀態:位置由時間函數決定,雙端各自演算即可)。"""
    H = ROWS * TILE
    rng = random.Random(97)
    n = 22
    for i in range(n):
        x0 = rng.random() * SCREEN_W
        y0 = rng.random() * H
        spd = 14 + rng.random() * 22
        ph = rng.random() * 6.28
        if kind == "petals":
            x = (x0 + t * 22 + 26 * math.sin(t * 1.4 + ph)) % SCREEN_W
            y = (y0 + t * spd) % H
            ang = t * 3 + ph
            pygame.draw.ellipse(s, (250, 196, 214),
                                (x, y, 6 + 2 * math.sin(ang), 4))
        elif kind == "snow":
            x = (x0 + 14 * math.sin(t * 0.9 + ph)) % SCREEN_W
            y = (y0 + t * spd * 0.8) % H
            pygame.draw.circle(s, (248, 252, 255), (int(x), int(y)),
                               2 if i % 3 else 3)
        elif kind == "leaves":
            x = (x0 + t * 30 + 20 * math.sin(t * 1.7 + ph)) % SCREEN_W
            y = (y0 + t * spd) % H
            col = ((214, 118, 54), (240, 160, 76), (178, 84, 44))[i % 3]
            pygame.draw.ellipse(s, col, (x, y, 7, 4 + 2 * math.sin(t * 4 + ph)))
        elif kind == "fireflies":
            if i >= 12:
                continue
            x = x0 + 34 * math.sin(t * 0.5 + ph) + 12 * math.sin(t * 1.3 + i)
            y = y0 + 24 * math.cos(t * 0.4 + ph)
            a = int(120 + 110 * math.sin(t * 2.2 + ph))
            if a > 40:
                surf = pygame.Surface((10, 10), pygame.SRCALPHA)
                pygame.draw.circle(surf, (220, 255, 140, a), (5, 5), 4)
                pygame.draw.circle(surf, (255, 255, 220, min(255, a + 60)),
                                   (5, 5), 2)
                s.blit(surf, (x % SCREEN_W, y % H))
        elif kind == "embers":
            x = (x0 + 16 * math.sin(t * 2 + ph)) % SCREEN_W
            y = H - ((y0 * 0.3 + t * spd * 1.4) % (H + 30))
            a = max(0, int(200 - (H - y) * 0.35))
            if a > 20:
                surf = pygame.Surface((6, 6), pygame.SRCALPHA)
                pygame.draw.circle(surf, (255, 150, 70, a), (3, 3), 2)
                s.blit(surf, (x, y))
        elif kind == "steam":
            if i >= 12:
                continue
            x = (x0 + 20 * math.sin(t * 0.6 + ph)) % SCREEN_W
            y = H - ((y0 * 0.4 + t * spd * 0.7) % (H + 40))
            grow = (H - y) / H
            rr = int(4 + grow * 9)
            a = max(0, int(70 * (1 - grow)))
            if a > 8:
                surf = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (240, 244, 250, a), (rr, rr), rr)
                s.blit(surf, (x, y))
        elif kind == "bubbles":
            x = (x0 + 12 * math.sin(t * 1.5 + ph)) % SCREEN_W
            y = H - ((y0 * 0.5 + t * spd) % (H + 20))
            rr = 2 + i % 3
            surf = pygame.Surface((rr * 2 + 2, rr * 2 + 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (210, 240, 255, 130), (rr + 1, rr + 1), rr, 1)
            s.blit(surf, (x, y))


# ----------------------------------------------------------------------
# 電腦 AI 的軍火官:主動道具與角色技能的使用判斷
# ----------------------------------------------------------------------
def _bot_enemies(game, p):
    return [q for q in game.players
            if q is not p and q.alive and not q.trapped and q.ghost_t <= 0
            and not (p.team is not None and q.team == p.team)
            and not game.boss_mode]


def _bot_aligned_enemy(game, p, maxd=7, need_clear=True):
    """面向四線上最近的敵人 → (方向名, 距離, 敵人) 或 None。"""
    pr, pc = p.tile()
    best = None
    for q in _bot_enemies(game, p):
        qr, qc = q.tile()
        if qr == pr and qc != pc:
            d = abs(qc - pc)
            dirn = "right" if qc > pc else "left"
            sr, sc = 0, (1 if qc > pc else -1)
        elif qc == pc and qr != pr:
            d = abs(qr - pr)
            dirn = "down" if qr > pr else "up"
            sr, sc = (1 if qr > pr else -1), 0
        else:
            continue
        if d > maxd:
            continue
        if need_clear and any(game.grid[pr + sr * i][pc + sc * i] != FLOOR
                              for i in range(1, d)):
            continue
        if best is None or d < best[1]:
            best = (dirn, d, q)
    return best


def _bot_in_danger(game, p):
    t = p.tile()
    if t in game.falling or t in game.blasts:
        return True
    for b in game.bubbles:
        if t in predicted_blast(game, b.r, b.c, b.power, b.xshape):
            return True
    return False


def _bot_near_dist(game, p):
    ds = [abs(q.tile()[0] - p.tile()[0]) + abs(q.tile()[1] - p.tile()[1])
          for q in _bot_enemies(game, p)]
    return min(ds) if ds else None


def _bot_danger_tiles(game):
    """預測所有水球爆炸範圍 + 現存水柱 + 落石。"""
    dang = set(game.falling) | set(game.blasts)
    for b in game.bubbles:
        dang |= predicted_blast(game, b.r, b.c, b.power, b.xshape)
    return dang


def _soccer_step(game, p, target, avoid=None):
    """BFS 求朝 target 格的第一步方向;avoid 內的格子繞路(目標除外)。"""
    from collections import deque as _dq
    start = p.tile()
    if start == target:
        return None
    avoid = avoid or set()
    seen = {start}
    q2 = _dq([(start, None)])
    while q2:
        (r, c), first = q2.popleft()
        for dirn, (dx, dy) in DIRS.items():
            nr, nc = r + dy, c + dx
            if (nr, nc) in seen:
                continue
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            if game.grid[nr][nc] != FLOOR and (nr, nc) != target:
                continue
            if game.bubble_at(nr, nc) is not None:
                continue
            if (nr, nc) in avoid and (nr, nc) != target:
                continue
            nf = first or dirn
            if (nr, nc) == target:
                return nf
            seen.add((nr, nc))
            q2.append(((nr, nc), nf))
        if len(seen) > 260:
            break
    return None


def bot_soccer(game, p):
    """足球 AI:射門/傳球/帶球避險/搶球/接應跑位/追擊/守門。"""
    if game.ball is None or game.goal_pause > 0:
        return None
    if _bot_in_danger(game, p):
        return None                     # 危險中交回原本的逃生邏輯
    b = game.ball
    tix = (p.team or 0) % 2
    enemy_goal_c = COLS - 1 if tix == 0 else 0
    danger = _bot_danger_tiles(game)
    pr, pc = p.tile()

    def lane_clear(r0, c0, r1, c1, block_enemy=True):
        """兩點同線且中途無牆/箱;block_enemy=敵人站線上視為不通(會被攔截)。"""
        if r0 != r1 and c0 != c1:
            return False
        d = abs(r1 - r0) + abs(c1 - c0)
        sr = (r1 > r0) - (r1 < r0)
        sc = (c1 > c0) - (c1 < c0)
        for i in range(1, d):
            tr, tc = r0 + sr * i, c0 + sc * i
            if game.grid[tr][tc] != FLOOR:
                return False
            if block_enemy and any(q.alive and not q.trapped
                                   and (q.team or 0) % 2 != tix
                                   and q.tile() == (tr, tc)
                                   for q in game.players):
                return False
        return True

    def face_toward(r1, c1):
        if r1 == pr:
            return "right" if c1 > pc else "left"
        return "down" if r1 > pr else "up"

    if b["carrier"] == p.id:
        # 1) 射門:對準敵門、距離內、線上無牆無敵人
        if pr in GOAL_ROWS:
            dist = abs(enemy_goal_c - pc)
            if dist <= SHOOT_RANGE and lane_clear(pr, pc, pr, enemy_goal_c):
                p.facing = face_toward(pr, enemy_goal_c)
                game.shoot_ball(p)
                return None
        # 2) 傳球:同線隊友明顯更接近敵門且傳球線淨空
        best = None
        for q in game.players:
            if (q is p or not q.alive or q.trapped
                    or (q.team or 0) % 2 != tix):
                continue
            qr, qc = q.tile()
            d = abs(qr - pr) + abs(qc - pc)
            if not (2 <= d <= SHOOT_RANGE):
                continue
            if not lane_clear(pr, pc, qr, qc):
                continue
            gain = abs(enemy_goal_c - pc) - abs(enemy_goal_c - qc)
            if gain >= 2 and (best is None or gain > best[0]):
                best = (gain, face_toward(qr, qc))
        # 被敵人貼身逼搶時,只要有安全傳球線就先傳
        pressured = any((q.team or 0) % 2 != tix and q.alive
                        and abs(q.tile()[0] - pr) + abs(q.tile()[1] - pc) <= 2
                        for q in game.players)
        if best is not None and (best[0] >= 4 or pressured):
            p.facing = best[1]
            game.shoot_ball(p)
            return None
        # 3) 帶球推進:先繞開危險,繞不出去就硬走
        step = _soccer_step(game, p, (GOAL_ROWS[1], enemy_goal_c),
                            avoid=danger)
        return step or _soccer_step(game, p, (GOAL_ROWS[1], enemy_goal_c))

    mates = sorted((q for q in game.players
                    if q.is_bot and q.alive and not q.trapped
                    and (q.team or 0) % 2 == tix),
                   key=lambda q: q.id)
    if b["carrier"] is None:
        bt = (int(b["y"] // TILE), int(b["x"] // TILE))
        chase = sorted(mates, key=lambda q: abs(bt[0] - q.tile()[0])
                       + abs(bt[1] - q.tile()[1]))
        if p in chase[:2]:              # 最近兩人搶球
            step = _soccer_step(game, p, bt, avoid=danger)
            return step or _soccer_step(game, p, bt)
        gk = (GOAL_ROWS[1], 1 if tix == 0 else COLS - 2)
        if p.tile() == gk:
            return "hold"
        return _soccer_step(game, p, gk, avoid=danger) or "hold"

    car = next((q for q in game.players if q.id == b["carrier"]), None)
    if car is None:
        return None
    if (car.team or 0) % 2 == tix:
        # 我方持球:前插到敵門前的接應點(上下兩列)
        spot_c = enemy_goal_c - 3 if tix == 0 else enemy_goal_c + 3
        spot_r = GOAL_ROWS[0] if (p.id // 2) % 2 == 0 else GOAL_ROWS[2]
        if p.tile() == (spot_r, spot_c):
            return "hold"
        return (_soccer_step(game, p, (spot_r, spot_c), avoid=danger)
                or "hold")
    # 敵方持球:最近者貼身追擊(丟球在他腳邊),其餘退守門口
    chasers = sorted(mates, key=lambda q: abs(car.tile()[0] - q.tile()[0])
                     + abs(car.tile()[1] - q.tile()[1]))
    if p in chasers[:2]:
        step = _soccer_step(game, p, car.tile(), avoid=danger)
        return step or _soccer_step(game, p, car.tile())
    gk = (GOAL_ROWS[1], 1 if tix == 0 else COLS - 2)
    if p.tile() == gk:
        return "hold"
    return _soccer_step(game, p, gk, avoid=danger) or "hold"

def bot_gadgets(game, p):
    """電腦依情勢使用主動道具與角色技能。"""
    pr, pc = p.tile()
    al = _bot_aligned_enemy(game, p, 7)

    # ---- 主動道具 ----
    kind = (p.slot_b if game.two_slot
            else (p.item_kind if p.item_count > 0 else None))
    if kind == "missile" and al and al[1] >= 3:
        p.facing = al[0]
        game.use_active(p)
    elif kind == "freeze" and al and al[1] <= 6:
        p.facing = al[0]
        game.use_active(p)
    elif kind == "magnet" and al and 2 <= al[1] <= 6:
        p.facing = al[0]
        game.use_active(p)
    elif kind == "dart":
        for b in game.bubbles:
            if b.r != pr and b.c != pc:
                continue
            d = abs(b.r - pr) + abs(b.c - pc)
            if not (1 <= d <= 7):
                continue
            bl = predicted_blast(game, b.r, b.c, b.power, b.xshape)
            if (pr, pc) in bl:
                continue
            if any(q.tile() in bl for q in _bot_enemies(game, p)):
                p.facing = (("right" if b.c > pc else "left") if b.r == pr
                            else ("down" if b.r > pr else "up"))
                game.use_active(p)
                break
    elif kind == "hook" and _bot_in_danger(game, p):
        game.use_active(p)

    # ---- 角色技能 ----
    if p.char is None or p.skill_cd > 0:
        return
    key = CHAR_DEFS[p.char]["key"]
    al_lob = _bot_aligned_enemy(game, p, 5, need_clear=False)
    danger = _bot_in_danger(game, p)
    near = _bot_near_dist(game, p)
    close_px = any(math.hypot(q.x - p.x, q.y - p.y) <= TILE * 1.7
                   for q in _bot_enemies(game, p))
    fire = False
    if key == "hoop" and al_lob and 2 <= al_lob[1] <= 5:
        p.facing = al_lob[0]; fire = True
    elif key == "strike" and al and al[1] <= 5:
        p.facing = al[0]; fire = True
    elif key == "engineer" and near is not None and near <= 3:
        fire = True
    elif key == "sword":
        dx, dy = DIRS[p.facing]
        fr, fc = pr + dy, pc + dx
        if (0 < fr < ROWS - 1 and 0 < fc < COLS - 1
                and (game.grid[fr][fc] == SOFT
                     or game.bubble_at(fr, fc) is not None)):
            fire = True
    elif key == "ninja" and danger:
        fire = True
    elif key == "medic":
        if p.curse_t > 0:
            fire = True
        else:
            fire = any(q.alive and q.trapped and q is not p
                       and (game.boss_mode
                            or (q.team is not None and q.team == p.team))
                       and abs(q.tile()[0] - pr) + abs(q.tile()[1] - pc) <= 4
                       for q in game.players)
    elif key == "guard" and al and al[1] <= 2:
        p.facing = al[0]; fire = True
    elif key == "chrono" and danger:
        fire = True
    elif key == "cyclone" and close_px:
        fire = True
    elif key == "mortar" and al_lob and 2 <= al_lob[1] <= 4:
        p.facing = al_lob[0]; fire = True
    elif key == "trapper" and near is not None and near <= 6:
        fire = True
    elif key == "bull" and al and 2 <= al[1] <= 4:
        p.facing = al[0]; fire = True
    elif key == "phantom" and danger:
        for b in game.bubbles:
            if b.owner is p and (b.r == pr or b.c == pc) \
                    and (b.r, b.c) != (pr, pc):
                p.facing = (("right" if b.c > pc else "left") if b.r == pr
                            else ("down" if b.r > pr else "up"))
                fire = True
                break
    elif key == "frost" and near is not None and near <= 2:
        fire = True
    elif key == "ripple" and near is not None and near <= 3:
        fire = True
    elif key == "tempo" and near is not None and near <= 4:
        fire = True
    elif key == "sarge" and al_lob and al_lob[1] <= 3:
        p.facing = al_lob[0]; fire = True
    elif key == "corsair":
        fire = any(math.hypot(q.x - p.x, q.y - p.y) <= TILE * 1.5
                   and ((game.two_slot and q.slot_b is not None)
                        or (not game.two_slot and q.item_count > 0))
                   for q in _bot_enemies(game, p))
    elif key == "volt" and (danger or (near is not None and near <= 4)):
        fire = True
    elif key == "boomer":
        mines = [b for b in game.bubbles if b.remote and b.owner is p]
        if mines:
            for b in mines:
                bl = predicted_blast(game, b.r, b.c, b.power, b.xshape)
                if (pr, pc) not in bl and any(q.tile() in bl
                                              for q in _bot_enemies(game, p)):
                    fire = True
                    break
        elif near is not None and near <= 5:
            fire = True
    elif key == "angler":
        for (ir, ic) in game.items:
            if ir == pr and ic != pc:
                d = abs(ic - pc)
                sr, sc = 0, (1 if ic > pc else -1)
                dirn = "right" if ic > pc else "left"
            elif ic == pc and ir != pr:
                d = abs(ir - pr)
                sr, sc = (1 if ir > pr else -1), 0
                dirn = "down" if ir > pr else "up"
            else:
                continue
            if d <= 4 and all(game.grid[pr + sr * i][pc + sc * i] == FLOOR
                              for i in range(1, d + 1)):
                p.facing = dirn
                fire = True
                break
    elif key == "gardener" and al and al[1] <= 3:
        p.facing = al[0]; fire = True
    elif key == "vendor" and near is not None and near <= 5 and p.surge_t <= 0:
        fire = True
    elif key == "sumo" and close_px:
        fire = True
    if fire:
        game.use_skill(p)


class Game:
    def __init__(self, num_players=2, bots=None, map_index=0, boss=False,
                 boss_diff=1, items_ext=False, turf=False, infect=False,
                 soccer=False, keymaps=None, bot_level=1, countdown=0.0):
        self.items_ext = bool(items_ext)
        self.turf = bool(turf)
        self.infect = bool(infect)
        self.soccer = bool(soccer)
        self.two_slot = False   # 連線對戰:雙道具槽制(X 使用 / Z 切換)
        self.pool_kinds, self.pool_weights = item_pool(self.items_ext)
        self.boss_diff = boss_diff % len(BOSS_DIFFS)
        self.keymaps = keymaps if keymaps is not None else KEYMAPS
        self.pads = {}            # instance id -> Joystick(由主迴圈維護)
        self.bot_level = max(0, min(3, bot_level))
        self.blv = BOT_LEVELS[self.bot_level]
        self._countdown0 = max(0.0, float(countdown))
        self.num_players = max(2, min(MAX_PLAYERS, num_players))
        self.bot_ids = set(bots or ())
        self.boss_mode = boss
        self.map_index = map_index % len(MAPS)
        self.map_cfg = (SOCCER_MAP if self.soccer
                        else BOSS_MAP if boss else MAPS[self.map_index])
        self.reset()

    # ---- 場地生成 ----
    def reset(self):
        self.grid = build_boss_grid() if self.boss_mode else build_grid(self.map_cfg)

        spawn_order = list(SPAWNS)
        if not self.boss_mode and getattr(self, "_countdown0", 0) > 0:
            random.shuffle(spawn_order)   # 正式開局(有倒數)才打亂出生位置
        self.players = [Player(i, *spawn_order[i], is_bot=(i in self.bot_ids))
                        for i in range(self.num_players)]
        for p in self.players:
            if p.is_bot:
                p.bot = Bot(p)

        # Boss 模式:玩家從下方出發並給予基礎強化(原作怪物模式風格)
        self.boss = None
        self.minions = []
        self.incoming = []   # [r, c, 倒數] 章魚王丟球的落點預警
        if self.boss_mode:
            diff = BOSS_DIFFS[self.boss_diff]
            self.map_cfg = dict(BOSS_MAP)
            self.map_cfg["drop"] = diff["drop"]
            for i, p in enumerate(self.players):
                r, c = BOSS_STARTS[i % len(BOSS_STARTS)]
                p.x = c * TILE + TILE / 2.0
                p.y = r * TILE + TILE / 2.0
                p.max_bubbles = 2
                p.power = 2
                p.needles = diff["needles"]   # 原作風格:討伐戰自帶針自救
            self.boss = Boss(self.boss_diff, self.num_players)
        self.bubbles = []
        self.blasts = {}     # (r,c) -> 剩餘秒數
        self.items = {}      # (r,c) -> 種類
        self.effects = []    # 視覺特效(飛鏢軌跡、落點漣漪等)
        self.missiles = []   # 飛行中的飛彈
        self.temp_walls = {}  # 守護者的臨時石牆 (r,c) -> 剩餘秒數
        self.traps = []       # 獵人的捕獸夾 [{"r","c","o"(owner id),"t"}]
        self.puddles = []     # 水靈的水漬 [{"r","c","o","t"}]
        self.strikes = []     # 士官長的空襲 [{"r","c","t"}]
        self.fever = False    # 終局狂熱是否已開始
        self.rain_t = 0.0     # 道具雨計時
        self.sd_interval = SD_INTERVAL
        self.sd_fast = False  # 崩塌是否已加速
        self.final_boost = False   # 決一死戰威力加成是否已發
        self.drops = []       # 空投中的道具 [{"r","c","t","k"}]
        self.announce = None  # 終局宣告 {"key","t","t0"}
        self.no_drop = set()  # 園丁種的箱子:摧毀時不掉道具
        # 場地機關(履帶/泥沼/大砲/傳送門):固定位置,強制清為地板
        self.terrain = {}
        self.art = build_tile_art(self.map_cfg)
        self.deco = list(self.map_cfg.get("deco", []))
        self.ambient = self.map_cfg.get("ambient")
        self.paint = {}          # 佔地模式:(r,c) -> 隊伍編號
        self.turf_result = None  # 佔地模式終場統計
        self.outbreak = False    # 感染模式:疫情是否已爆發
        self.ball = None         # 足球:{"carrier": pid或None, "x", "y"}
        self.blast_owner = {}    # 水柱格 → 造成者 pid(擊殺歸屬)
        self.feed = []           # 擊殺播報(左側戰況欄)
        self.scores = [0, 0]     # 足球:紅/藍進球數
        self.goal_pause = 0.0    # 進球慶祝倒數
        self.goal_tiles = ({(r, 0) for r in GOAL_ROWS},
                           {(r, COLS - 1) for r in GOAL_ROWS})
        self._kickoff_done = False
        self.countdown = getattr(self, "_countdown0", 0.0)
        self.go_flash = 0.0
        self.my_pids = set()      # 本機玩家 id(倒數時標記位置)
        self.sd_locked = set()   # 崩塌落定的格子(閘門不得重開)
        self.gate_state = {}     # gid -> 是否關閉
        gates = [(rc, sp) for rc, sp in self.terrain.items()
                 if sp[0] == "gate"]
        for (tr, tc), sp in gates:
            self.gate_state[sp[3]] = True
            if self.grid[tr][tc] == FLOOR:
                self.grid[tr][tc] = HARD
        if gates and not _spawns_connected(self.grid):
            for (tr, tc), sp in gates:      # 保險絲:逐一開門直到連通
                self.grid[tr][tc] = FLOOR
                self.gate_state[sp[3]] = False
                if _spawns_connected(self.grid):
                    break
        for spec in self.map_cfg.get("feat", []):
            r, c = spec[1], spec[2]
            self.grid[r][c] = FLOOR
            self.terrain[(r, c)] = spec
        self.item_spawn_t = random.uniform(*FIELD_SPAWN_EVERY)
        # 對戰/組隊:限時 + 場地崩塌
        self.match_left = None if self.boss_mode else MATCH_TIME
        self.falling = {}    # (r,c) -> 落下倒數(紅色預警中)
        self.sd_timer = 0.0
        self.sd_queue = []
        # 場地攻擊(轟炸機/企鵝,可多重併發)
        self.hazards = []
        self.hazard_t = HAZARD_FIRST + random.uniform(0, 4)
        if not self.boss_mode:
            # 由外向內兩圈的順時針螺旋
            for ring in (1, 2):
                r0, c0 = ring, ring
                r1, c1 = ROWS - 1 - ring, COLS - 1 - ring
                tiles = ([(r0, c) for c in range(c0, c1 + 1)]
                         + [(r, c1) for r in range(r0 + 1, r1 + 1)]
                         + [(r1, c) for c in range(c1 - 1, c0 - 1, -1)]
                         + [(r, c0) for r in range(r1 - 1, r0, -1)])
                self.sd_queue.extend(tiles)
        self.time = 0.0
        self.over = False
        self.winner = None

    # ---- 查詢 ----
    def bubble_at(self, r, c):
        for b in self.bubbles:
            if b.r == r and b.c == c:
                return b
        return None

    def passable(self, r, c, player=None):
        if not (0 <= r < ROWS and 0 <= c < COLS):
            return False
        t = self.grid[r][c]
        if t == HARD:
            return False
        if t == SOFT:
            # 飛碟可以飛越箱子
            if not (player is not None and player.mount == "ufo"):
                return False
        b = self.bubble_at(r, c)
        if b is not None and (player is None or player.id not in b.riders):
            if not (player is not None and getattr(player, "volt_t", 0) > 0):
                return False
        return True

    def active_bubbles(self, player):
        return sum(1 for b in self.bubbles if b.owner is player)

    # ---- 行為 ----
    def try_place_bubble(self, p):
        if not p.alive or p.frozen_t > 0 or p.daze_t > 0:
            return
        if (self.soccer and self.ball is not None
                and self.ball["carrier"] == p.id):
            self.shoot_ball(p)      # 持球者:空白鍵=射門,不能放水球
            return
        if p.trapped:
            # 被困住時按放球鍵 = 用針自救
            if p.needles > 0:
                p.needles -= 1
                p.trapped = False
            return
        r, c = p.tile()
        b_here = self.bubble_at(r, c)
        # 拳套:站在水球上按放球鍵 → 把它丟出去
        if p.has_glove and b_here is not None:
            self.throw_bubble(b_here, p.facing)
            return
        if self.grid[r][c] != FLOOR:
            return
        if b_here is not None:
            return
        if self.active_bubbles(p) >= p.max_bubbles:
            return
        b = Bubble(r, c, p, p.power)
        if self.match_left is not None and self.match_left <= SD_START:
            b.timer = min(b.timer, FEVER_FUSE)   # 終局狂熱:引信縮短
        for q in self.players:
            if q.alive and q.tile() == (r, c):
                b.riders.add(q.id)
        self.bubbles.append(b)

    def throw_bubble(self, b, facing):
        """拳套投擲:往面向丟 3 格以上,可飛越障礙,出界會繞回對面。"""
        dx, dy = DIRS[facing]
        ir, ic = ROWS - 2, COLS - 2
        r, c = b.r, b.c
        steps = 0
        landed = False
        for _ in range(ir * ic + 4):
            r = (r - 1 + dy) % ir + 1
            c = (c - 1 + dx) % ic + 1
            steps += 1
            if steps < 3:
                continue
            if self.grid[r][c] == FLOOR and self.bubble_at(r, c) is None:
                landed = True
                break
        if not landed:
            return
        b.riders = set()
        b.slide = None
        b.r, b.c = r, c
        # 落點上有人 → 讓他們能走出去
        for q in self.players:
            if q.alive and q.tile() == (r, c):
                b.riders.add(q.id)
        self.effects.append(dict(kind="ring", x=c * TILE + TILE // 2,
                                 y=r * TILE + TILE // 2, t=0.3, t0=0.3))
        # 丟進水柱裡 → 立刻引爆
        if (r, c) in self.blasts:
            self.explode(b)

    def kick_bubble(self, b, dx, dy):
        """運動鞋:把水球踢出去滑行。"""
        b.slide = (dx, dy)
        b.slide_t = 0.0
        b.riders = set()

    def swap_items(self, p):
        """雙槽制:對調優先槽與備用槽(Z 鍵)。"""
        if self.two_slot and p.alive:
            p.slot_a, p.slot_b = p.slot_b, p.slot_a

    # ---- 角色技能(C 鍵,冷卻制) ----
    def use_skill(self, p):
        if (p.char is None or not p.alive or p.trapped
                or p.frozen_t > 0 or p.daze_t > 0):
            return
        if p.skill_cd > 0:
            # 爆破專家例外:冷卻中仍可引爆已放置的遙控水雷
            if not (CHAR_DEFS[p.char]["key"] == "boomer"
                    and any(b.remote and b.owner is p for b in self.bubbles)):
                return
        cfg = CHAR_DEFS[p.char]
        key = cfg["key"]
        ok = False
        dx, dy = DIRS[p.facing]
        r, c = p.tile()
        if key == "hoop":
            # 長距投籃:拋到前方 4 格(找不到就往回找到 2 格),無視障礙
            if self.active_bubbles(p) < p.max_bubbles:
                for i in (4, 3, 2):
                    tr, tc = r + dy * i, c + dx * i
                    if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                            and self.grid[tr][tc] == FLOOR
                            and self.bubble_at(tr, tc) is None):
                        nb = Bubble(tr, tc, p, p.power)
                        for q in self.players:
                            if q.alive and q.tile() == (tr, tc):
                                nb.riders.add(q.id)
                        self.bubbles.append(nb)
                        self.effects.append(dict(kind="lob", ball="hoop",
                                                 ax=p.x, ay=p.y,
                                                 bx=tc * TILE + TILE // 2,
                                                 by=tr * TILE + TILE // 2,
                                                 t=0.45, t0=0.45))
                        ok = True
                        break
        elif key == "strike":
            # 香蕉球:前方生成短引信水球,直走 2 格後轉彎繼續滑
            tr, tc = r + dy, c + dx
            if (self.active_bubbles(p) < p.max_bubbles
                    and 0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                    and self.grid[tr][tc] == FLOOR
                    and self.bubble_at(tr, tc) is None):
                nb = Bubble(tr, tc, p, p.power)
                nb.timer = 2.4
                nb.slide = (dx, dy)
                nb.curve = {"steps": 0, "turned": False}
                self.bubbles.append(nb)
                self.effects.append(dict(kind="kickburst", x=p.x, y=p.y,
                                         dx=dx, dy=dy, t=0.3, t0=0.3))
                ok = True
        elif key == "engineer":
            # X 型炸藥:腳下放置對角線爆炸的特殊水球
            if (self.grid[r][c] == FLOOR and self.bubble_at(r, c) is None
                    and self.active_bubbles(p) < p.max_bubbles):
                nb = Bubble(r, c, p, p.power)
                nb.xshape = True
                self.effects.append(dict(kind="xmark",
                                         x=c * TILE + TILE // 2,
                                         y=r * TILE + TILE // 2,
                                         t=0.6, t0=0.6))
                for q in self.players:
                    if q.alive and q.tile() == (r, c):
                        nb.riders.add(q.id)
                self.bubbles.append(nb)
                ok = True
        elif key == "sword":
            # 居合斬:斬碎面前箱子或引爆水球(爆炸不朝自己延伸)
            tr, tc = r + dy, c + dx
            if 0 < tr < ROWS - 1 and 0 < tc < COLS - 1:
                self.effects.append(dict(kind="slash",
                                         x=tc * TILE + TILE // 2,
                                         y=tr * TILE + TILE // 2,
                                         dx=dx, dy=dy, t=0.22, t0=0.22))
                if self.grid[tr][tc] == SOFT:
                    self.grid[tr][tc] = FLOOR
                    self.spawn_item(tr, tc)
                    ok = True
                else:
                    b = self.bubble_at(tr, tc)
                    if b is not None:
                        self.explode(b, skip_dir=(-dx, -dy))
                        ok = True
        elif key == "ninja":
            # 瞬身:向前 3~1 格找空地,穿過一切
            for i in (3, 2, 1):
                tr, tc = r + dy * i, c + dx * i
                if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                        and self.grid[tr][tc] == FLOOR
                        and self.bubble_at(tr, tc) is None):
                    self.effects.append(dict(kind="smoke", x=p.x, y=p.y,
                                             t=0.4, t0=0.4))
                    p.x = tc * TILE + TILE / 2.0
                    p.y = tr * TILE + TILE / 2.0
                    self.effects.append(dict(kind="smoke", x=p.x, y=p.y,
                                             t=0.4, t0=0.4))
                    ok = True
                    break
        elif key == "medic":
            # 急救:自身淨化 + 短護盾;合作/組隊救 4 格內被困隊友
            p.curse_t = 0.0
            p.curse_kind = None
            p.shield_t = max(p.shield_t, 1.5)
            for q in self.players:
                if not (q.alive and q.trapped) or q is p:
                    continue
                mate = (self.boss_mode
                        or (q.team is not None and q.team == p.team))
                near = abs(q.tile()[0] - r) + abs(q.tile()[1] - c) <= 4
                if mate and near:
                    q.trapped = False
                    q.shield_t = max(q.shield_t, 1.0)
                    self.effects.append(dict(kind="heal", x=q.x, y=q.y,
                                             t=0.6, t0=0.6))
            self.effects.append(dict(kind="heal", x=p.x, y=p.y, t=0.6, t0=0.6))
            ok = True
        elif key == "guard":
            # 築牆:面前生成 5 秒臨時石牆
            tr, tc = r + dy, c + dx
            if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                    and self.grid[tr][tc] == FLOOR
                    and self.bubble_at(tr, tc) is None
                    and not any(q.alive and q.tile() == (tr, tc)
                                for q in self.players)):
                self.grid[tr][tc] = HARD
                self.temp_walls[(tr, tc)] = 5.0
                self.effects.append(dict(kind="wallup",
                                         x=tc * TILE + TILE // 2,
                                         y=tr * TILE + TILE // 2, t=0.4, t0=0.4))
                ok = True
        elif key == "chrono":
            # 回溯:回到約 3 秒前的位置
            target = None
            for (ts, hx, hy) in p.pos_hist:
                if self.time - ts >= 2.8:
                    target = (hx, hy)
            if target is not None:
                tr, tc = int(target[1] // TILE), int(target[0] // TILE)
                if self.passable(tr, tc, p):
                    self.effects.append(dict(kind="smoke", x=p.x, y=p.y,
                                             t=0.35, t0=0.35))
                    p.x, p.y = target
                    p.hook_to = None
                    self.effects.append(dict(kind="rewind", x=p.x, y=p.y,
                                             t=0.55, t0=0.55))
                    ok = True
        elif key == "cyclone":
            # 颶風掌:身邊敵人退兩格,鄰接水球被踢飛
            for q in self.players:
                if q is p or not q.alive or q.trapped:
                    continue
                if math.hypot(q.x - p.x, q.y - p.y) > TILE * 1.8:
                    continue
                ddx = 0 if abs(q.x - p.x) < 8 else (1 if q.x > p.x else -1)
                ddy = 0 if abs(q.y - p.y) < 8 else (1 if q.y > p.y else -1)
                if ddx == 0 and ddy == 0:
                    ddx, ddy = DIRS[p.facing]
                qr, qc = q.tile()
                for i in (2, 1):
                    tr, tc = qr + ddy * i, qc + ddx * i
                    if self.passable(tr, tc, q):
                        q.x = tc * TILE + TILE / 2.0
                        q.y = tr * TILE + TILE / 2.0
                        break
            for b in list(self.bubbles):
                if abs(b.r - r) + abs(b.c - c) == 1 and b.slide is None:
                    b.slide = (1 if b.c > c else (-1 if b.c < c else 0),
                               1 if b.r > r else (-1 if b.r < r else 0))
                    b.slide_t = 0.0
            self.effects.append(dict(kind="gust", x=p.x, y=p.y, t=0.5, t0=0.5))
            ok = True
        elif key == "mortar":
            # 震撼彈:前方 3 格小十字 — 炸箱、引爆水球、震退+暈眩敵人(不泡人)
            for i in (3, 2):
                tr, tc = r + dy * i, c + dx * i
                if not (0 < tr < ROWS - 1 and 0 < tc < COLS - 1):
                    continue
                if self.grid[tr][tc] == HARD:
                    continue
                tiles = [(tr, tc)]
                for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ar, ac = tr + ddy, tc + ddx
                    if (0 < ar < ROWS - 1 and 0 < ac < COLS - 1
                            and self.grid[ar][ac] != HARD):
                        tiles.append((ar, ac))
                self.effects.append(dict(kind="lob", ball="shell",
                                         ax=p.x, ay=p.y,
                                         bx=tc * TILE + TILE // 2,
                                         by=tr * TILE + TILE // 2,
                                         t=0.3, t0=0.3))
                self.effects.append(dict(kind="concuss",
                                         x=tc * TILE + TILE // 2,
                                         y=tr * TILE + TILE // 2,
                                         t=0.45, t0=0.45))
                for (ar, ac) in tiles:
                    if self.grid[ar][ac] == SOFT:
                        self.grid[ar][ac] = FLOOR
                        self.spawn_item(ar, ac)
                    hitb = self.bubble_at(ar, ac)
                    if hitb is not None:
                        self.explode(hitb)
                area = set(tiles)
                for q in self.players:
                    if q is p or not q.alive or q.trapped or q.shield_t > 0:
                        continue
                    if p.team is not None and q.team == p.team:
                        continue
                    if self.boss_mode:
                        continue
                    if q.tile() in area:
                        kdx = 0 if abs(q.x - (tc * TILE + TILE / 2)) < 8 \
                            else (1 if q.x > tc * TILE + TILE / 2 else -1)
                        kdy = 0 if abs(q.y - (tr * TILE + TILE / 2)) < 8 \
                            else (1 if q.y > tr * TILE + TILE / 2 else -1)
                        if kdx == 0 and kdy == 0:
                            kdx, kdy = dx, dy
                        qr, qc = q.tile()
                        if self.passable(qr + kdy, qc + kdx, q):
                            q.x = (qc + kdx) * TILE + TILE / 2.0
                            q.y = (qr + kdy) * TILE + TILE / 2.0
                        q.daze_t = max(q.daze_t, 1.0)
                ok = True
                break
        elif key == "trapper":
            # 捕獸夾:腳下佈陷阱(同時只能有一個)
            if (self.grid[r][c] == FLOOR
                    and not any(tp["r"] == r and tp["c"] == c
                                for tp in self.traps)):
                self.traps = [tp for tp in self.traps if tp["o"] != p.id]
                self.traps.append(dict(r=r, c=c, o=p.id, t=12.0))
                ok = True
        elif key == "bull":
            # 蠻牛衝撞:直衝最多 4 格,路上的人被推開並暈眩
            tr, tc = r, c
            hit = []
            for i in range(1, 5):
                nr, nc = r + dy * i, c + dx * i
                if not (0 < nr < ROWS - 1 and 0 < nc < COLS - 1):
                    break
                if self.grid[nr][nc] != FLOOR or self.bubble_at(nr, nc):
                    break
                for q in self.players:
                    if q is not p and q.alive and q.tile() == (nr, nc):
                        hit.append(q)
                tr, tc = nr, nc
            if (tr, tc) != (r, c):
                for q in hit:
                    qr, qc = q.tile()
                    for sdx, sdy in ((-dy, dx), (dy, -dx)):
                        if self.passable(qr + sdy, qc + sdx, q):
                            q.x = (qc + sdx) * TILE + TILE / 2.0
                            q.y = (qr + sdy) * TILE + TILE / 2.0
                            break
                    q.daze_t = max(q.daze_t, 0.8)
                self.effects.append(dict(kind="stampede", ax=p.x, ay=p.y,
                                         bx=tc * TILE + TILE // 2,
                                         by=tr * TILE + TILE // 2,
                                         t=0.45, t0=0.45))
                p.x = tc * TILE + TILE / 2.0
                p.y = tr * TILE + TILE / 2.0
                ok = True
        elif key == "phantom":
            # 換位術:與面前直線上最近的自有水球交換位置
            best = None
            for b in self.bubbles:
                if b.owner is not p:
                    continue
                ddr, ddc = b.r - r, b.c - c
                if dx and ddr == 0 and ddc * dx > 0:
                    d = abs(ddc)
                elif dy and ddc == 0 and ddr * dy > 0:
                    d = abs(ddr)
                else:
                    continue
                if d <= 7 and (best is None or d < best[0]):
                    best = (d, b)
            if best is not None:
                b = best[1]
                br, bc = b.r, b.c
                b.r, b.c = r, c
                b.riders = {q.id for q in self.players
                            if q.alive and q.tile() == (r, c)}
                ox2, oy2 = p.x, p.y
                p.x = bc * TILE + TILE / 2.0
                p.y = br * TILE + TILE / 2.0
                self.effects.append(dict(kind="swapflash", ax=ox2, ay=oy2,
                                         bx=p.x, by=p.y, t=0.4, t0=0.4))
                ok = True
        elif key == "frost":
            # 霜華綻放:兩格內敵人凍結(光盾可擋,不凍隊友)
            for q in self.players:
                if q is p or not q.alive or q.shield_t > 0:
                    continue
                if p.team is not None and q.team == p.team:
                    continue
                if self.boss_mode:
                    continue
                if abs(q.tile()[0] - r) + abs(q.tile()[1] - c) <= 2:
                    q.frozen_t = max(q.frozen_t, 1.2)
            self.effects.append(dict(kind="nova", x=p.x, y=p.y, t=0.55, t0=0.55))
            ok = True
        elif key == "ripple":
            # 漣漪足跡:開始留下水漬
            p.trail_t = 2.5
            p.last_trail = None
            self.effects.append(dict(kind="aqua", x=p.x, y=p.y, t=0.45, t0=0.45))
            ok = True
        elif key == "tempo":
            # 狂想加速:自己與身旁隊友加速
            p.haste_t = 2.5
            for q in self.players:
                if q is p or not q.alive:
                    continue
                mate = self.boss_mode or (p.team is not None and q.team == p.team)
                if mate and math.hypot(q.x - p.x, q.y - p.y) <= TILE * 1.8:
                    q.haste_t = 2.5
                    self.effects.append(dict(kind="notes", x=q.x, y=q.y,
                                             t=0.6, t0=0.6))
            self.effects.append(dict(kind="notes", x=p.x, y=p.y, t=0.6, t0=0.6))
            ok = True
        elif key == "sarge":
            # 空襲信標:前方直線 3 格,1 秒後轟炸
            marked = 0
            for i in (1, 2, 3):
                tr, tc = r + dy * i, c + dx * i
                if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                        and self.grid[tr][tc] != HARD):
                    self.strikes.append(dict(r=tr, c=tc, t=1.0,
                                             owner=p.id))
                    marked += 1
            ok = marked > 0
        elif key == "corsair":
            # 掠奪之手:偷走鄰近敵人的道具
            for q in self.players:
                if q is p or not q.alive or q.shield_t > 0:
                    continue
                if p.team is not None and q.team == p.team:
                    continue
                if self.boss_mode:
                    continue
                if math.hypot(q.x - p.x, q.y - p.y) > TILE * 1.6:
                    continue
                loot = None
                if self.two_slot:
                    if q.slot_b is not None and not (p.slot_a and p.slot_b):
                        loot = q.slot_b
                        q.slot_b = q.slot_a
                        q.slot_a = None
                else:
                    if q.item_count > 0:
                        loot = q.item_kind
                        q.item_count -= 1
                        if q.item_count <= 0:
                            q.item_kind = None
                if loot is not None:
                    self.apply_item(p, loot)
                    self.effects.append(dict(kind="loot", ax=q.x, ay=q.y,
                                             bx=p.x, by=p.y, t=0.5, t0=0.5))
                    ok = True
                    break
        elif key == "volt":
            # 雷光疾馳:高速 + 穿過水球
            p.volt_t = 1.4
            self.effects.append(dict(kind="spark", x=int(p.x), y=int(p.y),
                                     t=0.35, t0=0.35))
            ok = True
        elif key == "boomer":
            # 遙控水雷:已有 → 引爆;沒有 → 放置
            mines = [b for b in self.bubbles if b.remote and b.owner is p]
            if mines:
                for b in mines:
                    self.explode(b)
                ok = False          # 引爆不重置冷卻
            elif (self.grid[r][c] == FLOOR and self.bubble_at(r, c) is None
                    and self.active_bubbles(p) < p.max_bubbles):
                nb = Bubble(r, c, p, p.power)
                nb.remote = True
                nb.timer = 8.0
                self.effects.append(dict(kind="arm",
                                         x=c * TILE + TILE // 2,
                                         y=r * TILE + TILE // 2,
                                         t=0.6, t0=0.6))
                for q in self.players:
                    if q.alive and q.tile() == (r, c):
                        nb.riders.add(q.id)
                self.bubbles.append(nb)
                ok = True
        elif key == "angler":
            # 精準甩竿:釣回直線上最近的道具
            for i in (1, 2, 3, 4):
                tr, tc = r + dy * i, c + dx * i
                if not (0 < tr < ROWS - 1 and 0 < tc < COLS - 1):
                    break
                if self.grid[tr][tc] != FLOOR:
                    break
                if (tr, tc) in self.items:
                    kind = self.items[(tr, tc)]
                    if (self.two_slot and kind in ACTIVE_KINDS
                            and p.slot_a is not None and p.slot_b is not None):
                        break       # 槽滿釣不動
                    self.items.pop((tr, tc))
                    self.apply_item(p, kind)
                    self.effects.append(dict(kind="cast",
                                             ax=tc * TILE + TILE // 2,
                                             ay=tr * TILE + TILE // 2,
                                             bx=int(p.x), by=int(p.y),
                                             t=0.5, t0=0.5))
                    ok = True
                    break
        elif key == "gardener":
            # 快速種樹:前方直線 3 個木箱(不掉道具)
            planted = 0
            for i in (1, 2, 3):
                tr, tc = r + dy * i, c + dx * i
                if not (0 < tr < ROWS - 1 and 0 < tc < COLS - 1):
                    break
                if (self.grid[tr][tc] != FLOOR or self.bubble_at(tr, tc)
                        or any(q.alive and q.tile() == (tr, tc)
                               for q in self.players)):
                    continue
                self.grid[tr][tc] = SOFT
                self.no_drop.add((tr, tc))
                self.effects.append(dict(kind="sprout",
                                         x=tc * TILE + TILE // 2,
                                         y=tr * TILE + TILE // 2, t=0.5, t0=0.5))
                planted += 1
            ok = planted > 0
        elif key == "vendor":
            # 限時特賣:+1 水球 +1 威力,6 秒
            if p.surge_t <= 0:
                p.power = min(9, p.power + 1)
                p.max_bubbles = min(8, p.max_bubbles + 1)
            p.surge_t = 6.0
            self.effects.append(dict(kind="balloons", x=int(p.x), y=int(p.y),
                                     t=0.8, t0=0.8))
            ok = True
        elif key == "sumo":
            # 震地踏:震退身邊敵人,兩格內水球引信剩 0.4 秒
            for q in self.players:
                if q is p or not q.alive or q.trapped or q.shield_t > 0:
                    continue
                if p.team is not None and q.team == p.team:
                    continue
                if self.boss_mode:
                    continue
                if math.hypot(q.x - p.x, q.y - p.y) > TILE * 1.8:
                    continue
                ddx = 0 if abs(q.x - p.x) < 8 else (1 if q.x > p.x else -1)
                ddy = 0 if abs(q.y - p.y) < 8 else (1 if q.y > p.y else -1)
                if ddx == 0 and ddy == 0:
                    ddx, ddy = DIRS[p.facing]
                qr, qc = q.tile()
                if self.passable(qr + ddy, qc + ddx, q):
                    q.x = (qc + ddx) * TILE + TILE / 2.0
                    q.y = (qr + ddy) * TILE + TILE / 2.0
            for b in self.bubbles:
                if abs(b.r - r) + abs(b.c - c) <= 2:
                    b.timer = min(b.timer, 0.4)
            self.effects.append(dict(kind="quake", x=int(p.x), y=int(p.y),
                                     t=0.55, t0=0.55))
            ok = True
        if ok:
            p.skill_cd = cfg["cd"]

    def use_active(self, p):
        """使用手持道具(雙槽制用右槽;本機單槽制用庫存)。"""
        if not p.alive or p.trapped or p.frozen_t > 0 or p.daze_t > 0:
            return
        if self.two_slot:
            kind = p.slot_b
            if kind is None:
                return
        else:
            if p.item_count <= 0:
                return
            kind = p.item_kind
        fired = True
        if kind == "dart":
            fired = self._use_dart(p)
        elif kind == "hook":
            fired = self._use_hook(p)
        elif kind == "missile":
            fired = self._use_missile(p)
        elif kind == "magnet":
            fired = self._use_magnet(p)
        elif kind == "freeze":
            fired = self._use_freeze(p)
        else:
            fired = False
        if fired:
            if self.two_slot:
                p.slot_b = p.slot_a      # 備用槽自動遞補到優先槽
                p.slot_a = None
            else:
                p.item_count -= 1
                if p.item_count <= 0:
                    p.item_kind = None

    # 舊介面名稱保留(網路/事件呼叫點沿用)
    use_dart = use_active

    def _ray(self, p, max_range=99):
        """沿面向掃描:回傳 (經過的地板格清單, 碰到的阻擋格或 None)。"""
        dx, dy = DIRS[p.facing]
        r, c = p.tile()
        path = []
        for _ in range(max_range):
            r += dy
            c += dx
            if not (0 <= r < ROWS and 0 <= c < COLS) or self.grid[r][c] == HARD:
                return path, (r, c) if (0 <= r < ROWS and 0 <= c < COLS) else None
            if self.grid[r][c] == SOFT:
                return path, (r, c)
            path.append((r, c))
        return path, None

    def _use_dart(self, p):
        """飛鏢:引爆直線上第一顆水球。"""
        path, _ = self._ray(p)
        target = None
        end = p.tile()
        for t in path:
            end = t
            b = self.bubble_at(*t)
            if b is not None:
                target = b
                break
        self.effects.append(dict(kind="dart", ax=p.x, ay=p.y,
                                 bx=end[1] * TILE + TILE // 2,
                                 by=end[0] * TILE + TILE // 2, t=0.18, t0=0.18))
        if target is not None:
            self.explode(target)
        return True

    def _use_hook(self, p):
        """鉤爪:勾住前方 7 格內的牆/箱子/水球,把自己拉到它前面。"""
        path, hit = self._ray(p, 7)
        # 水球也算可勾附的目標
        stop_i = len(path)
        for i, t in enumerate(path):
            if self.bubble_at(*t) is not None:
                hit = t
                stop_i = i
                break
        clear = path[:stop_i]
        if hit is None or not clear:
            return False                      # 沒勾到東西 → 不消耗
        tr, tc = clear[-1]
        p.hook_to = (tc * TILE + TILE / 2.0, tr * TILE + TILE / 2.0)
        self.effects.append(dict(kind="dart", ax=p.x, ay=p.y,
                                 bx=hit[1] * TILE + TILE // 2,
                                 by=hit[0] * TILE + TILE // 2, t=0.25, t0=0.25))
        return True

    def _use_missile(self, p):
        """飛彈:發射飛行彈頭,命中時爆出十字水柱。"""
        dx, dy = DIRS[p.facing]
        self.missiles.append(dict(x=p.x, y=p.y, dx=dx, dy=dy, owner=p))
        return True

    def _use_magnet(self, p):
        """磁力槍:把直線上第一個玩家或水球吸到自己面前。"""
        path, _ = self._ray(p, 6)
        target_p = None
        target_b = None
        stop_i = len(path)
        for i, t in enumerate(path):
            for q in self.players:
                if q is not p and q.alive and q.ghost_t <= 0 and q.tile() == t:
                    target_p = q
                    stop_i = i
                    break
            if target_p is None:
                b = self.bubble_at(*t)
                if b is not None:
                    target_b = b
                    stop_i = i
            if target_p is not None or target_b is not None:
                break
        if target_p is None and target_b is None:
            return False                      # 沒吸到東西 → 不消耗
        # 自己面前的一格
        fr, fc = p.tile()[0] + DIRS[p.facing][1], p.tile()[1] + DIRS[p.facing][0]
        endx = p.x
        endy = p.y
        if target_p is not None:
            if target_p.shield_t > 0:
                return False                  # 光盾抵擋磁力
            target_p.hook_to = (fc * TILE + TILE / 2.0, fr * TILE + TILE / 2.0)
            endx, endy = target_p.x, target_p.y
        else:
            target_b.riders = set()
            target_b.slide = (-DIRS[p.facing][0], -DIRS[p.facing][1])
            target_b.slide_t = 0.0
            endx = target_b.c * TILE + TILE // 2
            endy = target_b.r * TILE + TILE // 2
        self.effects.append(dict(kind="dart", ax=p.x, ay=p.y,
                                 bx=endx, by=endy, t=0.22, t0=0.22))
        return True

    def _use_freeze(self, p):
        """冰凍槍:凍結直線上第一個敵人約 2 秒。"""
        path, _ = self._ray(p, 7)
        end = p.tile()
        hit = None
        for t in path:
            end = t
            for q in self.players:
                if (q is not p and q.alive and not q.trapped
                        and q.ghost_t <= 0 and q.tile() == t
                        and not (q.team is not None and q.team == p.team)):
                    hit = q
                    break
            if hit is not None:
                break
        self.effects.append(dict(kind="beam", ax=p.x, ay=p.y,
                                 bx=end[1] * TILE + TILE // 2,
                                 by=end[0] * TILE + TILE // 2, t=0.22, t0=0.22))
        if hit is not None and hit.shield_t <= 0:
            hit.frozen_t = 2.2
        return True

    def spawn_item(self, r, c):
        if (r, c) in self.no_drop:
            self.no_drop.discard((r, c))
            return
        if random.random() < self.map_cfg.get("drop", ITEM_DROP_RATE):
            kind = random.choices(self.pool_kinds, weights=self.pool_weights, k=1)[0]
            self.items[(r, c)] = kind

    def spawn_field_item(self):
        """原版風格:場地上隨機冒出道具。"""
        if len(self.items) >= FIELD_ITEM_CAP:
            return
        spots = [(r, c) for r in range(1, ROWS - 1) for c in range(1, COLS - 1)
                 if self.grid[r][c] == FLOOR and (r, c) not in self.items
                 and (r, c) not in self.blasts and self.bubble_at(r, c) is None]
        if not spots:
            return
        r, c = random.choice(spots)
        kind = random.choices(self.pool_kinds, weights=self.pool_weights, k=1)[0]
        self.items[(r, c)] = kind
        self.effects.append(dict(kind="ring", x=c * TILE + TILE // 2,
                                 y=r * TILE + TILE // 2, t=0.4, t0=0.4))

    def _paint_tiles(self, tiles, owner):
        if not self.turf:
            return
        if owner is None or owner.team is None:
            # 場地攻擊(轟炸機等無主爆炸):把漆面洗回空白
            for t in tiles:
                self.paint.pop(t, None)
            return
        for (r, c) in tiles:
            if self.grid[r][c] == FLOOR:
                self.paint[(r, c)] = owner.team

    def explode(self, first, skip_dir=None):
        """引爆水球(含連鎖)。skip_dir=抑制起爆水球的某一臂(劍客居合斬)。"""
        queue = [first]
        while queue:
            b = queue.pop()
            if b not in self.bubbles:
                continue
            self.bubbles.remove(b)
            tiles = [(b.r, b.c)]
            dirs4 = (((1, 1), (-1, -1), (1, -1), (-1, 1)) if b.xshape
                     else ((1, 0), (-1, 0), (0, 1), (0, -1)))
            for dx, dy in dirs4:
                if skip_dir is not None and b is first and (dx, dy) == skip_dir:
                    continue          # 居合斬:不朝劍客那側延伸
                for i in range(1, b.power + 1):
                    r, c = b.r + dy * i, b.c + dx * i
                    if not (0 <= r < ROWS and 0 <= c < COLS):
                        break
                    t = self.grid[r][c]
                    if t == HARD:
                        break
                    if t == SOFT:
                        self.grid[r][c] = FLOOR
                        self.spawn_item(r, c)
                        tiles.append((r, c))
                        break
                    # 地板格
                    tiles.append((r, c))
                    if (r, c) in self.items:      # 水柱會沖走道具
                        del self.items[(r, c)]
                    other = self.bubble_at(r, c)
                    if other is not None:
                        queue.append(other)       # 連鎖引爆
                        break
            for t in tiles:
                self.blasts[t] = max(self.blasts.get(t, 0.0), BLAST_TIME)
                if b.owner is not None and b.owner in self.players:
                    self.blast_owner[t] = b.owner.id
                elif b.owner is None:
                    self.blast_owner[t] = "plane"
                else:
                    self.blast_owner[t] = ("boss" if b.owner is self.boss
                                           else "minion")
            self._paint_tiles(tiles, b.owner)
            # 章魚王受擊(只有玩家的爆炸算傷害,受擊後有短暫無敵幀)
            if (self.boss is not None and b.owner in self.players
                    and self.boss.iframe <= 0
                    and set(tiles) & self.boss.footprint()):
                self.boss.hp -= 1
                self.boss.iframe = BOSS_IFRAME
                self.boss.flash = 0.2

    def _score_goal(self, team_ix):
        self.scores[team_ix] += 1
        self.goal_pause = GOAL_PAUSE
        self.ball = dict(carrier=None,
                         x=COLS // 2 * TILE + TILE / 2.0,
                         y=ROWS // 2 * TILE + TILE / 2.0)
        self.announce = dict(key="goal%d" % team_ix,
                             t=GOAL_PAUSE, t0=GOAL_PAUSE)

    def shoot_ball(self, p):
        """持球者射門:球朝面向飛出(可傳球/被攔截/遠射進門)。"""
        b = self.ball
        if b is None or b["carrier"] != p.id:
            return
        dx, dy = DIRS[p.facing]
        b["carrier"] = None
        b["x"] = p.x + dx * 12
        b["y"] = p.y + dy * 12
        b["fly"] = (dx, dy)
        b["dist"] = 0.0
        b["shooter"] = p.id
        b["team"] = (p.team or 0) % 2
        self.effects.append(dict(kind="kickburst", x=p.x, y=p.y,
                                 dx=dx, dy=dy, t=0.3, t0=0.3))

    def kickoff_reset(self, first=False):
        """足球開球:清場、依隊伍佈陣、球回中場。"""
        self.bubbles.clear()
        self.blasts.clear()
        self.traps.clear()
        self.puddles.clear()
        self.strikes.clear()
        left = [(2, 2), (4, 2), (8, 2), (10, 2)]
        right = [(2, COLS - 3), (4, COLS - 3), (8, COLS - 3), (10, COLS - 3)]
        li = ri = 0
        for p in self.players:
            if (p.team or 0) % 2 == 0 and li < len(left):
                p.spawn = left[li]; li += 1
            elif ri < len(right):
                p.spawn = right[ri]; ri += 1
            sr, sc = p.spawn
            self.grid[sr][sc] = FLOOR
            p.alive = True
            p.trapped = False
            p.respawn_t = 0.0
            p.death_t = None
            p.frozen_t = p.daze_t = p.wet_t = 0.0
            p.hook_to = None
            p.shield_t = 0.0 if first else 1.0
            p.x = sc * TILE + TILE / 2.0
            p.y = sr * TILE + TILE / 2.0
            p.facing = "right" if (p.team or 0) % 2 == 0 else "left"
        self.ball = dict(carrier=None,
                         x=COLS // 2 * TILE + TILE / 2.0,
                         y=ROWS // 2 * TILE + TILE / 2.0)
        if not first:
            self.effects.append(dict(kind="ring", x=self.ball["x"],
                                     y=self.ball["y"], t=0.4, t0=0.4))

    def convert(self, p):
        """把玩家轉為感染者(0 號病人另有威力補償)。"""
        if p.infected:
            return
        first = not any(q.infected for q in self.players)
        p.infected = True
        p.infect_t = self.time
        if first:
            p.power = min(9, p.power + 1)   # 0 號病人:1 打 7 的補償
        self.effects.append(dict(kind="ring", x=p.x, y=p.y, t=0.4, t0=0.4))

    def _register_kill(self, victim, killer):
        entry = dict(k=(killer.id if killer is not None else -1),
                     v=victim.id, m=0, s=0, t=5.0,
                     e=(victim.env_tag or "") if killer is None else "")
        if (killer is not None and killer is not victim
                and not (victim.team is not None
                         and victim.team == killer.team)):
            killer.streak += 1
            killer.multi_n = killer.multi_n + 1 if killer.multi_t > 0 else 1
            killer.multi_t = 8.0
            entry["m"] = killer.multi_n
            entry["s"] = killer.streak
        victim.streak = 0
        victim.multi_n = 0
        victim.multi_t = 0.0
        self.feed.append(entry)
        del self.feed[:-6]

    def kill(self, p, killer=None):
        if not p.alive:
            return
        if killer is None and p.last_hit_by is not None:
            killer = next((q for q in self.players
                           if q.id == p.last_hit_by), None)
        self._register_kill(p, killer)
        p.alive = False
        p.trapped = False
        if p.death_t is None:
            p.death_t = self.time
        if self.soccer:
            p.respawn_t = SOCCER_RESPAWN
            if self.ball and self.ball["carrier"] == p.id:
                self.ball["carrier"] = None
                self.ball["x"], self.ball["y"] = p.x, p.y
        elif self.turf:
            p.respawn_t = 10.0
        elif self.infect:
            if p.infected:
                nz = sum(1 for q in self.players if q.infected)
                over_half = max(0, nz - len(self.players) // 2)
                p.respawn_t = min(7.0, 3.0 + over_half)  # 鬼群過半 → 復活變慢
            else:
                p.respawn_t = 3.0
                p._to_infect = True   # 復活後加入感染者

    def water_hit(self, p):
        """對玩家造成一次「水攻擊」判定(光盾免疫、坐騎擋刀、困住/戳破)。"""
        if not p.alive or p.shield_t > 0:
            return
        if p.trapped:
            if p.trap_elapsed > TRAP_GRACE:
                self.kill(p)
        elif p.mount is not None:
            p.mount = None
            p.shield_t = 1.2
        else:
            p.trapped = True
            p.trap_timer = TRAP_TIME
            p.trap_elapsed = 0.0
            p.ghost_t = 0.0
            p.hook_to = None
            p.frozen_t = 0.0

    # ---- 場地攻擊:轟炸機 / 企鵝衝鋒 ----
    def start_hazard(self):
        for _ in range(10):
            if random.random() < 0.5:
                # 轟炸機:沿隨機一列每隔兩格投彈
                rr = random.randint(1, ROWS - 2)
                off = random.randint(1, 2)
                tiles = [(rr, c) for c in range(off, COLS - 1, 2)
                         if self.grid[rr][c] != HARD]
                if len(tiles) < 3:
                    continue
                d = random.choice((1, -1))
                self.hazards.append(dict(kind="plane", state="warn", t=HAZARD_WARN,
                                         row=rr, tiles=tiles, dir=d,
                                         x=(-50.0 if d > 0 else SCREEN_W + 50.0)))
                return
            else:
                # 企鵝:沿隨機直線衝鋒(撞到硬牆為止)
                horiz = random.random() < 0.5
                if horiz:
                    rr = random.randint(1, ROWS - 2)
                    d = random.choice((1, -1))
                    c = 1 if d > 0 else COLS - 2
                    lane = []
                    while 0 < c < COLS - 1 and self.grid[rr][c] != HARD:
                        lane.append((rr, c))
                        c += d
                    vx, vy = d, 0
                else:
                    cc = random.randint(1, COLS - 2)
                    d = random.choice((1, -1))
                    r = 1 if d > 0 else ROWS - 2
                    lane = []
                    while 0 < r < ROWS - 1 and self.grid[r][cc] != HARD:
                        lane.append((r, cc))
                        r += d
                    vx, vy = 0, d
                if len(lane) < 4:
                    continue
                er, ec = lane[0]
                self.hazards.append(dict(kind="penguin", state="warn", t=HAZARD_WARN,
                                         tiles=lane, vx=vx, vy=vy,
                                         x=ec * TILE + TILE / 2.0,
                                         y=er * TILE + TILE / 2.0))
                return

    def update_hazard(self, hz, dt):
        """更新單一場地攻擊;結束時回傳 True。"""
        if hz["state"] == "warn":
            hz["t"] -= dt
            if hz["t"] <= 0:
                hz["state"] = "go"
            return False
        if hz["kind"] == "plane":
            hz["x"] += hz["dir"] * (SCREEN_W / 1.1) * dt
            for tile in list(hz["tiles"]):
                tx = tile[1] * TILE + TILE // 2
                passed = (hz["x"] >= tx) if hz["dir"] > 0 else (hz["x"] <= tx)
                if passed:
                    hz["tiles"].remove(tile)
                    r, c = tile
                    b = self.bubble_at(r, c)
                    if b is not None:
                        self.explode(b)          # 引爆現有水球
                    elif self.grid[r][c] == FLOOR:
                        nb = Bubble(r, c, None, 1)
                        self.bubbles.append(nb)
                        self.explode(nb)         # 立即十字爆炸
            if not hz["tiles"] and (hz["x"] < -60 or hz["x"] > SCREEN_W + 60):
                return True
        else:   # 企鵝
            hz["x"] += hz["vx"] * 8.0 * TILE * dt
            hz["y"] += hz["vy"] * 8.0 * TILE * dt
            r, c = int(hz["y"] // TILE), int(hz["x"] // TILE)
            if not (0 <= r < ROWS and 0 <= c < COLS) or self.grid[r][c] == HARD:
                return True
            if self.grid[r][c] == SOFT:          # 撞碎箱子(照常掉道具)
                self.grid[r][c] = FLOOR
                self.spawn_item(r, c)
                self.effects.append(dict(kind="ring", x=c * TILE + TILE // 2,
                                         y=r * TILE + TILE // 2, t=0.3, t0=0.3))
            for q in self.players:
                if q.alive and math.hypot(q.x - hz["x"], q.y - hz["y"]) < TILE * 0.8:
                    if not q.trapped:
                        q.env_tag = hz["kind"]
                        q.last_hit_by = None
                    self.water_hit(q)
        return False

    def apply_item(self, p, kind):
        """套用道具效果。"""
        if kind == "bubble":
            p.max_bubbles = min(8, p.max_bubbles + 1)
        elif kind == "potion":
            p.power = min(9, p.power + 1)
        elif kind == "shoe":
            p.speed = min(6.5, p.speed + 0.45)
        elif kind == "ultra":                 # 大力藥丸:威力全滿
            p.power = 9
        elif kind == "reddevil":              # 紅色惡魔:速度全滿
            p.speed = 6.5
        elif kind == "needle":
            p.needles = min(5, p.needles + 1)
        elif kind in ACTIVE_KINDS:
            if self.two_slot:
                # 連線雙槽制:優先槽(右)先填,再填備用槽(左)
                if p.slot_b is None:
                    p.slot_b = kind
                elif p.slot_a is None:
                    p.slot_a = kind
            else:
                # 本機單槽制:同種疊加(上限 3),不同種替換
                if p.item_kind == kind:
                    p.item_count = min(3, p.item_count + 1)
                else:
                    p.item_kind = kind
                    p.item_count = 1
        elif kind == "glove":
            p.has_glove = True
        elif kind == "kick":
            p.has_kick = True
        elif kind in ("turtle", "owl", "ufo"):
            p.mount = kind                    # 換乘新坐騎
        elif kind == "ghost":
            p.ghost_t = GHOST_TIME
        elif kind == "shield":
            p.shield_t = SHIELD_TIME
        elif kind == "radar":
            p.radar_t = RADAR_TIME
        elif kind == "devil":                 # 惡魔面具:詛咒
            p.curse_t = CURSE_TIME
            # 電腦中咒固定亂放水球;真人隨機二選一
            p.curse_kind = "auto" if p.is_bot else random.choice(["reverse", "auto"])
            p.curse_drop_t = 0.5

    # ---- 每幀更新 ----
    def update(self, dt, keys, events):
        if self.over:
            return
        self.time += dt

        # 開場倒數:凍結玩法,只讓動畫與特效活著
        if self.countdown > 0:
            # 足球:倒數期間就先完成開球佈陣(標記才會指向正確位置)
            if (self.soccer and not self._kickoff_done
                    and any(p.team is not None for p in self.players)):
                self._kickoff_done = True
                self.kickoff_reset(first=True)
            self.countdown -= dt
            if self.countdown <= 0:
                self.countdown = 0.0
                self.go_flash = 0.7
            for p in self.players:
                p.anim += dt
            for fx in list(self.effects):
                fx["t"] -= dt
                if fx["t"] <= 0:
                    self.effects.remove(fx)
            return
        if self.go_flash > 0:
            self.go_flash = max(0.0, self.go_flash - dt)

        # 事件:放球/用針 + 使用道具(僅本機真人玩家,鍵盤最多 4 組鍵位)
        for e in events:
            if e.type == pygame.JOYBUTTONDOWN:
                for p in self.players:
                    if p.pad_iid != e.instance_id or p.is_bot:
                        continue
                    if e.button == 0:
                        self.try_place_bubble(p)     # A:放球/用針/射門
                    elif e.button == 1:
                        self.use_dart(p)             # B:使用道具
                    elif e.button == 2:
                        self.use_skill(p)            # X:角色技能
                    elif e.button == 3:
                        self.swap_items(p)           # Y:對調道具槽
                    break
            if e.type == pygame.KEYDOWN:
                for p in self.players:
                    if p.is_bot or p.is_remote:
                        continue
                    if p.use_net_keys:
                        km = NET_KEYMAP
                    elif p.id < len(self.keymaps):
                        km = self.keymaps[p.id]
                    else:
                        continue
                    if e.key in km["action"]:
                        self.try_place_bubble(p)
                    elif e.key in km.get("use", []):
                        self.use_dart(p)
                    elif e.key in km.get("swap", []):
                        self.swap_items(p)
                    elif e.key in km.get("skill", []):
                        self.use_skill(p)

        # 狀態計時(隱形/無敵/雷達/詛咒/踢球冷卻)
        for p in self.players:
            if not p.alive:
                # 佔地模式:復活倒數 → 回出生點重生(短暫護盾)
                if (self.turf or self.infect or self.soccer) \
                        and p.respawn_t > 0:
                    p.respawn_t -= dt
                    if p.respawn_t <= 0:
                        p.respawn_t = 0.0
                        sr, sc = p.spawn
                        if self.grid[sr][sc] != FLOOR or self.bubble_at(sr, sc):
                            for (tr, tc) in [(sr + a, sc + b2)
                                             for a in (-1, 0, 1) for b2 in (-1, 0, 1)]:
                                if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                                        and self.grid[tr][tc] == FLOOR
                                        and self.bubble_at(tr, tc) is None):
                                    sr, sc = tr, tc
                                    break
                        p.alive = True
                        p.trapped = False
                        p.death_t = None
                        p.frozen_t = p.daze_t = p.wet_t = 0.0
                        p.curse_t = 0.0
                        p.shield_t = 2.0
                        p.x = sc * TILE + TILE / 2.0
                        p.y = sr * TILE + TILE / 2.0
                        if p._to_infect:
                            p._to_infect = False
                            self.convert(p)
                        self.effects.append(dict(kind="ring", x=p.x, y=p.y,
                                                 t=0.35, t0=0.35))
                continue
            p.ghost_t = max(0.0, p.ghost_t - dt)
            p.shield_t = max(0.0, p.shield_t - dt)
            p.radar_t = max(0.0, p.radar_t - dt)
            p.kick_cd = max(0.0, p.kick_cd - dt)
            p.frozen_t = max(0.0, p.frozen_t - dt)
            p.daze_t = max(0.0, p.daze_t - dt)
            p.skill_cd = max(0.0, p.skill_cd - dt)
            p.feat_cd = max(0.0, p.feat_cd - dt)
            p.multi_t = max(0.0, p.multi_t - dt)
            p.haste_t = max(0.0, p.haste_t - dt)
            p.wet_t = max(0.0, p.wet_t - dt)
            p.volt_t = max(0.0, p.volt_t - dt)
            if p.surge_t > 0:
                p.surge_t -= dt
                if p.surge_t <= 0:      # 特賣結束:恢復
                    p.surge_t = 0.0
                    p.power = max(1, p.power - 1)
                    p.max_bubbles = max(1, p.max_bubbles - 1)
            if not p.pos_hist or self.time - p.pos_hist[-1][0] >= 0.1:
                p.pos_hist.append((self.time, p.x, p.y))
            # 水靈:走過的格子留下水漬
            if p.trail_t > 0 and p.alive and not p.trapped:
                p.trail_t = max(0.0, p.trail_t - dt)
                tt = p.tile()
                if tt != p.last_trail:
                    p.last_trail = tt
                    self.puddles.append(dict(r=tt[0], c=tt[1], o=p.id, t=1.1))
            if p.curse_t > 0:
                p.curse_t -= dt
                if p.curse_kind == "auto" and not p.trapped:
                    p.curse_drop_t -= dt
                    if p.curse_drop_t <= 0:
                        p.curse_drop_t = 0.9
                        self.try_place_bubble(p)   # 詛咒:不受控亂放水球
                if p.curse_t <= 0:
                    p.curse_kind = None

        # 電腦 AI 決策
        for p in self.players:
            if not (p.is_bot and p.alive):
                continue
            if p.trapped:
                p.bot_dir = None
                # 被困住 → 稍微反應一下之後自動用針
                if p.needles > 0 and p.trap_elapsed > self.blv["rescue"]:
                    self.try_place_bubble(p)
                continue
            p.bot_dir = p.bot.drive(self, dt)
            if self.soccer:
                if self.ball is not None and self.ball["carrier"] == p.id:
                    p.bot.want_bomb = False   # 持球時按鍵=射門,交給足球腦決定
                # 決策快取:0.15 秒或狀態改變才重算,消除逐幀抖動
                key = (self.ball["carrier"] if self.ball else None,
                       bool(self.ball and self.ball.get("fly")))
                p.bot.soccer_t = getattr(p.bot, "soccer_t", 0.0) - dt
                if (getattr(p.bot, "soccer_key", None) != key
                        or p.bot.soccer_t <= 0):
                    p.bot.soccer_cache = bot_soccer(self, p)
                    p.bot.soccer_key = key
                    p.bot.soccer_t = self.blv["soccer"]
                sd2 = p.bot.soccer_cache
                if sd2 == "hold":
                    p.bot_dir = None          # 站樁(守門/接應定位)
                elif sd2 is not None:
                    p.bot_dir = sd2
            if (self.blv["err_p"] > 0 and p.bot_dir is not None
                    and random.random() < self.blv["err_p"] * dt * 3.0):
                p.bot_dir = None              # 初級電腦:偶爾遲疑發呆
            p.bot.gadget_t = getattr(p.bot, "gadget_t",
                                     random.random() * 0.3) - dt
            if p.bot.gadget_t <= 0:
                p.bot.gadget_t = self.blv["gadget"]
                if random.random() < self.blv["act_p"]:
                    bot_gadgets(self, p)
            if p.bot.want_bomb:
                self.try_place_bubble(p)
                p.bot.want_bomb = False
                p.bot.bomb_cd = (0.6 if self.boss_mode
                                 else self.blv["bomb_cd"])
                p.bot.think_timer = 0.0   # 放完立刻重新思考 → 逃離

        # 移動
        for p in self.players:
            p.update_move(keys, dt, self)
            p.anim += dt
            # ---- 場地機關互動 ----
            if p.alive and p.hook_to is None:
                spec = self.terrain.get(p.tile())
                if spec is not None:
                    kind = spec[0]
                    if kind == "belt" and not p.trapped:
                        bdx, bdy = spec[3], spec[4]
                        # 玩家想往垂直方向離開時,履帶讓路(可從側邊走出)
                        perp = (("up", "down") if bdy == 0
                                else ("left", "right"))
                        if not any(d in p.want_dirs for d in perp):
                            amt = 2.3 * TILE * dt
                            nx = p.x + bdx * amt
                            ny = p.y + bdy * amt
                            tr, tc = int(ny // TILE), int(nx // TILE)
                            if (tr, tc) == p.tile() or self.passable(tr, tc, p):
                                p.x, p.y = nx, ny
                    elif kind == "cannon" and p.feat_cd <= 0 and not p.trapped:
                        dx, dy, dist = spec[3], spec[4], spec[5]
                        r0, c0 = spec[1], spec[2]
                        for i in range(dist, 0, -1):
                            tr, tc = r0 + dy * i, c0 + dx * i
                            if not (0 < tr < ROWS - 1 and 0 < tc < COLS - 1):
                                continue
                            if self.grid[tr][tc] == HARD:
                                continue
                            if self.bubble_at(tr, tc) is not None:
                                continue
                            if self.grid[tr][tc] == SOFT:
                                # 砲彈直接砸碎落點的箱子(照常掉道具)
                                self.grid[tr][tc] = FLOOR
                                self.spawn_item(tr, tc)
                                self.effects.append(dict(
                                    kind="ring", x=tc * TILE + TILE // 2,
                                    y=tr * TILE + TILE // 2, t=0.35, t0=0.35))
                            p.hook_to = (tc * TILE + TILE / 2.0,
                                         tr * TILE + TILE / 2.0)
                            p.feat_cd = 1.2
                            self.effects.append(dict(kind="ring",
                                                     x=p.x, y=p.y,
                                                     t=0.3, t0=0.3))
                            break
                    elif kind == "portal" and p.feat_cd <= 0:
                        pid = spec[3]
                        for (tr, tc), sp2 in self.terrain.items():
                            if (sp2[0] == "portal" and sp2[3] == pid
                                    and (tr, tc) != p.tile()):
                                if self.bubble_at(tr, tc) is None:
                                    self.effects.append(dict(
                                        kind="ring", x=p.x, y=p.y,
                                        t=0.3, t0=0.3))
                                    p.x = tc * TILE + TILE / 2.0
                                    p.y = tr * TILE + TILE / 2.0
                                    p.feat_cd = 1.2
                                    self.effects.append(dict(
                                        kind="ring", x=p.x, y=p.y,
                                        t=0.35, t0=0.35))
                                break
                    elif kind == "spring" and p.feat_cd <= 0 and not p.trapped:
                        # 彈跳墊:站上中心 → 朝面向彈飛 2 格(可越過障礙)
                        r0, c0 = spec[1], spec[2]
                        cx0 = c0 * TILE + TILE / 2.0
                        cy0 = r0 * TILE + TILE / 2.0
                        if abs(p.x - cx0) < TILE * 0.3 and abs(p.y - cy0) < TILE * 0.3:
                            sdx, sdy = DIRS[p.facing]
                            for i in (2, 1):
                                tr, tc = r0 + sdy * i, c0 + sdx * i
                                if (0 < tr < ROWS - 1 and 0 < tc < COLS - 1
                                        and self.grid[tr][tc] == FLOOR
                                        and self.bubble_at(tr, tc) is None):
                                    p.hook_to = (tc * TILE + TILE / 2.0,
                                                 tr * TILE + TILE / 2.0)
                                    p.feat_cd = 0.9
                                    self.effects.append(dict(
                                        kind="ring", x=p.x, y=p.y,
                                        t=0.25, t0=0.25))
                                    break
                    elif kind == "switch" and p.feat_cd <= 0:
                        # 壓力開關:切換同組閘門(有人/水球/崩塌的格子不關)
                        r0, c0 = spec[1], spec[2]
                        cx0 = c0 * TILE + TILE / 2.0
                        cy0 = r0 * TILE + TILE / 2.0
                        if abs(p.x - cx0) < TILE * 0.3 and abs(p.y - cy0) < TILE * 0.3:
                            gid = spec[3]
                            self.gate_state[gid] = not self.gate_state.get(gid, True)
                            closed = self.gate_state[gid]
                            for (tr, tc), sp2 in self.terrain.items():
                                if sp2[0] != "gate" or sp2[3] != gid:
                                    continue
                                if (tr, tc) in self.sd_locked:
                                    continue
                                if closed:
                                    if (self.grid[tr][tc] == FLOOR
                                            and self.bubble_at(tr, tc) is None
                                            and not any(q.alive and q.tile() == (tr, tc)
                                                        for q in self.players)):
                                        self.grid[tr][tc] = HARD
                                else:
                                    if self.grid[tr][tc] == HARD:
                                        self.grid[tr][tc] = FLOOR
                                self.effects.append(dict(
                                    kind="ring", x=tc * TILE + TILE // 2,
                                    y=tr * TILE + TILE // 2, t=0.25, t0=0.25))
                            p.feat_cd = 0.8

        # 水球:滑行、乘客判定、倒數引爆
        for b in list(self.bubbles):
            # 履帶運送:未滑行的水球被緩緩推走(約 2.3 格/秒)
            if b.slide is None:
                bspec = self.terrain.get((b.r, b.c))
                if bspec is not None and bspec[0] == "belt":
                    b.belt_t += dt
                    if b.belt_t >= 0.43:
                        b.belt_t = 0.0
                        bdx, bdy = bspec[3], bspec[4]
                        nr, nc = b.r + bdy, b.c + bdx
                        if (0 <= nr < ROWS and 0 <= nc < COLS
                                and self.grid[nr][nc] == FLOOR
                                and self.bubble_at(nr, nc) is None
                                and not any(q.alive and q.tile() == (nr, nc)
                                            for q in self.players)):
                            b.r, b.c = nr, nc
                            if (nr, nc) in self.blasts:   # 被推進水柱 → 連鎖
                                self.explode(b)
                                continue
                else:
                    b.belt_t = 0.0
            # 被踢出去的水球滑行
            if b.slide is not None:
                b.slide_t += dt
                while b.slide is not None and b.slide_t >= 0.085:
                    b.slide_t -= 0.085
                    dx, dy = b.slide
                    nr, nc = b.r + dy, b.c + dx
                    blocked = (not (0 <= nr < ROWS and 0 <= nc < COLS)
                               or self.grid[nr][nc] != FLOOR
                               or self.bubble_at(nr, nc) is not None
                               or any(q.alive and q.tile() == (nr, nc)
                                      for q in self.players))
                    if blocked:
                        b.slide = None
                        break
                    b.r, b.c = nr, nc
                    if b.curve is not None and not b.curve["turned"]:
                        b.curve["steps"] += 1
                        if b.curve["steps"] >= 2:
                            b.curve["turned"] = True
                            cdx, cdy = b.slide
                            # 轉彎:優先選開放的一側
                            for ndx, ndy in ((-cdy, cdx), (cdy, -cdx)):
                                nr2, nc2 = b.r + ndy, b.c + ndx
                                if (0 <= nr2 < ROWS and 0 <= nc2 < COLS
                                        and self.grid[nr2][nc2] == FLOOR
                                        and self.bubble_at(nr2, nc2) is None):
                                    b.slide = (ndx, ndy)
                                    break
                            else:
                                b.slide = (-cdy, cdx)
                    if (nr, nc) in self.blasts:    # 滑進水柱 → 連鎖
                        self.explode(b)
                        break
            if b not in self.bubbles:
                continue
            for pid in list(b.riders):
                q = self.players[pid]
                if q.tile() != (b.r, b.c):
                    b.riders.discard(pid)
            b.timer -= dt
            if b.timer <= 0:
                self.explode(b)

        # 水柱倒數
        for t in list(self.blasts):
            self.blasts[t] -= dt
            if self.blasts[t] <= 0:
                del self.blasts[t]

        # 飛彈:飛行 → 命中牆/箱/水球/玩家 → 十字爆炸
        for ms in list(self.missiles):
            ms["x"] += ms["dx"] * 9.0 * TILE * dt
            ms["y"] += ms["dy"] * 9.0 * TILE * dt
            r, c = int(ms["y"] // TILE), int(ms["x"] // TILE)
            hit = None
            if not (0 <= r < ROWS and 0 <= c < COLS) or self.grid[r][c] == HARD:
                hit = "wall"
            elif self.grid[r][c] == SOFT:
                hit = "box"
            else:
                b = self.bubble_at(r, c)
                if b is not None:
                    hit = b
                else:
                    for q in self.players:
                        if (q is not ms["owner"] and q.alive
                                and math.hypot(q.x - ms["x"], q.y - ms["y"])
                                < TILE * 0.5):
                            hit = "player"
                            break
            if hit is None:
                continue
            self.missiles.remove(ms)
            if isinstance(hit, Bubble):
                self.explode(hit)             # 直接引爆那顆水球
                continue
            # 撞牆/箱子:在前一格爆;撞玩家:原地爆
            er, ec = r, c
            if hit in ("wall", "box"):
                er, ec = r - ms["dy"], c - ms["dx"]
            if not (0 <= er < ROWS and 0 <= ec < COLS) \
                    or self.grid[er][ec] != FLOOR:
                continue
            nb = Bubble(er, ec, ms["owner"], 2)
            self.bubbles.append(nb)
            self.explode(nb)

        # 水柱判定:光盾免疫 → 坐騎擋刀 → 困住 / 戳破
        for p in self.players:
            if not p.alive:
                continue
            in_blast = p.tile() in self.blasts
            if p.trapped:
                p.trap_timer -= dt
                p.trap_elapsed += dt
                if in_blast and p.trap_elapsed > TRAP_GRACE:
                    ko = self.blast_owner.get(p.tile())
                    if isinstance(ko, int):
                        p.last_hit_by = ko
                        p.env_tag = None
                    elif ko is not None:
                        p.env_tag = ko
                    self.kill(p)          # 困住時再被炸 → 直接破
                elif p.trap_timer <= 0:
                    self.kill(p)          # 倒數結束 → 破
            elif in_blast:
                if p.shield_t > 0:
                    pass                  # 無敵光盾:完全免疫
                elif p.mount is not None:
                    p.mount = None        # 坐騎替你擋下這一發
                    p.shield_t = 1.2      # 短暫無敵避免連續判定
                else:
                    src_o = self.blast_owner.get(p.tile())
                    if isinstance(src_o, int):
                        p.last_hit_by = src_o
                        p.env_tag = None
                    else:
                        p.last_hit_by = None
                        p.env_tag = src_o
                    p.trapped = True
                    p.trap_timer = TRAP_TIME
                    p.trap_elapsed = 0.0
                    p.ghost_t = 0.0       # 被困住就現形
                    p.hook_to = None      # 中斷鉤爪飛行
                    p.frozen_t = 0.0      # 冰凍狀態解除(改為被困)

        # 玩家碰撞:對戰=戳破被困者;Boss/同隊=救援
        for p in self.players:
            if not (p.alive and p.trapped):
                continue
            for q in self.players:
                if q is p or not q.alive or q.trapped:
                    continue
                if math.hypot(p.x - q.x, p.y - q.y) < TILE * 0.7:
                    same_team = (p.team is not None and p.team == q.team)
                    if self.boss_mode or same_team:
                        p.trapped = False          # 隊友救援!
                        p.shield_t = max(p.shield_t, 1.0)
                        self.effects.append(dict(kind="ring", x=p.x, y=p.y,
                                                 t=0.35, t0=0.35))
                    else:
                        self.kill(p, killer=q)
                    break

        # 撿道具(騎飛碟時撿不到)
        for p in self.players:
            if not p.alive or p.trapped or p.mount == "ufo":
                continue
            t = p.tile()
            if t in self.items:
                kind = self.items[t]
                if (self.two_slot and kind in ACTIVE_KINDS
                        and p.slot_a is not None and p.slot_b is not None):
                    continue          # 兩格都滿 → 撿不起來,道具留在原地
                self.apply_item(p, self.items.pop(t))

        # 場地隨機刷道具(原版風格)
        self.item_spawn_t -= dt
        if self.item_spawn_t <= 0:
            self.item_spawn_t = random.uniform(*FIELD_SPAWN_EVERY)
            self.spawn_field_item()

        # ---- 對戰/組隊:限時與場地崩塌 ----
        if self.match_left is not None:
            # 場地攻擊排程(可併發,上限 4 個;崩塌開始後不再觸發新事件)
            self.hazard_t -= dt
            if (not self.soccer
                    and self.hazard_t <= 0 and self.match_left > SD_START
                    and len(self.hazards) < 4):
                self.hazard_t = random.uniform(*HAZARD_EVERY)
                self.start_hazard()
                if random.random() < 0.35 and len(self.hazards) < 4:
                    self.start_hazard()      # 雙重事件!
            for hz in list(self.hazards):
                if self.update_hazard(hz, dt):
                    self.hazards.remove(hz)
            self.match_left -= dt
            if self.match_left <= 0:
                self.over = True
                if self.soccer:
                    a, b2 = self.scores
                    self.winner = ("team0" if a > b2
                                   else ("team1" if b2 > a else None))
                elif self.infect:
                    self.winner = ("humans"
                                   if any(not p.infected for p in self.players)
                                   else "infected")
                elif self.turf:
                    n0 = sum(1 for v in self.paint.values() if v == 0)
                    n1 = sum(1 for v in self.paint.values() if v == 1)
                    self.turf_result = (n0, n1)
                    self.winner = ("team0" if n0 > n1
                                   else ("team1" if n1 > n0 else None))
                else:
                    self.winner = None        # 時間到 → 平手
                return

            # ---- 終局狂熱四階段(佔地/足球停用) ----
            if self.turf or self.soccer:
                pass
            elif not self.fever and self.match_left <= SD_START:
                self.fever = True
                self.announce = dict(key="fever", t=2.2, t0=2.2)
            if self.fever and self.match_left <= RAIN_START:
                self.rain_t -= dt
                if self.rain_t <= 0:
                    self.rain_t = RAIN_EVERY
                    if len(self.items) + len(self.drops) < FIELD_ITEM_CAP + 8:
                        spots = [(r, c) for r in range(1, ROWS - 1)
                                 for c in range(1, COLS - 1)
                                 if self.grid[r][c] == FLOOR
                                 and (r, c) not in self.items
                                 and (r, c) not in self.falling
                                 and self.bubble_at(r, c) is None]
                        if spots:
                            rr, cc = random.choice(spots)
                            kind = random.choices(self.pool_kinds,
                                                  self.pool_weights)[0]
                            self.drops.append(dict(r=rr, c=cc, t=0.8, k=kind))
            if self.fever and not self.sd_fast and self.match_left <= SD_FAST_AT:
                self.sd_fast = True
                self.sd_interval = SD_FAST_INTERVAL
                self.announce = dict(key="collapse", t=2.0, t0=2.0)
            if self.fever and not self.final_boost and self.match_left <= FINAL_AT:
                self.final_boost = True
                for q in self.players:
                    if q.alive:
                        q.power = min(9, q.power + 1)
                self.announce = dict(key="final", t=2.0, t0=2.0)

            # 空投道具落地
            for dp in list(self.drops):
                dp["t"] -= dt
                if dp["t"] <= 0:
                    self.drops.remove(dp)
                    t2 = (dp["r"], dp["c"])
                    if (self.grid[dp["r"]][dp["c"]] == FLOOR
                            and t2 not in self.items):
                        self.items[t2] = dp["k"]
                        self.effects.append(dict(
                            kind="ring", x=dp["c"] * TILE + TILE // 2,
                            y=dp["r"] * TILE + TILE // 2, t=0.3, t0=0.3))
            if (self.match_left <= SD_START and self.sd_queue
                    and not self.turf and not self.soccer):
                self.sd_timer -= dt
                if self.sd_timer <= 0:
                    self.sd_timer = self.sd_interval
                    t = self.sd_queue.pop(0)
                    if self.grid[t[0]][t[1]] != HARD:
                        self.falling[t] = SD_WARN
            for t in list(self.falling):
                self.falling[t] -= dt
                if self.falling[t] <= 0:
                    del self.falling[t]
                    r, c = t
                    if self.grid[r][c] == HARD:
                        continue
                    self.grid[r][c] = HARD    # 磚塊落地
                    self.sd_locked.add((r, c))
                    self.items.pop(t, None)
                    self.blasts.pop(t, None)
                    b = self.bubble_at(r, c)
                    if b is not None:
                        self.bubbles.remove(b)
                    for p in self.players:    # 被壓到直接淘汰(無敵也擋不住)
                        if p.alive and p.tile() == t:
                            p.env_tag = "fall"
                            p.last_hit_by = None
                            self.kill(p)
                    self.effects.append(dict(kind="ring", x=c * TILE + TILE // 2,
                                             y=r * TILE + TILE // 2, t=0.3, t0=0.3))

        # ---- 章魚王 Boss 模式 ----
        if self.boss is not None:
            self.boss.update(self, dt)

            # 落點預警 → 生成章魚王的水球(短引信)
            for m in list(self.incoming):
                m[2] -= dt
                if m[2] <= 0:
                    self.incoming.remove(m)
                    r, c = m[0], m[1]
                    if self.grid[r][c] == FLOOR and self.bubble_at(r, c) is None:
                        nb = Bubble(r, c, self.boss,
                                    self.boss.cfg["epw"] if self.boss.enraged()
                                    else self.boss.cfg["pw"])
                        nb.timer = 1.4
                        for q in self.players:
                            if q.alive and q.tile() == (r, c):
                                nb.riders.add(q.id)
                        self.bubbles.append(nb)

            # 小章魚:移動、被水柱炸死
            for mn in list(self.minions):
                mn.update(self, dt)
                if mn.tile() in self.blasts:
                    self.minions.remove(mn)
                    self.effects.append(dict(kind="ring", x=mn.x, y=mn.y,
                                             t=0.35, t0=0.35))

            # 接觸死亡:碰到怪物立即死亡(被困者除外;光盾可防)
            brect = self.boss.rect().inflate(-14, -14)
            for p in self.players:
                if not p.alive or p.trapped or p.shield_t > 0:
                    continue
                if brect.collidepoint(p.x, p.y):
                    p.env_tag = "boss"
                    p.last_hit_by = None
                    self.kill(p)
                    continue
                for mn in self.minions:
                    if math.hypot(p.x - mn.x, p.y - mn.y) < TILE * 0.62:
                        p.env_tag = "minion"
                        p.last_hit_by = None
                        self.kill(p)
                        break

        # 守護者的臨時石牆倒數
        for t in list(self.temp_walls):
            self.temp_walls[t] -= dt
            if self.temp_walls[t] <= 0:
                del self.temp_walls[t]
                r, c = t
                if self.grid[r][c] == HARD:   # 沒被崩塌覆蓋才還原
                    self.grid[r][c] = FLOOR
                    self.effects.append(dict(kind="ring",
                                             x=c * TILE + TILE // 2,
                                             y=r * TILE + TILE // 2,
                                             t=0.25, t0=0.25))

        # 空襲信標:倒數與轟炸
        for st in list(self.strikes):
            st["t"] -= dt
            if st["t"] > 0:
                continue
            self.strikes.remove(st)
            sr, sc = st["r"], st["c"]
            if self.grid[sr][sc] == HARD:
                continue
            if self.grid[sr][sc] == SOFT:
                self.grid[sr][sc] = FLOOR
                self.spawn_item(sr, sc)
            hb = self.bubble_at(sr, sc)
            if hb is not None:
                self.explode(hb)
            self.blasts[(sr, sc)] = max(self.blasts.get((sr, sc), 0), 0.45)
            if st.get("owner") is not None:
                for _bt in list(self.blasts):
                    if _bt == (sr, sc) or (abs(_bt[0]-sr)+abs(_bt[1]-sc)) <= 2:
                        self.blast_owner[_bt] = st["owner"]

        # 捕獸夾:倒數與觸發
        for tp in list(self.traps):
            tp["t"] -= dt
            if tp["t"] <= 0:
                self.traps.remove(tp)
                continue
            for q in self.players:
                if not q.alive or q.trapped or q.id == tp["o"]:
                    continue
                ow = next((z for z in self.players if z.id == tp["o"]), None)
                if ow is not None and ow.team is not None and q.team == ow.team:
                    continue
                if self.boss_mode:
                    continue
                if q.tile() == (tp["r"], tp["c"]):
                    q.frozen_t = max(q.frozen_t, 1.5)
                    self.traps.remove(tp)
                    self.effects.append(dict(kind="snap", x=int(q.x), y=int(q.y),
                                             t=0.4, t0=0.4))
                    break

        # 水漬:倒數與觸發(踩到 → 被泡)
        for pd in list(self.puddles):
            pd["t"] -= dt
            if pd["t"] <= 0:
                self.puddles.remove(pd)
                continue
            for q in self.players:
                if not q.alive or q.trapped or q.id == pd["o"]:
                    continue
                ow = next((z for z in self.players if z.id == pd["o"]), None)
                if ow is not None and ow.team is not None and q.team == ow.team:
                    continue
                if self.boss_mode:
                    continue
                if q.tile() == (pd["r"], pd["c"]):
                    if q.shield_t > 0:
                        continue
                    self.puddles.remove(pd)
                    q.wet_t = max(q.wet_t, 2.2)
                    self.effects.append(dict(kind="aqua", x=int(q.x), y=int(q.y),
                                             t=0.4, t0=0.4))
                    break

        # 足球模式:開球佈陣、撿球、進球判定
        if self.soccer:
            if not self._kickoff_done:
                self._kickoff_done = True
                self.kickoff_reset(first=True)
            if self.goal_pause > 0:
                self.goal_pause -= dt
                if self.goal_pause <= 0:
                    self.goal_pause = 0.0
                    self.kickoff_reset()
            elif self.ball is not None:
                b = self.ball
                if b.get("fly"):
                    fdx, fdy = b["fly"]
                    step = SHOOT_SPEED * TILE * dt
                    b["x"] += fdx * step
                    b["y"] += fdy * step
                    b["dist"] = b.get("dist", 0.0) + step
                    br = int(b["y"] // TILE)
                    bc = int(b["x"] // TILE)
                    goal_all = self.goal_tiles[0] | self.goal_tiles[1]
                    landed = False
                    if (not (0 <= br < ROWS and 0 <= bc < COLS)
                            or (self.grid[br][bc] != FLOOR
                                and (br, bc) not in goal_all)):
                        b["x"] -= fdx * step        # 撞牆/箱:停在前一格
                        b["y"] -= fdy * step
                        landed = True
                    else:
                        for gi, tiles in enumerate(self.goal_tiles):
                            if (br, bc) in tiles:
                                if gi == 1 - b.get("team", 0):
                                    self._score_goal(b.get("team", 0))
                                    b = None
                                else:
                                    landed = True   # 射自家門:球停門內
                                break
                        if b is not None:
                            for q in self.players:
                                if not (q.alive and not q.trapped):
                                    continue
                                if (q.id == b.get("shooter")
                                        and b["dist"] < TILE * 1.2):
                                    continue
                                if math.hypot(q.x - b["x"],
                                              q.y - b["y"]) < TILE * 0.55:
                                    b["carrier"] = q.id   # 傳球/攔截
                                    landed = True
                                    self.effects.append(dict(
                                        kind="ring", x=q.x, y=q.y,
                                        t=0.25, t0=0.25))
                                    break
                    if b is not None and (landed
                                          or b["dist"] >= SHOOT_RANGE * TILE):
                        b.pop("fly", None)
                        b.pop("shooter", None)
                        b["dist"] = 0.0
                elif b["carrier"] is None:
                    for q in self.players:
                        if (q.alive and not q.trapped
                                and math.hypot(q.x - b["x"], q.y - b["y"])
                                < TILE * 0.6):
                            b["carrier"] = q.id
                            self.effects.append(dict(kind="ring",
                                                     x=q.x, y=q.y,
                                                     t=0.25, t0=0.25))
                            break
                else:
                    car = next((q for q in self.players
                                if q.id == b["carrier"]), None)
                    if car is None or not car.alive:
                        b["carrier"] = None
                    else:
                        b["x"], b["y"] = car.x, car.y
                        if car.team is not None:
                            enemy_goal = self.goal_tiles[1 - (car.team % 2)]
                            if car.tile() in enemy_goal:
                                self.scores[car.team % 2] += 1
                                self.goal_pause = GOAL_PAUSE
                                b["carrier"] = None
                                b["x"] = COLS // 2 * TILE + TILE / 2.0
                                b["y"] = ROWS // 2 * TILE + TILE / 2.0
                                self.announce = dict(
                                    key="goal%d" % (car.team % 2),
                                    t=GOAL_PAUSE, t0=GOAL_PAUSE)

        # 感染模式:最後的生存者覺醒
        if self.infect and self.outbreak:
            humans = [p for p in self.players if not p.infected]
            if len(humans) == 1 and not getattr(humans[0], "last_stand", False):
                h = humans[0]
                h.last_stand = True
                h.shield_t = max(h.shield_t, 3.0)
                self.announce = dict(key="laststand", t=2.2, t0=2.2)

        # 感染模式:開場 3 秒疫情爆發
        if self.infect and not self.outbreak and self.time >= 3.0:
            self.outbreak = True
            cand = [p for p in self.players if p.alive]
            if cand:
                self.convert(random.choice(cand))
            self.announce = dict(key="outbreak", t=2.4, t0=2.4)

        # 終局宣告倒數
        if self.announce is not None:
            self.announce["t"] -= dt
            if self.announce["t"] <= 0:
                self.announce = None

        # 播報欄倒數
        for fe in list(self.feed):
            fe["t"] -= dt
            if fe["t"] <= 0:
                self.feed.remove(fe)

        # 特效倒數
        for fx in list(self.effects):
            fx["t"] -= dt
            if fx["t"] <= 0:
                self.effects.remove(fx)

        # 勝負判定
        if self.boss_mode:
            if self.boss.hp <= 0:
                self.over = True
                self.winner = "boss_win"       # 討伐成功
            elif not any(p.alive for p in self.players):
                self.over = True
                self.winner = "boss_lose"      # 全軍覆沒
            return
        if self.soccer:
            return                      # 足球:只由時間決定勝負
        if self.infect:
            if self.outbreak and all(p.infected for p in self.players):
                self.over = True
                self.winner = "infected"
            return
        if self.turf:
            return                      # 佔地模式:只由時間決定勝負
        alive = [p for p in self.players if p.alive]
        teams_on = any(p.team is not None for p in self.players)
        if teams_on:
            alive_teams = {p.team for p in alive}
            if len(alive_teams) <= 1:
                self.over = True
                if alive_teams:
                    self.winner = "team%d" % alive_teams.pop()
                else:
                    self.winner = None      # 同歸於盡 → 平手
            return
        if len(alive) <= 1:
            self.over = True
            self.winner = alive[0] if alive else None

    # ------------------------------------------------------------------
    # 繪圖
    # ------------------------------------------------------------------
    def draw(self, s):
        col_cfg = self.map_cfg["colors"]
        # 地板(烘焙貼圖:受光漸層 + 噪點),再疊上方塊投下的柔影
        art = self.art
        for r in range(ROWS):
            for c in range(COLS):
                s.blit(art["fa"] if (r + c) % 2 == 0 else art["fb"],
                       (c * TILE, r * TILE))
        for r in range(1, ROWS):
            for c in range(COLS):
                if self.grid[r][c] == FLOOR and self.grid[r - 1][c] != FLOOR:
                    s.blit(art["shadow"], (c * TILE, r * TILE))

        # 足球:場地標線 + 球門
        if self.soccer:
            mid = COLS // 2 * TILE + TILE // 2
            line_s = pygame.Surface((4, (ROWS - 2) * TILE), pygame.SRCALPHA)
            line_s.fill((255, 255, 255, 70))
            s.blit(line_s, (mid - 2, TILE))
            circ = pygame.Surface((TILE * 3, TILE * 3), pygame.SRCALPHA)
            pygame.draw.circle(circ, (255, 255, 255, 70),
                               (TILE * 3 // 2, TILE * 3 // 2),
                               TILE * 3 // 2 - 4, 4)
            s.blit(circ, (mid - TILE * 3 // 2,
                          ROWS // 2 * TILE + TILE // 2 - TILE * 3 // 2))
            for gi, tiles in enumerate(self.goal_tiles):
                gcol = ((235, 80, 80) if gi == 0 else (80, 130, 240))
                for (gr, gc) in tiles:
                    gx, gy = gc * TILE, gr * TILE
                    glow = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
                    glow.fill((*gcol, 46))
                    s.blit(glow, (gx, gy))
                    for k in range(1, 4):       # 球網
                        pygame.draw.line(s, (235, 240, 250),
                                         (gx, gy + k * TILE // 4),
                                         (gx + TILE, gy + k * TILE // 4), 1)
                        pygame.draw.line(s, (235, 240, 250),
                                         (gx + k * TILE // 4, gy),
                                         (gx + k * TILE // 4, gy + TILE), 1)
                    pygame.draw.rect(s, gcol, (gx, gy, TILE, TILE), 2)

        # 佔地模式:漆面
        if self.turf:
            for (r, c), tix in self.paint.items():
                if self.grid[r][c] == FLOOR:
                    s.blit(art["paint0" if tix == 0 else "paint1"],
                           (c * TILE, r * TILE))

        # 地板點綴(花叢/草叢/貝殼…)
        for (kind, r, c) in self.deco:
            if kind in DECO_FLOOR and self.grid[r][c] == FLOOR:
                draw_deco(s, kind, c * TILE, r * TILE, self.time)

        # ---- 場地機關(緊貼地板繪製,墊在水柱/方塊/落石之下) ----
        for (r, c), spec in self.terrain.items():
            if self.grid[r][c] != FLOOR:
                continue          # 被落石/築牆覆蓋 → 機關不再顯示(閘門另畫)
            x, y = c * TILE, r * TILE
            fk = spec[0]
            if fk == "belt":
                dx, dy = spec[3], spec[4]
                pygame.draw.rect(s, (52, 56, 68), (x + 3, y + 3, TILE - 6, TILE - 6),
                                 border_radius=6)
                pygame.draw.rect(s, (92, 96, 110), (x + 3, y + 3, TILE - 6, TILE - 6),
                                 2, border_radius=6)
                off = (self.time * 26) % 16
                cxm, cym = x + TILE // 2, y + TILE // 2
                for k in (-1, 0, 1):
                    ax = cxm + dx * (k * 16 + off - 8)
                    ay = cym + dy * (k * 16 + off - 8)
                    if abs(ax - cxm) <= 16 and abs(ay - cym) <= 16:
                        pygame.draw.polygon(s, (255, 214, 90), [
                            (ax + dx * 6, ay + dy * 6),
                            (ax - dx * 3 + dy * 6, ay - dy * 3 + dx * 6),
                            (ax - dx * 3 - dy * 6, ay - dy * 3 - dx * 6)])
            elif fk == "mud":
                pygame.draw.ellipse(s, (74, 92, 56), (x + 3, y + 6, TILE - 6, TILE - 10))
                pygame.draw.ellipse(s, (56, 72, 42), (x + 3, y + 6, TILE - 6, TILE - 10), 2)
                for k in range(3):
                    bx = x + 12 + k * 12
                    by = y + 16 + int(4 * math.sin(self.time * 2 + k * 2 + r + c))
                    pygame.draw.circle(s, (104, 124, 80), (bx, by), 3)
            elif fk == "spring":
                cxm, cym = x + TILE // 2, y + TILE // 2
                squish = 1.0 + 0.12 * math.sin(self.time * 5 + r + c)
                pygame.draw.ellipse(s, (196, 90, 90),
                                    (cxm - 15, cym - int(9 * squish), 30,
                                     int(18 * squish)))
                pygame.draw.ellipse(s, (240, 150, 140),
                                    (cxm - 15, cym - int(9 * squish), 30, 8))
                pygame.draw.ellipse(s, (140, 56, 60),
                                    (cxm - 15, cym - int(9 * squish), 30,
                                     int(18 * squish)), 2)
                for k in range(3):
                    yy = cym + 4 + k * 3
                    pygame.draw.line(s, (120, 124, 136),
                                     (cxm - 9 + k, yy), (cxm + 9 - k, yy), 2)
            elif fk == "switch":
                cxm, cym = x + TILE // 2, y + TILE // 2
                pressed = any(q.alive and q.tile() == (r, c)
                              for q in self.players)
                pygame.draw.circle(s, (96, 100, 112), (cxm, cym), 15)
                pygame.draw.circle(s, (60, 64, 76), (cxm, cym), 15, 2)
                bc = (240, 200, 90) if not pressed else (190, 150, 60)
                pygame.draw.circle(s, bc, (cxm, cym + (2 if pressed else 0)),
                                   9)
                pygame.draw.circle(s, (120, 96, 40),
                                   (cxm, cym + (2 if pressed else 0)), 9, 2)
            elif fk == "gate":
                # 開啟狀態:地板上的軌道板(關閉狀態在方塊層另畫)
                pygame.draw.rect(s, (110, 116, 130),
                                 (x + 6, y + 6, TILE - 12, TILE - 12), 2,
                                 border_radius=4)
                for k in (14, 24, 34):
                    pygame.draw.circle(s, (110, 116, 130), (x + k, y + TILE // 2), 2)
            elif fk == "ice":
                pygame.draw.rect(s, (196, 228, 248), (x + 2, y + 2, TILE - 4, TILE - 4),
                                 border_radius=8)
                pygame.draw.rect(s, (150, 196, 230), (x + 2, y + 2, TILE - 4, TILE - 4),
                                 2, border_radius=8)
                sh = int((self.time * 34 + (r * 7 + c * 11) % 30) % (TILE + 22)) - 14
                pygame.draw.line(s, (240, 250, 255), (x + sh, y + 6),
                                 (x + sh + 10, y + TILE - 6), 3)
                pygame.draw.line(s, (226, 242, 252), (x + sh + 14, y + 6),
                                 (x + sh + 20, y + TILE - 6), 2)
            elif fk == "cannon":
                dx, dy = spec[3], spec[4]
                cxm, cym = x + TILE // 2, y + TILE // 2
                pygame.draw.circle(s, (88, 92, 104), (cxm, cym), 16)
                pygame.draw.circle(s, (56, 60, 72), (cxm, cym), 16, 3)
                bl = pygame.Rect(0, 0, 14 + abs(dx) * 10, 14 + abs(dy) * 10)
                bl.center = (cxm + dx * 12, cym + dy * 12)
                pygame.draw.rect(s, (66, 70, 82), bl, border_radius=4)
                pygame.draw.circle(s, (120, 126, 140), (cxm, cym), 6)
            elif fk == "portal":
                pid = spec[3]
                col = (200, 120, 255) if pid == 0 else (90, 220, 230)
                cxm, cym = x + TILE // 2, y + TILE // 2
                for k in range(6):
                    ang = self.time * 3 + k * math.pi / 3
                    pygame.draw.circle(s, col,
                                       (int(cxm + 13 * math.cos(ang)),
                                        int(cym + 13 * math.sin(ang))), 3)
                pygame.draw.circle(s, col, (cxm, cym), 17, 2)

        # 水靈的水漬(淡藍漣漪)
        for pd in self.puddles:
            px = pd["c"] * TILE + TILE // 2
            py = pd["r"] * TILE + TILE // 2
            frac = max(0.0, min(1.0, pd["t"] / 1.1))
            surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
            pygame.draw.circle(surf, (140, 200, 250, int(120 * frac)),
                               (TILE // 2, TILE // 2), TILE // 2 - 6)
            pygame.draw.circle(surf, (220, 240, 255, int(160 * frac)),
                               (TILE // 2, TILE // 2),
                               int((TILE // 2 - 4) * (1.2 - frac)), 2)
            s.blit(surf, (pd["c"] * TILE, pd["r"] * TILE))

        # 獵人的捕獸夾(半隱形微光)
        for tp in self.traps:
            px = tp["c"] * TILE + TILE // 2
            py = tp["r"] * TILE + TILE // 2
            gl = 40 + int(24 * math.sin(self.time * 4 + tp["r"]))
            surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
            pygame.draw.circle(surf, (200, 210, 230, gl),
                               (TILE // 2, TILE // 2), 10, 2)
            for a in range(6):
                ang = a * 1.047 + self.time
                surf_x = TILE // 2 + int(10 * math.cos(ang))
                surf_y = TILE // 2 + int(10 * math.sin(ang))
                pygame.draw.line(surf, (200, 210, 230, gl),
                                 (surf_x, surf_y),
                                 (TILE // 2 + int(13 * math.cos(ang)),
                                  TILE // 2 + int(13 * math.sin(ang))), 2)
            s.blit(surf, (tp["c"] * TILE, tp["r"] * TILE))

        # 終局道具雨:影子 + 從天而降的道具
        for dp in getattr(self, "drops", []):
            px = dp["c"] * TILE + TILE // 2
            py = dp["r"] * TILE + TILE // 2
            k = max(0.0, min(1.0, dp["t"] / 0.8))
            sw = int(TILE * (0.35 + 0.35 * (1 - k)))
            sh = max(4, sw // 2)
            shadow = pygame.Surface((sw * 2, sh * 2), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow, (20, 24, 34, 110),
                                (0, 0, sw * 2, sh * 2))
            s.blit(shadow, (px - sw, py - sh))
            iy = py - int(k * TILE * 5)
            pygame.draw.circle(s, (255, 255, 255), (px, iy), 12)
            pygame.draw.circle(s, (200, 200, 210), (px, iy), 12, 2)
            draw_item_icon_scaled(s, px, iy, dp["k"], 0.7)

        # 足球:球體(白底黑斑,持球時跟著玩家)
        if self.soccer and self.ball is not None and self.goal_pause <= 0:
            b = self.ball
            if b["carrier"] is None:
                bx, by = b["x"], b["y"] + int(2 * math.sin(self.time * 4))
                sh = self.art["sh_item"]
                s.blit(sh, (bx - sh.get_width() // 2, b["y"] + 8))
            else:
                car = next((q for q in self.players
                            if q.id == b["carrier"]), None)
                if car is None:
                    bx, by = b["x"], b["y"]
                else:
                    ddx, ddy = DIRS[car.facing]
                    bx = car.x - ddx * 17
                    by = car.y - ddy * 17 + 8
            pygame.draw.circle(s, (250, 250, 255), (int(bx), int(by)), 14)
            pygame.draw.circle(s, (222, 228, 238), (int(bx + 3), int(by + 4)),
                               11)
            pygame.draw.circle(s, (250, 250, 255), (int(bx - 3), int(by - 4)),
                               9)
            pygame.draw.circle(s, (60, 64, 76), (int(bx), int(by)), 14, 2)
            spin = b.get("dist", 0.0) * 0.08 if b.get("fly") else self.time
            for k in range(3):
                ang = spin + k * 2.094
                pygame.draw.circle(s, (60, 64, 76),
                                   (int(bx + 6 * math.cos(ang)),
                                    int(by + 6 * math.sin(ang))), 4)

        # 士官長的空襲預警(紅色閃爍標記)
        for st in getattr(self, "strikes", []):
            px = st["c"] * TILE + TILE // 2
            py = st["r"] * TILE + TILE // 2
            blink = int(self.time * 8) % 2 == 0
            col = (255, 70, 70) if blink else (255, 150, 90)
            pygame.draw.rect(s, col,
                             (st["c"] * TILE + 5, st["r"] * TILE + 5,
                              TILE - 10, TILE - 10), 3, border_radius=8)
            # 信號彈紅煙柱
            for i in range(4):
                sy2 = py - 6 - i * 9 - int((1.0 - st["t"]) * 14)
                rr2 = 3 + i
                surf2 = pygame.Surface((rr2 * 2, rr2 * 2), pygame.SRCALPHA)
                pygame.draw.circle(surf2, (255, 90, 70, 150 - i * 30),
                                   (rr2, rr2), rr2)
                s.blit(surf2, (px - rr2 + int(3 * math.sin(self.time * 5 + i)),
                               sy2))
            ex = get_font(22).render("!", True, col)
            s.blit(ex, ex.get_rect(center=(px, py)))

        # 水柱(畫在方塊之下、道具之上皆可,這裡先畫)
        for (r, c), t in self.blasts.items():
            k = max(0.0, min(1.0, t / BLAST_TIME))
            pad = int(3 + 4 * (1 - k))
            rect = pygame.Rect(c * TILE + pad, r * TILE + pad,
                               TILE - pad * 2, TILE - pad * 2)
            pygame.draw.rect(s, C_WATER, rect, border_radius=10)
            core = rect.inflate(-TILE // 3, -TILE // 3)
            pygame.draw.ellipse(s, C_WATER_CORE, core)

        # 方塊(2.5D:頂面受光 + 前立面)
        deco_solid_at = {(r, c): kind for (kind, r, c) in self.deco
                         if kind in DECO_SOLID}
        for r in range(ROWS):
            for c in range(COLS):
                t = self.grid[r][c]
                if t == HARD:
                    if (r, c) not in deco_solid_at:
                        s.blit(art["hard"], (c * TILE, r * TILE))
                elif t == SOFT:
                    s.blit(art["soft"], (c * TILE, r * TILE))
        # 關閉中的閘門(金屬柵欄,蓋過硬磚樣式)
        for (r, c), spec in self.terrain.items():
            if spec[0] == "gate" and self.grid[r][c] == HARD \
                    and (r, c) not in self.sd_locked:
                gx, gy = c * TILE, r * TILE
                pygame.draw.rect(s, (74, 80, 96), (gx + 2, gy + 2,
                                                   TILE - 4, TILE - 4),
                                 border_radius=4)
                for k in range(4):
                    bx = gx + 9 + k * 10
                    pygame.draw.line(s, (150, 158, 176), (bx, gy + 5),
                                     (bx, gy + TILE - 5), 3)
                pygame.draw.rect(s, (170, 178, 196), (gx + 4, gy + 8,
                                                      TILE - 8, 4))
                pygame.draw.rect(s, (170, 178, 196), (gx + 4, gy + TILE - 14,
                                                      TILE - 8, 4))
                pygame.draw.rect(s, (44, 48, 60), (gx + 2, gy + 2,
                                                   TILE - 4, TILE - 4), 2,
                                 border_radius=4)

        # 實體造景(樹/屋/燈籠…),由上往下畫維持前後關係
        for (kind, r, c) in sorted(self.deco, key=lambda d: d[1]):
            if kind in DECO_SOLID and self.grid[r][c] == HARD:
                draw_deco(s, kind, c * TILE, r * TILE, self.time)

        # 道具
        for (r, c), kind in self.items.items():
            self.draw_item(s, r, c, kind)

        # 水球(底影 + 內光暈 + 雙高光)
        for b in self.bubbles:
            cx = b.c * TILE + TILE // 2
            cy = b.r * TILE + TILE // 2
            pulse = 1.0 + 0.08 * math.sin(self.time * 8 + b.r + b.c)
            urgency = 1.0 + max(0.0, (1.0 - b.timer / BUBBLE_FUSE)) * 0.12
            rad = int(TILE * 0.40 * pulse * urgency)
            sh = self.art["sh_ent"]
            s.blit(sh, (cx - sh.get_width() // 2, cy + rad - 8))
            surf = pygame.Surface((rad * 2 + 4, rad * 2 + 4), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*C_BUBBLE, 210), (rad + 2, rad + 2), rad)
            pygame.draw.circle(surf, (150, 205, 250, 120),
                               (rad + 2, rad + 3), rad - 3)      # 內層水色
            pygame.draw.circle(surf, (110, 160, 220, 160),
                               (rad + 2, rad + 2), rad, 2)       # 深藍外緣
            pygame.draw.circle(surf, (255, 255, 255, 130), (rad + 2, rad + 2), rad, 3)
            pygame.draw.circle(surf, (255, 255, 255, 210),
                               (rad + 2 - rad // 3, rad + 2 - rad // 3), rad // 4)
            pygame.draw.circle(surf, (255, 255, 255, 140),
                               (rad + 2 + rad // 3, rad + 2 + rad // 4),
                               max(2, rad // 7))
            s.blit(surf, (cx - rad - 2, cy - rad - 2))
            if b.xshape:
                # X 型炸藥:黃黑警示斜紋
                for sgn in (-1, 1):
                    pygame.draw.line(s, (255, 210, 60),
                                     (cx - rad // 2, cy - sgn * rad // 2),
                                     (cx + rad // 2, cy + sgn * rad // 2), 4)
                    pygame.draw.line(s, (50, 50, 55),
                                     (cx - rad // 2, cy - sgn * rad // 2),
                                     (cx + rad // 2, cy + sgn * rad // 2), 1)
            if b.remote:
                # 遙控水雷:天線 + 閃爍紅燈
                pygame.draw.line(s, (200, 206, 220),
                                 (cx, cy - rad), (cx, cy - rad - 10), 2)
                lit = int(self.time * 5) % 2 == 0
                pygame.draw.circle(s, (255, 70, 70) if lit else (140, 50, 50),
                                   (cx, cy - rad - 12), 3)

        # 泡泡雷達:顯示所有水球的爆炸範圍
        if any(p.alive and p.radar_t > 0 for p in self.players):
            overlay = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
            overlay.fill((255, 70, 70, 70))
            for b in self.bubbles:
                for (r, c) in predicted_blast(self, b.r, b.c, b.power, b.xshape):
                    s.blit(overlay, (c * TILE, r * TILE))

        # 特效(飛鏢軌跡、道具漣漪)
        for fx in self.effects:
            k = max(0.0, fx["t"] / fx["t0"])
            if fx["kind"] == "dart":
                pygame.draw.line(s, (255, 255, 255),
                                 (fx["ax"], fx["ay"]), (fx["bx"], fx["by"]),
                                 max(1, int(4 * k)))
            elif fx["kind"] == "beam":
                pygame.draw.line(s, (150, 220, 255),
                                 (fx["ax"], fx["ay"]), (fx["bx"], fx["by"]),
                                 max(1, int(6 * k)))
                pygame.draw.line(s, (240, 252, 255),
                                 (fx["ax"], fx["ay"]), (fx["bx"], fx["by"]),
                                 max(1, int(2 * k)))
            elif fx["kind"] == "ring":
                rad = int((1 - k) * TILE * 0.7) + 6
                surf = pygame.Surface((rad * 2 + 2, rad * 2 + 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (255, 255, 255, int(180 * k)),
                                   (rad + 1, rad + 1), rad, 3)
                s.blit(surf, (fx["x"] - rad - 1, fx["y"] - rad - 1))
            elif fx["kind"] == "lob":
                # 拋物線飛行物(hoop=籃球 / shell=砲彈)
                pr = 1 - k
                lx = fx["ax"] + (fx["bx"] - fx["ax"]) * pr
                ly = fx["ay"] + (fx["by"] - fx["ay"]) * pr \
                    - math.sin(pr * math.pi) * TILE * 1.6
                if fx.get("ball") == "shell":
                    pygame.draw.ellipse(s, (70, 74, 84),
                                        (lx - 8, ly - 5, 16, 11))
                    pygame.draw.circle(s, (150, 150, 160, ), (int(lx - 6), int(ly)), 2)
                else:
                    pygame.draw.circle(s, (235, 130, 50), (int(lx), int(ly)), 8)
                    pygame.draw.line(s, (120, 60, 20), (lx - 8, ly), (lx + 8, ly), 1)
                    pygame.draw.line(s, (120, 60, 20), (lx, ly - 8), (lx, ly + 8), 1)
            elif fx["kind"] == "kickburst":
                # 踢擊風壓弧
                ang = math.atan2(fx["dy"], fx["dx"])
                for i in range(3):
                    rr = int(10 + (1 - k) * 22 + i * 5)
                    rect = pygame.Rect(fx["x"] - rr, fx["y"] - rr, rr * 2, rr * 2)
                    pygame.draw.arc(s, (220, 250, 220), rect,
                                    -ang - 0.6, -ang + 0.6, 2)
            elif fx["kind"] == "slash":
                # 月牙斬痕
                ang = math.atan2(fx["dy"], fx["dx"])
                rr = int(TILE * 0.55)
                rect = pygame.Rect(fx["x"] - rr, fx["y"] - rr, rr * 2, rr * 2)
                w = max(1, int(5 * k))
                pygame.draw.arc(s, (255, 255, 255), rect,
                                -ang - 1.2, -ang + 1.2, w)
                pygame.draw.arc(s, (200, 230, 255), rect.inflate(-8, -8),
                                -ang - 0.9, -ang + 0.9, max(1, w - 2))
            elif fx["kind"] == "xmark":
                # 工程師:黃黑警示 X
                if int(fx["t"] * 10) % 2 == 0:
                    for sgn in (-1, 1):
                        pygame.draw.line(s, (255, 210, 60),
                                         (fx["x"] - 14, fx["y"] - 14 * sgn),
                                         (fx["x"] + 14, fx["y"] + 14 * sgn), 5)
                        pygame.draw.line(s, (40, 40, 40),
                                         (fx["x"] - 14, fx["y"] - 14 * sgn),
                                         (fx["x"] + 14, fx["y"] + 14 * sgn), 2)
            elif fx["kind"] == "smoke":
                # 忍者煙霧
                rng = random.Random(int(fx["x"]) * 7 + int(fx["y"]))
                for i in range(5):
                    ang = rng.random() * 6.28
                    d = (1 - k) * 16 + i * 3
                    rr = int(6 + (1 - k) * 8)
                    surf = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
                    pygame.draw.circle(surf, (200, 202, 212, int(130 * k)),
                                       (rr, rr), rr)
                    s.blit(surf, (fx["x"] + d * math.cos(ang) - rr,
                                  fx["y"] + d * math.sin(ang) - rr))
            elif fx["kind"] == "heal":
                # 醫護:綠十字上升
                for i in range(3):
                    hy = fx["y"] - (1 - k) * 26 - i * 10
                    hx = fx["x"] + int(8 * math.sin(i * 2.1 + fx["t"] * 6))
                    a = int(200 * k)
                    surf = pygame.Surface((12, 12), pygame.SRCALPHA)
                    pygame.draw.rect(surf, (110, 230, 130, a), (4, 0, 4, 12))
                    pygame.draw.rect(surf, (110, 230, 130, a), (0, 4, 12, 4))
                    s.blit(surf, (hx - 6, hy - 6))
            elif fx["kind"] == "wallup":
                # 築牆揚塵 + 上升石影
                h = int((1 - k) * TILE)
                pygame.draw.rect(s, (120, 126, 140),
                                 (fx["x"] - 16, fx["y"] + TILE // 2 - h,
                                  32, h), 2, border_radius=4)
                for i in range(4):
                    dx2 = (i - 1.5) * 10
                    pygame.draw.circle(s, (170, 160, 150),
                                       (int(fx["x"] + dx2),
                                        int(fx["y"] + TILE // 2 - (1 - k) * 8)),
                                       max(1, int(4 * k)))
            elif fx["kind"] == "rewind":
                # 時空迴旋:逆時針箭頭圈
                rr = int(14 + (1 - k) * 10)
                rect = pygame.Rect(fx["x"] - rr, fx["y"] - rr, rr * 2, rr * 2)
                st = fx["t"] * 9
                pygame.draw.arc(s, (170, 150, 255), rect, st, st + 4.6, 3)
                tipa = st
                tx = fx["x"] + rr * math.cos(tipa)
                ty = fx["y"] - rr * math.sin(tipa)
                pygame.draw.circle(s, (220, 210, 255), (int(tx), int(ty)), 4)
            elif fx["kind"] == "gust":
                # 颶風螺旋
                for arm in range(3):
                    pts = []
                    for i in range(8):
                        aa = arm * 2.094 + i * 0.35 + (1 - k) * 5
                        rr = 6 + i * 3 + (1 - k) * 18
                        pts.append((fx["x"] + rr * math.cos(aa),
                                    fx["y"] + rr * math.sin(aa)))
                    pygame.draw.lines(s, (210, 240, 255), False, pts,
                                      max(1, int(3 * k)))
            elif fx["kind"] == "concuss":
                # 震撼衝擊波:橙環 + 放射線
                rr = int((1 - k) * TILE * 0.9) + 8
                surf = pygame.Surface((rr * 2 + 4, rr * 2 + 4), pygame.SRCALPHA)
                pygame.draw.circle(surf, (255, 170, 70, int(200 * k)),
                                   (rr + 2, rr + 2), rr, 4)
                s.blit(surf, (fx["x"] - rr - 2, fx["y"] - rr - 2))
                for i in range(8):
                    aa = i * 0.785
                    pygame.draw.line(s, (255, 200, 120),
                                     (fx["x"] + (rr - 6) * math.cos(aa),
                                      fx["y"] + (rr - 6) * math.sin(aa)),
                                     (fx["x"] + (rr + 5) * math.cos(aa),
                                      fx["y"] + (rr + 5) * math.sin(aa)),
                                     max(1, int(2 * k)))
            elif fx["kind"] == "snap":
                # 捕獸夾閉合
                op = k * 0.9          # 開口角隨時間閉合
                for sgn in (-1, 1):
                    pts = []
                    for i in range(5):
                        aa = sgn * (op * (1 - i / 5.0)) + (math.pi / 2) * (1 - sgn) / 1
                        rr2 = 6 + i * 3
                        pts.append((fx["x"] + rr2 * math.cos(aa) * 1,
                                    fx["y"] - sgn * rr2 * 0.5 - (1 - k) * 3))
                    pygame.draw.lines(s, (200, 206, 220), False, pts, 3)
                pygame.draw.circle(s, (160, 166, 180), (fx["x"], fx["y"] + 4), 4)
            elif fx["kind"] == "stampede":
                # 衝撞沿路塵土
                for i in range(6):
                    pr = i / 6.0
                    dxp = fx["ax"] + (fx["bx"] - fx["ax"]) * pr
                    dyp = fx["ay"] + (fx["by"] - fx["ay"]) * pr
                    rr = max(1, int((5 + i) * k))
                    surf = pygame.Surface((rr * 2, rr * 2), pygame.SRCALPHA)
                    pygame.draw.circle(surf, (190, 160, 120, int(150 * k)),
                                       (rr, rr), rr)
                    s.blit(surf, (dxp - rr, dyp - rr + 10))
            elif fx["kind"] == "swapflash":
                # 幻影換位:紫色虛線 + 端點閃光
                steps = 9
                for i in range(steps):
                    if i % 2 == 0:
                        x1 = fx["ax"] + (fx["bx"] - fx["ax"]) * i / steps
                        y1 = fx["ay"] + (fx["by"] - fx["ay"]) * i / steps
                        x2 = fx["ax"] + (fx["bx"] - fx["ax"]) * (i + 1) / steps
                        y2 = fx["ay"] + (fx["by"] - fx["ay"]) * (i + 1) / steps
                        pygame.draw.line(s, (200, 140, 255), (x1, y1), (x2, y2),
                                         max(1, int(3 * k)))
                for (ex2, ey2) in ((fx["ax"], fx["ay"]), (fx["bx"], fx["by"])):
                    rr = int(6 + (1 - k) * 10)
                    pygame.draw.circle(s, (230, 190, 255), (int(ex2), int(ey2)),
                                       rr, 2)
            elif fx["kind"] == "nova":
                # 霜華:雪花放射環
                rr = int((1 - k) * TILE * 1.6) + 8
                surf = pygame.Surface((rr * 2 + 4, rr * 2 + 4), pygame.SRCALPHA)
                pygame.draw.circle(surf, (170, 220, 255, int(170 * k)),
                                   (rr + 2, rr + 2), rr, 3)
                s.blit(surf, (fx["x"] - rr - 2, fx["y"] - rr - 2))
                for i in range(6):
                    aa = i * 1.047 + (1 - k)
                    fx2 = fx["x"] + rr * math.cos(aa)
                    fy2 = fx["y"] + rr * math.sin(aa)
                    for j in range(6):
                        ab = j * 1.047
                        pygame.draw.line(s, (220, 245, 255),
                                         (fx2, fy2),
                                         (fx2 + 6 * math.cos(ab),
                                          fy2 + 6 * math.sin(ab)), 1)
            elif fx["kind"] == "aqua":
                # 水靈水珠
                for i in range(6):
                    aa = i * 1.047 + (1 - k) * 2
                    d = (1 - k) * 20 + 6
                    pygame.draw.circle(s, (150, 210, 250),
                                       (int(fx["x"] + d * math.cos(aa)),
                                        int(fx["y"] + d * math.sin(aa) - (1 - k) * 8)),
                                       max(1, int(3 * k)))
            elif fx["kind"] == "notes":
                # 節奏音符上飄
                cols = ((255, 180, 120), (170, 220, 255), (200, 255, 170))
                for i in range(3):
                    ny = fx["y"] - (1 - k) * 30 - i * 8
                    nx = fx["x"] + int(10 * math.sin(i * 2 + fx["t"] * 8)) + (i - 1) * 10
                    pygame.draw.circle(s, cols[i], (nx, int(ny)), 4)
                    pygame.draw.line(s, cols[i], (nx + 4, ny), (nx + 4, ny - 12), 2)
                    pygame.draw.line(s, cols[i], (nx + 4, ny - 12), (nx + 9, ny - 9), 2)
            elif fx["kind"] == "loot":
                # 海盜金幣:沿線拋物線,錯開三枚
                for i in range(3):
                    pr = max(0.0, min(1.0, (1 - k) * 1.4 - i * 0.15))
                    lx = fx["ax"] + (fx["bx"] - fx["ax"]) * pr
                    ly = fx["ay"] + (fx["by"] - fx["ay"]) * pr \
                        - math.sin(pr * math.pi) * 26
                    pygame.draw.circle(s, (250, 210, 90), (int(lx), int(ly)), 5)
                    pygame.draw.circle(s, (190, 150, 40), (int(lx), int(ly)), 5, 1)
                    pygame.draw.line(s, (190, 150, 40),
                                     (lx - 2, ly), (lx + 2, ly), 1)
            elif fx["kind"] == "spark":
                # 電光爆閃
                rng = random.Random(int(fx["t0"] * 100) + int(fx["x"]))
                for i in range(6):
                    aa = rng.random() * 6.28
                    r1 = 6 + (1 - k) * 6
                    r2 = r1 + 10 + rng.random() * 8
                    pygame.draw.line(s, (255, 245, 140),
                                     (fx["x"] + r1 * math.cos(aa),
                                      fx["y"] + r1 * math.sin(aa)),
                                     (fx["x"] + r2 * math.cos(aa),
                                      fx["y"] + r2 * math.sin(aa)),
                                     max(1, int(3 * k)))
            elif fx["kind"] == "arm":
                # 水雷警備:紅燈同心圈
                if int(fx["t"] * 8) % 2 == 0:
                    for rr in (8, 14):
                        pygame.draw.circle(s, (255, 90, 80),
                                           (fx["x"], fx["y"] - 14), rr, 2)
            elif fx["kind"] == "cast":
                # 釣客:釣竿 + 釣線 + 道具收回
                px2, py2 = fx["bx"], fx["by"]     # 玩家端
                rodx, rody = px2 + 14, py2 - 22   # 竿尖
                pygame.draw.line(s, (150, 110, 70), (px2 + 2, py2 + 6),
                                 (rodx, rody), 3)
                pr = 1 - k
                ix2 = fx["ax"] + (rodx - fx["ax"]) * pr
                iy2 = fx["ay"] + (rody - fx["ay"]) * pr
                pygame.draw.line(s, (235, 240, 250), (rodx, rody), (ix2, iy2), 1)
                pygame.draw.circle(s, (250, 90, 80), (int(ix2), int(iy2) - 6), 4)
                pygame.draw.circle(s, (250, 250, 255), (int(ix2), int(iy2) - 6), 4, 1)
            elif fx["kind"] == "sprout":
                # 園丁:破土綠芽
                h = (1 - k) * 16
                pygame.draw.line(s, (110, 180, 90),
                                 (fx["x"], fx["y"] + 10),
                                 (fx["x"], fx["y"] + 10 - h), 3)
                pygame.draw.ellipse(s, (140, 210, 105),
                                    (fx["x"] - 9, fx["y"] + 8 - h, 9, 6))
                pygame.draw.ellipse(s, (160, 225, 120),
                                    (fx["x"], fx["y"] + 6 - h, 9, 6))
                for i in range(3):
                    pygame.draw.circle(s, (150, 120, 90),
                                       (fx["x"] + (i - 1) * 9,
                                        int(fx["y"] + 12 - (1 - k) * 5)),
                                       max(1, int(3 * k)))
            elif fx["kind"] == "balloons":
                # 氣球商人:氣球升空
                cols = ((250, 130, 150), (140, 190, 255), (255, 220, 120))
                for i in range(3):
                    by2 = fx["y"] - (1 - k) * 34 - i * 6
                    bx2 = fx["x"] + int(9 * math.sin(i * 2.2 + fx["t"] * 5)) + (i - 1) * 12
                    pygame.draw.ellipse(s, cols[i], (bx2 - 5, by2 - 7, 10, 13))
                    pygame.draw.line(s, (230, 234, 244), (bx2, by2 + 6),
                                     (bx2 - 2, by2 + 14), 1)
            elif fx["kind"] == "quake":
                # 力士震地:放射裂紋 + 塵環
                rng = random.Random(int(fx["x"]) + int(fx["y"]) * 3)
                for i in range(7):
                    aa = i * 0.897 + rng.random() * 0.3
                    ln = (1 - k) * 26 + 8
                    mid = (fx["x"] + ln * 0.5 * math.cos(aa) + rng.randint(-4, 4),
                           fx["y"] + ln * 0.5 * math.sin(aa) + rng.randint(-4, 4))
                    pygame.draw.lines(s, (110, 90, 70), False,
                                      [(fx["x"], fx["y"]), mid,
                                       (fx["x"] + ln * math.cos(aa),
                                        fx["y"] + ln * math.sin(aa))],
                                      max(1, int(3 * k)))
                rr = int((1 - k) * 26) + 6
                surf = pygame.Surface((rr * 2 + 2, rr * 2 + 2), pygame.SRCALPHA)
                pygame.draw.circle(surf, (180, 150, 110, int(120 * k)),
                                   (rr + 1, rr + 1), rr, 4)
                s.blit(surf, (fx["x"] - rr - 1, fx["y"] - rr - 1))

        # 飛行中的飛彈
        for ms in self.missiles:
            mx, my = int(ms["x"]), int(ms["y"])
            dx, dy = ms["dx"], ms["dy"]
            tip = (mx + dx * 12, my + dy * 12)
            tail = (mx - dx * 10, my - dy * 10)
            pygame.draw.line(s, (160, 166, 178), tail, tip, 7)
            pygame.draw.circle(s, (210, 70, 70), tip, 5)
            flame = (mx - dx * 14 + random.randint(-2, 2),
                     my - dy * 14 + random.randint(-2, 2))
            pygame.draw.circle(s, (255, 190, 80), flame, 4)

        # ---- 章魚王 Boss 模式:落點預警 / 小章魚 / 章魚王 ----
        if self.boss is not None:
            pulse = 0.5 + 0.5 * math.sin(self.time * 12)
            for m in self.incoming:
                r, c = m[0], m[1]
                cx = c * TILE + TILE // 2
                cy = r * TILE + TILE // 2
                rad = int(TILE * 0.32 + 4 * pulse)
                surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
                pygame.draw.circle(surf, (255, 70, 70, 160),
                                   (TILE // 2, TILE // 2), rad, 3)
                pygame.draw.line(surf, (255, 70, 70, 200),
                                 (TILE // 2 - 7, TILE // 2), (TILE // 2 + 7, TILE // 2), 3)
                pygame.draw.line(surf, (255, 70, 70, 200),
                                 (TILE // 2, TILE // 2 - 7), (TILE // 2, TILE // 2 + 7), 3)
                s.blit(surf, (cx - TILE // 2, cy - TILE // 2))
            for mn in self.minions:
                self.draw_minion(s, mn)
            self.draw_boss(s)

        # ---- 對戰/組隊:落石預警 + 倒數計時 ----
        if self.match_left is not None:
            pulse2 = 0.5 + 0.5 * math.sin(self.time * 14)
            for (r, c), tt in self.falling.items():
                k = max(0.0, min(1.0, tt / SD_WARN))
                x, y = c * TILE, r * TILE
                surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
                surf.fill((200, 40, 40, int(70 + 70 * pulse2)))
                s.blit(surf, (x, y))
                # 落下中的磚塊(越接近落地越大)
                sz = int(TILE * (1.0 - 0.6 * k))
                rect = pygame.Rect(0, 0, sz, sz)
                rect.center = (x + TILE // 2, y + TILE // 2)
                pygame.draw.rect(s, (70, 74, 84), rect, border_radius=4)
                pygame.draw.rect(s, (40, 44, 52), rect, 2, border_radius=4)
            mins = max(0, int(self.match_left)) // 60
            secs = max(0, int(self.match_left)) % 60
            danger_time = self.match_left <= SD_START
            col = (255, 90, 90) if danger_time else (255, 255, 255)
            txt = "%d:%02d" % (mins, secs)
            if danger_time:
                txt += T("  場地崩塌中!", "  ARENA COLLAPSING!")
            tsurf = get_font(16).render(txt, True, col)
            tr = tsurf.get_rect(midtop=(SCREEN_W // 2, 4))
            bg = pygame.Surface((tr.w + 14, tr.h + 6), pygame.SRCALPHA)
            bg.fill((0, 0, 0, 120))
            s.blit(bg, (tr.x - 7, tr.y - 3))
            s.blit(tsurf, tr)

        # ---- 場地攻擊:紅色驚嘆號預警 / 轟炸機 / 企鵝 ----
        for hz in self.hazards:
            if hz["state"] == "warn":
                bounce = int(3 * math.sin(self.time * 10))
                for (r, c) in hz["tiles"]:
                    x = c * TILE
                    y = r * TILE
                    surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
                    surf.fill((220, 50, 50, 60))
                    s.blit(surf, (x, y))
                    # 紅色驚嘆號
                    ex = x + TILE // 2
                    ey = y + TILE // 2 + bounce
                    pygame.draw.rect(s, (230, 40, 40),
                                     (ex - 4, ey - 15, 8, 18), border_radius=4)
                    pygame.draw.circle(s, (230, 40, 40), (ex, ey + 11), 4)
                    pygame.draw.rect(s, (255, 200, 200),
                                     (ex - 1, ey - 13, 2, 12))
            elif hz["kind"] == "plane":
                px = int(hz["x"])
                py = hz["row"] * TILE + TILE // 2 - 26
                d = hz["dir"]
                # 機身 + 機翼 + 尾翼(原創簡易造型)
                pygame.draw.ellipse(s, (120, 140, 165), (px - 26, py - 8, 52, 16))
                pygame.draw.polygon(s, (95, 115, 140),
                                    [(px - 4, py - 4), (px - 22 * d, py - 22),
                                     (px - 14 * d, py - 2)])
                pygame.draw.polygon(s, (95, 115, 140),
                                    [(px - 4, py + 4), (px - 22 * d, py + 22),
                                     (px - 14 * d, py + 2)])
                pygame.draw.polygon(s, (95, 115, 140),
                                    [(px - 24 * d, py - 6), (px - 32 * d, py - 16),
                                     (px - 26 * d, py)])
                pygame.draw.circle(s, (200, 225, 245), (px + 14 * d, py - 2), 5)
            else:   # 企鵝衝鋒
                px, py = int(hz["x"]), int(hz["y"])
                wob = int(2 * math.sin(self.time * 20))
                # 衝刺尾流
                for i in range(1, 4):
                    tx = px - hz["vx"] * i * 14
                    ty = py - hz["vy"] * i * 14
                    surf = pygame.Surface((26, 26), pygame.SRCALPHA)
                    pygame.draw.circle(surf, (200, 230, 255, 90 - i * 25), (13, 13), 12)
                    s.blit(surf, (tx - 13, ty - 13))
                # 身體(黑)+ 肚子(白)+ 嘴腳(橘)
                pygame.draw.ellipse(s, (35, 40, 52),
                                    (px - 22, py - 25 + wob, 44, 50))
                pygame.draw.ellipse(s, (245, 248, 252),
                                    (px - 13, py - 10 + wob, 26, 32))
                for dd in (-9, 9):
                    pygame.draw.circle(s, (255, 255, 255), (px + dd, py - 13 + wob), 6)
                    pygame.draw.circle(s, (30, 30, 40),
                                       (px + dd + hz["vx"] * 3,
                                        py - 13 + wob + hz["vy"] * 3), 3)
                pygame.draw.polygon(s, (240, 150, 50),
                                    [(px - 5, py - 6 + wob), (px + 5, py - 6 + wob),
                                     (px, py + 2 + wob)])
                for sign in (-1, 1):   # 小翅膀
                    pygame.draw.ellipse(s, (35, 40, 52),
                                        (px + sign * 20 - 5, py - 4 + wob, 10, 20))

        # 玩家(活著的最後畫,被困的畫大水泡)
        for p in self.players:
            if p.alive:
                self.draw_player(s, p)

        # 地圖名稱小標籤
        label = get_font(15).render(
            T(self.map_cfg["zh"], self.map_cfg["en"]), True, (255, 255, 255))
        lr = label.get_rect(topright=(SCREEN_W - 8, 6))
        bg = pygame.Surface((lr.w + 12, lr.h + 6), pygame.SRCALPHA)
        bg.fill((0, 0, 0, 110))
        s.blit(bg, (lr.x - 6, lr.y - 3))
        s.blit(label, lr)

        if self.soccer:
            st = render_text(17, "%d : %d" % tuple(self.scores),
                             (255, 255, 255))
            bg3 = pygame.Surface((st.get_width() + 56, st.get_height() + 8),
                                 pygame.SRCALPHA)
            bg3.fill((16, 24, 20, 170))
            bx3 = SCREEN_W // 2 - bg3.get_width() // 2
            s.blit(bg3, (bx3, 26))
            pygame.draw.rect(s, (235, 80, 80), (bx3 + 6, 31, 18, 12),
                             border_radius=4)
            pygame.draw.rect(s, (80, 130, 240),
                             (bx3 + bg3.get_width() - 24, 31, 18, 12),
                             border_radius=4)
            s.blit(st, (SCREEN_W // 2 - st.get_width() // 2, 30))
        if self.infect:
            nh = sum(1 for q in self.players if not q.infected)
            nz = sum(1 for q in self.players if q.infected)
            it = render_text(15, T("生存 %d   感染 %d" % (nh, nz),
                                   "ALIVE %d   INFECTED %d" % (nh, nz)),
                             (200, 250, 180))
            bg2 = pygame.Surface((it.get_width() + 16, it.get_height() + 6),
                                 pygame.SRCALPHA)
            bg2.fill((10, 30, 12, 150))
            s.blit(bg2, (SCREEN_W // 2 - bg2.get_width() // 2, 26))
            s.blit(it, (SCREEN_W // 2 - it.get_width() // 2, 29))
        if self.turf:
            n0 = sum(1 for v in self.paint.values() if v == 0)
            n1 = sum(1 for v in self.paint.values() if v == 1)
            total = max(1, n0 + n1)
            bw, bh = 240, 16
            bx = SCREEN_W // 2 - bw // 2
            by2 = 28          # 讓出上方給比賽計時器
            pygame.draw.rect(s, (30, 34, 46), (bx - 2, by2 - 2, bw + 4, bh + 4),
                             border_radius=8)
            w0 = int(bw * n0 / total)
            pygame.draw.rect(s, TURF_COLS[0], (bx, by2, w0, bh),
                             border_radius=6)
            pygame.draw.rect(s, TURF_COLS[1], (bx + w0, by2, bw - w0, bh),
                             border_radius=6)
            pygame.draw.rect(s, (220, 226, 240), (bx - 2, by2 - 2, bw + 4, bh + 4),
                             2, border_radius=8)
            s.blit(render_text(13, str(n0), (255, 255, 255)), (bx - 26, by2 + 1))
            t1 = render_text(13, str(n1), (255, 255, 255))
            s.blit(t1, (bx + bw + 8, by2 + 1))
        if self.ambient:
            draw_ambient(s, self.ambient, self.time)
        for vs, pos in self.art["vin_strips"]:
            s.blit(vs, pos)
        self.draw_hud(s)

        # 終局狂熱:紅色脈動邊框
        if (self.match_left is not None and self.match_left <= SD_START
                and not self.over):
            a = 46 + int(26 * math.sin(self.time * 5))
            edge = pygame.Surface((SCREEN_W, 8), pygame.SRCALPHA)
            edge.fill((255, 60, 50, a))
            s.blit(edge, (0, 0))
            s.blit(edge, (0, ROWS * TILE - 8))
            edge_v = pygame.Surface((8, ROWS * TILE), pygame.SRCALPHA)
            edge_v.fill((255, 60, 50, a))
            s.blit(edge_v, (0, 0))
            s.blit(edge_v, (SCREEN_W - 8, 0))

        # 開場倒數:大數字 + 標記自己的位置
        if self.countdown > 0:
            dim = pygame.Surface((SCREEN_W, SCREEN_H - HUD_H), pygame.SRCALPHA)
            dim.fill((10, 16, 28, 88))
            s.blit(dim, (0, 0))
            n = math.ceil(self.countdown)
            frac = self.countdown - int(self.countdown)
            k = (84 + 30 * frac) / 96.0
            base_n = render_text(96, str(n), (255, 235, 130))
            base_s = render_text(96, str(n), (40, 30, 10))
            tw2, th2 = base_n.get_size()
            num = pygame.transform.scale(base_n,
                                         (int(tw2 * k), int(th2 * k)))
            sh2 = pygame.transform.scale(base_s,
                                         (int(tw2 * k), int(th2 * k)))
            cx2, cy2 = SCREEN_W // 2, (SCREEN_H - HUD_H) // 2 - 20
            s.blit(sh2, sh2.get_rect(center=(cx2 + 3, cy2 + 3)))
            s.blit(num, num.get_rect(center=(cx2, cy2)))
            mine = self.my_pids or {q.id for q in self.players
                                    if not q.is_bot
                                    and not getattr(q, "is_remote", False)}
            bob = int(4 * math.sin(self.time * 6))
            for q in self.players:
                if q.id not in mine or not q.alive:
                    continue
                ax, ay = int(q.x), int(q.y) - 34 + bob
                pygame.draw.polygon(s, (255, 235, 130),
                                    [(ax - 9, ay - 12), (ax + 9, ay - 12),
                                     (ax, ay)])
                label = (T("你在這!", "YOU!") if len(mine) == 1
                         else "P%d" % (q.id + 1))
                lt = render_text(15, label, (255, 235, 130))
                s.blit(lt, lt.get_rect(center=(ax, ay - 22)))
        elif self.go_flash > 0:
            a2 = int(255 * min(1.0, self.go_flash / 0.5))
            go = get_font(76).render("GO!", True, (140, 240, 150))
            go.set_alpha(a2)
            s.blit(go, go.get_rect(center=(SCREEN_W // 2,
                                           (SCREEN_H - HUD_H) // 2 - 20)))

        # 終局宣告橫幅
        if self.announce is not None:
            key = self.announce["key"]
            texts = {"goal0": T("GOAL!!紅隊得分!", "GOAL!! RED SCORES!"),
                     "goal1": T("GOAL!!藍隊得分!", "GOAL!! BLUE SCORES!"),
                     "outbreak": T("感染爆發!快逃!!",
                                   "OUTBREAK! RUN!!"),
                     "laststand": T("最後的生存者!撐住!!",
                                    "LAST SURVIVOR! HOLD ON!!"),
                     "fever": T("⚡ 終局狂熱!引信縮短、全員加速 ⚡",
                                "FINAL FEVER! Short fuses, speed up!"),
                     "collapse": T("崩塌加速!!", "COLLAPSE SURGE!!"),
                     "final": T("決一死戰!全員威力 +1", "SHOWDOWN! +1 POWER")}
            txt = texts.get(key, "")
            frac = self.announce["t"] / self.announce["t0"]
            alpha = int(255 * min(1.0, frac * 3))
            size = 34 if key == "fever" else 40
            f = get_font(size)
            surf = f.render(txt, True, (255, 226, 120))
            surf.set_alpha(alpha)
            bg = pygame.Surface((surf.get_width() + 44, surf.get_height() + 18),
                                pygame.SRCALPHA)
            bg.fill((60, 20, 24, min(190, alpha)))
            pygame.draw.rect(bg, (255, 120, 90, alpha), bg.get_rect(), 3,
                             border_radius=12)
            cy = ROWS * TILE // 3
            s.blit(bg, bg.get_rect(center=(SCREEN_W // 2, cy)))
            s.blit(surf, surf.get_rect(center=(SCREEN_W // 2, cy)))

        if self.over:
            self.draw_over(s)

    def draw_item(self, s, r, c, kind):
        cx = c * TILE + TILE // 2
        bob = int(2 * math.sin(self.time * 4 + r * 2 + c))
        cy = r * TILE + TILE // 2 + bob
        sh = self.art["sh_item"]
        s.blit(sh, (cx - sh.get_width() // 2,
                    r * TILE + TILE - 12 - bob // 2))
        rad = TILE // 3 + 2
        pygame.draw.circle(s, (216, 224, 236), (cx, cy), rad)      # 底盤
        pygame.draw.circle(s, (255, 255, 255), (cx - 2, cy - 3), rad - 3)
        pygame.draw.circle(s, (168, 178, 196), (cx, cy), rad, 2)   # 外圈
        pygame.draw.circle(s, (255, 255, 255), (cx - rad // 2,
                                                cy - rad // 2), 3)  # 光點
        draw_item_icon(s, cx, cy, kind)
        # 旋轉星光
        tw = (self.time * 3 + r + c) % 6.28
        sx = cx + int((rad + 3) * math.cos(tw))
        sy = cy + int((rad + 3) * math.sin(tw)) - 2
        pygame.draw.line(s, (255, 250, 210), (sx - 3, sy), (sx + 3, sy), 1)
        pygame.draw.line(s, (255, 250, 210), (sx, sy - 3), (sx, sy + 3), 1)

    def draw_player(self, s, p):
        x, y = int(p.x), int(p.y)
        rad = int(TILE * 0.36)

        # 腳下柔影(2.5D 立體感)
        if p.alive and not (p.ghost_t > 0 and not p.trapped):
            sh = self.art["sh_ent"]
            s.blit(sh, (x - sh.get_width() // 2, y + rad - 8))

        # 隱形衣:只畫一個淡淡的影子
        if p.ghost_t > 0 and not p.trapped:
            surf = pygame.Surface((rad * 2 + 4, rad * 2 + 4), pygame.SRCALPHA)
            pygame.draw.ellipse(surf, (*p.color, 55), surf.get_rect().inflate(-4, -4))
            s.blit(surf, (x - rad - 2, y - rad - 2))
            return

        if p.trapped:
            # 困住的大水泡
            wob = math.sin(p.anim * 10) * 2
            brad = rad + 10
            surf = pygame.Surface((brad * 2 + 8, brad * 2 + 8), pygame.SRCALPHA)
            pygame.draw.circle(surf, (150, 205, 255, 130),
                               (brad + 4, brad + 4), brad + int(wob))
            pygame.draw.circle(surf, (255, 255, 255, 180),
                               (brad + 4, brad + 4), brad + int(wob), 3)
            s.blit(surf, (x - brad - 4, y - brad - 4 - 3))
            # 倒數弧線
            frac = max(0.0, p.trap_timer / TRAP_TIME)
            if frac > 0:
                rect = pygame.Rect(x - brad - 2, y - brad - 5,
                                   (brad + 2) * 2, (brad + 2) * 2)
                pygame.draw.arc(s, (255, 90, 90), rect,
                                math.pi / 2, math.pi / 2 + frac * 2 * math.pi, 4)
            y -= 3  # 微微浮起

        # 濕身:身上的水珠
        if p.wet_t > 0 and p.alive:
            for k in range(3):
                ddx = int(10 * math.sin(self.time * 3 + k * 2.1))
                ddy = (int(self.time * 40 + k * 17) % 18) - 4
                pygame.draw.circle(s, (150, 205, 250),
                                   (x + ddx, y - rad + ddy), 2)

        # 感染者:綠色瘴氣光環 + 頭頂棘刺
        if getattr(p, "infected", False) and p.alive:
            aura = pygame.Surface((rad * 2 + 26, rad * 2 + 26), pygame.SRCALPHA)
            gl = 90 + int(40 * math.sin(self.time * 5 + p.id))
            pygame.draw.circle(aura, (110, 230, 90, gl),
                               (rad + 13, rad + 13), rad + 10, 4)
            s.blit(aura, (x - rad - 13, y - rad - 13))
            for k in range(3):
                ang = self.time * 2.4 + k * 2.094
                sx2 = x + int((rad + 6) * math.cos(ang))
                sy2 = y - rad - 4 + int(3 * math.sin(ang * 2))
                pygame.draw.circle(s, (110, 230, 90), (sx2, sy2), 3)
                pygame.draw.line(s, (150, 250, 120), (sx2, sy2),
                                 (sx2, sy2 - 6), 2)

        # 組隊戰:隊伍色光環
        if p.team is not None:
            if self.turf:
                tcol = TURF_COLS[p.team % 2]
            else:
                tcol = (235, 80, 80) if p.team == 0 else (80, 130, 240)
            ring = pygame.Surface((rad * 2 + 20, rad + 14), pygame.SRCALPHA)
            pygame.draw.ellipse(ring, (*tcol, 150), ring.get_rect(), 4)
            s.blit(ring, (x - rad - 10, y + rad - 10))

        # 坐騎(畫在身體下方)
        if p.mount == "turtle":
            pygame.draw.ellipse(s, (90, 170, 90), (x - rad - 4, y + 2, (rad + 4) * 2, rad + 6))
            pygame.draw.ellipse(s, (50, 120, 50), (x - rad - 4, y + 2, (rad + 4) * 2, rad + 6), 2)
            pygame.draw.circle(s, (120, 200, 120), (x + rad + 5, y + rad // 2 + 4), 5)
        elif p.mount == "owl":
            pygame.draw.ellipse(s, (150, 110, 70), (x - rad - 3, y, (rad + 3) * 2, rad + 8))
            for sign in (-1, 1):
                wing_x = x + sign * (rad + 4)
                flap = int(3 * math.sin(p.anim * 12))
                pygame.draw.ellipse(s, (120, 86, 52),
                                    (wing_x - 6, y - 2 + flap, 12, rad + 4))
        elif p.mount == "ufo":
            hover = int(2 * math.sin(p.anim * 6))
            pygame.draw.ellipse(s, (150, 156, 170),
                                (x - rad - 8, y + 4 + hover, (rad + 8) * 2, rad + 4))
            pygame.draw.ellipse(s, (100, 106, 120),
                                (x - rad - 8, y + 4 + hover, (rad + 8) * 2, rad + 4), 2)
            for dd in (-rad, 0, rad):
                pygame.draw.circle(s, (255, 230, 120), (x + dd, y + 6 + rad // 2 + hover), 3)

        # 身體
        squash = 1.0 + 0.05 * math.sin(p.anim * 9)
        body = pygame.Rect(0, 0, int(rad * 2), int(rad * 2 * squash))
        body.center = (x, y)
        shadow = pygame.Surface((rad * 2, rad), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 60), shadow.get_rect())
        s.blit(shadow, (x - rad, y + rad - 6))
        pygame.draw.ellipse(s, p.color, body)
        dark = tuple(max(0, v - 60) for v in p.color)
        pygame.draw.ellipse(s, dark, body, 3)

        # 無敵光盾:發亮的圓環
        if p.shield_t > 0:
            glow = int(150 + 100 * math.sin(p.anim * 14))
            ring = pygame.Surface((rad * 2 + 16, rad * 2 + 16), pygame.SRCALPHA)
            pygame.draw.circle(ring, (140, 210, 255, glow),
                               (rad + 8, rad + 8), rad + 7, 3)
            s.blit(ring, (x - rad - 8, y - rad - 8))

        # 惡魔面具詛咒:紫色小角
        if p.curse_t > 0:
            for sign in (-1, 1):
                hx = x + sign * (rad - 4)
                pygame.draw.polygon(s, (150, 70, 200),
                                    [(hx, y - rad + 2), (hx + sign * 6, y - rad - 8),
                                     (hx + sign * 2, y - rad - 1)])

        # 被冰凍:罩上冰塊
        if p.frozen_t > 0:
            ice = pygame.Surface((rad * 2 + 14, rad * 2 + 14), pygame.SRCALPHA)
            irect = ice.get_rect().inflate(-2, -2)
            pygame.draw.rect(ice, (150, 210, 245, 140), irect, border_radius=8)
            pygame.draw.rect(ice, (230, 248, 255, 200), irect, 3, border_radius=8)
            pygame.draw.line(ice, (255, 255, 255, 180),
                             (6, irect.h - 8), (irect.w - 10, 8), 2)
            s.blit(ice, (x - rad - 7, y - rad - 7))

        # 暈眩:三顆星星繞頭
        if p.daze_t > 0 and p.alive:
            for k in range(3):
                ang = self.time * 6 + k * 2.094
                sx = x + int(14 * math.cos(ang))
                sy = y - rad - 8 + int(4 * math.sin(ang * 2))
                pts = []
                for j in range(10):
                    a2 = j * math.pi / 5 - math.pi / 2 + ang * 0.3
                    rr = 5 if j % 2 == 0 else 2
                    pts.append((sx + rr * math.cos(a2), sy + rr * math.sin(a2)))
                pygame.draw.polygon(s, (255, 226, 110), pts)

        # 電光使疾馳:身上電弧
        if p.volt_t > 0 and p.alive:
            rng = random.Random(int(self.time * 20) + p.id)
            for _ in range(3):
                a1 = rng.random() * 6.28
                a2 = a1 + rng.random() * 1.2 - 0.6
                p1 = (x + int((rad + 3) * math.cos(a1)),
                      y + int((rad + 3) * math.sin(a1)))
                pm = (x + int((rad + 9) * math.cos((a1 + a2) / 2)),
                      y + int((rad + 9) * math.sin((a1 + a2) / 2)))
                p2 = (x + int((rad + 4) * math.cos(a2)),
                      y + int((rad + 4) * math.sin(a2)))
                pygame.draw.lines(s, (255, 245, 140), False, [p1, pm, p2], 2)

        # 眼睛朝向
        ox, oy = DIRS[p.facing]
        ex, ey = x + ox * 6, y - 4 + oy * 5
        for ddx in (-7, 7):
            pygame.draw.circle(s, (255, 255, 255), (ex + ddx, ey), 6)
            pygame.draw.circle(s, (30, 30, 40), (ex + ddx + ox * 2, ey + oy * 2), 3)

        # 角色專屬配件(看得出是哪隻)
        if p.char is not None:
            draw_char_gear(s, p.char, x, y, rad, p.facing, self.time + p.id)

        # 頭上編號
        name = "CPU" if p.is_bot else p.name[:6]
        tag = render_text(14, name, (255, 255, 255))
        tr = tag.get_rect(center=(x, y - rad - 10))
        bg = tr.inflate(8, 2)
        pygame.draw.rect(s, (*[c // 2 for c in p.color], ), bg, border_radius=6)
        s.blit(tag, tr)

    def draw_minion(self, s, mn):
        x, y = int(mn.x), int(mn.y)
        wob = math.sin(mn.anim * 8) * 2
        col = (170, 100, 200)
        # 觸手
        for i in range(4):
            tx = x - 12 + i * 8
            ty = y + 10 + int(3 * math.sin(mn.anim * 10 + i))
            pygame.draw.circle(s, col, (tx, ty), 4)
        # 頭
        pygame.draw.circle(s, col, (x, y + int(wob)), 12)
        pygame.draw.circle(s, (120, 60, 150), (x, y + int(wob)), 12, 2)
        for dd in (-4, 4):
            pygame.draw.circle(s, (255, 255, 255), (x + dd, y - 2 + int(wob)), 4)
            pygame.draw.circle(s, (30, 30, 40), (x + dd, y - 1 + int(wob)), 2)

    def draw_boss(self, s):
        bz = self.boss
        x, y = int(bz.cx), int(bz.cy)
        enr = bz.enraged()
        body = (210, 70, 90) if enr else (160, 70, 180)
        dark = (150, 40, 60) if enr else (110, 40, 130)
        rad = int(TILE * 1.35)
        bob = int(4 * math.sin(bz.anim * 3))

        # 影子
        sh = pygame.Surface((rad * 2, rad), pygame.SRCALPHA)
        pygame.draw.ellipse(sh, (0, 0, 0, 70), sh.get_rect())
        s.blit(sh, (x - rad, y + rad // 2 + 8))
        # 觸手(8 隻,沿下緣擺動)
        for i in range(8):
            ang = math.pi * (0.15 + 0.7 * i / 7)
            tx = x + int(math.cos(ang) * rad * 0.95)
            ty = y + int(math.sin(ang) * rad * 0.55) + rad // 2
            wig = int(5 * math.sin(bz.anim * 6 + i * 1.3))
            pygame.draw.circle(s, dark, (tx, ty + wig), 11)
            pygame.draw.circle(s, body, (tx, ty + wig - 4), 9)
        # 頭
        pygame.draw.circle(s, body, (x, y + bob), rad)
        pygame.draw.circle(s, dark, (x, y + bob), rad, 4)
        # 受擊閃白
        if bz.flash > 0:
            fl = pygame.Surface((rad * 2, rad * 2), pygame.SRCALPHA)
            pygame.draw.circle(fl, (255, 255, 255, int(200 * bz.flash / 0.2)),
                               (rad, rad), rad)
            s.blit(fl, (x - rad, y + bob - rad))
        # 眼睛(生氣眉)
        for sign in (-1, 1):
            ex = x + sign * rad // 3
            ey = y + bob - rad // 5
            pygame.draw.circle(s, (255, 255, 255), (ex, ey), 13)
            pygame.draw.circle(s, (30, 30, 40), (ex, ey + 3), 6)
            pygame.draw.line(s, dark, (ex - sign * 12, ey - 16),
                             (ex + sign * 10, ey - 9), 5)
        # 嘴
        pygame.draw.arc(s, dark, (x - 16, y + bob + rad // 4, 32, 18),
                        0, math.pi, 4)

        # 血條(頂部置中)
        bw, bh = 340, 16
        bx = (SCREEN_W - bw) // 2
        by = 6
        frac = max(0.0, bz.hp / bz.max_hp)
        pygame.draw.rect(s, (20, 24, 34), (bx - 2, by - 2, bw + 4, bh + 4),
                         border_radius=6)
        col = (230, 60, 60) if enr else (240, 150, 60)
        pygame.draw.rect(s, col, (bx, by, int(bw * frac), bh), border_radius=5)
        pygame.draw.rect(s, (255, 255, 255), (bx - 2, by - 2, bw + 4, bh + 4),
                         2, border_radius=6)
        label = get_font(14).render(
            T("章魚王(%s) %d / %d" % (bz.cfg["zh"], bz.hp, bz.max_hp),
              "OCTOPUS KING (%s) %d / %d" % (bz.cfg["en"], bz.hp, bz.max_hp)),
            True, (255, 255, 255))
        s.blit(label, label.get_rect(center=(SCREEN_W // 2, by + bh // 2)))

        # 台詞泡泡
        if bz.taunt_t > 0 and bz.taunt:
            txt = get_font(17).render(bz.taunt, True, (40, 30, 50))
            tr = txt.get_rect(center=(x, y - rad - 22))
            tr.clamp_ip(pygame.Rect(4, 26, SCREEN_W - 8, ROWS * TILE))
            box = tr.inflate(16, 10)
            pygame.draw.rect(s, (255, 255, 255), box, border_radius=10)
            pygame.draw.rect(s, (120, 90, 140), box, 2, border_radius=10)
            s.blit(txt, tr)

    def draw_hud(self, s):
        pygame.draw.rect(s, C_HUD, (0, ROWS * TILE, SCREEN_W, HUD_H))
        if self.num_players > 4:
            # 5~8 人:兩排精簡格
            f = get_font(14)
            cw = SCREEN_W // 4
            ch = HUD_H // 2
            for p in self.players:
                x0 = (p.id % 4) * cw + 8
                y0 = ROWS * TILE + (p.id // 4) * ch + 4
                pygame.draw.circle(s, p.color if p.alive else (90, 90, 100),
                                   (x0 + 9, y0 + 13), 8)
                pygame.draw.circle(s, (20, 20, 28), (x0 + 9, y0 + 13), 8, 2)
                if p.alive:
                    txt = T("P%d 泡%d 力%d 針%d" % (p.id + 1, p.max_bubbles,
                                                    p.power, p.needles),
                            "P%d B%d P%d N%d" % (p.id + 1, p.max_bubbles,
                                                 p.power, p.needles))
                    col = C_TEXT
                elif (self.turf or self.infect) and p.respawn_t > 0:
                    txt = T("P%d 復活%d" % (p.id + 1, math.ceil(p.respawn_t)),
                            "P%d BK%d" % (p.id + 1, math.ceil(p.respawn_t)))
                    col = (255, 210, 130)
                else:
                    txt = T("P%d 淘汰" % (p.id + 1), "P%d OUT" % (p.id + 1))
                    col = (150, 150, 160)
                s.blit(render_text(14, txt, col), (x0 + 22, y0 + 5))
                # 手持道具槽(小圖示)
                if p.alive and p.item_kind:
                    icx, icy = x0 + cw - 30, y0 + 13
                    pygame.draw.circle(s, (255, 255, 255), (icx, icy), 10)
                    pygame.draw.circle(s, (200, 200, 200), (icx, icy), 10, 1)
                    draw_item_icon_scaled(s, icx, icy, p.item_kind, 0.55)
                    ct = render_text(11, "x%d" % p.item_count, (255, 230, 140))
                    s.blit(ct, (icx + 9, icy + 2))
            return
        f = get_font(17)
        seg = SCREEN_W // self.num_players
        for p in self.players:
            x0 = p.id * seg + 12
            y0 = ROWS * TILE + 10
            pygame.draw.circle(s, p.color if p.alive else (90, 90, 100),
                               (x0 + 10, y0 + 22), 12)
            pygame.draw.circle(s, (20, 20, 28), (x0 + 10, y0 + 22), 12, 2)
            who = render_text(13, T("電腦", "CPU") if p.is_bot else p.name[:6],
                              (255, 255, 255))
            s.blit(who, who.get_rect(center=(x0 + 10, y0 + 48)))
            if p.alive:
                line1 = T("水球%d 威力%d 速度%.1f" % (p.max_bubbles, p.power, p.speed),
                          "BUB%d PWR%d SPD%.1f" % (p.max_bubbles, p.power, p.speed))
                flags = []
                if p.has_glove:
                    flags.append(T("拳", "G"))
                if p.has_kick:
                    flags.append(T("踢", "K"))
                if p.mount:
                    flags.append({"turtle": T("龜", "T"), "owl": T("鴞", "O"),
                                  "ufo": T("碟", "U")}[p.mount])
                if p.shield_t > 0:
                    flags.append(T("盾", "S"))
                if p.ghost_t > 0:
                    flags.append(T("隱", "I"))
                if p.curse_t > 0:
                    flags.append(T("咒", "X"))
                if p.item_kind:
                    it = ""
                else:
                    it = ""
                line2 = T("針%d %s" % (p.needles, "".join(flags)),
                          "PIN%d %s" % (p.needles, " ".join(flags)))
                col = C_TEXT
            elif (self.turf or self.infect) and p.respawn_t > 0:
                line1 = T("復活 %d" % math.ceil(p.respawn_t),
                          "BACK %d" % math.ceil(p.respawn_t))
                line2 = ""
                col = (255, 210, 130)
            else:
                line1 = T("已淘汰", "OUT")
                line2 = ""
                col = (150, 150, 160)
            s.blit(render_text(17, line1, col), (x0 + 30, y0 + 2))
            if line2:
                s.blit(render_text(17, line2, (190, 200, 215)),
                       (x0 + 30, y0 + 26))
            # 手持道具槽(圖示 + 數量)
            if p.alive and p.item_kind:
                icx = x0 + seg - 34
                icy = y0 + 22
                pygame.draw.circle(s, (255, 255, 255), (icx, icy), 15)
                pygame.draw.circle(s, (200, 200, 200), (icx, icy), 15, 2)
                draw_item_icon_scaled(s, icx, icy, p.item_kind, 0.8)
                badge = pygame.Rect(icx + 6, icy + 6, 16, 14)
                pygame.draw.rect(s, (40, 44, 56), badge, border_radius=5)
                ct = render_text(11, "x%d" % p.item_count, (255, 230, 140))
                s.blit(ct, ct.get_rect(center=badge.center))

    def draw_over(self, s):
        overlay = pygame.Surface((SCREEN_W, ROWS * TILE), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        s.blit(overlay, (0, 0))
        big = get_font(52)
        small = get_font(24)
        if self.boss_mode:
            if self.winner == "boss_win":
                msg = T("討伐成功!章魚王倒下了!", "VICTORY! The Octopus King falls!")
                col = (120, 230, 140)
            else:
                msg = T("全軍覆沒……", "Party wiped out...")
                col = (230, 120, 120)
        elif self.winner == "humans":
            msg = T("生存者守住了!", "SURVIVORS HOLD OUT!")
            col = (170, 240, 150)
        elif self.winner == "infected":
            msg = T("感染者全面勝利!", "THE INFECTED PREVAIL!")
            col = (120, 230, 100)
        elif self.winner in ("team0", "team1"):
            ix = int(self.winner[-1])
            if self.soccer:
                msg = T("%s獲勝!(%d:%d)"
                        % ("紅隊" if ix == 0 else "藍隊",
                           self.scores[0], self.scores[1]),
                        "%s WINS! (%d:%d)"
                        % ("RED" if ix == 0 else "BLUE",
                           self.scores[0], self.scores[1]))
            elif self.turf and self.turf_result:
                msg = T("%s佔地獲勝!(%d:%d 格)"
                        % (TURF_ZH[ix], self.turf_result[0],
                           self.turf_result[1]),
                        "%s WINS TURF! (%d:%d tiles)"
                        % (TURF_EN[ix], self.turf_result[0],
                           self.turf_result[1]))
            else:
                msg = T("%s獲勝!" % ("紅隊" if ix == 0 else "藍隊"),
                        "%s TEAM WINS!" % ("RED" if ix == 0 else "BLUE"))
            col = (235, 80, 80) if ix == 0 else (80, 130, 240)
        elif self.winner is not None:
            if self.winner.is_bot:
                msg = T("電腦(%s)獲勝!" % self.winner.name,
                        "CPU (%s) WINS!" % self.winner.name)
            else:
                msg = T("%s 獲勝!" % self.winner.name,
                        "%s WINS!" % self.winner.name)
            col = self.winner.color
        else:
            if self.turf and self.turf_result:
                msg = T("平手!(%d:%d 格)" % self.turf_result,
                        "DRAW! (%d:%d tiles)" % self.turf_result)
            else:
                msg = T("平手!", "DRAW!")
            col = (240, 240, 240)
        t1 = big.render(msg, True, col)
        if getattr(self, "net_play", False):
            if getattr(self, "net_is_host", False):
                hint = T("點下方「返回房間」與大家一起回大廳",
                         "Click 'Back to room' below to return to the lobby")
            else:
                hint = T("等待房主返回房間…(Esc 離開)",
                         "Waiting for the host to return to the room... (Esc leaves)")
            t2 = small.render(hint, True, (235, 235, 235))
            s.blit(t1, t1.get_rect(center=(SCREEN_W // 2, ROWS * TILE // 2 - 30)))
            s.blit(t2, t2.get_rect(center=(SCREEN_W // 2, ROWS * TILE // 2 + 30)))
            return
        hint = T("R 再來一局 / M 換地圖 / Esc 回選單",
                 "R restart / M change map / Esc menu")
        t2 = small.render(hint, True, (235, 235, 235))
        s.blit(t1, t1.get_rect(center=(SCREEN_W // 2, ROWS * TILE // 2 - 30)))
        s.blit(t2, t2.get_rect(center=(SCREEN_W // 2, ROWS * TILE // 2 + 30)))


# ----------------------------------------------------------------------
# 滑鼠按鈕 UI(每幀重建可點擊區域)
# ----------------------------------------------------------------------
class UI:
    def __init__(self):
        self.regions = []
        self.mouse = (0, 0)

    def begin(self, mouse):
        self.regions = []
        self.mouse = mouse

    def hotspot(self, rect, cid):
        """隱形可點擊區域(自訂繪製,例如地圖卡片、房間格位)。"""
        r = pygame.Rect(rect)
        self.regions.append((r, cid))
        return r.collidepoint(self.mouse)   # 回傳是否 hover

    def button(self, s, rect, label, cid, enabled=True, size=20,
               base=(52, 96, 168)):
        rect = pygame.Rect(rect)
        hov = enabled and rect.collidepoint(self.mouse)
        col = tuple(min(255, c + 34) for c in base) if hov else base
        if not enabled:
            col = (66, 72, 86)
        pygame.draw.rect(s, col, rect, border_radius=10)
        pygame.draw.rect(s, (255, 255, 255) if hov else (18, 24, 38),
                         rect, 2, border_radius=10)
        txt = render_text(size, label,
                          (255, 255, 255) if enabled else (150, 156, 170))
        s.blit(txt, txt.get_rect(center=rect.center))
        if enabled:
            self.regions.append((rect, cid))

    def click(self, pos):
        for rect, cid in self.regions:
            if rect.collidepoint(pos):
                return cid
        return None


ui = UI()


# ----------------------------------------------------------------------
# 標題畫面
# ----------------------------------------------------------------------
def draw_title(s, t):
    s.fill((30, 60, 96))
    for i in range(14):   # 背景泡泡
        x = (i * 137 + int(t * 30)) % (SCREEN_W + 80) - 40
        y = SCREEN_H - ((i * 211 + int(t * 55)) % (SCREEN_H + 120)) + 60
        r = 8 + (i * 7) % 22
        surf = pygame.Surface((r * 2 + 2, r * 2 + 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (150, 200, 255, 60), (r + 1, r + 1), r)
        pygame.draw.circle(surf, (220, 240, 255, 90), (r + 1, r + 1), r, 2)
        s.blit(surf, (x, y))

    big = get_font(60)
    mid = get_font(22)
    sml = get_font(17)

    bob = int(4 * math.sin(t * 1.8))
    title = big.render(T("泡泡大作戰", "BUBBLE BATTLE"), True, (255, 255, 255))
    sh2 = big.render(T("泡泡大作戰", "BUBBLE BATTLE"), True, (20, 40, 70))
    s.blit(sh2, sh2.get_rect(center=(SCREEN_W // 2 + 3, 128 + bob + 3)))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 128 + bob)))
    sub = mid.render(T("水球對戰・佔地・感染・足球・章魚王・連線",
                       "Battles, turf, outbreak, soccer, boss & online"),
                     True, (190, 220, 255))
    s.blit(sub, sub.get_rect(center=(SCREEN_W // 2, 182)))

    # 四大入口
    bw, bh, gap = 340, 58, 14
    bx = SCREEN_W // 2 - bw // 2
    y = 244
    ui.button(s, (bx, y, bw, bh), T("連線房間(最多 8 人)",
                                    "ONLINE ROOM (up to 8P)"),
              "net", size=23, base=(46, 140, 96))
    y += bh + gap
    ui.button(s, (bx, y, bw, bh), T("本機遊玩", "LOCAL PLAY"),
              "local", size=24, base=(64, 108, 190))
    y += bh + gap
    ui.button(s, (bx, y, bw, bh), T("道具圖鑑", "ITEM GUIDE"),
              "items", size=23, base=(120, 100, 60))
    y += bh + gap
    ui.button(s, (bx, y, bw, bh), T("遊戲教學", "HOW TO PLAY"),
              "tutorial", size=23, base=(150, 110, 170))
    y += bh + gap + 4
    ui.button(s, (SCREEN_W // 2 - 90, y, 180, 40), T("離開遊戲", "Quit"),
              "quit", size=17, base=(120, 60, 60))

    tips = [
        T("快捷鍵:N 連線   I 圖鑑   M 靜音   F11 全螢幕",
          "Hotkeys: N online   I guide   M mute   F11 fullscreen"),
    ]
    y = SCREEN_H - 40
    for line in tips:
        txt = sml.render(line, True, (215, 224, 240))
        s.blit(txt, txt.get_rect(center=(SCREEN_W // 2, y)))
        y += 24


def draw_pad_lobby(s, t, slots, n_pads):
    """手把派對大廳:鍵盤按動作鍵、手把按 A 加入;各自選角,全員準備後開戰。"""
    s.fill((26, 46, 76))
    big = get_font(36)
    mid = get_font(19)
    sml = get_font(15)
    title = big.render(T("手把派對(最多 8 人)", "PAD PARTY (up to 8P)"),
                       True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 46)))
    info = mid.render(T("偵測到手把:%d 支" % n_pads,
                        "Controllers detected: %d" % n_pads),
                      True, (170, 220, 255))
    s.blit(info, info.get_rect(center=(SCREEN_W // 2, 84)))

    cw, chh, gap = 168, 150, 8
    x0 = (SCREEN_W - cw * 4 - gap * 3) // 2
    y0 = 108
    for i in range(8):
        cx = x0 + (i % 4) * (cw + gap)
        cy = y0 + (i // 4) * (chh + gap)
        card = pygame.Rect(cx, cy, cw, chh)
        if i < len(slots):
            sl = slots[i]
            pygame.draw.rect(s, (44, 66, 100), card, border_radius=10)
            pygame.draw.rect(s, (120, 200, 140) if sl["ready"]
                             else (110, 140, 190), card, 3, border_radius=10)
            pn = mid.render("P%d" % (i + 1), True, (255, 230, 140))
            s.blit(pn, (cx + 10, cy + 8))
            srct = (T("鍵盤 %s", "KB %s") % KEYMAPS[sl["src"][1]]["label"]
                    if sl["src"][0] == "kb"
                    else T("手把 #%d", "Pad #%d") % sl["src"][1])
            st = sml.render(srct, True, (185, 205, 230))
            s.blit(st, (cx + 10, cy + 34))
            ch = CHAR_DEFS[sl["char"]]
            cn = mid.render(T(ch["zh"], ch["en"]), True, (255, 255, 255))
            s.blit(cn, cn.get_rect(center=(card.centerx, cy + 72)))
            hint = sml.render(T("← → 換角色", "arrows: char"), True,
                              (160, 180, 210))
            s.blit(hint, hint.get_rect(center=(card.centerx, cy + 96)))
            bar = pygame.Rect(cx + 10, cy + chh - 34, cw - 20, 24)
            if sl["ready"]:
                pygame.draw.rect(s, (60, 160, 96), bar, border_radius=7)
                rt = sml.render(T("準備完成 ✓", "READY"), True, (255, 255, 255))
            else:
                pygame.draw.rect(s, (70, 82, 104), bar, border_radius=7)
                rt = sml.render(T("再按一次準備", "press again: ready"),
                                True, (215, 224, 240))
            s.blit(rt, rt.get_rect(center=bar.center))
        else:
            pygame.draw.rect(s, (34, 50, 76), card, border_radius=10)
            pygame.draw.rect(s, (70, 90, 120), card, 2, border_radius=10)
            e1 = sml.render(T("鍵盤:按動作鍵加入", "KB: press action"),
                            True, (150, 170, 200))
            e2 = sml.render(T("手把:按 A 加入", "Pad: press A"),
                            True, (150, 170, 200))
            s.blit(e1, e1.get_rect(center=(card.centerx, card.centery - 12)))
            s.blit(e2, e2.get_rect(center=(card.centerx, card.centery + 12)))

    ready_all = len(slots) >= 2 and all(sl["ready"] for sl in slots)
    ui.button(s, (SCREEN_W // 2 - 210, SCREEN_H - 100, 200, 46),
              T("開始遊戲!", "START!"), "padstart", size=20,
              base=(46, 140, 96) if ready_all else (70, 80, 96))
    ui.button(s, (SCREEN_W // 2 + 10, SCREEN_H - 100, 200, 46),
              T("返回", "Back"), "back", size=20, base=(110, 70, 70))
    tips = sml.render(T("手把:A 加入/準備  B 取消  十字鍵/搖桿選角  戰鬥中 A放球 B道具 X技能 Y換槽",
                        "Pad: A join/ready  B cancel  dpad char | in-game: A bomb B item X skill Y swap"),
                      True, (200, 214, 235))
    s.blit(tips, tips.get_rect(center=(SCREEN_W // 2, SCREEN_H - 34)))


TUTORIAL_PAGES = [
    ("鍵盤操作", [
        ("head", "本機四組鍵位(同一鍵盤)"),
        ("row", "P1:WASD 移動|空白 放球|E / 左Ctrl 道具|Q 技能"),
        ("row", "P2:方向鍵 移動|Enter 放球|右Ctrl 道具|右Shift 技能"),
        ("row", "P3:IJKL 移動|O 放球|P 道具|U 技能"),
        ("row", "P4:數字鍵盤 8456 移動|0 放球|+ 道具|− 技能"),
        ("head", "連線房間中"),
        ("row", "方向鍵 移動|空白 放球|X 道具|C 技能|Z 換道具槽"),
        ("head", "通用"),
        ("row", "M 靜音|F11 全螢幕|Esc 返回上一頁"),
        ("row", "標題與本機選單可用數字鍵快速選模式"),
    ]),
    ("手把與觸控", [
        ("head", "藍牙 / USB 手把(隨插隨用)"),
        ("row", "左搖桿或十字鍵 移動"),
        ("row", "A 放球・射門|B 使用道具|X 角色技能|Y 換道具槽"),
        ("row", "連線房間中,主機與加入者都可直接用手把遊玩"),
        ("head", "手把派對(本機遊玩 → 手把派對)"),
        ("row", "手把按 A 加入,鍵盤按各自的放球鍵加入(最多 8 人)"),
        ("row", "←→ 或十字鍵選角色,再按一次加入鍵=準備,Start 開戰"),
        ("head", "螢幕觸控(安卓預設開啟)"),
        ("row", "左半螢幕按住拖曳=虛擬搖桿"),
        ("row", "右下:放球/道具/技能/換槽|左上 ≡ = 返回"),
        ("row", "標題左上角可切換「觸控按鍵」開關(改用手把時關閉)"),
    ]),
    ("遊戲基礎", [
        ("head", "水球"),
        ("row", "放下 3 秒後炸出十字水柱,水柱可連鎖引爆其他水球"),
        ("row", "被水柱噴到會被困進泡泡:持有「針」會自動掙脫,"),
        ("row", "隊友碰你=救援,敵人碰你=直接戳破!"),
        ("head", "成長"),
        ("row", "炸開木箱掉道具:威力/加彈/跑鞋…共 20 種(見道具圖鑑)"),
        ("row", "24 隻角色各有專屬技能,注意冷卻時間"),
        ("head", "終盤"),
        ("row", "狂熱:引信縮短、全員加速|場地崩塌:遠離閃紅的邊緣!"),
        ("row", "開場 3 秒倒數,金色箭頭=你的位置,出生點每場隨機"),
    ]),
    ("遊戲模式(上)", [
        ("head", "大亂鬥"),
        ("row", "1~8 人混戰,最後生存者獲勝"),
        ("head", "組隊戰"),
        ("row", "紅藍分隊,把對方全部泡爆"),
        ("head", "佔地大作戰(橘 vs 青)"),
        ("row", "水柱把地板染成隊色,陣亡 10 秒後復活"),
        ("row", "時間結束比哪隊佔地多,轟炸機會洗掉漆面"),
        ("head", "感染大作戰"),
        ("row", "開場 3 秒隨機一人感染爆發;被泡爆=3 秒後復活成感染者"),
        ("row", "生存者有人撐到時間結束就贏;最後的生存者會覺醒!"),
    ]),
    ("遊戲模式(下)", [
        ("head", "水球足球 4v4"),
        ("row", "把球帶進或射進敵方球門!持球會減速、被泡爆才掉球"),
        ("row", "放球鍵=射門(直線 6 格),碰隊友=傳球、碰敵人=被攔截"),
        ("head", "章魚王討伐"),
        ("row", "單人+電腦隊友或雙人合作,打倒巨大章魚王(三段難度)"),
        ("head", "連線房間(LAN 最多 8 人)"),
        ("row", "同一 Wi-Fi 即可連線;房主可調模式/地圖/道具/積分"),
        ("row", "電腦強度四級:初級/中級/高級/專家"),
        ("head", "手把派對"),
        ("row", "一台電腦,鍵盤+手把混搭,最多 8 人同樂"),
    ]),
]


def draw_tutorial(s, t, page):
    """遊戲教學:分頁介紹操作與模式。"""
    s.fill((28, 48, 80))
    big = get_font(34)
    zh, rows = TUTORIAL_PAGES[page]
    title = big.render(T("遊戲教學:%s" % zh, "HOW TO PLAY: %s" % zh),
                       True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 52)))

    panel = pygame.Rect(28, 92, SCREEN_W - 56, SCREEN_H - 208)
    pygame.draw.rect(s, (36, 58, 94), panel, border_radius=14)
    pygame.draw.rect(s, (80, 110, 160), panel, 2, border_radius=14)
    y = panel.y + 18
    for kind, text in rows:
        if kind == "head":
            ht = render_text(20, "◆ " + text, (255, 220, 120))
            s.blit(ht, (panel.x + 22, y))
            y += 32
        else:
            rt = render_text(17, text, (225, 234, 248))
            s.blit(rt, (panel.x + 44, y))
            y += 27

    # 頁碼圓點
    for i in range(len(TUTORIAL_PAGES)):
        col = (255, 230, 130) if i == page else (110, 130, 160)
        pygame.draw.circle(s, col,
                           (SCREEN_W // 2 - (len(TUTORIAL_PAGES) - 1) * 14
                            + i * 28, SCREEN_H - 96), 6)

    ui.button(s, (28, SCREEN_H - 70, 150, 44), T("← 上一頁", "← Prev"),
              "tprev", enabled=page > 0, size=18)
    ui.button(s, (SCREEN_W - 178, SCREEN_H - 70, 150, 44),
              T("下一頁 →", "Next →"), "tnext",
              enabled=page < len(TUTORIAL_PAGES) - 1, size=18)
    ui.button(s, (SCREEN_W // 2 - 75, SCREEN_H - 70, 150, 44),
              T("返回", "Back"), "back", size=18, base=(110, 70, 70))


def draw_local_menu(s, t):
    """本機遊玩選單:左欄經典對戰,右欄特殊模式與章魚王。"""
    s.fill((28, 52, 84))
    big = get_font(38)
    mid = get_font(22)
    sml = get_font(16)
    title = big.render(T("本機遊玩", "LOCAL PLAY"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 56)))

    bw, bh, gap = 280, 42, 10
    # 左欄:經典對戰
    head = mid.render(T("經典對戰", "CLASSIC"), True, (255, 230, 140))
    s.blit(head, head.get_rect(center=(SCREEN_W // 4 + 6, 110)))
    lx = SCREEN_W // 4 + 6 - bw // 2
    classic = [
        (("mode", 1), T("單人 vs 電腦×1", "1P vs CPU×1")),
        (("mode", 2), T("單人 vs 電腦×2", "1P vs CPU×2")),
        (("mode", 3), T("單人 vs 電腦×3", "1P vs CPU×3")),
        (("mode", 4), T("雙人對戰", "2P versus")),
        (("mode", 5), T("雙人 + 電腦×2", "2P + CPU×2")),
        (("mode", 6), T("三人對戰", "3P versus")),
        (("mode", 7), T("四人對戰", "4P versus")),
    ]
    y = 132
    for cid, label in classic:
        ui.button(s, (lx, y, bw, bh), label, cid, size=19)
        y += bh + gap

    # 右欄:特殊模式 + 章魚王
    head2 = mid.render(T("特殊模式", "SPECIAL"), True, (255, 230, 140))
    s.blit(head2, head2.get_rect(center=(SCREEN_W * 3 // 4 - 6, 110)))
    rx = SCREEN_W * 3 // 4 - 6 - bw // 2
    y = 132
    ui.button(s, (rx, y, bw, bh), T("佔地大作戰 4v4", "Turf War 4v4"),
              ("mode", 8), size=19, base=(150, 106, 40)); y += bh + gap
    ui.button(s, (rx, y, bw, bh), T("感染大作戰", "Outbreak"),
              ("mode", 9), size=19, base=(60, 130, 70)); y += bh + gap
    ui.button(s, (rx, y, bw, bh), T("水球足球 4v4", "Splash Soccer 4v4"),
              ("mode", 10), size=19, base=(52, 120, 150)); y += bh + gap
    note = sml.render(T("(特殊模式:1P + 電腦×7)", "(1P + CPU×7)"),
                      True, (185, 205, 230))
    s.blit(note, note.get_rect(center=(SCREEN_W * 3 // 4 - 6, y + 4)))
    y += 26
    ui.button(s, (rx, y, bw, bh), T("章魚王討伐(1P+電腦隊友)",
                                    "Octopus Boss (1P+CPU)"),
              "boss1", size=17, base=(150, 70, 120)); y += bh + gap
    ui.button(s, (rx, y, bw, bh), T("章魚王討伐(雙人合作)",
                                    "Octopus Boss (2P co-op)"),
              "boss2", size=17, base=(150, 70, 120)); y += bh + gap

    ui.button(s, (rx, y, bw, bh), T("手把派對(鍵盤+手把,8人)",
                                     "Pad Party (KB+pads, 8P)"),
              "padlobby", size=17, base=(170, 120, 50)); y += bh + gap

    ui.button(s, (SCREEN_W // 2 - 90, SCREEN_H - 96, 180, 42),
              T("返回", "Back"), "back", size=19, base=(110, 70, 70))

    tips = T("P1:WASD+空白+左Ctrl   P2:方向鍵+Enter+右Ctrl   P3:IJKL+O+P   P4:數字鍵盤",
             "P1: WASD+Space+LCtrl   P2: Arrows+Enter+RCtrl   P3: IJKL+O+P   P4: Numpad")
    txt = sml.render(tips, True, (215, 224, 240))
    s.blit(txt, txt.get_rect(center=(SCREEN_W // 2, SCREEN_H - 34)))

_PREVIEWS = {}


def get_preview(ix):
    """產生(並快取)地圖縮圖,使用固定亂數種子讓縮圖穩定。"""
    if ix not in _PREVIEWS:
        rng = random.Random(1234 + ix * 7)
        grid = build_grid(MAPS[ix], rng)
        cell = 10
        surf = pygame.Surface((COLS * cell, ROWS * cell))
        colors = MAPS[ix]["colors"]
        for r in range(ROWS):
            for c in range(COLS):
                t = grid[r][c]
                if t == HARD:
                    col = colors["hard"]
                elif t == SOFT:
                    col = colors["soft"]
                else:
                    col = colors["fa"] if (r + c) % 2 == 0 else colors["fb"]
                surf.fill(col, (c * cell, r * cell, cell, cell))
        for spec in MAPS[ix].get("feat", []):
            fr, fc = spec[1], spec[2]
            fcol = {"belt": (255, 214, 90), "mud": (70, 90, 52),
                "ice": (196, 228, 248), "spring": (220, 110, 110),
                "switch": (240, 200, 90), "gate": (120, 128, 146),
                    "cannon": (60, 64, 76), "portal": (200, 120, 255)}[spec[0]]
            pygame.draw.rect(surf, fcol, (fc * cell + 2, fr * cell + 2,
                                          cell - 4, cell - 4))
        pygame.draw.rect(surf, (30, 30, 40), surf.get_rect(), 2)
        _PREVIEWS[ix] = surf
    return _PREVIEWS[ix]


def draw_map_select(s, t, cur=None):
    s.fill((26, 34, 52))
    big = get_font(42)
    sml = get_font(20)
    tiny = get_font(17)

    title = big.render(T("選擇地圖", "SELECT MAP"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 55)))
    hint = sml.render(T("點選地圖卡片(共 %d 張),0 隨機,Esc 返回" % len(MAPS),
                        "Click a map (%d total), 0 = random, Esc = back" % len(MAPS)),
                      True, (255, 230, 140))
    hint.set_alpha(int(255 * (0.65 + 0.35 * math.sin(t * 4))))
    s.blit(hint, hint.get_rect(center=(SCREEN_W // 2, 100)))

    cols_n = 4 if len(MAPS) <= 20 else 6
    rows_n = (len(MAPS) + cols_n - 1) // cols_n
    cw = (SCREEN_W - 32) // cols_n
    ch = min(205, (SCREEN_H - 190) // rows_n)
    compact = ch < 170
    x0 = (SCREEN_W - cw * cols_n) // 2
    y0 = 118
    extra = {
        2: T("移速+18%", "+18% speed"),
        3: T("道具豐富", "rich drops"),
        4: T("箱子超多", "dense boxes"),
        6: T("中央開闊", "open center"),
    }
    for i, m in enumerate(MAPS):
        cx = x0 + (i % cols_n) * cw
        cy = y0 + (i // cols_n) * ch
        card = pygame.Rect(cx + 6, cy + 6, cw - 12, ch - 12)
        hov = ui.hotspot(card, ("map", i))
        chosen = (cur == i)
        base = (56, 70, 100) if hov else (44, 54, 76)
        if chosen:
            base = (58, 88, 70)
        pygame.draw.rect(s, base, card, border_radius=10)
        pygame.draw.rect(s, (255, 220, 120) if chosen
                         else ((255, 230, 140) if hov else (96, 116, 156)),
                         card, 3 if chosen else 2, border_radius=10)
        pv = get_preview(i)
        if compact:
            ph = ch - 44
            pw = int(pv.get_width() * ph / pv.get_height())
            pv = pygame.transform.smoothscale(pv, (pw, ph))
            s.blit(pv, (cx + (cw - pw) // 2, cy + 10))
        else:
            s.blit(pv, (cx + (cw - pv.get_width()) // 2, cy + 20))
        if i < 9:
            num = tiny.render("[%d]" % (i + 1), True, (255, 230, 140))
            s.blit(num, (card.x + 6, card.y + 3))
        name = (tiny if compact else sml).render(T(m["zh"], m["en"]),
                                                 True, (240, 244, 252))
        s.blit(name, name.get_rect(center=(cx + cw // 2, cy + ch - 18 if compact
                                           else cy + ch - 38)))
        if not compact and i in extra:
            tag = tiny.render(extra[i], True, (170, 210, 255))
            s.blit(tag, tag.get_rect(center=(cx + cw // 2, cy + ch - 18)))
    by = y0 + rows_n * ch + 6
    # 隨機地圖:問號卡片(選定後每場開局才隨機挑圖)
    rcard = pygame.Rect(SCREEN_W // 2 - 200, by, 190, 48)
    rhov = ui.hotspot(rcard, ("map", -1))
    rbase = (40, 96, 70)
    if cur == -1:
        rbase = (56, 128, 86)
    if rhov:
        rbase = tuple(min(255, v + 18) for v in rbase)
    pygame.draw.rect(s, rbase, rcard, border_radius=10)
    pygame.draw.rect(s, (255, 220, 120) if cur == -1 else (110, 190, 150),
                     rcard, 3 if cur == -1 else 2, border_radius=10)
    qf = get_font(30)
    wob = int(2 * math.sin(t * 4))
    qm = qf.render("?", True, (255, 235, 150))
    s.blit(qm, qm.get_rect(center=(rcard.x + 28, rcard.centery + wob)))
    rl = get_font(18).render(T("隨機地圖", "Random map"), True, (235, 245, 240))
    s.blit(rl, rl.get_rect(midleft=(rcard.x + 52, rcard.centery)))
    ui.button(s, (SCREEN_W // 2 + 10, by + 4, 180, 40),
              T("返回", "Back"), "back", size=19, base=(110, 70, 70))


# ----------------------------------------------------------------------
# 區域連線(LAN)對戰
#   主機權威:客戶端每幀送按鍵,主機模擬並以 ~30Hz 廣播狀態快照。
#   同一份程式可走 Wi-Fi、手機熱點、或系統層藍牙 PAN 網路共享。
# ----------------------------------------------------------------------
NET_PORT = 17641
SNAPSHOT_EVERY = 1      # 每幀送快照(60Hz,搭配 TCP_NODELAY)


def get_local_ip():
    """取得本機區網 IP(不會真的發出封包)。"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


class LineConn:
    """非阻塞的「一行一則 JSON」連線,含送出緩衝。"""

    def __init__(self, sock):
        self.sock = sock
        try:
            # 關閉 Nagle 演算法:小封包立即送出(延遲問題的主因)
            self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except OSError:
            pass
        self.sock.setblocking(False)
        self.inbuf = b""
        self.outbuf = b""
        self.closed = False

    def send_json(self, obj):
        if self.closed:
            return
        self.outbuf += (json.dumps(obj, separators=(",", ":")) + "\n").encode()
        self.flush()

    def flush(self):
        if self.closed or not self.outbuf:
            return
        try:
            n = self.sock.send(self.outbuf)
            self.outbuf = self.outbuf[n:]
        except (BlockingIOError, InterruptedError):
            pass
        except OSError:
            self.closed = True

    def poll(self):
        """回傳這一輪收到的 JSON 物件清單;連線中斷時設 closed。"""
        msgs = []
        if self.closed:
            return msgs
        try:
            while True:
                data = self.sock.recv(65536)
                if not data:          # 對方關閉連線
                    self.closed = True
                    break
                self.inbuf += data
        except (BlockingIOError, InterruptedError):
            pass
        except OSError:
            self.closed = True
        while b"\n" in self.inbuf:
            line, self.inbuf = self.inbuf.split(b"\n", 1)
            if line.strip():
                try:
                    msgs.append(json.loads(line.decode()))
                except (ValueError, UnicodeDecodeError):
                    pass
        return msgs

    def close(self):
        self.closed = True
        try:
            self.sock.close()
        except OSError:
            pass


PLAYER_NET_FIELDS = ("alive", "trapped", "trap_timer", "facing", "max_bubbles",
                     "power", "speed", "needles", "item_kind", "item_count",
                     "has_glove", "has_kick", "mount", "ghost_t", "shield_t",
                     "radar_t", "curse_t", "team", "frozen_t", "slot_a", "slot_b", "char", "skill_cd", "name", "wet_t", "daze_t", "respawn_t", "infected")


def make_snapshot(g):
    """把主機的遊戲狀態壓成可傳輸的快照。"""
    if g.winner is None or isinstance(g.winner, str):
        winner = g.winner
    else:
        winner = g.winner.id
    d = {
        "t": "st",
        "time": round(g.time, 3),
        "over": g.over,
        "winner": winner,
        "grid": "".join(str(v) for row in g.grid for v in row),
        "players": [
            [round(p.x, 1), round(p.y, 1)] + [getattr(p, f) for f in PLAYER_NET_FIELDS]
            for p in g.players],
        "bubbles": [[b.r, b.c, round(b.timer, 2), 1 if b.remote else 0,
                     1 if b.xshape else 0]
                    for b in g.bubbles],
        "blasts": [[r, c, round(t, 2)] for (r, c), t in g.blasts.items()],
        "items": [[r, c, k] for (r, c), k in g.items.items()],
        "effects": g.effects,
        "incoming": [[m[0], m[1], round(m[2], 2)] for m in g.incoming],
        "minions": [[round(mn.x, 1), round(mn.y, 1)] for mn in g.minions],
        "tl": None if g.match_left is None else round(g.match_left, 1),
        "fall": [[r, c, round(t, 2)] for (r, c), t in g.falling.items()],
        "ms": [[round(m["x"], 1), round(m["y"], 1), m["dx"], m["dy"]]
               for m in g.missiles],
        "hz": g.hazards,
        "tf": 1 if g.turf else 0,
        "if": 1 if g.infect else 0,
        "so": 1 if g.soccer else 0,
        "bl": ([g.ball["carrier"] if g.ball["carrier"] is not None else -1,
                round(g.ball["x"], 1), round(g.ball["y"], 1)]
               if g.ball else None),
        "sc2": g.scores,
        "gp": round(g.goal_pause, 2),
        "cd": round(g.countdown, 2),
        "gf": round(g.go_flash, 2),
        "fd": [[fe["k"], fe["v"], fe["m"], fe["s"], round(fe["t"], 2),
                fe.get("e", "")]
               for fe in g.feed],
        "pt": [[r, c, v] for (r, c), v in g.paint.items()],
        "tr": g.turf_result,
        "tp": g.traps,
        "pd": g.puddles,
        "sk": g.strikes,
        "dr": g.drops,
        "an": g.announce,
    }
    if g.boss is not None:
        bz = g.boss
        d["boss"] = [round(bz.cx, 1), round(bz.cy, 1), bz.hp,
                     round(bz.flash, 2), bz.taunt, round(bz.taunt_t, 2),
                     bz.max_hp, bz.diff_ix]
    return d


def apply_snapshot(view, d):
    """把快照套到客戶端的顯示用 Game 物件上。"""
    view.time = d["time"]
    view.over = d["over"]
    w = d["winner"]
    view.winner = view.players[w] if isinstance(w, int) else w
    flat = d["grid"]
    for r in range(ROWS):
        for c in range(COLS):
            view.grid[r][c] = int(flat[r * COLS + c])
    for p, arr in zip(view.players, d["players"]):
        p.x, p.y = arr[0], arr[1]
        for f, v in zip(PLAYER_NET_FIELDS, arr[2:]):
            setattr(p, f, v)
        p.anim = view.time + p.id
    view.bubbles = []
    for bd in d["bubbles"]:
        r, c, t = bd[0], bd[1], bd[2]
        rm = len(bd) > 3 and bd[3]
        b = Bubble(r, c, None, 1)
        b.timer = t
        b.remote = bool(rm)
        b.xshape = bool(len(bd) > 4 and bd[4])
        view.bubbles.append(b)
    view.blasts = {(r, c): t for (r, c, t) in d["blasts"]}
    view.items = {(r, c): k for (r, c, k) in d["items"]}
    view.effects = d["effects"]
    view.incoming = [list(m) for m in d["incoming"]]
    view.match_left = d.get("tl")
    view.falling = {(r, c): t for (r, c, t) in d.get("fall", [])}
    view.missiles = [dict(x=x, y=y, dx=dx, dy=dy, owner=None)
                     for (x, y, dx, dy) in d.get("ms", [])]
    view.hazards = d.get("hz") or []
    view.turf = bool(d.get("tf"))
    view.infect = bool(d.get("if"))
    view.soccer = bool(d.get("so"))
    bl = d.get("bl")
    view.ball = (dict(carrier=(None if bl[0] < 0 else bl[0]),
                      x=bl[1], y=bl[2]) if bl else None)
    view.scores = d.get("sc2") or [0, 0]
    view.goal_pause = d.get("gp") or 0.0
    view.countdown = d.get("cd") or 0.0
    view.go_flash = d.get("gf") or 0.0
    old_fd = {(fe["k"], fe["v"], fe["m"], fe["s"], fe.get("e", "")): fe
              for fe in getattr(view, "feed", [])}
    view.feed = [old_fd.get((k, v, m, s2, e2))
                 or dict(k=k, v=v, m=m, s=s2, t=t2, e=e2)
                 for (k, v, m, s2, t2, e2) in d.get("fd") or []]
    for fe, row in zip(view.feed, d.get("fd") or []):
        fe["t"] = row[4]
    view.paint = {(r, c): v for (r, c, v) in d.get("pt") or []}
    view.turf_result = d.get("tr")
    view.traps = d.get("tp") or []
    view.puddles = d.get("pd") or []
    view.strikes = d.get("sk") or []
    view.drops = d.get("dr") or []
    view.announce = d.get("an")
    view.minions = []
    for (x, y) in d["minions"]:
        mn = Minion(1, 1)
        mn.x, mn.y = x, y
        mn.anim = view.time
        view.minions.append(mn)
    if view.boss is not None and "boss" in d:
        bz = view.boss
        arr = d["boss"]
        bz.cx, bz.cy, bz.hp, bz.flash, bz.taunt, bz.taunt_t = arr[:6]
        if len(arr) >= 8:
            bz.max_hp = arr[6]
            bz.diff_ix = arr[7] % len(BOSS_DIFFS)
            bz.cfg = BOSS_DIFFS[bz.diff_ix]
        bz.anim = view.time


# ----------------------------------------------------------------------
# 道具圖鑑
# ----------------------------------------------------------------------
def draw_item_book(s, t):
    s.fill((30, 38, 58))
    big = get_font(38)
    name_f = get_font(19)
    desc_f = get_font(14)
    sml = get_font(18)

    title = big.render(T("道具圖鑑", "ITEM GUIDE"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 40)))
    hint = sml.render(T("箱子和場地上都會出現道具!",
                        "Items appear from boxes & on the field!"),
                      True, (255, 230, 140))
    s.blit(hint, hint.get_rect(center=(SCREEN_W // 2 - 80, 78)))
    ui.button(s, (SCREEN_W - 150, 58, 120, 36), T("返回", "Back"), "back",
              size=18, base=(110, 70, 70))

    cols = 2
    n_items = len(ITEM_ORDER)
    rows = (n_items + cols - 1) // cols
    cell_w = SCREEN_W // cols
    cell_h = min(71, (SCREEN_H - 104) // rows)
    compact = cell_h < 64
    y0 = 100
    for i, kind in enumerate(ITEM_ORDER):
        d = ITEM_DEFS[kind]
        cx0 = (i % cols) * cell_w
        cy0 = y0 + (i // cols) * cell_h
        card = pygame.Rect(cx0 + 10, cy0 + 3, cell_w - 20, cell_h - 6)
        pygame.draw.rect(s, (44, 54, 78), card, border_radius=8)
        # 圖示(白底圓,和遊戲內相同)
        rad = 15 if compact else 19
        icx, icy = card.x + 30, card.centery
        bob = int(1.5 * math.sin(t * 3 + i))
        pygame.draw.circle(s, (255, 255, 255), (icx, icy + bob), rad)
        pygame.draw.circle(s, (200, 200, 200), (icx, icy + bob), rad, 2)
        draw_item_icon(s, icx, icy + bob, kind)
        # 名稱與說明
        nf = get_font(16) if compact else name_f
        df = get_font(12) if compact else desc_f
        name = nf.render(T(d["zh"], d["en"]), True, (255, 240, 180))
        s.blit(name, (card.x + 56, card.y + 3 if compact else card.y + 6))
        if d.get("ext"):
            tag = get_font(11).render(T("擴充", "EXT"), True, (150, 240, 190))
            tr = tag.get_rect(topleft=(card.x + 56 + name.get_width() + 8,
                                       card.y + 6 if compact else card.y + 10))
            pygame.draw.rect(s, (40, 90, 70), tr.inflate(8, 4), border_radius=5)
            s.blit(tag, tr)
        line_h = 14 if compact else 17
        dy0 = card.y + (22 if compact else 29)
        for j, line in enumerate(T(d["dz"], d["de"])):
            txt = df.render(line, True, (220, 228, 240))
            s.blit(txt, (card.x + 56, dy0 + j * line_h))


# ----------------------------------------------------------------------
# 連線畫面
# ----------------------------------------------------------------------
def draw_room_menu(s, t, notice):
    s.fill((26, 34, 52))
    big = get_font(40)
    sml = get_font(19)
    title = big.render(T("連線房間", "ONLINE ROOM"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 110)))
    bw, bh = 320, 56
    x = SCREEN_W // 2 - bw // 2
    ui.button(s, (x, 190, bw, bh), T("建立房間(我當房主)", "Create a room (be the host)"),
              "host", size=22, base=(46, 140, 96))
    ui.button(s, (x, 190 + 76, bw, bh), T("加入房間(輸入主機 IP)", "Join a room (enter host IP)"),
              "join", size=22)
    ui.button(s, (x, 190 + 152, bw, bh), T("返回標題", "Back to title"),
              "back", size=22, base=(110, 70, 70))
    lines = [
        T("最多 8 人同場!兩台以上裝置需在同一網路:", "Up to 8 players! All devices must share a network:"),
        T("同 Wi-Fi、手機/平板熱點,或藍牙 PAN 網路共享皆可", "same Wi-Fi, a phone hotspot, or Bluetooth PAN"),
    ]
    y = 470
    for line in lines:
        txt = sml.render(line, True, (220, 228, 244))
        s.blit(txt, txt.get_rect(center=(SCREEN_W // 2, y)))
        y += 30
    if notice:
        n = sml.render(notice, True, (255, 140, 140))
        s.blit(n, n.get_rect(center=(SCREEN_W // 2, SCREEN_H - 40)))


def _draw_slot_avatar(s, cx, cy, color, rad=22):
    """格位裡的小角色頭像(原創圖形)。"""
    pygame.draw.ellipse(s, color, (cx - rad, cy - rad, rad * 2, rad * 2))
    dark = tuple(max(0, v - 60) for v in color)
    pygame.draw.ellipse(s, dark, (cx - rad, cy - rad, rad * 2, rad * 2), 3)
    for dd in (-8, 8):
        pygame.draw.circle(s, (255, 255, 255), (cx + dd, cy - 4), 6)
        pygame.draw.circle(s, (30, 30, 40), (cx + dd, cy - 3), 3)


def _draw_crown(s, cx, cy):
    """房主皇冠(原創圖形)。"""
    pts = [(cx - 14, cy + 6), (cx - 14, cy - 4), (cx - 7, cy + 1),
           (cx, cy - 8), (cx + 7, cy + 1), (cx + 14, cy - 4), (cx + 14, cy + 6)]
    pygame.draw.polygon(s, (255, 210, 70), pts)
    pygame.draw.polygon(s, (170, 130, 30), pts, 2)


def draw_room(s, t, slots, mode, map_ix, is_host, my_pid, notice, diff_ix=1,
              items_ext=False, cpu_lv=1):
    """房間大廳:8 個玩家格位 + 房主控制列。
    slots: 長度 8 的清單,每項 {"k":"host"/"hu"/"cpu"/"emp", "r":bool}
    """
    s.fill((28, 52, 84))
    for i in range(10):   # 背景泡泡
        x = (i * 173 + int(t * 24)) % (SCREEN_W + 60) - 30
        y = SCREEN_H - ((i * 149 + int(t * 40)) % (SCREEN_H + 100)) + 50
        r = 6 + (i * 5) % 16
        surf = pygame.Surface((r * 2 + 2, r * 2 + 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (150, 200, 255, 40), (r + 1, r + 1), r)
        s.blit(surf, (x, y))

    big = get_font(34)
    sml = get_font(17)
    tiny = get_font(15)
    title = big.render(T("遊戲房間", "GAME ROOM"), True, (255, 255, 255))
    s.blit(title, title.get_rect(midleft=(24, 40)))
    ipt = get_font(20).render(T("房間 IP:%s" % get_local_ip(),
                                "Room IP: %s" % get_local_ip())
                              if is_host else
                              T("你是 P%d" % (my_pid + 1), "You are P%d" % (my_pid + 1)),
                              True, (255, 230, 140))
    ir = ipt.get_rect(midright=(SCREEN_W - 24, 40))
    pygame.draw.rect(s, (40, 66, 104), ir.inflate(20, 12), border_radius=8)
    s.blit(ipt, ir)

    # 8 個格位(4x2)
    cw, chh = 172, 190
    x0 = (SCREEN_W - cw * 4) // 2
    y0 = 76
    for i in range(MAX_PLAYERS):
        cx0 = x0 + (i % 4) * cw
        cy0 = y0 + (i // 4) * chh
        card = pygame.Rect(cx0 + 6, cy0 + 6, cw - 12, chh - 12)
        info = slots[i]
        kind = info.get("k", "emp")
        team = info.get("t")
        clickable = is_host and kind in ("emp", "cpu")
        if mode in ("team", "turf", "soccer"):
            # 組隊戰:房主點任何佔用格換隊;加入者點自己的格位換隊
            if is_host and kind in ("hu", "host"):
                clickable = True
            if (not is_host) and i == my_pid:
                clickable = True
        hov = False
        if clickable:
            hov = ui.hotspot(card, ("slot", i))
        base = (38, 70, 110) if kind != "emp" else (34, 50, 74)
        if mode in ("team", "turf", "soccer") and team is not None and kind != "emp":
            base = (74, 44, 52) if team == 0 else (40, 56, 96)
        if hov:
            base = tuple(min(255, c + 22) for c in base)
        pygame.draw.rect(s, base, card, border_radius=12)
        border = (255, 230, 140) if i == my_pid else (90, 120, 160)
        pygame.draw.rect(s, border, card, 3 if i == my_pid else 2, border_radius=12)
        num = tiny.render("P%d" % (i + 1), True, (200, 214, 235))
        s.blit(num, (card.x + 8, card.y + 6))

        cxm = card.centerx
        if kind == "emp":
            txt = sml.render(T("空位", "Empty"), True, (150, 165, 190))
            s.blit(txt, txt.get_rect(center=(cxm, card.centery - 8)))
            if is_host:
                tip = tiny.render(T("點擊加入電腦", "Click to add CPU"),
                                  True, (120, 190, 150))
                s.blit(tip, tip.get_rect(center=(cxm, card.centery + 20)))
            continue
        ch_ix = info.get("c", 0)
        draw_char_icon(s, cxm, card.y + 62, ch_ix, PLAYER_COLORS[i], rad=17)
        cn = tiny.render(T(CHAR_DEFS[ch_ix]["zh"], CHAR_DEFS[ch_ix]["en"]),
                         True, (200, 216, 240))
        s.blit(cn, cn.get_rect(center=(cxm, card.y + 88)))
        if kind == "host":
            _draw_crown(s, cxm, card.y + 30)
        pname = info.get("n") or ""
        if pname:
            name = pname[:8]
        elif kind == "host":
            name = T("房主", "HOST")
        elif kind == "cpu":
            name = T("電腦", "CPU")
        else:
            name = T("玩家", "PLAYER")
        nt = sml.render(name, True, (240, 246, 255))
        s.blit(nt, nt.get_rect(center=(cxm, card.y + 106)))
        # 積分模式:星星積分徽章(配色取自卡片底色,自動搭配各模式)
        if "s" in info:
            sb = pygame.Rect(card.right - 58, card.y + 28, 50, 20)
            pill = tuple(int(v * 0.55) for v in base)
            edge = tuple(min(255, v + 55) for v in base)
            pygame.draw.rect(s, pill, sb, border_radius=10)
            pygame.draw.rect(s, edge, sb, 1, border_radius=10)
            star = tiny.render("★", True, (255, 214, 90))
            num = tiny.render("%d" % info["s"], True, (240, 246, 255))
            tw = star.get_width() + 2 + num.get_width()
            sx = sb.centerx - tw // 2
            s.blit(star, (sx, sb.centery - star.get_height() // 2))
            s.blit(num, (sx + star.get_width() + 2,
                         sb.centery - num.get_height() // 2))
        # 組隊戰/佔地:隊伍徽章
        if mode in ("team", "turf", "soccer") and team is not None:
            if mode == "turf":
                bt = TURF_COLS[team % 2]
                tcol = tuple(int(v * 0.62) for v in bt)
            else:
                tcol = (215, 70, 70) if team == 0 else (70, 110, 220)
            tb = pygame.Rect(card.right - 58, card.y + 6, 50, 20)
            pygame.draw.rect(s, tcol, tb, border_radius=6)
            tt = tiny.render((T(TURF_ZH[team % 2], TURF_EN[team % 2])
                              if mode == "turf" else
                              (T("紅隊", "RED") if team == 0
                               else T("藍隊", "BLUE"))),
                             True, (255, 255, 255))
            s.blit(tt, tt.get_rect(center=tb.center))
        # 準備狀態橫幅
        ready = (kind in ("host", "cpu")) or info.get("r", False)
        bar = pygame.Rect(card.x + 12, card.bottom - 40, card.w - 24, 28)
        if ready:
            pygame.draw.rect(s, (60, 160, 96), bar, border_radius=8)
            rt = tiny.render(T("準備完成 ✓", "READY ✓"), True, (255, 255, 255))
        else:
            pygame.draw.rect(s, (70, 82, 104), bar, border_radius=8)
            rt = tiny.render(T("等待中…", "waiting..."), True, (210, 218, 232))
        s.blit(rt, rt.get_rect(center=bar.center))
        if is_host and hov:
            if mode in ("team", "turf", "soccer"):
                tip = (T("點擊換隊/移除", "click: team / remove") if kind == "cpu"
                       else T("點擊換隊", "click to swap team"))
            elif kind == "cpu":
                tip = T("點擊移除", "click to remove")
            else:
                tip = None
            if tip:
                xt = tiny.render(tip, True, (255, 200, 150))
                s.blit(xt, xt.get_rect(center=(cxm, card.y + 124)))
        elif (not is_host) and hov and mode in ("team", "turf", "soccer"):
            xt = tiny.render(T("點擊換隊", "click to swap team"), True, (255, 200, 150))
            s.blit(xt, xt.get_rect(center=(cxm, card.y + 124)))

    # 底部控制列
    by = y0 + 2 * chh + 10
    total = sum(1 for sl in slots if sl.get("k") != "emp")
    humans_ready = all(sl.get("r", False) for sl in slots if sl.get("k") == "hu")
    if mode == "boss":
        mode_label = T("模式:章魚王討伐(合作)", "Mode: Octopus Boss (co-op)")
    elif mode == "team":
        mode_label = T("模式:組隊戰(紅vs藍)", "Mode: Team Battle (R vs B)")
    elif mode == "turf":
        mode_label = T("模式:佔地大作戰(橘vs青)", "Mode: Turf War (O vs T)")
    elif mode == "infect":
        mode_label = T("模式:感染大作戰", "Mode: Outbreak")
    elif mode == "soccer":
        mode_label = T("模式:水球足球(紅vs藍)", "Mode: Splash Soccer")
    else:
        mode_label = T("模式:大亂鬥(對戰)", "Mode: Battle (versus)")
    diff_label = T("難度:%s" % BOSS_DIFFS[diff_ix]["zh"],
                   "Difficulty: %s" % BOSS_DIFFS[diff_ix]["en"])
    if mode == "boss":
        map_label = T("地圖:深海王座", "Map: Abyss Throne")
    elif map_ix is None or map_ix < 0:
        map_label = T("地圖:隨機 ?", "Map: Random ?")
    else:
        map_label = T("地圖:%s" % MAPS[map_ix]["zh"],
                      "Map: %s" % MAPS[map_ix]["en"])
    items_label = (T("道具:擴充(20 種)", "Items: Extended (20)") if items_ext
                   else T("道具:普通(16 種)", "Items: Standard (16)"))
    if is_host:
        ch_label = T("角色:%s ▼" % CHAR_DEFS[slots[0].get("c", 0)]["zh"],
                     "Char: %s v" % CHAR_DEFS[slots[0].get("c", 0)]["en"])
        cpu_label = T("電腦:%s" % BOT_LEVELS[cpu_lv]["zh"],
                      "CPU: %s" % BOT_LEVELS[cpu_lv]["en"])
        ui.button(s, (24, by + 52, 140, 44), items_label, "items_toggle",
                  size=14,
                  base=(60, 130, 110) if items_ext else (70, 90, 120))
        ui.button(s, (172, by + 52, 150, 44), cpu_label, "cpulv_cycle",
                  size=16, base=(60, 100, 160 + cpu_lv * 25))
        ui.button(s, (330, by + 52, 150, 44), ch_label, "char_cycle", size=15,
                  base=(96, 84, 150))
        score_on = any("s" in sl for sl in slots if sl.get("k") != "emp")
        ui.button(s, (488, by + 52, 110, 44),
                  T("積分:開", "Score: ON") if score_on else T("積分:關", "Score: OFF"),
                  "score_toggle", size=15,
                  base=(150, 120, 40) if score_on else (70, 90, 120))
        if score_on:
            ui.button(s, (602, by + 52, 90, 44), T("重新計分", "Reset"),
                      "score_reset", size=14, base=(120, 60, 60))
        ui.button(s, (24, by, 210, 44), mode_label, "mode_toggle", size=16,
                  base=(150, 70, 120) if mode == "boss"
                  else ((150, 100, 50) if mode == "team" else (52, 96, 168)))
        if mode == "boss":
            ui.button(s, (244, by, 200, 44), diff_label, "diff_cycle", size=16,
                      base=(170, 90, 60))
        else:
            ui.button(s, (244, by, 200, 44), map_label, "map_pick", size=16,
                      base=(120, 100, 60))
        ui.button(s, (454, by, 130, 44),
                  T("開始遊戲", "START"), "start", size=19,
                  enabled=(total >= 2 and humans_ready), base=(46, 140, 96))
        ui.button(s, (594, by, 100, 44), T("關閉房間", "Close"), "leave",
                  size=16, base=(120, 60, 60))
        if not (total >= 2 and humans_ready):
            tip = tiny.render(T("需要至少 2 位參加者,且所有玩家準備完成",
                                "Need 2+ participants and all players ready"),
                              True, (255, 210, 150))
            s.blit(tip, tip.get_rect(midleft=(24, by + 62)))
    else:
        info = mode_label + "    " + (diff_label if mode == "boss" else map_label)
        info += "    " + T("電腦:%s" % BOT_LEVELS[cpu_lv]["zh"],
                           "CPU: %s" % BOT_LEVELS[cpu_lv]["en"])
        s.blit(sml.render(info, True, (210, 224, 245)), (24, by + 4))
        s.blit(sml.render(items_label, True, (170, 220, 200)), (24, by + 32))
        me_ready = slots[my_pid].get("r", False) if 0 <= my_pid < MAX_PLAYERS else False
        ui.button(s, (SCREEN_W - 340, by, 200, 44),
                  T("取消準備", "Unready") if me_ready else T("準備!", "READY!"),
                  "ready", size=19,
                  base=(120, 100, 60) if me_ready else (46, 140, 96))
        my_ch = slots[my_pid].get("c", 0) if 0 <= my_pid < MAX_PLAYERS else 0
        ch_label = T("角色:%s ▼" % CHAR_DEFS[my_ch]["zh"],
                     "Char: %s v" % CHAR_DEFS[my_ch]["en"])
        ui.button(s, (SCREEN_W - 340, by + 52, 200, 44), ch_label, "char_cycle",
                  size=16, enabled=not me_ready, base=(96, 84, 150))
        if me_ready:
            tipc = tiny.render(T("取消準備後才能更換角色", "Unready to change character"),
                               True, (200, 190, 230))
            s.blit(tipc, (SCREEN_W - 340, by + 100))
        ui.button(s, (SCREEN_W - 128, by, 104, 44), T("離開", "Leave"), "leave",
                  size=17, base=(120, 60, 60))
    if notice:
        n = tiny.render(notice, True, (255, 150, 150))
        s.blit(n, n.get_rect(center=(SCREEN_W // 2, SCREEN_H - 12)))


def draw_net_join(s, t, ip_text, notice):
    s.fill((26, 34, 52))
    big = get_font(36)
    sml = get_font(19)
    title = big.render(T("加入房間", "Join a room"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 130)))
    tip = sml.render(T("輸入房主畫面顯示的房間 IP", "Type the room IP shown on the host's screen"),
                     True, (220, 226, 240))
    s.blit(tip, tip.get_rect(center=(SCREEN_W // 2, 185)))
    cursor = "_" if int(t * 2) % 2 == 0 else " "
    field = get_font(34).render(ip_text + cursor, True, (255, 230, 140))
    fr = field.get_rect(center=(SCREEN_W // 2, 270))
    pygame.draw.rect(s, (44, 54, 78), pygame.Rect(SCREEN_W // 2 - 190, 240, 380, 60),
                     border_radius=12)
    s.blit(field, fr)
    ui.button(s, (SCREEN_W // 2 - 190, 330, 180, 48), T("連線", "Connect"),
              "connect", size=20, base=(46, 140, 96))
    ui.button(s, (SCREEN_W // 2 + 10, 330, 180, 48), T("返回", "Back"),
              "back", size=20, base=(110, 70, 70))
    if notice:
        n = sml.render(notice, True, (255, 140, 140))
        s.blit(n, n.get_rect(center=(SCREEN_W // 2, 410)))


# ----------------------------------------------------------------------
# 章魚王難度選擇
# ----------------------------------------------------------------------
def draw_boss_diff(s, t):
    s.fill((24, 40, 66))
    big = get_font(40)
    sml = get_font(18)
    title = big.render(T("選擇討伐難度", "SELECT DIFFICULTY"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 80)))

    descs = [
        T("血量低、攻擊慢、自帶 3 支針", "Low HP, slow attacks, 3 needles"),
        T("標準體驗", "The standard hunt"),
        T("威力3水球、小章魚更多更快", "Power-3 bubbles, more & faster minions"),
        T("彈幕狂潮、僅 1 支針,獻給勇者", "Barrage storms, only 1 needle. Good luck"),
    ]
    cols = [(60, 140, 90), (52, 96, 168), (170, 110, 50), (150, 50, 60)]
    y = 150
    for i, d in enumerate(BOSS_DIFFS):
        label = "[%d] %s" % (i + 1, T(d["zh"], d["en"]))
        ui.button(s, (SCREEN_W // 2 - 190, y, 380, 62), label,
                  ("diff", i), size=24, base=cols[i])
        tip = sml.render(descs[i], True, (205, 216, 235))
        s.blit(tip, tip.get_rect(center=(SCREEN_W // 2, y + 78)))
        y += 106
    ui.button(s, (SCREEN_W // 2 - 70, y + 6, 140, 42), T("返回", "Back"),
              "back", size=18, base=(90, 96, 112))


# ----------------------------------------------------------------------
# 連線雙道具槽面板(全螢幕右側黑邊 / 視窗模式退回畫面右上角)
# ----------------------------------------------------------------------
def draw_slot_panel(surf, x, y, size, sa, sb, t):
    """直式雙槽:上=優先槽(X 使用),下=備用槽(Z 對調)。"""
    pad = size // 6
    title = get_font(max(13, size // 5)).render(T("道具槽", "ITEMS"), True,
                                                (235, 240, 250))
    surf.blit(title, title.get_rect(midtop=(x + size // 2, y)))
    y += title.get_height() + 6
    for i, (kind, label, hot) in enumerate(
            ((sb, T("X 使用", "X use"), True),
             (sa, T("Z 對調", "Z swap"), False))):
        box = pygame.Rect(x, y + i * (size + pad + 18), size, size)
        pygame.draw.rect(surf, (30, 38, 54), box, border_radius=10)
        if hot:
            glow = 200 + int(55 * math.sin(t * 5))
            pygame.draw.rect(surf, (255, glow, 90), box, 3, border_radius=10)
        else:
            pygame.draw.rect(surf, (95, 105, 125), box, 2, border_radius=10)
        if kind:
            cx, cy = box.center
            rad = size // 2 - 8
            pygame.draw.circle(surf, (255, 255, 255), (cx, cy), rad)
            pygame.draw.circle(surf, (200, 200, 200), (cx, cy), rad, 2)
            draw_item_icon_scaled(surf, cx, cy, kind, min(1.6, size / 44.0))
        else:
            dash = get_font(size // 3).render("-", True, (90, 100, 120))
            surf.blit(dash, dash.get_rect(center=box.center))
        lab = get_font(max(12, size // 6)).render(label, True,
                                                  (255, 220, 140) if hot
                                                  else (180, 190, 210))
        surf.blit(lab, lab.get_rect(midtop=(box.centerx, box.bottom + 2)))


def draw_slot_panel_inline(surf, sa, sb, t):
    """視窗模式(無黑邊)的精簡版:畫在畫布右上角,右格=優先。"""
    size = 42
    x0 = SCREEN_W - size * 2 - 26
    y0 = 30
    bg = pygame.Surface((size * 2 + 22, size + 26), pygame.SRCALPHA)
    bg.fill((0, 0, 0, 130))
    surf.blit(bg, (x0 - 8, y0 - 6))
    for i, (kind, hot) in enumerate(((sa, False), (sb, True))):
        box = pygame.Rect(x0 + i * (size + 10), y0, size, size)
        pygame.draw.rect(surf, (30, 38, 54), box, border_radius=8)
        if hot:
            glow = 200 + int(55 * math.sin(t * 5))
            pygame.draw.rect(surf, (255, glow, 90), box, 3, border_radius=8)
        else:
            pygame.draw.rect(surf, (95, 105, 125), box, 2, border_radius=8)
        if kind:
            cx, cy = box.center
            pygame.draw.circle(surf, (255, 255, 255), (cx, cy), size // 2 - 5)
            draw_item_icon_scaled(surf, cx, cy, kind, 0.9)
    lab = get_font(12).render(T("X用 Z換", "X use Z swap"), True, (235, 235, 245))
    surf.blit(lab, lab.get_rect(midtop=(x0 + size + 5, y0 + size + 3)))


# ----------------------------------------------------------------------
# 名字輸入畫面(進入房間前;支援中文輸入法 TEXTINPUT)
# ----------------------------------------------------------------------
def draw_name_entry(s, t, name_text):
    s.fill((26, 36, 58))
    big = get_font(38)
    sml = get_font(18)
    title = big.render(T("輸入你的名字", "ENTER YOUR NAME"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 150)))
    tip = sml.render(T("最多 8 個字,支援中文;Enter 或點「繼續」確認,留空使用預設",
                       "Up to 8 chars; Enter or Continue; blank = default"),
                     True, (220, 226, 240))
    s.blit(tip, tip.get_rect(center=(SCREEN_W // 2, 200)))
    cursor = "|" if int(t * 2) % 2 == 0 else " "
    box = pygame.Rect(SCREEN_W // 2 - 190, 250, 380, 62)
    pygame.draw.rect(s, (44, 54, 78), box, border_radius=12)
    pygame.draw.rect(s, (110, 130, 170), box, 2, border_radius=12)
    field = get_font(30).render(name_text + cursor, True, (255, 230, 140))
    s.blit(field, field.get_rect(center=box.center))
    ui.button(s, (SCREEN_W // 2 - 150, 340, 140, 46), T("繼續", "Continue"),
              "name_ok", size=19, base=(60, 130, 90))
    ui.button(s, (SCREEN_W // 2 + 10, 340, 140, 46), T("返回", "Back"),
              "back", size=19, base=(90, 96, 112))


# ----------------------------------------------------------------------
# 角色選擇畫面(進入房間前)
# ----------------------------------------------------------------------
def draw_char_select(s, t, current):
    s.fill((26, 36, 58))
    big = get_font(34)
    nf = get_font(15)
    sf = get_font(13)
    title = big.render(T("選擇角色", "CHOOSE YOUR CHARACTER"), True, (255, 255, 255))
    s.blit(title, title.get_rect(center=(SCREEN_W // 2, 34)))
    hint = sf.render(T("點選角色進入房間;技能鍵為 C(冷卻制),Esc 返回",
                       "Click a character; skill key is C. Esc back"),
                     True, (255, 230, 140))
    s.blit(hint, hint.get_rect(center=(SCREEN_W // 2, 62)))

    cols = 6
    cw = (SCREEN_W - 24) // cols
    rows_n = (len(CHAR_DEFS) + cols - 1) // cols
    chh = 96
    x0 = (SCREEN_W - cw * cols) // 2
    y0 = 78
    hover_ix = None
    for i, cd in enumerate(CHAR_DEFS):
        cx0 = x0 + (i % cols) * cw
        cy0 = y0 + (i // cols) * chh
        card = pygame.Rect(cx0 + 4, cy0 + 4, cw - 8, chh - 8)
        hov = ui.hotspot(card, ("char", i))
        if hov:
            hover_ix = i
        base = (46, 58, 84)
        if i == current:
            base = (60, 92, 70)
        if hov:
            base = tuple(min(255, v + 20) for v in base)
        pygame.draw.rect(s, base, card, border_radius=9)
        pygame.draw.rect(s, (255, 220, 120) if i == current else (96, 116, 156),
                         card, 3 if i == current else 1, border_radius=9)
        bob = int(2 * math.sin(t * 3 + i))
        draw_char_icon(s, card.centerx, card.y + 28 + bob,
                       i, PLAYER_COLORS[i % len(PLAYER_COLORS)], rad=13)
        name = nf.render(T(cd["zh"], cd["en"]), True, (255, 244, 200))
        s.blit(name, name.get_rect(midtop=(card.centerx, card.y + 48)))
        sk = sf.render(T(cd["skill_zh"], cd["skill_en"]), True, (150, 220, 200))
        s.blit(sk, sk.get_rect(midtop=(card.centerx, card.y + 68)))

    # 底部詳情欄:顯示游標所指(否則顯示目前選擇)的完整說明
    show = hover_ix if hover_ix is not None else current
    bar = pygame.Rect(16, y0 + rows_n * chh + 8, SCREEN_W - 32, 92)
    pygame.draw.rect(s, (36, 48, 72), bar, border_radius=12)
    pygame.draw.rect(s, (96, 116, 156), bar, 2, border_radius=12)
    cd = CHAR_DEFS[show]
    draw_char_icon(s, bar.x + 40, bar.centery, show,
                   PLAYER_COLORS[show % len(PLAYER_COLORS)], rad=20)
    nm = get_font(21).render(T(cd["zh"], cd["en"]), True, (255, 244, 200))
    s.blit(nm, (bar.x + 76, bar.y + 10))
    sk = get_font(16).render(T("技能:%s(冷卻 %d 秒)" % (cd["skill_zh"], int(cd["cd"])),
                               "Skill: %s (%ds CD)" % (cd["skill_en"], int(cd["cd"]))),
                             True, (150, 220, 200))
    s.blit(sk, (bar.x + 76, bar.y + 38))
    desc = get_font(14).render(" ".join(T(cd["dz"], cd["de"])), True, (215, 224, 240))
    s.blit(desc, (bar.x + 76, bar.y + 62))
    ui.button(s, (SCREEN_W // 2 - 70, bar.bottom + 8, 140, 36),
              T("返回", "Back"), "back", size=16, base=(90, 96, 112))


def draw_skill_panel(surf, x, y, size, ch_ix, cd_left, t):
    """右側黑邊的技能面板(在道具槽下方)。"""
    if ch_ix is None:
        return
    cd = CHAR_DEFS[ch_ix]
    title = get_font(max(13, size // 5)).render(T("技能", "SKILL"), True,
                                                (235, 240, 250))
    surf.blit(title, title.get_rect(midtop=(x + size // 2, y)))
    y += title.get_height() + 6
    box = pygame.Rect(x, y, size, size)
    pygame.draw.rect(surf, (30, 38, 54), box, border_radius=10)
    ready = cd_left <= 0
    if ready:
        glow = 200 + int(55 * math.sin(t * 5))
        pygame.draw.rect(surf, (120, glow, 140), box, 3, border_radius=10)
    else:
        pygame.draw.rect(surf, (95, 105, 125), box, 2, border_radius=10)
    draw_char_icon(surf, box.centerx, box.centery, ch_ix,
                   (200, 208, 224), rad=size // 3)
    if not ready:
        # 冷卻遮罩 + 秒數
        frac = min(1.0, cd_left / CHAR_DEFS[ch_ix]["cd"])
        mask = pygame.Surface((size, int(size * frac)), pygame.SRCALPHA)
        mask.fill((10, 14, 22, 170))
        surf.blit(mask, (box.x, box.bottom - int(size * frac)))
        sec = get_font(size // 3).render("%.0f" % math.ceil(cd_left), True,
                                         (255, 255, 255))
        surf.blit(sec, sec.get_rect(center=box.center))
    lab = get_font(max(12, size // 6)).render(
        T("C %s" % cd["skill_zh"], "C %s" % cd["skill_en"]),
        True, (150, 230, 190) if ready else (170, 180, 200))
    surf.blit(lab, lab.get_rect(midtop=(box.centerx, box.bottom + 2)))


# ----------------------------------------------------------------------
# 主程式
# ----------------------------------------------------------------------
def main():
    if ANDROID:
        try:
            pygame.mixer.pre_init(22050, -16, 2, 512)
        except pygame.error:
            pass
    pygame.init()
    _init_font()
    music = MusicBox()
    sfx = Sfx()
    sfx_watch = SfxDetector()
    pygame.joystick.init()
    pads = {}
    for _ji in range(pygame.joystick.get_count()):
        _js = pygame.joystick.Joystick(_ji)
        _js.init()
        if is_real_pad(_js):
            pads[_js.get_instance_id()] = _js
    lobby_slots = []      # 手把派對大廳
    pending_pad = None    # 手把派對開戰名單
    tut_page = 0          # 遊戲教學頁碼
    touch = TouchPad()
    touch_ui = ANDROID    # 螢幕按鍵(安卓預設開;可在標題頁切換改用手把)
    pygame.display.set_caption(T("泡泡大作戰 Bubble Battle", "Bubble Battle"))

    # 全螢幕等比縮放:遊戲一律畫在原尺寸畫布上,再放大置中、四周留黑
    if ANDROID:
        try:
            pygame.display.set_mode((SCREEN_W, SCREEN_H),
                                    pygame.FULLSCREEN | pygame.SCALED)
        except pygame.error:
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.Surface((SCREEN_W, SCREEN_H))
    try:
        screen = screen.convert()      # 與顯示同像素格式,加速每幀 blit
    except pygame.error:
        pass
    fullscreen = True
    display = None
    scale = 1.0
    off_x = off_y = 0
    scaled_size = (SCREEN_W, SCREEN_H)

    def apply_display():
        nonlocal display, scale, off_x, off_y, scaled_size
        try:
            if ANDROID:
                # 安卓:固定邏輯解析度 + GPU 硬體縮放(避免每幀軟體放大)
                display = pygame.display.set_mode(
                    (SCREEN_W, SCREEN_H),
                    pygame.FULLSCREEN | pygame.SCALED)
            elif fullscreen:
                display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        except pygame.error:
            display = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        dw, dh = display.get_size()
        scale = min(dw / SCREEN_W, dh / SCREEN_H)
        scaled_size = (max(1, int(SCREEN_W * scale)), max(1, int(SCREEN_H * scale)))
        off_x = (dw - scaled_size[0]) // 2
        off_y = (dh - scaled_size[1]) // 2

    def present(net_slots=None):
        display.fill((0, 0, 0))
        if scaled_size == (SCREEN_W, SCREEN_H):
            display.blit(screen, (off_x, off_y))
        else:
            display.blit(pygame.transform.smoothscale(screen, scaled_size),
                         (off_x, off_y))
        # 即時戰況欄:優先畫在左側黑邊,沒有黑邊就貼畫面左緣
        fg = None
        if state == "game":
            fg = game
        elif state == "net_game":
            fg = game if net_role == "host" else view
        if fg is not None and getattr(fg, "feed", None):
            if off_x >= 150:
                draw_feed(display, fg, 10, off_y + 70, max_w=off_x - 16)
            else:
                draw_feed(display, fg, off_x + 6, off_y + 70)

        # 連線雙道具槽 + 技能面板:畫在右側黑邊(道具在上、技能在下)
        if net_slots is not None and off_x >= 110:
            sa, sb, ch_ix, cd_left = net_slots
            size = min(96, off_x - 44)
            px = off_x + scaled_size[0] + (off_x - size) // 2
            draw_slot_panel(display, px, 18, size, sa, sb, t)
            panel_h = 26 + 2 * (size + size // 6 + 18)
            draw_skill_panel(display, px, 18 + panel_h + 16, size, ch_ix, cd_left, t)
        # 螢幕觸控按鍵(最上層、實際解析度)
        if touch_ui:
            touch.draw(display, state in ("game", "net_game"))
        pygame.display.flip()

    def to_canvas(pos):
        """把實際螢幕座標換算回遊戲畫布座標(滑鼠用)。"""
        return ((pos[0] - off_x) / scale, (pos[1] - off_y) / scale)

    apply_display()
    clock = pygame.time.Clock()

    state = "title"
    pending_mode = None    # (人數, 電腦編號集合)
    pending_turf = False   # 本機佔地模式
    pending_infect = False # 本機感染模式
    pending_soccer = False # 本機足球模式
    pending_boss = set()   # 本機章魚王:電腦隊友編號集合(待選難度) 本機遊戲用
    game = None
    t = 0.0
    notice = ""            # 標題畫面訊息(例如斷線)

    # ---- 連線房間狀態 ----
    net_listen = None          # 房主的監聽 socket
    room_conns = {}            # pid -> LineConn(房主側)
    room_ready = {}            # pid -> bool
    room_cpu = set()           # 被房主加入的電腦格位
    room_team = {0: 0}         # pid -> 0(紅)/1(藍),組隊戰使用
    room_items = False         # 道具池:False=普通 True=擴充
    room_char = {}             # pid -> 角色編號
    room_score_on = False      # 積分模式開關(房主決定)
    room_scores = {}           # pid -> 累積積分(每場存活到最後 +1)
    room_order = []            # 上一場的 pid 順序(結算積分用)
    picking_char = False       # 房間內是否開著角色選單
    my_char = 0                # 自己選的角色
    my_name = ""               # 自己的名字(進房前輸入)
    room_name = {}             # pid -> 名字(主機側)
    sel_after = None           # 角色選完後要去哪("host"/"join")
    room_mode = "versus"
    room_diff = 1              # 章魚王房間難度(預設普通)
    room_cpu_lv = 1            # 電腦強度(預設中級)
    room_map = 0
    pidmap = {}                # 大廳 pid -> 遊戲內 id
    net = None                 # 客戶端往房主的連線
    net_role = None            # "host" / "client"
    my_pid = None              # 客戶端在房間內的格位
    my_gid = 0                 # 客戶端在遊戲內的編號
    last_lb = None             # 客戶端最近收到的大廳狀態
    view = None                # 客戶端顯示用 Game
    net_ip = ""
    net_notice = ""
    net_frame = 0

    num_keys = {}
    for i in range(1, 10):
        num_keys[getattr(pygame, "K_%d" % i)] = i
        num_keys[getattr(pygame, "K_KP%d" % i)] = i

    # ---------------- 房間輔助 ----------------
    def team_members(tix):
        ids = {0} | set(room_conns) | set(room_cpu)
        return [i for i in ids if room_team.get(i, 0) == tix]

    def team_has_space(tix):
        return len(team_members(tix)) < 4       # 每隊最多 4 人

    def auto_team():
        return 0 if len(team_members(0)) <= len(team_members(1)) else 1

    def flip_team(i):
        nonlocal net_notice
        target = 1 - room_team.get(i, 0)
        if team_has_space(target):
            room_team[i] = target
        else:
            net_notice = T("那一隊已滿 4 人", "That team is full (4 max)")

    def rebalance_teams():
        # 進入組隊模式時,把所有人平均分成紅藍兩隊
        ids = [0] + sorted(set(room_conns) | set(room_cpu))
        for n, i in enumerate(ids):
            room_team[i] = n % 2

    def room_slots():
        slots = []
        for i in range(MAX_PLAYERS):
            if i == 0:
                d = {"k": "host", "r": True}
            elif i in room_conns:
                d = {"k": "hu", "r": bool(room_ready.get(i))}
            elif i in room_cpu:
                d = {"k": "cpu", "r": True}
            else:
                slots.append({"k": "emp"})
                continue
            if room_mode in ("team", "turf", "soccer"):
                d["t"] = room_team.get(i, 0)
            d["c"] = room_char.get(i, 0)
            d["n"] = room_name.get(i, "")
            if room_score_on:
                d["s"] = room_scores.get(i, 0)
            slots.append(d)
        return slots

    def room_broadcast():
        msg = {"t": "lb", "slots": room_slots(),
               "mode": room_mode, "map": room_map, "diff": room_diff,
               "items": room_items, "cl": room_cpu_lv}
        for conn in room_conns.values():
            conn.send_json(msg)

    def close_room():
        nonlocal net_listen
        for conn in room_conns.values():
            conn.close()
        room_conns.clear()
        room_ready.clear()
        room_cpu.clear()
        if net_listen is not None:
            try:
                net_listen.close()
            except OSError:
                pass
            net_listen = None

    def client_teardown():
        nonlocal net, net_role, view, my_pid, last_lb
        if net is not None:
            net.close()
        net = None
        net_role = None
        view = None
        my_pid = None
        last_lb = None

    def start_room_game():
        nonlocal game, state, net_role, net_frame, pidmap
        order = [0] + sorted(set(room_conns) | room_cpu)
        n = len(order)
        botgids = sorted(order.index(pid) for pid in room_cpu)
        mi = room_map if room_map >= 0 else random.randrange(len(MAPS))
        game = Game(n, bots=set(botgids), map_index=mi, countdown=3.0,
                    boss=(room_mode == "boss"), boss_diff=room_diff,
                    items_ext=room_items, turf=(room_mode == "turf"),
                    infect=(room_mode == "infect"),
                    soccer=(room_mode == "soccer"),
                    bot_level=room_cpu_lv)
        if room_mode in ("team", "turf", "soccer"):
            for pid in order:
                game.players[order.index(pid)].team = room_team.get(pid, 0)
        for pid in order:
            gp = game.players[order.index(pid)]
            gp.char = room_char.get(pid, 0)
            nm = room_name.get(pid, "")
            if nm:
                gp.name = nm
        room_order[:] = order
        game._scored = False
        pidmap = {pid: order.index(pid) for pid in room_conns}
        for pid, gid in pidmap.items():
            game.players[gid].is_remote = True
        game.players[0].use_net_keys = True   # 房主也用方向鍵+空白鍵
        game.net_play = True
        game.net_is_host = True
        game.two_slot = True
        for pid, conn in room_conns.items():
            conn.send_json({"t": "go", "mode": room_mode, "map": mi,
                            "n": n, "bots": botgids, "you": pidmap[pid],
                            "diff": room_diff, "items": room_items})
        net_role = "host"
        net_frame = 0
        state = "net_game"

    def host_open_room():
        nonlocal net_listen, state, net_role
        try:
            net_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            net_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            net_listen.bind(("0.0.0.0", NET_PORT))
            net_listen.listen(4)
            net_listen.setblocking(False)
            net_role = "host"
            state = "room_host"
            return True
        except OSError as err:
            return T("無法開啟連接埠:%s" % err, "Can't open port: %s" % err)

    # ---------------- 點擊分派 ----------------
    def lobby_slot(src):
        for sl in lobby_slots:
            if sl["src"] == src:
                return sl
        return None

    def lobby_press(src):
        sl = lobby_slot(src)
        if sl is None:
            if len(lobby_slots) < 8:
                lobby_slots.append(dict(src=src,
                                        char=len(lobby_slots) % len(CHAR_DEFS),
                                        ready=False))
        else:
            sl["ready"] = not sl["ready"]

    def lobby_cycle(src, d):
        sl = lobby_slot(src)
        if sl is not None and not sl["ready"]:
            sl["char"] = (sl["char"] + d) % len(CHAR_DEFS)

    def lobby_cancel(src):
        sl = lobby_slot(src)
        if sl is not None:
            if sl["ready"]:
                sl["ready"] = False
            else:
                lobby_slots.remove(sl)

    def pad_party_ready():
        return (len(lobby_slots) >= 2
                and all(sl["ready"] for sl in lobby_slots))

    def handle_click(cid):
        nonlocal state, game, pending_mode, pending_turf, pending_infect
        nonlocal pending_soccer, pending_pad, touch_ui, tut_page
        nonlocal room_mode, room_map, net, net_role
        nonlocal net_notice, view, my_pid, last_lb, net_ip, notice
        nonlocal room_diff, pending_boss, room_items, my_char, sel_after, room_cpu_lv
        nonlocal room_score_on, picking_char
        if cid is None:
            return
        if state in ("title", "local_menu"):
            notice = ""
            if cid == "touch_toggle":
                touch_ui = not touch_ui
            elif cid == "music_toggle":
                music.toggle_mute()
            elif cid == "tutorial":
                tut_page = 0
                state = "tutorial"
            elif cid == "local":
                state = "local_menu"
            elif cid == "padlobby":
                lobby_slots.clear()
                state = "pad_lobby"
            elif cid == "back":
                state = "title"
            elif isinstance(cid, tuple) and cid[0] == "mode":
                modes = {1: (2, {1}), 2: (3, {1, 2}), 3: (4, {1, 2, 3}),
                         4: (2, set()), 5: (4, {2, 3}), 6: (3, set()),
                         7: (4, set()), 8: (8, set(range(1, 8))),
                         9: (8, set(range(1, 8))),
                         10: (8, set(range(1, 8)))}
                pending_turf = (cid[1] == 8)
                pending_infect = (cid[1] == 9)
                pending_soccer = (cid[1] == 10)
                pending_mode = modes[cid[1]]
                state = "map"
            elif cid == "boss1":
                pending_boss = {1}
                state = "boss_diff"
            elif cid == "boss2":
                pending_boss = set()
                state = "boss_diff"
            elif cid == "net":
                net_notice = ""
                state = "room_menu"
            elif cid == "items":
                state = "items"
            elif cid == "quit":
                pygame.quit(); sys.exit()
        elif state == "tutorial":
            if cid == "back":
                state = "title"
            elif cid == "tprev":
                tut_page = max(0, tut_page - 1)
            elif cid == "tnext":
                tut_page = min(len(TUTORIAL_PAGES) - 1, tut_page + 1)
        elif state == "pad_lobby":
            if cid == "back":
                state = "local_menu"
            elif cid == "padstart" and pad_party_ready():
                pending_pad = [dict(sl) for sl in lobby_slots]
                pending_mode = None
                state = "map"
        elif state == "boss_diff":
            if cid == "back":
                state = "title"
            elif isinstance(cid, tuple) and cid[0] == "diff":
                game = Game(2, bots=pending_boss, boss=True,
                            boss_diff=cid[1], countdown=3.0)
                state = "game"
        elif state == "items":
            if cid == "back":
                state = "title"
        elif state == "map":
            if cid == "back":
                state = "title"
            elif isinstance(cid, tuple) and cid[0] == "map":
                ix = cid[1] if cid[1] >= 0 else random.randrange(len(MAPS))
                if pending_pad:
                    kms = []
                    for sl in pending_pad:
                        if sl["src"][0] == "kb":
                            kms.append(KEYMAPS[sl["src"][1]])
                        else:
                            kms.append({"dirs": {}, "action": [], "use": []})
                    game = Game(len(pending_pad), bots=set(), map_index=ix,
                                keymaps=kms, countdown=3.0)
                    game.pads = pads
                    for i, sl in enumerate(pending_pad):
                        gp = game.players[i]
                        gp.char = sl["char"]
                        if sl["src"][0] == "pad":
                            gp.pad_iid = sl["src"][1]
                    pending_pad = None
                    state = "game"
                elif pending_mode:
                    np_, bots = pending_mode
                    game = Game(np_, bots=bots, map_index=ix,
                                turf=pending_turf, infect=pending_infect,
                                soccer=pending_soccer, countdown=3.0)
                    if pending_turf or pending_soccer:
                        for gp in game.players:
                            gp.team = gp.id % 2
                    state = "game"
        elif state == "room_menu":
            if cid == "host":
                sel_after = "host"
                pygame.key.start_text_input()
                state = "name_entry"
            elif cid == "join":
                sel_after = "join"
                pygame.key.start_text_input()
                state = "name_entry"
            elif cid == "back":
                state = "title"
        elif state == "name_entry":
            if cid == "name_ok":
                pygame.key.stop_text_input()
                state = "char_sel"
            elif cid == "back":
                pygame.key.stop_text_input()
                state = "room_menu"
        elif state == "char_sel":
            if cid == "back":
                state = "room_menu"
            elif isinstance(cid, tuple) and cid[0] == "char":
                my_char = cid[1]
                if sel_after == "host":
                    r = host_open_room()
                    if r is not True:
                        net_notice = r
                        state = "room_menu"
                    else:
                        room_char.clear()
                        room_char[0] = my_char
                        room_name.clear()
                        room_name[0] = my_name or T("房主", "Host")
                else:
                    net_ip = ""
                    net_notice = ""
                    state = "net_join"
        elif state == "net_join":
            if cid == "back":
                state = "room_menu"
            elif cid == "connect":
                try_connect()
        elif state == "room_host":
            if isinstance(cid, tuple) and cid[0] == "slot":
                i = cid[1]
                if room_mode in ("team", "turf", "soccer") and (i == 0 or i in room_conns):
                    flip_team(i)                     # 換隊(房主/真人)
                elif i in room_cpu:
                    if room_mode == "team":
                        # 電腦:紅隊 → 藍隊 → 移除
                        if room_team.get(i, 0) == 0 and team_has_space(1):
                            room_team[i] = 1
                        else:
                            room_cpu.discard(i)
                            room_team.pop(i, None)
                            room_char.pop(i, None)
                            room_name.pop(i, None)
                            room_scores.pop(i, None)
                    else:
                        room_cpu.discard(i)
                        room_char.pop(i, None)
                        room_name.pop(i, None)
                        room_scores.pop(i, None)
                elif i not in room_conns and i != 0:
                    room_cpu.add(i)
                    room_team[i] = auto_team()
                    room_char[i] = random.randrange(len(CHAR_DEFS))
                    room_name[i] = T("電腦%d" % (i + 1), "CPU %d" % (i + 1))
                room_broadcast()
            elif cid == "mode_toggle":
                room_mode = {"versus": "team", "team": "turf",
                             "turf": "infect", "infect": "soccer",
                             "soccer": "boss", "boss": "versus"}[room_mode]
                if room_mode in ("team", "turf", "soccer"):
                    rebalance_teams()
                room_broadcast()
            elif cid == "items_toggle":
                room_items = not room_items
                room_broadcast()
            elif picking_char and cid == "back":
                picking_char = False
            elif picking_char and isinstance(cid, tuple) and cid[0] == "char":
                room_char[0] = cid[1]
                my_char = cid[1]
                picking_char = False
                room_broadcast()
            elif cid == "char_cycle":
                picking_char = True
            elif cid == "score_toggle":
                room_score_on = not room_score_on
                room_broadcast()
            elif cid == "score_reset":
                room_scores.clear()
                room_broadcast()
            elif cid == "cpulv_cycle":
                room_cpu_lv = (room_cpu_lv + 1) % len(BOT_LEVELS)
                room_broadcast()
            elif cid == "diff_cycle" and room_mode == "boss":
                room_diff = (room_diff + 1) % len(BOSS_DIFFS)
                room_broadcast()
            elif cid == "map_pick" and room_mode != "boss":
                state = "room_map"
            elif cid == "start":
                if room_mode in ("team", "turf", "soccer") and (not team_members(0)
                                            or not team_members(1)):
                    net_notice = T("組隊戰兩隊都要有人!", "Both teams need players!")
                else:
                    start_room_game()
            elif cid == "leave":
                close_room()
                net_role = None
                state = "room_menu"
        elif state == "room_map":
            if cid == "back":
                state = "room_host"
            elif isinstance(cid, tuple) and cid[0] == "map":
                room_map = cid[1]          # -1 = 每場開局隨機
                room_broadcast()
                state = "room_host"
        elif state == "room_client":
            if cid == "ready":
                me = last_lb["slots"][my_pid] if (last_lb and my_pid is not None) else {}
                net.send_json({"t": "rd", "v": 0 if me.get("r") else 1})
            elif picking_char and cid == "back":
                picking_char = False
            elif picking_char and isinstance(cid, tuple) and cid[0] == "char":
                my_char = cid[1]
                picking_char = False
                net.send_json({"t": "ch", "v": my_char, "n": my_name})
            elif cid == "char_cycle":
                me = last_lb["slots"][my_pid] if (last_lb and my_pid is not None) else {}
                if not me.get("r"):
                    picking_char = True
            elif isinstance(cid, tuple) and cid[0] == "slot" and cid[1] == my_pid:
                net.send_json({"t": "tm"})   # 要求換隊
            elif cid == "leave":
                client_teardown()
                state = "room_menu"
        elif state == "net_game":
            if cid == "lobbyret" and net_role == "host" and game.over:
                for conn in room_conns.values():
                    conn.send_json({"t": "lb2"})
                for pid in room_ready:
                    room_ready[pid] = False
                room_broadcast()
                state = "room_host"

    def try_connect():
        nonlocal net, net_role, state, net_notice, view, my_pid, last_lb
        target = net_ip.strip()
        if not target:
            return
        draw_net_join(screen, t, net_ip, T("連線中…", "Connecting..."))
        present()
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(4.0)
            sk.connect((target, NET_PORT))
            net = LineConn(sk)
            net_role = "client"
            view = None
            my_pid = None
            last_lb = None
            net_notice = ""
            state = "room_client"
        except OSError as err:
            net_notice = T("連線失敗:%s" % err, "Failed: %s" % err)

    # ---------------- 主迴圈 ----------------
    while True:
        dt = min(clock.tick(FPS) / 1000.0, 0.05)
        t += dt
        events = pygame.event.get()
        music.play(music_group_for(state))
        keys = pygame.key.get_pressed()
        mouse = to_canvas(pygame.mouse.get_pos())

        for e in events:
            # 螢幕觸控(虛擬搖桿與按鍵)
            if touch_ui and e.type in (pygame.FINGERDOWN,
                                       pygame.FINGERMOTION, pygame.FINGERUP):
                # SCALED 模式下 pygame 已把手指座標轉為邏輯座標,直接使用
                dw2, dh2 = display.get_size()
                touch.handle(e, dw2, dh2)

            # 手把熱插拔(所有畫面皆生效)
            if e.type == pygame.JOYDEVICEADDED:
                try:
                    _js = pygame.joystick.Joystick(e.device_index)
                    _js.init()
                    if not is_real_pad(_js):
                        raise pygame.error("sensor device ignored")
                    new_iid = _js.get_instance_id()
                    pads[new_iid] = _js
                    # 安卓手把重新註冊:把失效的大廳位/玩家改綁到新 id
                    for sl in lobby_slots:
                        if (sl["src"][0] == "pad"
                                and sl["src"][1] not in pads):
                            sl["src"] = ("pad", new_iid)
                            break
                    if game is not None:
                        heal_pads(game, pads)
                except pygame.error:
                    pass
            elif e.type == pygame.JOYDEVICEREMOVED:
                pads.pop(e.instance_id, None)

            # 手把派對大廳:加入/準備/選角/開戰
            if state == "pad_lobby":
                if e.type == pygame.KEYDOWN:
                    for k, km in enumerate(KEYMAPS):
                        if e.key in km["action"]:
                            lobby_press(("kb", k))
                        elif e.key == km["dirs"]["left"]:
                            lobby_cycle(("kb", k), -1)
                        elif e.key == km["dirs"]["right"]:
                            lobby_cycle(("kb", k), 1)
                        elif e.key in km.get("use", []):
                            lobby_cancel(("kb", k))
                elif e.type == pygame.JOYBUTTONDOWN:
                    psrc = ("pad", e.instance_id)
                    if e.button == 0:
                        lobby_press(psrc)
                    elif e.button == 1:
                        lobby_cancel(psrc)
                    elif e.button in (6, 7) and pad_party_ready():
                        handle_click("padstart")
                elif e.type == pygame.JOYHATMOTION and e.value[0] != 0:
                    lobby_cycle(("pad", e.instance_id),
                                1 if e.value[0] > 0 else -1)

            if e.type == pygame.QUIT:
                close_room(); client_teardown()
                pygame.quit(); sys.exit()
            if state == "name_entry" and e.type == pygame.TEXTINPUT:
                for chch in e.text:
                    if chch.isprintable() and len(my_name) < 8:
                        my_name += chch
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                handle_click(ui.click(to_canvas(e.pos)))
            if e.type == pygame.KEYDOWN and e.key == pygame.K_F11:
                fullscreen = not fullscreen
                apply_display()
                continue
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if state in ("game", "items", "room_menu",
                                 "char_sel", "name_entry", "local_menu"):
                        state = "title"
                    elif state == "pad_lobby":
                        state = "local_menu"
                    elif state == "tutorial":
                        state = "title"
                    elif state in ("map", "boss_diff"):
                        state = "local_menu"
                    elif state == "net_join":
                        state = "room_menu"
                    elif state == "room_map":
                        state = "room_host"
                    elif state == "room_host":
                        if picking_char:
                            picking_char = False
                        else:
                            close_room(); net_role = None
                            state = "room_menu"
                    elif state == "room_client":
                        if picking_char:
                            picking_char = False
                        else:
                            client_teardown()
                            state = "room_menu"
                    elif state == "net_game":
                        if net_role == "host":
                            close_room(); net_role = None
                        else:
                            client_teardown()
                        state = "title"
                    else:
                        pygame.quit(); sys.exit()
                elif state == "name_entry":
                    if e.key == pygame.K_BACKSPACE:
                        my_name = my_name[:-1]
                    elif e.key == pygame.K_RETURN:
                        handle_click("name_ok")
                if (e.key == pygame.K_m
                        and state not in ("name_entry", "net_join")):
                    music.toggle_mute()
                    sfx.toggle_mute()
                elif state == "tutorial":
                    if e.key == pygame.K_LEFT:
                        tut_page = max(0, tut_page - 1)
                    elif e.key == pygame.K_RIGHT:
                        tut_page = min(len(TUTORIAL_PAGES) - 1, tut_page + 1)
                elif state in ("title", "local_menu"):
                    notice = ""
                    if e.key == pygame.K_i:
                        handle_click("items")
                    elif e.key == pygame.K_n:
                        handle_click("net")
                    elif e.key in (pygame.K_8, pygame.K_KP8):
                        handle_click("boss1")
                    elif e.key in (pygame.K_9, pygame.K_KP9):
                        handle_click("boss2")
                    else:
                        n = num_keys.get(e.key)
                        if n is not None and 1 <= n <= 7:
                            handle_click(("mode", n))
                elif state == "items" and e.key == pygame.K_i:
                    state = "title"
                elif state == "boss_diff":
                    n = num_keys.get(e.key)
                    if n is not None and 1 <= n <= len(BOSS_DIFFS):
                        handle_click(("diff", n - 1))
                elif state in ("map", "room_map"):
                    n = num_keys.get(e.key)
                    if n is not None and 1 <= n <= len(MAPS):
                        handle_click(("map", n - 1))
                    elif e.key in (pygame.K_0, pygame.K_KP0):
                        handle_click(("map", -1))
                elif state == "game":
                    if e.key == pygame.K_r:
                        game.reset()
                    elif e.key == pygame.K_m and not game.boss_mode:
                        state = "map"
                elif state == "net_join":
                    if e.key == pygame.K_RETURN:
                        try_connect()
                    elif e.key == pygame.K_BACKSPACE:
                        net_ip = net_ip[:-1]
                    elif e.unicode and (e.unicode.isalnum() or e.unicode in ".-"):
                        if len(net_ip) < 40:
                            net_ip += e.unicode

        # ---- 每幀處理與繪圖 ----
        ui.begin(mouse)
        touch_acts = touch.take() if touch_ui else []
        if "esc" in touch_acts:
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN,
                                                 key=pygame.K_ESCAPE))
        if (state in ("game", "net_game") and game is not None
                and net_role != "client"):
            heal_pads(game, pads)
            tp = next((q for q in game.players
                       if not q.is_bot and not q.is_remote), None)
            attach_local_input(game, tp, pads, touch, touch_ui)
            if tp is not None:
                for act in touch_acts:
                    if act == "a":
                        game.try_place_bubble(tp)
                    elif act == "b":
                        game.use_dart(tp)
                    elif act == "x":
                        game.use_skill(tp)
                    elif act == "y":
                        game.swap_items(tp)

        if state == "title":
            draw_title(screen, t)
            ui.button(screen, (16, 16, 168, 40),
                      T("觸控按鍵:開", "Touch: ON") if touch_ui
                      else T("觸控按鍵:關", "Touch: OFF"),
                      "touch_toggle", size=15,
                      base=(60, 130, 110) if touch_ui else (70, 90, 120))
            ui.button(screen, (16, 62, 168, 40),
                      T("音樂:關閉中", "Music: OFF") if music.muted
                      else T("音樂:開啟中", "Music: ON"),
                      "music_toggle", size=15,
                      base=(70, 90, 120) if music.muted else (150, 110, 60))
        elif state == "local_menu":
            draw_local_menu(screen, t)
        elif state == "tutorial":
            draw_tutorial(screen, t, tut_page)
        elif state == "pad_lobby":
            draw_pad_lobby(screen, t, lobby_slots, len(pads))
            if notice:
                n = get_font(18).render(notice, True, (255, 150, 150))
                screen.blit(n, n.get_rect(center=(SCREEN_W // 2, SCREEN_H - 82)))
        elif state == "items":
            draw_item_book(screen, t)
        elif state == "boss_diff":
            draw_boss_diff(screen, t)
        elif state in ("map", "room_map"):
            draw_map_select(screen, t,
                            cur=room_map if state == "room_map" else None)
        elif state == "room_menu":
            draw_room_menu(screen, t, net_notice)
        elif state == "name_entry":
            draw_name_entry(screen, t, my_name)
        elif state == "char_sel":
            draw_char_select(screen, t, my_char)
        elif state == "net_join":
            draw_net_join(screen, t, net_ip, net_notice)
        elif state == "room_host":
            # 收新玩家 / 大廳訊息
            total = 1 + len(room_conns) + len(room_cpu)
            if net_listen is not None and total < MAX_PLAYERS:
                try:
                    conn, addr = net_listen.accept()
                    pid = next(i for i in range(1, MAX_PLAYERS)
                               if i not in room_conns and i not in room_cpu)
                    room_conns[pid] = LineConn(conn)
                    room_ready[pid] = False
                    room_team[pid] = auto_team()
                    room_conns[pid].send_json({"t": "hi", "pid": pid})
                    room_broadcast()
                except (BlockingIOError, InterruptedError, StopIteration):
                    pass
            for pid, conn in list(room_conns.items()):
                for m in conn.poll():
                    if m.get("t") == "rd":
                        room_ready[pid] = bool(m.get("v"))
                        room_broadcast()
                    elif m.get("t") == "tm" and room_mode in ("team", "turf", "soccer"):
                        flip_team(pid)      # 加入者要求換隊
                        room_broadcast()
                    elif m.get("t") == "ch":
                        room_char[pid] = int(m.get("v", 0)) % len(CHAR_DEFS)
                        nm = str(m.get("n", "")).strip()[:8]
                        if nm:
                            room_name[pid] = nm
                        elif pid not in room_name:
                            room_name[pid] = T("玩家%d" % (pid + 1),
                                               "Player %d" % (pid + 1))
                        room_broadcast()
                if conn.closed:
                    del room_conns[pid]
                    room_ready.pop(pid, None)
                    room_team.pop(pid, None)
                    room_char.pop(pid, None)
                    room_name.pop(pid, None)
                    room_scores.pop(pid, None)
                    room_broadcast()
                else:
                    conn.flush()
            net_frame += 1
            if net_frame % 20 == 0:
                room_broadcast()
            if picking_char:
                draw_char_select(screen, t, room_char.get(0, 0))
            else:
                draw_room(screen, t, room_slots(), room_mode, room_map,
                          True, 0, "", room_diff, room_items, room_cpu_lv)
        elif state == "room_client":
            for m in net.poll():
                if m.get("t") == "hi":
                    my_pid = m.get("pid")
                    net.send_json({"t": "ch", "v": my_char, "n": my_name})
                elif m.get("t") == "lb":
                    last_lb = m
                elif m.get("t") == "go":
                    view = Game(m["n"], bots=set(m.get("bots", [])),
                                boss=(m["mode"] == "boss"),
                                map_index=m.get("map", 0),
                                boss_diff=m.get("diff", 1),
                                items_ext=m.get("items", False))
                    view.net_play = True
                    view.my_pids = {my_pid} if my_pid is not None else set()
                    view.two_slot = True
                    my_gid = m.get("you", 1)
                    net_frame = 0
                    state = "net_game"
            net.flush()
            if net is not None and net.closed:
                client_teardown()
                notice = T("與房間斷線", "Disconnected from the room")
                state = "title"
            elif picking_char:
                draw_char_select(screen, t, my_char)
            elif last_lb is not None and my_pid is not None:
                draw_room(screen, t, last_lb["slots"], last_lb.get("mode", "versus"),
                          last_lb.get("map", 0), False, my_pid, net_notice,
                          last_lb.get("diff", 1), last_lb.get("items", False),
                          last_lb.get("cl", 1))
            else:
                screen.fill((26, 34, 52))
                w = get_font(26).render(T("進入房間中…", "Entering the room..."),
                                        True, (255, 255, 255))
                screen.blit(w, w.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2)))
        elif state == "net_game" and net_role == "host":
            # 房主:收所有客戶端輸入 → 模擬 → 廣播快照
            for pid, conn in list(room_conns.items()):
                gid = pidmap.get(pid)
                pl = game.players[gid] if gid is not None else None
                for m in conn.poll():
                    if m.get("t") == "in" and pl is not None:
                        pl.remote_dirs = [d for d in m.get("d", [])
                                          if d in ("up", "down", "left", "right")]
                        if m.get("b"):
                            game.try_place_bubble(pl)
                        if m.get("u"):
                            game.use_dart(pl)
                        if m.get("s"):
                            game.swap_items(pl)
                        if m.get("k"):
                            game.use_skill(pl)
                if conn.closed:
                    if pl is not None and pl.alive:
                        game.kill(pl)      # 斷線者直接淘汰
                    del room_conns[pid]
                    room_ready.pop(pid, None)
            game.update(dt, keys, events)
            if game.over and room_score_on and not getattr(game, "_scored", True):
                game._scored = True
                statuses = []
                for pid in room_order:
                    gid = room_order.index(pid)
                    gp = game.players[gid] if gid < len(game.players) else None
                    if getattr(game, "infect", False):
                        inf = gp is not None and gp.infected
                        statuses.append((not inf,
                                         gp.infect_t if (gp and inf) else None))
                    elif getattr(game, "turf", False) or getattr(game, "soccer", False):
                        win = (game.winner is None
                               or (gp is not None
                                   and game.winner == "team%d" % (gp.team or 0)))
                        statuses.append((win, 0.0))
                    else:
                        statuses.append((gp is not None and gp.alive,
                                         gp.death_t if gp is not None else 0.0))
                pts = placement_points(statuses)
                for k, pid in enumerate(room_order):
                    room_scores[pid] = room_scores.get(pid, 0) + pts[k]
            game.draw(screen)
            net_frame += 1
            if net_frame % SNAPSHOT_EVERY == 0:
                snap = make_snapshot(game)
                for conn in room_conns.values():
                    conn.send_json(snap)
            for conn in room_conns.values():
                conn.flush()
            if game.over:
                ui.button(screen, (SCREEN_W // 2 - 110, ROWS * TILE // 2 + 66,
                                   220, 46),
                          T("返回房間", "Back to room"), "lobbyret",
                          size=20, base=(46, 140, 96))
        elif state == "net_game" and net_role == "client":
            km = NET_KEYMAP
            dirs = [d for d in ("up", "down", "left", "right")
                    if keys[km["dirs"][d]]]
            if touch_ui:
                dirs = sorted(set(dirs) | set(pad_dirs(touch)))
            for _js in pads.values():
                dirs = sorted(set(dirs) | set(pad_dirs(_js)))
            bomb = use = swp = skl = 0
            for e in events:
                if e.type == pygame.JOYBUTTONDOWN:
                    if e.button == 0:
                        bomb += 1
                    elif e.button == 1:
                        use += 1
                    elif e.button == 2:
                        skl += 1
                    elif e.button == 3:
                        swp += 1
            for act in touch_acts:
                if act == "a":
                    bomb += 1
                elif act == "b":
                    use += 1
                elif act == "x":
                    skl += 1
                elif act == "y":
                    swp += 1
            for e in events:
                if e.type == pygame.KEYDOWN:
                    if e.key in km["action"]:
                        bomb += 1
                    elif e.key in km["use"]:
                        use += 1
                    elif e.key in km.get("swap", []):
                        swp += 1
                    elif e.key in km.get("skill", []):
                        skl += 1
            net.send_json({"t": "in", "d": dirs, "b": bomb, "u": use, "s": swp, "k": skl})
            last_st = None
            back_to_room = False
            for m in net.poll():
                if m.get("t") == "st":
                    last_st = m
                elif m.get("t") == "lb2":
                    back_to_room = True
            net.flush()
            if back_to_room:
                view = None
                state = "room_client"
                screen.fill((26, 34, 52))
            elif net.closed:
                client_teardown()
                notice = T("與房間斷線", "Disconnected from the room")
                state = "title"
            else:
                if view is not None and last_st is not None:
                    apply_snapshot(view, last_st)
                if view is not None:
                    view.draw(screen)
                    tag = get_font(15).render(
                        T("你是 P%d(空白放球,X 用道具,Z 對調道具槽)" % (my_gid + 1),
                          "You are P%d (Space bomb, X use item, Z swap)" % (my_gid + 1)),
                        True, (255, 255, 255))
                    bg = pygame.Surface((tag.get_width() + 12,
                                         tag.get_height() + 6), pygame.SRCALPHA)
                    bg.fill((0, 0, 0, 110))
                    screen.blit(bg, (6, 3))
                    screen.blit(tag, (12, 6))
                else:
                    screen.fill((26, 34, 52))
                    w = get_font(26).render(T("等待主機資料…", "Waiting for host..."),
                                            True, (255, 255, 255))
                    screen.blit(w, w.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2)))
        else:
            game.update(dt, keys, events)
            game.draw(screen)

        # 音效偵測(本機與連線皆適用)
        if state == "game" and game is not None:
            sfx_watch.tick(game, sfx)
        elif state == "net_game":
            sfx_watch.tick(game if net_role == "host" else view, sfx)

        net_slots = None
        if state == "net_game":
            me = None
            if net_role == "host" and game is not None:
                me = game.players[0]
            elif net_role == "client" and view is not None:
                me = view.players[my_gid] if my_gid < len(view.players) else None
            if me is not None:
                net_slots = (me.slot_a, me.slot_b, me.char, me.skill_cd)
                if off_x < 110:      # 視窗模式:畫在畫布右上角
                    draw_slot_panel_inline(screen, me.slot_a, me.slot_b, t)
                    if me.char is not None:
                        cdl = me.skill_cd
                        lab = get_font(12).render(
                            T("C %s%s" % (CHAR_DEFS[me.char]["skill_zh"],
                                          "" if cdl <= 0 else "(%d)" % math.ceil(cdl)),
                              "C %s%s" % (CHAR_DEFS[me.char]["skill_en"],
                                          "" if cdl <= 0 else " (%d)" % math.ceil(cdl))),
                            True, (150, 230, 190) if cdl <= 0 else (170, 180, 200))
                        screen.blit(lab, (SCREEN_W - lab.get_width() - 18, 104))
                    net_slots = None
        present(net_slots)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pygame.quit()   # Ctrl+C 直接安靜離開,不噴 traceback
