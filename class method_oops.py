class animal:
    legs='4'
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))
animal.walk('dog')
animal.walk('cat')