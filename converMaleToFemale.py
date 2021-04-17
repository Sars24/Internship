engine= pyttsx3.init()
 
rate = engine.getProperty("rate")
print(rate)

engine.setProperty("rate",20)

volume = engine.getProperty("volume")
print(" colume is {0}".format(volume))

engine.setProperty("volume",1)


voices = engine.getProperty("voices")

print("Male Voice : {0}".format(voices[0].id))
print("Female Voice : {0}".format(voices[1].id)) 

engine.setProperty("voices", voices[1].id)


engine.say("hello, I am a candidate for the internship")
engine.runAndWait()