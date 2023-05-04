"""
bean tts model
"""
class TTS(object):
    def __init__(self, text = "", voice = "", output_name = "") -> None:
        self.text = text
        self.voice = voice
        self.output_name = output_name
        
    def set_text(self, text):
        self.text = text
        
    def get_text(self):
        return self.text
    
    def set_voice(self, voice):
        self.voice = voice
        
    def get_voice(self):
        return self.voice
    
    def set_output_name(self, output_name):
        self.output_name = output_name
        
    def get_output_name(self):
        return self.output_name
        
        
    
    