import time

class STRFFilter():
    def Process(self, engine, text):
        if not "%" in text:
            return text
        t = time.gmtime()
        day = time.strftime("%d", t)
        month = time.strftime("%m", t)
        year = time.strftime("%Y", t)

        return text.replace("%y", year).replace("%m", month).replace("%d", day)