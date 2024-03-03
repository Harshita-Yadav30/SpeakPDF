import PyPDF2
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import os, io

#Extract Content from PDF
# def extract_content(filename):
#     pdfFileObj = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfReader(pdfFileObj)

#     text_content = []

#     for index, text in enumerate(pdfReader.pages):
#         pageObj = text
#         text_content.append(pageObj.extract_text())

#     pdfFileObj.close()
#     return text_content

def extract_content(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text_content = ""

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()

    return text_content

#Text to Speech Conversion
# def text_to_speech(text, file, language='en'):
#     tts = gTTS(text=text, lang=language, slow=False)
#     filename = f"{file.replace(' ','_')}.mp3"
#     path = os.path.join("C:/Users/harsh/OneDrive/Desktop/Projects/SpeakPDF/converted_files/", filename)

#     tts.save(path)
#     return path

def text_to_speech(text, file, ch, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    with io.BytesIO() as f:
        tts.write_to_fp(f)
        audio_data = f.getvalue()
    
    filename = file.split('.')[0] + ".mp3"
    
    if ch == 1:
        path = os.path.join("C:/Users/harsh/OneDrive/Desktop/Projects/SpeakPDF/static/converted_files", filename)
    else:
        path = os.path.join("C:/Users/harsh/OneDrive/Desktop/Projects/SpeakPDF/static/hindi_files", filename)

    with open(path, 'wb') as audio_file:
        audio_file.write(audio_data)
    return path

# Path:- C:/Users/harsh/Downloads/SWD Brochure - Aatmabodh'24.pdf

#Play the audio
def play_audio(audio_file):
    try:
        playsound(audio_file, True)

    except Exception as e:
        print("Error playing audio file:", e)


#English to Hindi Conversion
def translate_to_hindi(text):
    if text:
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='hi').text
        return translated_text
    else:
        print("Problem")

#Main Program
def run():
    print("Choose:")
    print("\t1. To listen to the PDF content")
    print("\t2. To convert PDF content from English to Hindi")
    choice = int(input("Enter your choice: "))

    path = input("Enter the complete path to the PDF file: ")

    if choice == 1:
        text_to_speech(extract_content(path))

    elif choice == 2:
        text_to_speech(translate_to_hindi(extract_content(path)))
