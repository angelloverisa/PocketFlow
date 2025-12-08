import os
import sys
from waitress import serve
from PocketFlow.wsgi import application 

def main():
    # Mengatur PATH untuk PyInstaller
    if getattr(sys, 'frozen', False):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'PocketFlow.settings'
        # Jika Anda perlu mengakses berkas statis atau media
        os.environ['STATIC_ROOT'] = os.path.join(sys._MEIPASS, 'static')
    
    # Menjalankan server Waitress
    print("Starting Django server on http://127.0.0.1:8000/")
    serve(application, host='127.0.0.1', port='8000')

if __name__ == '__main__':
    main()