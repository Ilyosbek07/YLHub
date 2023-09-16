import os
import PyPDF2
from mutagen.mp3 import MP3
from django.conf import settings

def get_num_pages(path):
    try:
        pdf_reader = PyPDF2.PdfReader(path)
        num_pages = len(pdf_reader.pages)
        return num_pages
    except:
        return None
    
def get_audio_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None
    