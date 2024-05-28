import spacy
import speech_recognition as sr
from spacytextblob.spacytextblob import SpacyTextBlob
import pyttsx3

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

r = sr.Recognizer()

print(" say somthing ...")

for  i in range(0,1):    
     
    try:
         
    
        with sr.Microphone() as source2:
             

            audio2 = r.listen(source2)

            print("processing ....")
             
            text = r.recognize_google(audio2)
            text = text.lower()
            print(text)
            
            data=nlp(text)
         
            if data._.polarity>0:
                command="you have decent review"
            else:
                command="you are doing totally wrong   just stop doing it"
                
            engine = pyttsx3.init()
            engine.say(command) 
            engine.runAndWait()
                  


    except Exception as e:
        print("crashed",e)
            
