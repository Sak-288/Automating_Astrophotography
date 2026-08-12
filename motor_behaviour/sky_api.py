from skyfield.api import load
from skyfield.api import N, W, wgs84
import time
from motor_turn import move

ts = load.timescale()
t = ts.now()
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']
casablanca = earth + wgs84.latlon(33.5899 * N, 7.6039 * W)

astrometric = casablanca.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

move(az, 1)
time.sleep (5)
move(alt, 1)