# 🎯 Cod Mod War

**Görüntü işleme ile ekran üzerindeki belirli noktaları tespit ederek fare konumlandırması yapan bir Python projesi. Eğitim teknik gelişim ve eğlence amacıyla geliştirilmiştir. Beta aşamasındadır**

## 🧠 Amaç

Bu proje, Call of Duty: Modern Warfare gibi FPS oyunlarında ekranın belirli alanlarında görsel hedeflerin tespiti ve otomatik işaretleme amacıyla geliştirilmiştir. Görüntü işleme teknikleriyle, ekranın merkezine yakın bir bölgede hedef tespiti yaparak fareyi bu hedefe yönlendirmektedir.  
**Tamamen teknik gelişim, görüntü işleme pratiği ve Python becerilerini artırmak amacıyla yazılmıştır.**

## ⚙️ Özellikler

- Ekranın orta bölgesini tarar (optimizasyon ve hız için)
- Grid yapısı ile ekranı 32 adet kareye ayırır
- Belirlenen karelerde hedef araması yapar
- Eşleşme sağlandığında imleci otomatik olarak hedefin üzerine taşır
- Görüntü işleme ve otomasyon teknikleri içerir

## 📐 Ölçüm grid

Proje, farklı ekran çözünürlüklerinde de tutarlı çalışabilmesi için ekranı 32 eş parçaya (4 satır x 8 sütun) böler. Sadece ortadaki 4 kare alanı tarar. Böylece ekran boyutundan bağımsız olarak her zaman merkeze yakın alan hızlı ve etkili şekilde analiz edilir. Bu yöntem, performans optimizasyonu ve gereksiz alanların işlenmesini engellemek için kullanılmıştır.

![Örnek Görsel](img/Ölçüler.png)


## 🛠️ Kullanılan Teknolojiler

- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [MSS](https://github.com/BoboTiG/python-mss)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [pywin32](https://github.com/mhammond/pywin32)
- [PyAutoIt](https://pypi.org/project/PyAutoIt/)
- [Playsound](https://pypi.org/project/playsound/)
- [Keyboard](https://pypi.org/project/keyboard/)
- [Pillow (PIL)](https://python-pillow.org/)

## 📦 Kurulum

```bash
pip install opencv-python numpy mss pyautogui pywin32 -U pyautoit playsound keyboard Pillow
