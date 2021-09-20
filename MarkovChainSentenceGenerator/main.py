import random
text = """KENNEDY SPACE CENTER, FL, September 18, 2021 – After three days orbiting Earth, the astronauts of Inspiration4 flying aboard SpaceX’s Dragon spacecraft safely splashed down in the Atlantic Ocean off the coast of Kennedy Space Center, Florida, at 7:06 p.m. EDT. The return marks the completion of the world’s first all-civilian human spaceflight to orbit, which launched on a flight-proven SpaceX Falcon 9 rocket from historic Launch Complex 39A at NASA’s Kennedy Space Center in Florida on Wednesday, Sept. 15, 2021.

Teams on SpaceX’s Go Searcher recovery ship are in the process of securing the spacecraft to be hoisted onto the main deck of the ship, where the Inspiration4 crew will egress the spacecraft and receive medical checks before a helicopter ride back to Kennedy Space Center.

The mission completed several historic firsts, including the:

· First all-civilian human spaceflight to orbit 

· First black female spacecraft pilot

· Youngest American in space

· First person to fly to space with a prosthetic

· Farthest flight for a human spaceflight since the Hubble missions

· First time SpaceX has operated three Dragons in space

· First free-flight of a Dragon spacecraft on a human spaceflight mission
KENNER
· Largest contiguous window ever flown in space

· First splashdown of a Dragon crew in the Atlantic Ocean

· First thrice-flown Falcon 9 booster to launch a human spaceflight mission

Finally, true to the mission’s name and purpose, Inspriation4 has raised nearly $154M dollars and counting for St. Jude Children’s Research Hospital®.

To learn more and see highlights from the Inspiration4 mission, visit www.inspiration4.com and follow Twitter (@inspiration4x), Facebook (@inspiration4mission) Instagram (@inspiration4) and YouTube (@Inspiration4). To support St. Jude Children’s Research Hospital and learn more about auction items from the flight and additional support opportunities, visit stjude.org/inspiration4. 

###

Media Contacts: 

Brian Bianco

BCW for Inspiration4"""
order = 5
alldic = {} 

for i in range(0 , len(text)-order):
    ngram = text[i:i+order]
    if ngram not in alldic:
        alldic[ngram] = []
    alldic[ngram].append(text[i+order]) 

currentgram = text[0:order]
result = currentgram
for i in range(0,999):
    poss = alldic[currentgram]
    next =  random.choice(poss)
    result = result + next
    len1 = len(result)
    currentgram = result[len1-order:len1]

print(result)
