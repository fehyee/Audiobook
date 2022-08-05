import pyttsx3
import PyPDF2

speaker = pyttsx3.init() #Initialize the pyttsx3 module
book = open(r'c:\Users\ANTHONY\Downloads\PORTFOLIO\Audiobook\sample.pdf', 'rb') #Open the book
pdfReader = PyPDF2.PdfFileReader(book) #Read the book
Pages_no = pdfReader.numPages #Get the number of pages in the book



voices = speaker.getProperty('voices') #Gets the current voice type
speaker.setProperty('voice', voices[0].id) #Changing index, changes voice

rate = speaker.getProperty('rate') #Gets the current rate
speaker.setProperty('rate', 150) #Sets the new rate of speech (from 2.0x to 1.5x)

volume = speaker.getProperty('volume') #Gets the current volume (min=0, max=1)
speaker.setProperty('volume', 1.0) #Sets up the volume

#Loop through the total number of pages
for each_page in range(0, Pages_no):
    page = pdfReader.getPage(each_page)
    text = page.extract_text()
    #speaker.say(text)
    speaker.save_to_file(text, 'audioplay.mp3')
    speaker.runAndWait()
speaker.stop()


    
