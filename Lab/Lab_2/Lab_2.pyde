sunLocation = (250, 250)
sunRadius=50
yellow=(255,255,0)

earthRadius=30
blue=(0,0,255)
earthOrbitalRadius=170
earthSpeed=0.5

marsRadius=20
red=(255,0,0)
marsOrbitalRadius=80
marsSpeed=1

moonRadius=10
white=(255,255,255)
moonOrbitalRadius=45
moonSpeed=2.3

def getLocation(orbitAroundLocation,orbitRadius,speed,time):
    centerX=orbitAroundLocation[0]+orbitRadius*sin(speed*time)
    centerY=orbitAroundLocation[1]+orbitRadius*cos(speed*time)
    return (centerX,centerY)

def drawCelestialBody(location,radius,color):
    fill(*color)
    locX,locY=location
    ellipse(locX,locY,radius*2,radius*2)  
    
class Sun:
    def __init__(self, location, radius, sun_color):
        self._location = location
        self._radius = radius
        self._color = sun_color
        self.planet_list = []
    
    def _getLocation(self, time):
        return getLocation(self._location, 0, 0, time)

    def draw(self, time):
        drawCelestialBody(self._getLocation(time), self._radius, self._color)
        for i in self.planet_list:
            #drawCelestialBody(i._getLocation(time), i._radius, i._color)
            i.draw(time)

    def addPlanet(self, radius, orbital_radius, color, speed):
        p = Planet(radius, orbital_radius, color, speed, self)
        self.planet_list.append(p)
        return p
         
class Planet(Sun):
    def __init__(self, radius, orbital_radius, planet_color, speed, orbiting_around):
        self._radius = radius
        self._orbital_radius = orbital_radius
        self._color = planet_color
        self._speed = speed
        self.planet_list = []
        self.orbiting_around = orbiting_around
    
    def _getLocation(self, time):
        return getLocation(self.orbiting_around._getLocation(time), self._orbital_radius, self._speed, time)

def setup():
    size(500,500)
    global sun
    global t
    t=0
    sun=Sun(sunLocation,sunRadius,yellow)
    earth=sun.addPlanet(earthRadius,earthOrbitalRadius,blue,earthSpeed)
    sun.addPlanet(marsRadius,marsOrbitalRadius,red,marsSpeed)
    earth.addPlanet(moonRadius,moonOrbitalRadius,white,moonSpeed)
    
def draw():
    global t
    t+=0.02
    background(0)
    sun.draw(t)