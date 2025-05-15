import cv2
import numpy as np
import mss
from win32api import GetSystemMetrics
import win32api
import win32gui
import win32con
import autoit

class cod():
    def __init__(self):
        self.screen_resulation()
        self.sam_mask = self.sample_img()
    
    def screen_resulation(self):
        yukseklik = GetSystemMetrics(1)
        genislik = GetSystemMetrics(0)
        
        # print("Width =", GetSystemMetrics(0))
        # print("Height =", GetSystemMetrics(1))
        # self.capture_yukseklik = round(2*(yukseklik/4)) 
        # self.capture_genislik =  round(2*(genislik/8))
        # self.capture_y = round(1*(yukseklik/4))
        # self.capture_x = round(3*(genislik/8))
        
        self.merkez_nokta = round((genislik/2)), round((yukseklik/2))
        
        self.birim_yukseklik = yukseklik / 4
        self.birim_genislik = genislik / 8

        self.capture_yukseklik = round(2*(self.birim_yukseklik)) 
        self.capture_genislik =  round(2*(self.birim_genislik))
        self.capture_y = round(1*(self.birim_yukseklik))
        self.capture_x = round(3*(self.birim_genislik))
        # if window_name is None:
        #     hwnd = win32gui.GetDesktopWindow()
        # else:
        #     hwnd = win32gui.FindWindow(None, window_name)
        #     # win32gui.SetForegroundWindow(hwnd)
        #     # win32gui.ShowWindow(hwnd,win32con.SW_NORMAL)
        #     # win32gui.SetFocus(hwnd)
        #     if not hwnd:
        #         raise Exception('{} penceresi bulunamadı.'.format(window_name))

        # # Pencerenin olculerini ogreniyoruz
        # window_rect = win32gui.GetWindowRect(hwnd)
        # genislik = window_rect[2] - window_rect[0]
        # yukseklik = window_rect[3] - window_rect[1]

        # self.merkez_nokta = round((genislik/2)), round((yukseklik/2))
        
        # birim_yukseklik = yukseklik / 4
        # birim_genislik = genislik / 8

        # self.capture_yukseklik = round(2*(birim_yukseklik)) 
        # self.capture_genislik =  round(2*(birim_genislik))
        # self.capture_y = round(1*(birim_yukseklik)) + window_rect [1]
        # self.capture_x = round(3*(birim_genislik)) + window_rect[0]
        
    def screenshot(self):

        with mss.mss() as sct:
            # Yakalanacak ekranın bir kısmı
            monitor = {"top": self.capture_y, "left": self.capture_x, "width": self.capture_genislik, "height": self.capture_yukseklik} #{"top": 0, "left": 0, "width": 600, "height": 300}

            # Ekrandan ham pikselleri alın, bir Numpy dizisine kaydedin
            img = np.array(sct.grab(monitor))
            
            # Görseli BGR 'dan HSV 'ye ceviriyoruz
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # HSV renk uzayını kırmızı renk için daraltmaya calısıyoruz
            lower_red = np.array([1,225,0])    #([161,155,84])  ([0,225,0])   ([180,0,140])   ([0,203,141])
            upper_red = np.array([2,255,255])  #([179,255,255]) ([5,255,255]) ([179,255,144]) ([3,255,255])
            # HSV göreselde kırmızıyı arıyoruz
            mask = cv2.inRange(hsv, lower_red, upper_red)
            # Bitwise-AND mask and original image
            # res = cv2.bitwise_and(img,img, mask= mask)
            
            # cv2.imshow('frame',img)
            # cv2.imshow('mask',mask)
            # cv2.imshow('res',res)

            return img, mask
    
    def sample_img(self):
        # Arayacagimizi goruntuyu bilgisayara tanıtıyoruz
        sample_img = cv2.imread('img\\red-ping2.png') 
        # Görseli BGR 'dan HSV 'ye ceviriyoruz
        hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)
       
        # HSV renk uzayını kırmızı renk için daraltmaya calısıyoruz
        lower_red = np.array([1,225,0])    #([161,155,84])  ([0,225,0])   ([180,0,140])   ([0,203,141])
        upper_red = np.array([2,255,255])  #([179,255,255]) ([5,255,255]) ([179,255,144]) ([3,255,255])
        # HSV göreselde kırmızıyı arıyoruz
        mask = cv2.inRange(hsv, lower_red, upper_red)
        # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(sample_img, sample_img, mask= mask)
       
        # cv2.imshow('frame',sample_img)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        
        return mask
            
    def img_search(self, threshold = 0.33, ciz = 1):
        
        mon_img, mon_mask = self.screenshot()
        
        # Ekran goruntusunun icerisinde ornek resmi ariyoruz
        Sonuc =	cv2.matchTemplate(mon_mask, self.sam_mask, cv2.TM_CCOEFF_NORMED) 
        # Bulunan objenin kordinatlarini buluyor
        min_val, max_val, min_loc, max_loc	=	cv2.minMaxLoc(Sonuc) 
        
        if (max_val > threshold): 
            w, h = self.sam_mask.shape[::-1]
            x, y = max_loc
            
            if(ciz == 1):
                Ust_Sol 							=	max_loc #Bulunan Objenin Ust ve Sol Uzakligi
                Alt_Sag								=	(Ust_Sol[0] + w, Ust_Sol[1] + h) #Bulunan Objenin Alt ve Sag Uzakligi
                cv2.rectangle(mon_img, Ust_Sol, Alt_Sag, (0,255,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle    
         
                ust_sol = round(((w/2) + x)), round((y + 48))
                alt_sag = round((ust_sol[0] + 1)), round((ust_sol[1] + 1))
                cv2.rectangle(mon_img, ust_sol, alt_sag, (225,0,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle    
                
                #cv2.imshow('EKRAN',mon_img) 
                print('kordinat',str(int(max_loc[0]+self.capture_x)),str(int(max_loc[1]+self.capture_y)), 'en boy', w,h) 
                
                return (x + (self.capture_x)), (y + self.capture_y), w, h
            # Çekilen görüntünün üstündeki kordinatları söylediği için ekleme yapıyoruz     
            return (x + (self.capture_x)), (y + self.capture_y), w, h
                          
        else:
            # print('hadiama', max_val)
            # print("Tespit Edilemedi")
            pass
            
    def shoot_point(self, x=None, y=None, w=None, h=None, body_height = 55,):
        # Nisan noktasini y den daha hassas degistirebiliriz
        shoot_point = round(((w/2) + x)), round((y + body_height))
        
        # https://stackoverflow.com/questions/63396535/moving-cursor-in-a-game-using-pyautoit-makes-the-cursor-always-look-up-down
        # https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
        # https://stackoverflow.com/questions/67647899/move-mouse-in-fullscreen-game-with-python
        # https://www.unknowncheats.me/forum/general-programming-and-reversing/343136-move-mouse-fps-game.html
        #pyautogui.moveTo(shoot_point[0], shoot_point[1], sensivity)
        #win32api.SetCursorPos((shoot_point[0], shoot_point[1]))
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, shoot_point[0], shoot_point[1], 0, 0)
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(shoot_point[0]/win32api.GetSystemMetrics(0)*65535), int(shoot_point[1]/win32api.GetSystemMetrics(1)*65535) ,2 ,2)
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(shoot_point[0]), int(shoot_point[1]), 0, 0)
        #ctypes.windll.user32.SetCursorPos(shoot_point[0], shoot_point[1], 0, 0)
        #autoit.mouse_move(960, 540,1) #1
        
        autoit.mouse_move(shoot_point[0], shoot_point[1],0)#0
        autoit.mouse_move(self.merkez_nokta[0],self.merkez_nokta[1], 1) #2
        
    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)