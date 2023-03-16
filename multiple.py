class Life:
    def parents(self):
        print("Parents try to give every child better life than they had.")
class Respect:
    def never(self):
        print("Never disrespect them in your life journey.")
class Love:
    def true(self):
        print("Their love towards you is true.")
class Peace(Life, Respect, Love):
    def live(self):
        print("Live peaceful with them.")
p=Peace()
p.parents()
p.never()
p.true()
p.live()