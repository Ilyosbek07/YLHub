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
    
def format_seconds(seconds):
    result = {}
    result["days"] = seconds // 86400
    seconds %= 86400
    result["hours"] = seconds // 3600
    seconds %= 3600
    result["minutes"] = seconds // 60
    seconds %= 60
    result["seconds"] = seconds
    return result

def merge_two_sorted_queries_list(list1, list2, is_dict=False):
    result = []
    if is_dict:
        while list1 and list2:
            if list1[0]["updated_at"] < list2[0]["updated_at"]:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
    else:
        while list1 and list2:
            if list1[0].updated_at > list2[0].updated_at:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
    if list1: result += list1
    elif list2: result += list2
    return result
