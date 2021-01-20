# Build language translator python code

from googletrans import Translator

translater=Translator()

story='''Tell me who does not love baby yoda from Mandolarian?
Baby yoda, Baby yoda,
Baby yoda has shaken me like soda.
'''

out=translater.translate(story,dest="bn")

print(out.text)

