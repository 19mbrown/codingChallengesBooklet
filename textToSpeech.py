from gtts import gTTS

tts = gTTS(input("Enter a string: "), lang='en', tld='co.uk')
tts.save('hello.mp3')
