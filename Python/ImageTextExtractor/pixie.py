"""
Informações sobre o programa:

Este programa extrai textos de capturas de tela.
Melhorias ainda podem ser feitas neste código.

Link para baixar o executável, tesseract e o banco de dados com os idiomas português, inglês e espanhol:
    https://drive.google.com/drive/folders/1lDVniifW8cQoKCfncXj322wi1hILP1es?usp=share_link

OCR - Reconehcimento de Caracter Ótico
open-cv (pip install opencv-python)
tesseract (pip install pytesseract)

links úteis:
    corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
    instalar idioma: https://github.com/tesseract-ocr/tessdata
    idiomas: print(pytesseract.get_languages())
"""

# Author(s): Dhytm <alissondin.developer@gmail.com>;
#            https://github.com/Dhytm
#
# License: MIT License,
# https://github.com/Dhytm/Contributions/blob/main/LICENSE


import pytesseract
import cv2
import pyautogui
import pyperclip as pc
import os
print('▶  ピクシーへようこそ ©')
print('▶  Created by Dhytm <https://github.com/Dhytm>\n')


def pixie():
    """_summary_

    How to use it:
        Run the code;
        Enter the language of the text to be extracted;
        With the commands "Win+Shift+S" capture only the area of the screen containing the text for extraction;
            Automatically after the capture, will appear in your transfer area the place for you to
            save the image. Use the "Win+V" command to get the path and save the capture in the location you entered;
        Go back to the screen where the code is being executed and press "enter"
            Automatically the image text will be sent to your clipboard.
    """

    def encode_idiom(idiom):
        if idiom == '':
            idiom = 'por'
        elif 'eng' in idiom:
            idiom = 'eng'
        elif 'spa' in idiom:
            idiom = 'spa'
        return idiom

    print('▶  Everything is ready for extraction. Go ahead!')
    print('▶  [format - JPG]\n')

    idiom = input('▶  [eng] [spa] (NaN = [por]): ')
    idiom = encode_idiom(idiom)
    print(f'▶  [{idiom}]')

    print(f'▶  Path: {os.getcwd()}')
    pc.copy(f'{str(os.getcwd())}')

    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('win', 'shift', 's')

    input('>> press enter to continue: ')

    # Read the image
    pasta = './'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if '.jpg' in str(arquivo).casefold() or '.png' in str(arquivo).casefold():
                image = cv2.imread(rf'{arquivo}')

    path = r"Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = rf'{path}\tesseract.exe'

    # Extract the text from the image
    txt = pytesseract.image_to_string(image, lang=f"{idiom}")

    print(f'\n▶  extração completa de texto:\n"\n{str(txt)}\n"\n')
    pc.copy(txt)

    pasta = './'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if '.jpg' in str(arquivo).casefold().strip() or '.png' in str(arquivo).casefold().strip():
                os.remove(arquivo)
                print(f'▶  "{arquivo}" has been removed!')
                break
    print(f'▶  extraction already available on the clipboard!')
    nexecut = input('>>  rerun (y/n)? ')
    if 'y' in str(nexecut).casefold().strip():
        pixie()
    else:
        pass


pixie()
