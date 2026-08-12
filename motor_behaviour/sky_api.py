from skyfield.api import load
from skyfield.api import N, W, wgs84
import time
from motor_turn import move
import re

def parse_dms(s: str) -> float:
    m = re.match(r"(-?\d+)deg\s+(\d+)'\s+([\d.]+)\"", s)
    d, mm, ss = int(m.group(1)), int(m.group(2)), float(m.group(3))
    sign = -1 if d < 0 else 1
    return sign * (abs(d) + mm/60 + ss/3600)

ts = load.timescale()
t = ts.now()
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']
casablanca = earth + wgs84.latlon(33.5899 * N, 7.6039 * W)

astrometric = casablanca.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

move(parse_dms(str(alt)), 0)
move(parse_dms(str(alt)), 1)
