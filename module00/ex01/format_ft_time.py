import time
from datetime import datetime

secs = time.time()
science = "{:e}".format(secs)
print(f"Seconds since January 1, 1970: {secs:,} or {science} in scientitific notation")
print(datetime.now().strftime("%b %d %Y"))
