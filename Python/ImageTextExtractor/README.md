This program extracts text from screenshots.
Improvements can still be made to this code.

    How to use it:
        Download the "Tesseract-OCR" folder on:
            https://drive.google.com/drive/folders/1lDVniifW8cQoKCfncXj322wi1hILP1es?usp=share_link;
        Keep the "Tesseract-OCR" folder in the same location as the "pixie.py" file;
        Run the code;
        Enter the language of the text to be extracted;
        With the commands "Win+Shift+S" capture only the area of the screen containing the text for extraction;
            Automatically after the capture, will appear in your transfer area the place for you to
            save the image. Use the "Win+V" command to get the path and save the capture in the location you entered;
        Go back to the screen where the code is being executed and press "enter"
            Automatically the image text will be sent to your clipboard.            

Link to download the executable, Tesseract-OCR folder and the database in Portuguese, English and Spanish:
    https://drive.google.com/drive/folders/1lDVniifW8cQoKCfncXj322wi1hILP1es?usp=share_link

Useful links:<br />
    fix windows installation: 
        https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i<br />
    install new language: 
        https://github.com/tesseract-ocr/tessdata<br />
    languages: 

            print(pytesseract.get_languages())
