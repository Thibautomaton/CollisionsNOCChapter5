from Particle import Particle
from bordure import Bordure
from Box2D import b2ContactListener

class MyContactListener(b2ContactListener):
    def BeginContact(self, contact):
        a = contact.fixtureA.body.userData
        b = contact.fixtureB.body.userData


        if isinstance(a, Particle) and isinstance(b, Particle):
            if a.lifespan<950:
                a.markedFD =True
                print("delete")
            if b.lifespan<950:
                b.markedFD = True
                print("delete")



    def EndContact(self, contact):
        a = contact.fixtureA.body.userData
        b = contact.fixtureB.body.userData

        if isinstance(b, Bordure) and isinstance(a, Particle):
            a.border = (0, 0, 255)

        elif isinstance(a, Bordure) and isinstance(b, Particle):
            b.border = (0, 255, 0)


