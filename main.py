from codpy import cod
import cv2
import playsound as ps
import keyboard
import time
import os

print("""
      
      
                     ______
                  .-"      "-.
               ' /            \ ' 
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |    DİKKAT BU UYGULAMA TEST ASAMASINDADIR !!!
                |/     /\     \|
      (@_       (_     ^^     _)    OLUMSUZ SONUCLAR DOGURABİLİR
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________> 
       )_/        \          /
      (@           `--------` yapımcı ayalkin V: 0.1""")

time.sleep(1)
for i in range(20):
    print('')

print("""
                        ____________
                      .~      ,   . ~.
                     /                \ 
                    /      /~\/~\   ,  \ 
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
      
      
                     BAŞARILAR ÇAYLAAAK
      """)





window_name= "Call of Duty®: Modern Warfare®"

cd = cod()
ilk_giris = 0

while True:
  
  if ilk_giris == 1:
    
      while True:
          if keyboard.is_pressed("shift+s"):
              os.system("cls")
              print("""
                    
          _/﹋\_
          (҂`_´)
          <,︻╦╤─ ҉ - -SSS
          _/﹋\_       ÇATIŞMAYA DEVAAAAAAA@m
    """)
              cd.screen_resulation(window_name)
              break
      
  sound = ps.playsound("sound\ichigo bankai.mp3")
  ilk_giris = 1
  
  ########################################################################
  while True:
    last_time = time.time()
    
    kordinat = cd.img_search(threshold = 0.39) # 120 olduğu zaman 0.39 
    
    if kordinat is not None:
      cd.shoot_point(x = kordinat[0], y = kordinat[1], w = kordinat[2], h = kordinat[3], 
                     body_height = 55 )  
    
    cv2.waitKey(1)  
  ########################################################################
    
    # Shift + s tuşlarına basınca programı durduruyor
    if keyboard.is_pressed("shift+s"):
      cv2.destroyAllWindows()
      os.system("cls")
      print("""   
       ___
      (._.)
       <|>
      _/\_    Program durduruldu...""") 
      sound = ps.playsound("sound\ganbare ganbare senpai.mp3")
      break
    
    print("fps:", round((1 / (time.time() - last_time))))
  


# 0x306e4 
# 0x10104
# 0xf03ae
# 0x10672 windowcapture.py - Başlıksız (Çalışma Alanı) - Visual Studio Code
# 0x220956 Fatura
# 0xe0452 İstediğin Buysa • 110 - Google Chrome
# 0x5044c
# 0x180486 Windows PowerShell
# 0x1b06ae Call of Duty®: Modern Warfare®
# 0x3807a2
# 0x403ce
# 0x203e2 Posta
# 0x30400 Gelen Kutusu - Hotmail - Posta
# 0x20252 Ayarlar
# 0x203ee Ayarlar
# 0x10302 NVIDIA GeForce Overlay
# 0x3009d6
# 0x101ae
# 0x101a6
# 0x10192
# 0x10180
# 0x1017e
# 0x2017c
# 0x3017a
# 0xa063a
# 0x309ac
# 0x10146 Program Manager
# None