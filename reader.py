import pyttsx3
import PyPDF3

book = open('./basic/oop.pdf', 'rb')

pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for num in range(3, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
