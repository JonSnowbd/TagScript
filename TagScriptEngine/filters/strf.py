import time
import re

STRF_REGEX = re.compile(r"strf{(.+?)}")

class STRFFilter():
    def Process(self, engine, text):
        matches = STRF_REGEX.finditer(text)
        if matches is None:
            return text

        t = time.gmtime()
        for match in matches:
            try:
                text = text.replace(match.group(0), time.strftime(match.group(1), t))
            except ValueError as e:
                text = text.replace(match.group(0), f"<<strf error>> {type(e).__name__}: {e}")
    
        return text