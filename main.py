import time
import speech_recognition as sr
from gtts import gTTS
import pygame

def bicara(teks, lang='id'):
    """Mengubah teks menjadi suara dan memutarnya."""
    print(f"Bot: {teks}")
    
    # Simpan suara ke file audio sementara
    tts = gTTS(text=teks, lang=lang, slow=False)
    filename = "temp_response.mp3"
    tts.save(filename)
    
    # Putar file audio menggunakan pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    pygame.mixer.quit()

def dengar_suara():
    """Merekam suara dari mikrofon dan mengonversinya menjadi teks."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n[Mendengarkan... Silakan bicara]")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
        try:
            print("[Mengenali suara...]")
            teks = recognizer.recognize_google(audio, language="id-ID")
            print(f"Anda: {teks}")
            return teks.lower()
        except sr.UnknownValueError:
            print("Bot: Maaf, suara tidak terdengar jelas.")
            return None
        except sr.RequestError:
            print("Bot: Gagal terhubung ke layanan konversi suara.")
            return None

def percakapan_utama():
    bicara("Halo! Saya asisten suara Anda. Ada yang bisa saya bantu?")
    
    while True:
        input_user = dengar_suara()
        
        if not input_user:
            continue
            
        # Logika percakapan sederhana
        if "keluar" in input_user or "stop" in input_user:
            bicara("Sampai jumpa lagi!")
            break
        elif "halo" in input_user or "hai" in input_user:
            bicara("Halo juga! Bagaimana kabarmu hari ini?")
        elif "nama kamu siapa" in input_user:
            bicara("Saya adalah program bot percakapan buatan Python.")
        else:
            bicara(f"Kamu tadi bilang: {input_user}")

if __name__ == "__main__":
    percakapan_utama()