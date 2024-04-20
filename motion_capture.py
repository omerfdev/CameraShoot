# motion_capture.py

import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Kamera nesnesi oluştur
kamera = cv2.VideoCapture(0)

# Mail gönderme fonksiyonu
def mail_gonder(gonderilecek_adres, gonderen_adres, gonderen_sifre, foto):
    msg = MIMEMultipart()
    msg['From'] = gonderen_adres
    msg['To'] = gonderilecek_adres
    msg['Subject'] = "Hareket Algılandı!"

    text = MIMEText("Hareket algılandı ve fotoğraf ektedir.")
    msg.attach(text)

    image = MIMEImage(open(foto, 'rb').read(), name='motion_capture.jpg')
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gonderen_adres, gonderen_sifre)
    server.sendmail(gonderen_adres, gonderilecek_adres, msg.as_string())
    server.quit()

# Ana döngü
while True:
    ret, kare = kamera.read()

    # Burada kare işlenir ve hareket algılanıp algılanmadığı kontrol edilir

    if hareket_algılandı: # Hareket algılandıysa
        cv2.imwrite("motion_capture.jpg", kare) # Fotoğrafı kaydet
        mail_gonder("alıcı@mail.com", "gonderici@mail.com", "gonderici_sifre", "motion_capture.jpg") # Fotoğrafı mail ile gönder

        # İşlem tamamlandığında çıkış yap
        break

# Kamera nesnesini serbest bırak
kamera.release()
cv2.destroyAllWindows()
