#Kelvin Mei,Daniel Zheng
#ML2 Period 9

import pygame, sys, os, random
from pygame.locals import *
pygame.init ()
pygame.mixer.init ()
pygame.font.init ()
width = 1024
height = 768
size = width, height
screen = pygame.display.set_mode (size)
pygame.display.set_caption ('MapleSim')
dif = pygame.image.load("Dif.jpg")
dif = pygame.transform.scale (dif,(1024,768))
dif = dif.convert_alpha()
easy = pygame.image.load ("Easy.png").convert_alpha()
easyglow = pygame.image.load ("EasyGlow.png").convert_alpha()
normal = pygame.image.load ("Normal.png").convert_alpha()
normalglow = pygame.image.load ("NormalGlow.png").convert_alpha()
hard = pygame.image.load ("Hard.png").convert_alpha()
hardglow = pygame.image.load ("HardGlow.png").convert_alpha()
#Character Load
S = pygame.image.load ("CharS.png").convert_alpha()
W1 = pygame.image.load("CharW1.png").convert_alpha()
W2 = pygame.image.load("CharW2.png").convert_alpha()
W3 = pygame.image.load("CharW3.png").convert_alpha()
W4 = pygame.image.load("CharW4.png").convert_alpha()
S2 = pygame.image.load ("CharS2.png").convert_alpha()
W11 = pygame.image.load("CharW11.png").convert_alpha()
W22 = pygame.image.load("CharW22.png").convert_alpha()
W33 = pygame.image.load("CharW33.png").convert_alpha()
W44 = pygame.image.load("CharW44.png").convert_alpha()
alert = pygame.image.load ("CharAlert.png").convert_alpha()
Fly = pygame.image.load("Fly.png").convert_alpha()
Fly1 = pygame.image.load("Fly1.png").convert_alpha()
Fly2 = pygame.image.load("Fly2.png").convert_alpha()
Flying = [Fly1,Fly2]
Duck = pygame.image.load("Duck.png").convert_alpha()
charhit = pygame.image.load ("CharHit.png").convert_alpha()
#Monster Load
M = pygame.image.load("Monster.png").convert_alpha()
MH = pygame.image.load("MH.png").convert_alpha()
MD1 = pygame.image.load("MD1.png").convert_alpha()
MD2 = pygame.image.load("MD2.png").convert_alpha()
MD3 = pygame.image.load("MD3.png").convert_alpha()
MD4 = pygame.image.load("MD4.png").convert_alpha()
MD5 = pygame.image.load("MD5.png").convert_alpha()
MD6 = pygame.image.load("MD6.png").convert_alpha()
deathset = [MD1,MD2,MD3,MD4,MD5,MD6]
pig1 = pygame.image.load("Pig1.png").convert_alpha()
pig2 = pygame.image.load("Pig2.png").convert_alpha()
pig3 = pygame.image.load("Pig3.png").convert_alpha()
pigH1 = pygame.image.load("PigH1.png").convert_alpha()
pigD1 = pygame.image.load("PigD1.png").convert_alpha()
pigD2 = pygame.image.load("PigD2.png").convert_alpha()
pigD3 = pygame.image.load("PigD3.png").convert_alpha()
pigA1 = pygame.image.load("PigA.png").convert_alpha()
pigA2 = pygame.image.load("PigA2.png").convert_alpha()
pigA3 = pygame.image.load("PigA3.png").convert_alpha()
bg2 = pygame.image.load("Background.jpg").convert_alpha()
pigmove = [pig2,pig3]
pigdie = [pigD1,pigD2,pigD3]
pigaset = [pigA1,pigA2,pigA3]
walk = [W1,W2,W3,W4]
walk2 = [W11,W22,W33,W44]
#tele
Tele1 = pygame.image.load("Tele1.png").convert_alpha()
Tele2 = pygame.image.load("Tele2.png").convert_alpha()
Tele3 = pygame.image.load("Tele3.png").convert_alpha()
Tele4 = pygame.image.load("Tele4.png").convert_alpha()
teleset = [alert,Tele1,Tele2,Tele3,Tele4]
#AttackRight
AR1 = pygame.image.load("AR1.png").convert_alpha()
AR2 = pygame.image.load("AR2.png").convert_alpha()
AR3 = pygame.image.load("AR3.png").convert_alpha()
AR4 = pygame.image.load("AR4.png").convert_alpha()
AR5 = pygame.image.load("AR5.png").convert_alpha()
AR6 = pygame.image.load("AR6.png").convert_alpha()
AR7 = pygame.image.load("AR7.png").convert_alpha()
AR8 = pygame.image.load("AR8.png").convert_alpha()
AR9 = pygame.image.load("AR9.png").convert_alpha()
arset = [AR1,AR2,AR3,AR4,AR5,AR6,AR7,AR8,AR9]
#AttackLeft
AL1 = pygame.image.load("AL1.png").convert_alpha()
AL2 = pygame.image.load("AL2.png").convert_alpha()
AL3 = pygame.image.load("AL3.png").convert_alpha()
AL4 = pygame.image.load("AL4.png").convert_alpha()
AL5 = pygame.image.load("AL5.png").convert_alpha()
AL6 = pygame.image.load("AL6.png").convert_alpha()
AL7 = pygame.image.load("AL7.png").convert_alpha()
AL8 = pygame.image.load("AL8.png").convert_alpha()
AL9 = pygame.image.load("AL9.png").convert_alpha()
alset = [AL1,AL2,AL3,AL4,AL5,AL6,AL7,AL8,AL9]
#Carnival Edge
CE1 = pygame.image.load("CE1.png").convert_alpha()
CE2 = pygame.image.load("CE2.png").convert_alpha()
CE3 = pygame.image.load("CE3.png").convert_alpha()
CE4 = pygame.image.load("CE4.png").convert_alpha()
CE5 = pygame.image.load("CE5.png").convert_alpha()
CE6 = pygame.image.load("CE6.png").convert_alpha()
CE7 = pygame.image.load("CE7.png").convert_alpha()
CE8 = pygame.image.load("CE8.png").convert_alpha()
CE9 = pygame.image.load("CE9.png").convert_alpha()
CE10 = pygame.image.load("CE10.png").convert_alpha()
CE11 = pygame.image.load("CE11.png").convert_alpha()
CE12 = pygame.image.load("CE12.png").convert_alpha()
CE13 = pygame.image.load("CE13.png").convert_alpha()
CE14 = pygame.image.load("CE14.png").convert_alpha()
CE15 = pygame.image.load("CE15.png").convert_alpha()
CE16 = pygame.image.load("CE16.png").convert_alpha()
CE17 = pygame.image.load("CE17.png").convert_alpha()
CE18 = pygame.image.load("CE18.png").convert_alpha()
CE19 = pygame.image.load("CE19.png").convert_alpha()
ceset = [CE1,CE2,CE3,CE4,CE5,CE6,CE7,CE8,CE9,CE10,CE11,CE12,CE13,CE14,CE15,CE16,CE17,CE18,CE19]
#Basic ATK
Swing1 = pygame.image.load("Swing1.png").convert_alpha()
Swing2 = pygame.image.load("Swing2.png").convert_alpha()
Swing3 = pygame.image.load("Swing3.png").convert_alpha()
Swing4 = pygame.image.load("Swing4.png").convert_alpha()
Trans = pygame.image.load("Trans.png").convert_alpha()
Trans2 = pygame.image.load("Trans2.png").convert_alpha()
swingset = [Trans,Swing1,Swing2,Swing3,Swing4]
Slash1 = pygame.image.load ("Slash1.png").convert_alpha()
Slash2 = pygame.image.load("Slash2.png").convert_alpha()
Slash3 = pygame.image.load("Slash3.png").convert_alpha()
slashset = [Slash1,Slash2,Slash3]
Slice1 = pygame.image.load ("Slice1.png").convert_alpha()
Slice2 = pygame.image.load ("Slice2.png").convert_alpha()
Slice3 = pygame.image.load ("Slice3.png").convert_alpha()
sliceset = [Trans2,Slice1,Slice2,Slice3]
#ultimate
Ult1 = pygame.image.load ("Ult1.png").convert_alpha()
Ult2 = pygame.image.load ("Ult2.png").convert_alpha()
Ult3 = pygame.image.load ("Ult3.png").convert_alpha()
Ult4 = pygame.image.load ("Ult4.png").convert_alpha()
Ult5 = pygame.image.load ("Ult5.png").convert_alpha()
Ult6 = pygame.image.load ("Ult6.png").convert_alpha()
Ult7 = pygame.image.load ("Ult7.png").convert_alpha()
Ult8 = pygame.image.load ("Ult8.png").convert_alpha()
Ult9 = pygame.image.load ("Ult9.png").convert_alpha()
Ult10 = pygame.image.load ("Ult10.png").convert_alpha()
Ult11 = pygame.image.load ("Ult11.png").convert_alpha()
Ult12 = pygame.image.load ("Ult12.png").convert_alpha()
Ult13 = pygame.image.load ("Ult13.png").convert_alpha()
Ult14 = pygame.image.load ("Ult14.png").convert_alpha()
Ult15 = pygame.image.load ("Ult15.png").convert_alpha()
Ult16 = pygame.image.load ("Ult16.png").convert_alpha()
Ult17 = pygame.image.load ("Ult17.png").convert_alpha()
Ult18 = pygame.image.load ("Ult18.png").convert_alpha()
Ult19 = pygame.image.load ("Ult19.png").convert_alpha()
Ult20 = pygame.image.load ("Ult20.png").convert_alpha()
Ult21 = pygame.image.load ("Ult21.png").convert_alpha()
Ult22 = pygame.image.load ("Ult22.png").convert_alpha()
Ult23 = pygame.image.load ("Ult23.png").convert_alpha()
Ult24 = pygame.image.load ("Ult24.png").convert_alpha()
Ult25 = pygame.image.load ("Ult25.png").convert_alpha()
Ult26 = pygame.image.load ("Ult26.png").convert_alpha()
Ult27 = pygame.image.load ("Ult27.png").convert_alpha()
Ult28 = pygame.image.load ("Ult28.png").convert_alpha()
Ult29 = pygame.image.load ("Ult29.png").convert_alpha()
Ult30 = pygame.image.load ("Ult30.png").convert_alpha()
Ult31 = pygame.image.load ("Ult31.png").convert_alpha()
Ult32 = pygame.image.load ("Ult32.png").convert_alpha()
ultimate= [Ult1,Ult2,Ult3,Ult4,Ult5,Ult6,Ult7,Ult8,Ult9,Ult10,Ult11,Ult12,Ult13,Ult14,Ult15,Ult16,Ult17,Ult18,Ult19,Ult20,Ult21,Ult22,Ult23,Ult24,Ult25,Ult26,Ult27,Ult28,Ult29,Ult30,Ult31,Ult32]
#demolition
Demo1 = pygame.image.load ("Demo1.png").convert_alpha()
Demo2 = pygame.image.load ("Demo2.png").convert_alpha()
Demo3 = pygame.image.load ("Demo3.png").convert_alpha()
Demo4 = pygame.image.load ("Demo4.png").convert_alpha()
predemo = [Demo1,Demo2,Demo3,Demo4]
Demo5 = pygame.image.load ("Demo5.png").convert_alpha()
Demo6 = pygame.image.load ("Demo6.png").convert_alpha()
Demo7 = pygame.image.load ("Demo7.png").convert_alpha()
Demo8 = pygame.image.load ("Demo8.png").convert_alpha()
Demo9 = pygame.image.load ("Demo9.png").convert_alpha()
Demo10 = pygame.image.load ("Demo10.png").convert_alpha()
Demo11 = pygame.image.load ("Demo11.png").convert_alpha()
postdemo = [Demo5,Demo6,Demo7,Demo8,Demo9,Demo10,Demo11]
DemoF1 = pygame.image.load ("DemoF1.png").convert_alpha()
DemoF2 = pygame.image.load ("DemoF2.png").convert_alpha()
DemoF3 = pygame.image.load ("DemoF3.png").convert_alpha()
DemoF4 = pygame.image.load ("DemoF4.png").convert_alpha()
DemoF5 = pygame.image.load ("DemoF5.png").convert_alpha()
DemoF6 = pygame.image.load ("DemoF6.png").convert_alpha()
DemoF7 = pygame.image.load ("DemoF7.png").convert_alpha()
DemoF8 = pygame.image.load ("DemoF8.png").convert_alpha()
DemoF9 = pygame.image.load ("DemoF9.png").convert_alpha()
DemoF10 = pygame.image.load ("DemoF10.png").convert_alpha()
DemoF11 = pygame.image.load ("DemoF11.png").convert_alpha()
DemoF12 = pygame.image.load ("DemoF12.png").convert_alpha()
DemoF13 = pygame.image.load ("DemoF13.png").convert_alpha()
DemoF14 = pygame.image.load ("DemoF14.png").convert_alpha()
DemoF15 = pygame.image.load ("DemoF15.png").convert_alpha()
DemoF16 = pygame.image.load ("DemoF16.png").convert_alpha()
DemoF17 = pygame.image.load ("DemoF17.png").convert_alpha()
DemoF18 = pygame.image.load ("DemoF18.png").convert_alpha()
DemoF19 = pygame.image.load ("DemoF19.png").convert_alpha()
DemoF20 = pygame.image.load ("DemoF20.png").convert_alpha()
DemoF21 = pygame.image.load ("DemoF21.png").convert_alpha()
demohit = [DemoF1,DemoF2,DemoF3,DemoF4,DemoF5,DemoF6,DemoF7,DemoF8,DemoF9,DemoF10,DemoF11,DemoF12,DemoF13,DemoF14,DemoF15,DemoF16,DemoF17,DemoF18,DemoF19,DemoF20,DemoF21]
#Hurricane <3
H1 = pygame.image.load ("H1.png").convert_alpha()
H2 = pygame.image.load ("H2.png").convert_alpha()
H3 = pygame.image.load ("H3.png").convert_alpha()
H4 = pygame.image.load ("H4.png").convert_alpha()
H5 = pygame.image.load ("H5.png").convert_alpha()
H6 = pygame.image.load ("H6.png").convert_alpha()
H7 = pygame.image.load ("H7.png").convert_alpha()
H8 = pygame.image.load ("H8.png").convert_alpha()
H9 = pygame.image.load ("H9.png").convert_alpha()
H10 = pygame.image.load ("H10.png").convert_alpha()
H11 = pygame.image.load ("H11.png").convert_alpha()
H12 = pygame.image.load ("H12.png").convert_alpha()
H13 = pygame.image.load ("H13.png").convert_alpha()
preh = [H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13]
HE1 = pygame.image.load ("HE1.png").convert_alpha()
HE2 = pygame.image.load ("HE2.png").convert_alpha()
HE3 = pygame.image.load ("HE3.png").convert_alpha()
HE4 = pygame.image.load ("HE4.png").convert_alpha()
HE5 = pygame.image.load ("HE5.png").convert_alpha()
posth = [HE1,HE2,HE3,HE4,HE5]
HO1 = pygame.image.load ("HO1.png").convert_alpha()
HO2 = pygame.image.load ("HO2.png").convert_alpha()
HO3 = pygame.image.load ("HO3.png").convert_alpha()
shootset = [HO1,HO2,HO3]
Ball = pygame.image.load ("Ball.png").convert_alpha()
Hhit = pygame.image.load ("Hurricanehit.png").convert_alpha()
#Final
EA1 = pygame.image.load ("EA1.png").convert_alpha()
EA2 = pygame.image.load ("EA2.png").convert_alpha()
EA3 = pygame.image.load ("EA3.png").convert_alpha()
EA4 = pygame.image.load ("EA4.png").convert_alpha()
EA5 = pygame.image.load ("EA5.png").convert_alpha()
EA6 = pygame.image.load ("EA6.png").convert_alpha()
EA7 = pygame.image.load ("EA7.png").convert_alpha()
EA8 = pygame.image.load ("EA8.png").convert_alpha()
EA9 = pygame.image.load ("EA9.png").convert_alpha()
EA10 = pygame.image.load ("EA10.png").convert_alpha()
EA11 = pygame.image.load ("EA11.png").convert_alpha()
EA12 = pygame.image.load ("EA12.png").convert_alpha()
EA13 = pygame.image.load ("EA13.png").convert_alpha()
EA14 = pygame.image.load ("EA14.png").convert_alpha()
EA15 = pygame.image.load ("EA15.png").convert_alpha()
EA16 = pygame.image.load ("EA16.png").convert_alpha()
EA17 = pygame.image.load ("EA17.png").convert_alpha()
EA18 = pygame.image.load ("EA18.png").convert_alpha()
EA19 = pygame.image.load ("EA19.png").convert_alpha()
EA20 = pygame.image.load ("EA20.png").convert_alpha()
EA21 = pygame.image.load ("EA21.png").convert_alpha()
EA22 = pygame.image.load ("EA22.png").convert_alpha()
EA23 = pygame.image.load ("EA23.png").convert_alpha()
EA24 = pygame.image.load ("EA24.png").convert_alpha()
EA25 = pygame.image.load ("EA25.png").convert_alpha()
EA26 = pygame.image.load ("EA26.png").convert_alpha()
EA27 = pygame.image.load ("EA27.png").convert_alpha()
EA28 = pygame.image.load ("EA28.png").convert_alpha()
EA29 = pygame.image.load ("EA29.png").convert_alpha()
EA30 = pygame.image.load ("EA30.png").convert_alpha()
EA31 = pygame.image.load ("EA31.png").convert_alpha()
EA32 = pygame.image.load ("EA32.png").convert_alpha()
EA33 = pygame.image.load ("EA33.png").convert_alpha()
EA34 = pygame.image.load ("EA34.png").convert_alpha()
EA35 = pygame.image.load ("EA35.png").convert_alpha()
EA36 = pygame.image.load ("EA36.png").convert_alpha()
EA37 = pygame.image.load ("EA37.png").convert_alpha()
EA38 = pygame.image.load ("EA38.png").convert_alpha()
EA39 = pygame.image.load ("EA39.png").convert_alpha()
EA40 = pygame.image.load ("EA40.png").convert_alpha()
EA41 = pygame.image.load ("EA41.png").convert_alpha()
EA42 = pygame.image.load ("EA42.png").convert_alpha()
EA43 = pygame.image.load ("EA43.png").convert_alpha()
EA44 = pygame.image.load ("EA44.png").convert_alpha()
EA45 = pygame.image.load ("EA45.png").convert_alpha()
EA46 = pygame.image.load ("EA46.png").convert_alpha()
EAball = pygame.image.load ("EAball.png").convert_alpha()
EAball1 = pygame.image.load ("EAball1.png").convert_alpha()
EAball2 = pygame.image.load ("EAball2.png").convert_alpha()
Trans3 = pygame.image.load ("Trans3.png").convert_alpha()
preea = [Trans3,EA1,EA2,EA3]
ea = [EA4,EA5,EA6,EA7,EA8,EA9,EA10,EA11,EA12,EA13,EA14,EA15,EA16,EA17,EA18,EA19,EA20,EA21,EA22,EA23,EA24,EA25,EA26,EA27,EA28,EA29,EA30,EA31,EA32,EA33,EA34,EA35,EA36,EA37,EA38,EA39,EA40,EA41,EA42,EA43,EA44,EA45,EA46]
EAE1 = pygame.image.load ("EAE1.png").convert_alpha()
EAE2 = pygame.image.load ("EAE2.png").convert_alpha()
EAE3 = pygame.image.load ("EAE3.png").convert_alpha()
EAE4 = pygame.image.load ("EAE4.png").convert_alpha()
EAE5 = pygame.image.load ("EAE5.png").convert_alpha()
EAE6 = pygame.image.load ("EAE6.png").convert_alpha()
EAE7 = pygame.image.load ("EAE7.png").convert_alpha()
EAE8 = pygame.image.load ("EAE8.png").convert_alpha()
EAEset = [EAE1,EAE2,EAE3,EAE4,EAE5,EAE6,EAE7,EAE8]
#emotes
Smile = pygame.image.load("CSmile.png").convert_alpha()
Cry = pygame.image.load("CCry.png").convert_alpha()
Puzzled = pygame.image.load("CF6.png").convert_alpha()
Cheer = pygame.image.load("CCheer.png").convert_alpha()
Glit = pygame.image.load("CGlitter.png").convert_alpha()
Glit2 = pygame.image.load("CGlitter2.png").convert_alpha()
Glitter = [Glit, Glit2, Glit, Glit2, Glit, Glit2]
Angry = pygame.image.load("Angry.png").convert_alpha()
Troubled = pygame.image.load("Troubled.png").convert_alpha()
Hot = pygame.image.load("Hot.png").convert_alpha()
Damn = pygame.image.load("Damn.png").convert_alpha()
Blaze1 =pygame.image.load("Blaze1.png").convert_alpha()
Blaze2 =pygame.image.load("Blaze2.png").convert_alpha()
Blazeset = [Blaze1,Blaze2]
#bg
bg = pygame.image.load("Background.png").convert_alpha()
menubefore = pygame.image.load("Menu.jpg")
menu2 = pygame.transform.scale (menubefore, (1024,768))
Start = menu2.convert_alpha()
explainbefore = pygame.image.load("Info.jpg")
explan = pygame.transform.scale (explainbefore, (1024,768))
explainimg = explan.convert_alpha()
studbefore = pygame.image.load ("Studio.jpg")
studder = pygame.transform.scale (studbefore , (1024,768))
studs = studder.convert_alpha ()
credbefore = pygame.image.load ("Credits.jpg")
creder = pygame.transform.scale (credbefore, (1024,768))
creds = creder.convert_alpha()
bg2 = pygame.transform.scale (bg2, (1024,768))
bg2 = bg2.convert_alpha()
#Misc.
font= pygame.font.Font ('Font.TTF', 30)
startsim = pygame.image.load("StartSim.png").convert_alpha()
startglow = pygame.image.load("StartSimGlow.png").convert_alpha()
returning = pygame.image.load("Return.png").convert_alpha()
returningglow = pygame.image.load("ReturnGlow.png").convert_alpha()
explanation = pygame.image.load("Explanation.png").convert_alpha()
explanationglow = pygame.image.load("ExplanationGlow.png").convert_alpha()
credit = pygame.image.load("Credits.png").convert_alpha()
creditsglow = pygame.image.load("CreditsGlow.png").convert_alpha()
stud = pygame.image.load("Stud.png").convert_alpha()
studglow = pygame.image.load("StudGlow.png").convert_alpha()
game = pygame.image.load("Game.png").convert_alpha()
gameglow = pygame.image.load("GameGlow.png").convert_alpha()
#soundtextloading
itrack1 = pygame.image.load("track1.png").convert_alpha()
itrack2 = pygame.image.load("track2.png").convert_alpha()
itrack3 = pygame.image.load("track3.png").convert_alpha()
itrack4 = pygame.image.load("track4.png").convert_alpha()
itrack5 = pygame.image.load("track5.png").convert_alpha()
itrack6 = pygame.image.load("track6.png").convert_alpha()
itrack7 = pygame.image.load("track7.png").convert_alpha()
itrack8 = pygame.image.load("track8.png").convert_alpha()
itrack9 = pygame.image.load("track9.png").convert_alpha()
itrack10 = pygame.image.load("track10.png").convert_alpha()
itrack11 = pygame.image.load("track11.png").convert_alpha()
itrack12 = pygame.image.load("track12.png").convert_alpha()
itrack13 = pygame.image.load("track13.png").convert_alpha()
itrack14 = pygame.image.load("track14.png").convert_alpha()
itrack15 = pygame.image.load("track15.png").convert_alpha()
itrack16 = pygame.image.load("track16.png").convert_alpha()
itrack17 = pygame.image.load("track17.png").convert_alpha()
itrack18 = pygame.image.load("track18.png").convert_alpha()
itrack19 = pygame.image.load("track19.png").convert_alpha()
itrack20 = pygame.image.load("track20.png").convert_alpha()
itrack21 = pygame.image.load("track21.png").convert_alpha()
itrack22 = pygame.image.load("track22.png").convert_alpha()
itrack23 = pygame.image.load("track23.png").convert_alpha()
itrack24 = pygame.image.load("track24.png").convert_alpha()
itrack25 = pygame.image.load("track25.png").convert_alpha()
itrack26 = pygame.image.load("track26.png").convert_alpha()
itrack27 = pygame.image.load("track27.png").convert_alpha()
itrack28 = pygame.image.load("track28.png").convert_alpha()
itrack29 = pygame.image.load("track29.png").convert_alpha()
itrack30 = pygame.image.load("track30.png").convert_alpha()
itrack31 = pygame.image.load("track31.png").convert_alpha()
itrack32 = pygame.image.load("track32.png").convert_alpha()
itrack1b = pygame.image.load("track1b.png").convert_alpha()
itrack2b = pygame.image.load("track2b.png").convert_alpha()
itrack3b = pygame.image.load("track3b.png").convert_alpha()
itrack4b = pygame.image.load("track4b.png").convert_alpha()
itrack5b = pygame.image.load("track5b.png").convert_alpha()
itrack6b = pygame.image.load("track6b.png").convert_alpha()
itrack7b = pygame.image.load("track7b.png").convert_alpha()
itrack8b = pygame.image.load("track8b.png").convert_alpha()
itrack9b = pygame.image.load("track9b.png").convert_alpha()
itrack10b = pygame.image.load("track10b.png").convert_alpha()
itrack11b = pygame.image.load("track11b.png").convert_alpha()
itrack12b = pygame.image.load("track12b.png").convert_alpha()
itrack13b = pygame.image.load("track13b.png").convert_alpha()
itrack14b = pygame.image.load("track14b.png").convert_alpha()
itrack15b = pygame.image.load("track15b.png").convert_alpha()
itrack16b = pygame.image.load("track16b.png").convert_alpha()
itrack17b = pygame.image.load("track17b.png").convert_alpha()
itrack18b = pygame.image.load("track18b.png").convert_alpha()
itrack19b = pygame.image.load("track19b.png").convert_alpha()
itrack20b = pygame.image.load("track20b.png").convert_alpha()
itrack21b = pygame.image.load("track21b.png").convert_alpha()
itrack22b = pygame.image.load("track22b.png").convert_alpha()
itrack23b = pygame.image.load("track23b.png").convert_alpha()
itrack24b = pygame.image.load("track24b.png").convert_alpha()
itrack25b = pygame.image.load("track25b.png").convert_alpha()
itrack26b = pygame.image.load("track26b.png").convert_alpha()
itrack27b = pygame.image.load("track27b.png").convert_alpha()
itrack28b = pygame.image.load("track28b.png").convert_alpha()
itrack29b = pygame.image.load("track29b.png").convert_alpha()
itrack30b = pygame.image.load("track30b.png").convert_alpha()
itrack31b = pygame.image.load("track31b.png").convert_alpha()
itrack32b = pygame.image.load("track32b.png").convert_alpha()
charcor = (511,640)
direction = 'right'
pigdirection = "left"
dummycor = (0, 0)
Ldummy = False
Rdummy = False
Mon = False
Menu = True
Explain = False
Gmode = False
Cred = False
Music = False
Dlevel = False
Textcor = (0,0)
arrows = (charcor[0]+ 150,charcor[1] + 30)
laz=pygame.mixer.Sound ('Lazer.wav')
carn=pygame.mixer.Sound ('CE.wav')
sla=pygame.mixer.Sound ('Slash.wav')
sli=pygame.mixer.Sound ('Slice.wav')
swi = pygame.mixer.Sound ('Swing.wav')
naut = pygame.mixer.Sound ('Naut.wav')
DemoSlash = pygame.mixer.Sound ('DemoSlash.wav')
Fatality = pygame.mixer.Sound ('Fatality.wav')
Hsound = pygame.mixer.Sound ('Hurricane.wav')
EAsfx = pygame.mixer.Sound ('EAsfx.wav')
EAE = pygame.mixer.Sound ('EAE.wav')
Teleporting = pygame.mixer.Sound ('Teleport.wav')
########################################################################
def emotes ():
    if event.type == KEYDOWN:
        if event.key == pygame.K_1:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Smile, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Smile, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_2:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Cry, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Cry, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_3:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Puzzled, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Puzzled, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_4:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Cheer, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Cheer, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_5:
            if charcor[1] == 640:
                if direction == 'right':
                    for emote in Glitter:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if Ldummy == True:
                            screen.blit (M, (dummycor))
                        if Rdummy == True:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        screen.blit (emote, (charcor))
                        pygame.display.flip ()
                        pygame.time.delay (300)
                if direction == 'left':
                    for emote in Glitter:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if Ldummy == True:
                            screen.blit (M, (dummycor))
                        if Rdummy == True:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        screen.blit (pygame.transform.flip (emote, True, False), (charcor))
                        pygame.display.flip ()
                        pygame.time.delay (300)
        if event.key == pygame.K_6:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Angry, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Angry, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_7:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Troubled, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Troubled, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_8:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Hot, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Hot, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_9:
            if charcor[1] == 640:
                if direction == 'right':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (Damn, (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
                if direction == 'left':
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pygame.transform.flip (Damn, True, False), (charcor))
                    pygame.display.flip ()
                    pygame.time.delay (1000)
        if event.key == pygame.K_0:
            if charcor[1] == 640:
                if direction == 'right':
                    for blaze in Blazeset:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if Ldummy == True:
                            screen.blit (M, (dummycor))
                        if Rdummy == True:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        screen.blit (blaze, (charcor))
                        pygame.display.flip ()
                        pygame.time.delay (300)
                if direction == 'left':
                    for blaze in Blazeset:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if Ldummy == True:
                            screen.blit (M, (dummycor))
                        if Rdummy == True:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        screen.blit (pygame.transform.flip (blaze, True, False), (charcor))
                        pygame.display.flip ()
                        pygame.time.delay (300)
load = True
########################################################################
while 1:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit ()
                sys.exit()
    while Menu == True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        if load == True:
            pygame.mixer.music.load ('Title.ogg')
            pygame.mixer.music.play (loops=5, start = 0.0)
            pygame.mixer.music.unpause()
            load = False
        screen.blit (Start, (0,0))
        screen.blit (startsim, (105,400))
        screen.blit (explanation, (105,467))
        screen.blit (credit, (105,540))
        screen.blit (stud, (500, 0))
        screen.blit (game, (105, 605))
        if pygame.mouse.get_pos()[0] > 105 and pygame.mouse.get_pos()[0] < 283 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 467:
            screen.blit (Start, (0,0))
            screen.blit (explanation, (105,467))
            screen.blit (credit, (105,540))
            screen.blit (startglow, (105,400))
            screen.blit (stud, (500, 0))
            screen.blit (game, (105, 605))
            if pygame.mouse.get_pressed () != (0,0,0):
                Menu = False
                pygame.mixer.music.pause()
                pygame.mixer.music.load ('Aquarium.wav')
                pygame.mixer.music.play (loops=5, start = 0.0)
        if pygame.mouse.get_pos()[0] > 105 and pygame.mouse.get_pos()[0] < 320 and pygame.mouse.get_pos()[1] > 467 and pygame.mouse.get_pos()[1] < 540:
            screen.blit (Start, (0,0))
            screen.blit (startsim, (105,400))
            screen.blit (credit, (105,540))
            screen.blit (explanationglow, (105,467))
            screen.blit (stud, (500, 0))
            screen.blit (game, (105, 605))
            if pygame.mouse.get_pressed () != (0,0,0):
                Menu = False
                Explain = True
                pygame.mixer.music.pause()
                pygame.mixer.music.load ('Title2010Winter.wav')
                pygame.mixer.music.play (loops=5, start = 0.0)
        if pygame.mouse.get_pos()[0] > 105 and pygame.mouse.get_pos()[0] < 218 and pygame.mouse.get_pos()[1] > 540 and pygame.mouse.get_pos()[1] < 605:
            screen.blit (Start, (0,0))
            screen.blit (startsim, (105,400))
            screen.blit (explanation, (105,467))
            screen.blit (creditsglow, (105,540))
            screen.blit (stud, (500, 0))
            screen.blit (game, (105, 605))
            if pygame.mouse.get_pressed () != (0,0,0):
                Menu = False
                Cred = True
                pygame.mixer.music.pause()
                pygame.mixer.music.load ('CBD_town.wav')
                pygame.mixer.music.play (loops=5, start = 0.0)
        if pygame.mouse.get_pos()[0] > 500 and pygame.mouse.get_pos()[0] < 770 and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 86:
            screen.blit (Start, (0,0))
            screen.blit (startsim, (105,400))
            screen.blit (explanation, (105,467))
            screen.blit (credit, (105,540))
            screen.blit (studglow, (500, 0))
            screen.blit (game, (105, 605))
            if pygame.mouse.get_pressed () != (0,0,0):
                Menu = False
                Music = True
                pygame.mixer.music.pause()
        if pygame.mouse.get_pos()[0] > 105 and pygame.mouse.get_pos()[0] < 371 and pygame.mouse.get_pos()[1] > 605 and pygame.mouse.get_pos()[1] < 688:
            screen.blit (Start, (0,0))
            screen.blit (gameglow, (105, 605))
            screen.blit (startsim, (105,400))
            screen.blit (explanation, (105,467))
            screen.blit (credit, (105,540))
            screen.blit (stud, (500, 0))
            if pygame.mouse.get_pressed () != (0,0,0):
                Menu = False
                Dlevel = True
                lose = False
                pygame.mixer.music.pause()
                pygame.mixer.music.load ('CaveOfHontale.ogg')
                pygame.mixer.music.play (loops=-1, start = 0.0)
        pygame.display.flip()
    
    while Dlevel == True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        screen.blit (dif,(0,0))
        screen.blit (returning, (900,0))
        screen.blit (easy,(475,400))
        screen.blit (normal,(460,318))
        screen.blit (hard,(290,225))
        if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
            screen.blit (returningglow, (900,0))
            if pygame.mouse.get_pressed () == (1,0,0):
                Menu = True
                Dlevel = False
                charcor = (511,640)
                load = True
        if pygame.mouse.get_pos()[0] > 290 and pygame.mouse.get_pos ()[0] < 762 and pygame.mouse.get_pos ()[1] > 225 and pygame.mouse.get_pos ()[1] < 318:
            screen.blit (hardglow,(290,225))
            if pygame.mouse.get_pressed () == (1,0,0):
                hardness = 3
                Gmode = True
                Dlevel = False
                charhp = 50000
                charcor = (511,568)
                Beg = True
        if pygame.mouse.get_pos()[0] > 460 and pygame.mouse.get_pos ()[0] < 622 and pygame.mouse.get_pos ()[1] > 318 and pygame.mouse.get_pos ()[1] < 400:
            screen.blit (normalglow,(460,318))
            if pygame.mouse.get_pressed () == (1,0,0):
                hardness = 2
                Gmode = True
                Dlevel = False
                charhp = 20000
                charcor = (511,568)
                Beg = True
        if pygame.mouse.get_pos()[0] > 475 and pygame.mouse.get_pos ()[0] < 611 and pygame.mouse.get_pos ()[1] > 400 and pygame.mouse.get_pos ()[1] < 499:
            screen.blit (easyglow,(475,400))
            if pygame.mouse.get_pressed () == (1,0,0):
                hardness = 1
                Gmode = True
                Dlevel = False
                charhp = 5000
                charcor = (511,568)
                Beg = True
        pygame.display.flip()


    
        
    while Gmode == True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        screen.blit (bg2,(0,0))
        screen.blit (returning, (900,0))
        try:
            health = font.render ('Health =' + str (charhp), 1, (0,0,205))
            screen.blit (health, (0,0))
        except:
            health = font.render ('Health is Not AVAILABLE',1,(255,255,0))
            screen.blit (health, (0,0))
        try:
            mhealth = font.render ('Pig Health =' + str (mhp), 1, (230,230,250))
            screen.blit (mhealth, (300,0))
        except:
            mhealth = font.render ('Pig Health is Not AVAILABLE',1,(230,230,250))
            screen.blit (mhealth, (300,0)) 
        if Beg == True:
            if hardness == 1:
                Mon = True
                mhp = random.randint (80000,160000)
                dummycor = (800,590)
            if hardness == 2:
                Mon = True
                mhp = random.randint (200000,400000)
                dummycor = (800,590)
            if hardness == 3:
                Mon = True
                mhp = random.randint (300000,900000)
                dummycor = (800,590)
            Beg = False
        if Mon == True:
            if pigdirection == "left":
                screen.blit (pig1, (dummycor))
            else:
                screen.blit (pygame.transform.flip(pig1,True,False), (dummycor))
        if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
            screen.blit (returningglow, (900,0))
            if pygame.mouse.get_pressed () == (1,0,0):
                Menu = True
                Gmode = False
                charcor = (511,640)
                load = True
        if direction == 'right':
            screen.blit (S, (charcor))
        if direction == 'left':
            screen.blit (S2, (charcor))
        pygame.display.flip()
        if Mon == True:
            if random.randint(0,5) == 5:
                if dummycor[0] > charcor [0]:
                    pigdirection = "left"
                else: pigdirection = "right"
                if pigdirection == "left":
                    if dummycor[0] - 20 >= 0:
                        for pigs in pigmove:
                            screen.blit (bg2,(0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (health, (0,0))
                            screen.blit (mhealth, (300,0))
                            if direction == 'right':
                                screen.blit (S, (charcor))
                            if direction == 'left':
                                screen.blit (S2, (charcor))
                            dummycor = (dummycor[0] - 20,dummycor[1])
                            screen.blit (pigs,dummycor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                if pigdirection == "right":
                    if dummycor[0] + 20 <= 1024:
                        for pigs in pigmove:
                            screen.blit (bg2,(0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (health, (0,0))
                            screen.blit (mhealth, (300,0))
                            if direction == 'right':
                                screen.blit (S, (charcor))
                            if direction == 'left':
                                screen.blit (S2, (charcor))
                            dummycor = (dummycor[0] + 20,dummycor[1])
                            screen.blit (pygame.transform.flip(pigs,True,False),dummycor)
                            pygame.display.flip()
                            pygame.time.delay (100)
        if Mon == True:
            if pigdirection == "left":
                if dummycor[0]-40 < charcor[0] and dummycor[0] + 20 > charcor[0]:
                    for lol in pigaset:
                        screen.blit (bg2,(0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if lol == pigA1:
                            charcor = charcor[0]-8,charcor[1]
                        if lol == pigA2:
                            charcor = charcor[0]-8,charcor[1]-5
                        if lol == pigA3:
                            charcor = charcor[0]-8,charcor[1]+5
                        if direction == "right":
                            screen.blit(charhit, charcor)
                        if direction == "left":
                            screen.blit(pygame.transform.flip(charhit,True,False), charcor)
                        if lol == pigA3 and lose == False:
                            Textcor = (charcor[0], charcor[1] - 25)
                            if hardness == 1:
                                decrement=(random.randint (300, 600))
                            if hardness == 2:
                                decrement=(random.randint (600, 900))
                            if hardness == 3:
                                decrement=(random.randint (3000, 6000))
                            text= font.render (str (decrement), 1, (0,0,205))
                            screen.blit (text, Textcor)
                            if charhp - decrement <= 0:
                                charhp = 0
                                lose = True
                            else:
                                charhp = charhp - decrement
                        screen.blit (lol,dummycor)
                        pygame.display.flip()
                        pygame.time.delay (100)
            if pigdirection == "right":
                if dummycor[0]+40 > charcor[0] and dummycor[0] - 20 < charcor[0]:
                    for lol in pigaset:
                        screen.blit (bg2,(0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if lol == pigA1:
                            charcor = charcor[0]+8,charcor[1]
                        if lol == pigA2:
                            charcor = charcor[0]+8,charcor[1]-5
                        if lol == pigA3:
                            charcor = charcor[0]+8,charcor[1]+5
                        if direction == "right":
                            screen.blit(charhit, charcor)
                        if direction == "left":
                            screen.blit(pygame.transform.flip(charhit,True,False), charcor)
                        if lol == pigA3 and lose == False:
                            Textcor = (charcor[0], charcor[1] - 25)
                            if hardness == 1:
                                decrement=(random.randint (300, 600))
                            if hardness == 2:
                                decrement=(random.randint (600, 900))
                            if hardness == 3:
                                decrement=(random.randint (3000, 6000))
                            text= font.render (str (decrement), 1, (0,0,205))
                            screen.blit (text, Textcor)
                            if charhp - decrement <= 0:
                                charhp = 0
                                lose = True
                            else:
                                charhp = charhp - decrement
                        screen.blit (pygame.transform.flip(lol,True,False),dummycor)
                        pygame.display.flip()
                        pygame.time.delay (100)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = "right"
                Teleporting.play(loops=0, maxtime=0, fade_ms=0)
                for q in teleset:
                    screen.blit (bg2, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (health, (0,0))
                    screen.blit (mhealth, (300,0))
                    if Mon == True:
                        if pigdirection == "left":
                            if q == Tele1:
                                screen.blit(pig3,dummycor)
                            if q == Tele2:
                                screen.blit(pig1,dummycor)
                            if q == Tele3:
                                screen.blit(pig2,dummycor)
                            if q == Tele4:
                                screen.blit(pig3,dummycor)
                            if q == alert:
                                screen.blit(pig2,dummycor)
                        if pigdirection == "right":
                            if q == Tele1:
                                screen.blit(pygame.transform.flip(pig3,True,False),dummycor)
                            if q == Tele2:
                                screen.blit(pygame.transform.flip(pig1,True,False),dummycor)
                            if q == Tele3:
                                screen.blit(pygame.transform.flip(pig2,True,False),dummycor)
                            if q == Tele4:
                                screen.blit(pygame.transform.flip(pig3,True,False),dummycor)
                            if q == alert:
                                screen.blit(pygame.transform.flip(pig2,True,False),dummycor)
                    if q == alert:
                        screen.blit (q,(charcor))
                    if q == Tele1:
                        screen.blit (q,(charcor[0] -28,charcor[1] - 49))
                    if q == Tele2:
                        screen.blit (q,(charcor[0] -27,charcor[1] - 6))
                    if q == Tele3:
                        screen.blit (q,(charcor[0] -33,charcor[1] + 21))
                    if q == Tele4:
                        screen.blit (q,(charcor[0] -35,charcor[1] + 26))
                    if pigdirection == 'left':
                        dummycor = dummycor[0] - 5,dummycor[1]
                    if pigdirection == 'right':
                        dummycor = dummycor[0] + 5,dummycor[1]
                    pygame.display.flip()
                    pygame.time.delay(30)
                if charcor[0] + 150 >= 1024:
                    charcor= (980, charcor[1])
                else:
                    charcor= (charcor[0] + 150, charcor[1])
                Teleporting.fadeout(300)
            if event.key == K_LEFT:
                direction = "left"
                Teleporting.play(loops=0, maxtime=0, fade_ms=0)
                for q in teleset:
                    screen.blit (bg2, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (health, (0,0))
                    screen.blit (mhealth, (300,0))
                    if Mon == True:
                        if pigdirection == "left":
                            if q == Tele1:
                                screen.blit(pig3,dummycor)
                            if q == Tele2:
                                screen.blit(pig1,dummycor)
                            if q == Tele3:
                                screen.blit(pig2,dummycor)
                            if q == Tele4:
                                screen.blit(pig3,dummycor)
                            if q == alert:
                                screen.blit(pig2,dummycor)
                        if pigdirection == "right":
                            if q == Tele1:
                                screen.blit(pygame.transform.flip(pig3,True,False),dummycor)
                            if q == Tele2:
                                screen.blit(pygame.transform.flip(pig1,True,False),dummycor)
                            if q == Tele3:
                                screen.blit(pygame.transform.flip(pig2,True,False),dummycor)
                            if q == Tele4:
                                screen.blit(pygame.transform.flip(pig3,True,False),dummycor)
                            if q == alert:
                                screen.blit(pygame.transform.flip(pig2,True,False),dummycor)
                    if q == alert:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor))
                    if q == Tele1:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -28,charcor[1] - 49))
                    if q == Tele2:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -27,charcor[1] - 6))
                    if q == Tele3:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -33,charcor[1] + 21))
                    if q == Tele4:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -35,charcor[1] + 26))
                    if pigdirection == 'left':
                        dummycor = dummycor[0] - 5,dummycor[1]
                    if pigdirection == 'right':
                        dummycor = dummycor[0] + 5,dummycor[1]
                    pygame.display.flip()
                    pygame.time.delay(30)
                if charcor[0] - 150 <= 0:
                    charcor = (0,charcor[1])
                else:
                    charcor= (charcor[0] - 150, charcor[1])
                Teleporting.fadeout(300)
        if lose == True:
            blah = pygame.mixer.Sound ('Lose.wav')
            blah.play(loops=0, maxtime=0, fade_ms=0)
            Menu = True
            Gmode = False
            lose = False
            load = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sli.play(loops=0, maxtime=0, fade_ms=0)
                    for y in sliceset:
                        decrement=(random.randint (10000, 20000))
                        text= font.render (str (decrement), 1, (230,230,255))
                        screen.blit (bg2, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if not (dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]) and (Mon == True):
                            if pigdirection == "left":
                                if y == Trans2:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice1:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice2:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice3:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                            if pigdirection == "right":
                                if y == Trans2:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice1:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice2:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice3:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                        if Mon == True and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]:
                            if pigdirection == "left":
                                screen.blit (pigH1, (dummycor))
                                dummycor = dummycor[0] -10,dummycor[1]
                            if pigdirection == "right":
                                screen.blit (pygame.transform.flip (pigH1, True, False), (dummycor))
                                dummycor = dummycor[0] +10,dummycor[1]
                        if y == Slice3:
                            screen.blit (y, (charcor[0] - 36, charcor [1] - 68))
                        if y == Slice2:
                            screen.blit (y, (charcor[0]-20,charcor[1]-62))
                        if y == Slice1:
                            screen.blit (y, (charcor[0]+1,charcor[1]-9))
                        if y == Trans2:
                            screen.blit (y,charcor)
                        if Mon == True:
                            if dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and y == Slice3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (80)
                        if (Mon == True) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and y == Slice3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if mhp - decrement <= 0:
                                mhp = 0
                            if mhp - decrement > 0:
                                mhp = mhp - decrement
                            mhealth = font.render ('Pig Health =' + str (mhp), 1, (230,230,255))
                    sli.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sli.play(loops=0, maxtime=0, fade_ms=0)
                    for y in sliceset:
                        decrement=(random.randint (10000, 20000))
                        text= font.render (str (decrement), 1, (230,230,255))
                        screen.blit (bg2, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if not (dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]) and (Mon == True):
                            if pigdirection == "left":
                                if y == Trans2:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice1:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice2:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if y == Slice3:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                            if pigdirection == "right":
                                if y == Trans2:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice1:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice2:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if y == Slice3:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                        if Mon == True and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]:
                            if pigdirection == "left":
                                screen.blit (pigH1, (dummycor))
                                dummycor = dummycor[0] -10,dummycor[1]
                            if pigdirection == "right":
                                screen.blit (pygame.transform.flip (pigH1, True, False), (dummycor))
                                dummycor = dummycor[0] +10,dummycor[1]
                        if y == Slice3:
                            screen.blit (pygame.transform.flip(y,True,False), (charcor[0]-72, charcor [1] - 69))
                        if y == Slice2:
                            screen.blit (pygame.transform.flip(y,True,False),(charcor[0]-95,charcor[1]-62))
                        if y == Slice1:
                            screen.blit (pygame.transform.flip(y,True,False), (charcor[0]-33, charcor[1]-9))
                        if y == Trans2:
                            screen.blit (pygame.transform.flip(y,True,False), charcor)
                        if Mon == True:
                            if dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and y == Slice3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (80)
                        if (Mon == True) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and y == Slice3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if mhp - decrement <= 0:
                                mhp = 0
                            if mhp - decrement > 0:
                                mhp = mhp - decrement
                            mhealth = font.render ('Pig Health =' + str (mhp), 1, (230,230,255))
                    sli.fadeout (300)
        if mhp == 0 and Mon == True:
            diediedie=pygame.mixer.Sound ('Win.wav')
            diediedie.play(loops=0, maxtime=0, fade_ms=0)
            if pigdirection == 'left':
                for f in pigdie:
                    screen.blit (bg2, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (health, (0,0))
                    screen.blit (mhealth, (300,0))
                    if direction == "right":
                         screen.blit (S, (charcor))
                    else:
                        screen.blit (S2, (charcor))
                    screen.blit (f,dummycor)
                    pygame.display.flip()
                    pygame.time.delay (100)
                Mon = False
            if pigdirection == 'right':
                for f in pigdie:
                    screen.blit (bg2, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (health, (0,0))
                    screen.blit (mhealth, (300,0))
                    if direction == "right":
                        screen.blit (S, (charcor))
                    else:
                        screen.blit (S2, (charcor))
                    screen.blit (pygame.transform.flip(f,True,False),dummycor)
                    pygame.display.flip()
                    pygame.time.delay (100)
                Mon = False
            diediedie.fadeout (300)
        if Mon == False:
            Cred= True
            Gmode = False
            pygame.mixer.music.pause()
            pygame.mixer.music.load ('CBD_town.wav')
            pygame.mixer.music.play (loops=5, start = 0.0)
            
        if event.type == KEYDOWN:
            if event.key == K_z:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    swi.play(loops=0, maxtime=0, fade_ms=0)
                    for z in swingset:
                        decrement=(random.randint (19999, 49999))
                        text= font.render (str (decrement), 1, (230,230,255))
                        screen.blit (bg2, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if not (dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]) and (Mon == True):
                            if pigdirection == "left":
                                if z == Trans:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing1:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing2:
                                    screen.blit (pig1, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing3:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing4:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]  
                            if pigdirection == "right":
                                if z == Trans:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing1:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing2:
                                    screen.blit (pygame.transform.flip (pig1, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing3:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing4:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                        if Mon == True and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0]:
                            if pigdirection == "left":
                                screen.blit (pigH1, (dummycor))
                                dummycor = dummycor[0] -10,dummycor[1]
                            if pigdirection == "right":
                                screen.blit (pygame.transform.flip (pigH1, True, False), (dummycor))
                                dummycor = dummycor[0] +10,dummycor[1]
                        if z == Swing3:
                            screen.blit (z, (charcor[0]-57,charcor[1]-40))
                        if z == Swing2:
                            screen.blit (z, (charcor[0]-42,charcor[1]-21))
                        if z == Swing1:
                            screen.blit (z, (charcor[0]-37,charcor[1]-1))
                        if z == Swing4:
                            screen.blit (z, (charcor[0]-65, charcor[1] -10))
                        if z == Trans:
                            screen.blit(z,charcor)
                        if Mon == True:
                            if dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0] and z == Swing4:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Mon == True) and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0] and z == Swing4:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if mhp - decrement <= 0:
                                mhp = 0
                            if mhp - decrement > 0:
                                mhp = mhp - decrement
                            mhealth = font.render ('Health of Dummy =' + str (mhp), 1, (230,230,255))
                    swi.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    swi.play(loops=0, maxtime=0, fade_ms=0)
                    for z in swingset:
                        decrement=(random.randint (19999, 49999))
                        text= font.render (str (decrement), 1, (230,230,255))
                        screen.blit (bg2, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (health, (0,0))
                        screen.blit (mhealth, (300,0))
                        if not (dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]) and (Mon == True):
                            if pigdirection == "left":
                                if z == Trans:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing1:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing2:
                                    screen.blit (pig1, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing3:
                                    screen.blit (pig2, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]
                                if z == Swing4:
                                    screen.blit (pig3, (dummycor))
                                    dummycor = dummycor[0] - 15,dummycor[1]  
                            if pigdirection == "right":
                                if z == Trans:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing1:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing2:
                                    screen.blit (pygame.transform.flip (pig1, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing3:
                                    screen.blit (pygame.transform.flip (pig2, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                                if z == Swing4:
                                    screen.blit (pygame.transform.flip (pig3, True, False), (dummycor))
                                    dummycor = dummycor[0] + 15,dummycor[1]
                        if Mon == True and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0]:
                            if pigdirection == "left":
                                screen.blit (pigH1, (dummycor))
                                dummycor = dummycor[0] -10,dummycor[1]
                            if pigdirection == "right":
                                screen.blit (pygame.transform.flip (pigH1, True, False), (dummycor))
                                dummycor = dummycor[0] +10,dummycor[1]
                        if z == Swing3:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0], charcor[1]-40))
                        if z == Swing2:
                            screen.blit (pygame.transform.flip(z,True,False),(charcor[0]-2,charcor[1]-21))
                        if z == Swing1:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0]-2, charcor[1]-1))
                        if z == Swing4:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0]-114, charcor[1]-10))
                        if z == Trans:
                            screen.blit(pygame.transform.flip(z,True,False),charcor)
                        if Mon == True:
                            if (dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0]) and z == Swing4:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Mon == True) and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0] and z == Swing4:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if mhp - decrement <= 0:
                                mhp = 0
                            if mhp - decrement > 0:
                                mhp = mhp - decrement
                            mhealth = font.render ('Health of Dummy =' + str (mhp), 1, (230,230,255))
                    swi.fadeout (300)
                    
                    
            
                        
            
            
            


    while Explain == True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        screen.blit (explainimg, (0,0))
        screen.blit (returning, (900,0))
        if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
            screen.blit (returningglow, (900,0))
            if pygame.mouse.get_pressed () == (1,0,0):
                Menu = True
                Explain = False
                load = True
        pygame.display.flip ()
    while Cred == True:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        screen.blit (creds, (0,0))
        screen.blit (returning, (900,0))
        if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
            screen.blit (returningglow, (900,0))
            if pygame.mouse.get_pressed () == (1,0,0):
                Menu = True
                Cred = False
                load = True
        pygame.display.flip ()
    while Music == True:
        pygame.mixer.music.pause()
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
        screen.blit (studs, (0,0))
        screen.blit (returning, (900,0))
        if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
            screen.blit (returningglow, (900,0))
            if pygame.mouse.get_pressed () == (1,0,0):
                Menu = True
                Music = False
                load = True
                pygame.mixer.stop ()
        screen.blit (itrack1, (10,350))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 217 and pygame.mouse.get_pos ()[1] > 350 and pygame.mouse.get_pos ()[1] < 403:
            screen.blit (itrack1b, (10,350))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track1 = pygame.mixer.Sound ('AboveTheTreetops.wav')
                track1.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack2, (10,403))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 95 and pygame.mouse.get_pos ()[1] > 403 and pygame.mouse.get_pos ()[1] < 449:
            screen.blit (itrack2b, (10,403))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track2 = pygame.mixer.Sound ('amoria.wav')
                track2.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack3, (10,449))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 110 and pygame.mouse.get_pos ()[1] > 449 and pygame.mouse.get_pos ()[1] < 499:
            screen.blit (itrack3b, (10,449))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track3 = pygame.mixer.Sound ('battleBGMTypeC.wav')
                track3.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack4, (10,499))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 200 and pygame.mouse.get_pos ()[1] > 499 and pygame.mouse.get_pos ()[1] < 546:
            screen.blit (itrack4b, (10,499))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track4 = pygame.mixer.Sound ('BoatQuay_town.wav')
                track4.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack5, (10,546))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 138 and pygame.mouse.get_pos ()[1] > 546 and pygame.mouse.get_pos ()[1] < 588:
            screen.blit (itrack5b, (10,546))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track5 = pygame.mixer.Sound ('CastleBoss.wav')
                track5.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack6, (10,588))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 68 and pygame.mouse.get_pos ()[1] > 588 and pygame.mouse.get_pos ()[1] < 640:
            screen.blit (itrack6b, (10,588))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track6 = pygame.mixer.Sound ('CBD_field.wav')
                track6.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack7, (10,640))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 166 and pygame.mouse.get_pos ()[1] > 640 and pygame.mouse.get_pos ()[1] < 693:
            screen.blit (itrack7b, (10,640))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track7 = pygame.mixer.Sound ('CygnusGarden.wav')
                track7.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack8, (10,693))
        if pygame.mouse.get_pos ()[0] > 10 and pygame.mouse.get_pos ()[0] < 192 and pygame.mouse.get_pos ()[1] > 693 and pygame.mouse.get_pos ()[1] < 744:
            screen.blit (itrack8b, (10,693))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track8 = pygame.mixer.Sound ('dolphin_night.wav')
                track8.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack9, (300,350))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 486 and pygame.mouse.get_pos ()[1] > 350 and pygame.mouse.get_pos ()[1] < 401:
            screen.blit (itrack9b, (300,350))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track9 = pygame.mixer.Sound ('dolphin_noon.wav')
                track9.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack10, (300,401))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 466 and pygame.mouse.get_pos ()[1] > 401 and pygame.mouse.get_pos ()[1] < 453:
            screen.blit (itrack10b, (300,401))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track10 = pygame.mixer.Sound ('FindingForest.wav')
                track10.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack11, (300,453))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 502 and pygame.mouse.get_pos ()[1] > 453 and pygame.mouse.get_pos ()[1] < 506:
            screen.blit (itrack11b, (300,453))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track11 = pygame.mixer.Sound ('FirstStepMaster.wav')
                track11.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack12, (300,506))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 440 and pygame.mouse.get_pos ()[1] > 506 and pygame.mouse.get_pos ()[1] < 558:
            screen.blit (itrack12b, (300,506))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track12 = pygame.mixer.Sound ('Forgetfulness.wav')
                track12.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack13, (300,558))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 545 and pygame.mouse.get_pos ()[1] > 558 and pygame.mouse.get_pos ()[1] < 610:
            screen.blit (itrack13b, (300,558))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track13 = pygame.mixer.Sound ('GrandmastersGauntlet.wav')
                track13.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack14, (300,610))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 444 and pygame.mouse.get_pos ()[1] > 610 and pygame.mouse.get_pos ()[1] < 662:
            screen.blit (itrack14b, (300,610))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track14 = pygame.mixer.Sound ('HighEnough.wav')
                track14.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack15, (300,662))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 498 and pygame.mouse.get_pos ()[1] > 662 and pygame.mouse.get_pos ()[1] < 714:
            screen.blit (itrack15b, (300,662))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track15 = pygame.mixer.Sound ('MoonlightShadow.wav')
                track15.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack16, (300,714))
        if pygame.mouse.get_pos ()[0] > 300 and pygame.mouse.get_pos ()[0] < 432 and pygame.mouse.get_pos ()[1] > 714 and pygame.mouse.get_pos ()[1] < 760:
            screen.blit (itrack16b, (300,714))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track16 = pygame.mixer.Sound ('Remembrance.wav')
                track16.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack17, (590,350))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 712 and pygame.mouse.get_pos ()[1] > 350 and pygame.mouse.get_pos ()[1] < 403:
            screen.blit (itrack17b, (590,350))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track17 = pygame.mixer.Sound ('Repentance.wav')
                track17.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack18, (590,403))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 706 and pygame.mouse.get_pos ()[1] > 403 and pygame.mouse.get_pos ()[1] < 453:
            screen.blit (itrack18b, (590,403))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track18 = pygame.mixer.Sound ('ShopBgm.wav')
                track18.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack19, (590,453))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 754 and pygame.mouse.get_pos ()[1] > 453 and pygame.mouse.get_pos ()[1] < 506:
            screen.blit (itrack19b, (590,453))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track19 = pygame.mixer.Sound ('TimeTemple.wav')
                track19.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack20, (590,506))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 765 and pygame.mouse.get_pos ()[1] > 506 and pygame.mouse.get_pos ()[1] < 555:
            screen.blit (itrack20b, (590,506))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track20 = pygame.mixer.Sound ('Title_Japan.wav')
                track20.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack21, (590,555))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 685 and pygame.mouse.get_pos ()[1] > 555 and pygame.mouse.get_pos ()[1] < 609:
            screen.blit (itrack21b, (590,555))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track21 = pygame.mixer.Sound ('Title_Japan2.wav')
                track21.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack22, (590,609))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 724 and pygame.mouse.get_pos ()[1] > 609 and pygame.mouse.get_pos ()[1] < 659:
            screen.blit (itrack22b, (590,609))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track22 = pygame.mixer.Sound ('Title_Japan3.wav')
                track22.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack23, (590,659))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 783 and pygame.mouse.get_pos ()[1] > 659 and pygame.mouse.get_pos ()[1] < 706:
            screen.blit (itrack23b, (590,659))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track23 = pygame.mixer.Sound ('Title_Japan4.wav')
                track23.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack24, (590,706))
        if pygame.mouse.get_pos ()[0] > 590 and pygame.mouse.get_pos ()[0] < 754 and pygame.mouse.get_pos ()[1] > 706 and pygame.mouse.get_pos ()[1] < 749:
            screen.blit (itrack24b, (590,706))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track24 = pygame.mixer.Sound ('Title_Japan5.wav')
                track24.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack25, (450,120))
        if pygame.mouse.get_pos ()[0] > 450 and pygame.mouse.get_pos ()[0] < 642 and pygame.mouse.get_pos ()[1] > 120 and pygame.mouse.get_pos ()[1] < 169:
            screen.blit (itrack25b, (450,120))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track25 = pygame.mixer.Sound ('TowerOfGoddess.wav')
                track25.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack26, (450,169))
        if pygame.mouse.get_pos ()[0] > 450 and pygame.mouse.get_pos ()[0] < 715 and pygame.mouse.get_pos ()[1] > 169 and pygame.mouse.get_pos ()[1] < 221:
            screen.blit (itrack26b, (450,169))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track26 = pygame.mixer.Sound ('WhenTheMorningComes.wav')
                track26.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack27, (450,221))
        if pygame.mouse.get_pos ()[0] > 450 and pygame.mouse.get_pos ()[0] < 623 and pygame.mouse.get_pos ()[1] > 221 and pygame.mouse.get_pos ()[1] < 268:
            screen.blit (itrack27b, (450,221))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track27 = pygame.mixer.Sound ('WhiteChristmas.wav')
                track27.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack28, (450,268))
        if pygame.mouse.get_pos ()[0] > 450 and pygame.mouse.get_pos ()[0] < 640 and pygame.mouse.get_pos ()[1] > 268 and pygame.mouse.get_pos ()[1] < 312:
            screen.blit (itrack28b, (450,268))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track28 = pygame.mixer.Sound ('WindAndFlower.wav')
                track28.play(loops=0, maxtime=0, fade_ms=0)    
        screen.blit (itrack29, (750,120))
        if pygame.mouse.get_pos ()[0] > 750 and pygame.mouse.get_pos ()[0] < 879 and pygame.mouse.get_pos ()[1] > 120 and pygame.mouse.get_pos ()[1] < 169:
            screen.blit (itrack29b, (750,120))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track29 = pygame.mixer.Sound ('ShiningSea.wav')
                track29.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack30, (750,169))
        if pygame.mouse.get_pos ()[0] > 750 and pygame.mouse.get_pos ()[0] < 893 and pygame.mouse.get_pos ()[1] > 169 and pygame.mouse.get_pos ()[1] < 223:
            screen.blit (itrack30b, (750,169))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track30 = pygame.mixer.Sound ('Heartybear.wav')
                track30.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack31, (750,223))
        if pygame.mouse.get_pos ()[0] > 750 and pygame.mouse.get_pos ()[0] < 882 and pygame.mouse.get_pos ()[1] > 223 and pygame.mouse.get_pos ()[1] < 270:
            screen.blit (itrack31b, (750,223))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track31 = pygame.mixer.Sound ('ElinForest.wav')
                track31.play(loops=0, maxtime=0, fade_ms=0)
        screen.blit (itrack32, (750,270))
        if pygame.mouse.get_pos ()[0] > 750 and pygame.mouse.get_pos ()[0] < 865 and pygame.mouse.get_pos ()[1] > 270 and pygame.mouse.get_pos ()[1] < 319:
            screen.blit (itrack32b, (750,270))
            if pygame.mouse.get_pressed() == (1,0,0):
                pygame.mixer.stop ()
                track32 = pygame.mixer.Sound ('Elfwood.wav')
                track32.play(loops=0, maxtime=0, fade_ms=0)
        pygame.display.flip ()

    screen.blit (bg, (0,0))
    screen.blit (returning, (900,0))
    if pygame.mouse.get_pos ()[0] > 900 and pygame.mouse.get_pos ()[0] < 1015 and pygame.mouse.get_pos ()[1] > 0 and pygame.mouse.get_pos ()[1] < 76:
        screen.blit (returningglow, (900,0))
        if pygame.mouse.get_pressed () == (1,0,0):
            Menu = True
            load = True
    try:
        hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
        screen.blit (hpcount, (0,0))
    except:
        hpcount = font.render ('Health is Not AVAILABLE',1,(255,255,0))
        screen.blit (hpcount, (0,0))
    if dummycor[1] < 640:
        dummycor = (dummycor[0], dummycor[1] + 20)
    if Ldummy == True:
        screen.blit (M, (dummycor))
    if Rdummy == True:
        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
    if charcor[1] >= 640:
        if direction == 'right':
            screen.blit (S, (charcor))
        if direction == 'left':
            screen.blit (S2, (charcor))
    if charcor[1] < 640:
        for i in Flying:
            screen.blit (bg, (0,0))
            screen.blit (returning, (900,0))
            screen.blit (hpcount, (0,0))
            if Ldummy == True:
                screen.blit (M, (dummycor))
            if Rdummy == True:
                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
            if direction == 'right':
                screen.blit (i, (charcor))
            if direction == 'left':
                screen.blit (pygame.transform.flip (i, True, False), (charcor))
            pygame.display.flip ()
            pygame.time.delay (100)
        if charcor[1]+20 > 640:
            charcor=charcor[0], 640
        else:
            charcor = charcor[0], charcor[1] + 20
    pygame.display.flip ()
    if event.type == KEYDOWN:
        if event.key == pygame.K_RIGHT and charcor[1] == 640:
            direction = 'right'
            if charcor[0] + 20 < 1024:
                for pics in walk:
                    charcor = (charcor[0] + 20, charcor [1])
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pics, (charcor))
                    pygame.display.flip()
                    pygame.time.delay (100)
        if event.key == pygame.K_LEFT and charcor[1] == 640:      
            direction = 'left'
            if charcor[0] - 20 > 0:
                for pics2 in walk2:
                    charcor = (charcor[0] - 20, charcor [1])
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if Ldummy == True:
                        screen.blit (M, (dummycor))
                    if Rdummy == True:
                        screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    screen.blit (pics2, (charcor))
                    pygame.display.flip()
                    pygame.time.delay (100)
        if event.key == pygame.K_UP and (not event.key == pygame.K_LEFT) and (not event.key == pygame.K_RIGHT):
            if charcor[1] - 50 < 0:
                charcor = (charcor[0],0)
            else:
                charcor = charcor [0], charcor [1] - 50
            if charcor[1] == 640:
                screen.blit (bg, (0,0))
                screen.blit (returning, (900,0))
                screen.blit (hpcount, (0,0))
                screen.blit (Fly, (charcor))
                pygame.display.flip ()
                pygame.time.delay (100)
        if event.key == pygame.K_LEFT and charcor[1] != 640 and (not event.key == pygame.K_UP):
            direction = 'left'
            charcor = charcor [0] - 30, charcor [1] - 30
        if event.key == pygame.K_RIGHT and charcor[1] != 640  and (not event.key == pygame.K_UP):
            direction = 'right'
            charcor = charcor [0] + 30, charcor [1] - 30
        if event.key == pygame.K_DOWN:
            if charcor[1] == 640:
                screen.blit (bg, (0,0))
                screen.blit (returning, (900,0))
                screen.blit (hpcount, (0,0))
                if Ldummy == True:
                    screen.blit (M, (dummycor))
                if Rdummy == True:
                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                if direction == 'right':
                    screen.blit (Duck, (charcor[0], charcor[1] + 31))
                if direction == 'left':
                    screen.blit (pygame.transform.flip (Duck, True, False), (charcor [0], charcor[1] + 31))
                pygame.display.flip ()
                pygame.time.delay (100)
            if charcor[1] < 640:
                if charcor[1] + 20 > 640:
                    charcor=charcor[0],640
                else:
                    charcor = charcor [0], charcor[1] + 20
        if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
            direction = 'left'
            charcor = charcor [0] - 30, charcor [1] - 50
        if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
            direction = 'left'
            charcor = charcor [0] - 30, charcor [1] - 50
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            Teleporting.play(loops=0, maxtime=0, fade_ms=0)
            for q in teleset:
                screen.blit (bg, (0,0))
                screen.blit (returning, (900,0))
                screen.blit (hpcount, (0,0))
                if Ldummy == True:
                    screen.blit (M, (dummycor))
                if Rdummy == True:
                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                if direction == "right":
                    if q == alert:
                        screen.blit (q,(charcor))
                    if q == Tele1:
                        screen.blit (q,(charcor[0] -28,charcor[1] - 49))
                    if q == Tele2:
                        screen.blit (q,(charcor[0] -27,charcor[1] - 6))
                    if q == Tele3:
                        screen.blit (q,(charcor[0] -33,charcor[1] + 21))
                    if q == Tele4:
                        screen.blit (q,(charcor[0] -35,charcor[1] + 26))
                if direction == "left":
                    if q == alert:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor))
                    if q == Tele1:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -28,charcor[1] - 49))
                    if q == Tele2:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -27,charcor[1] - 6))
                    if q == Tele3:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -33,charcor[1] + 21))
                    if q == Tele4:
                        screen.blit (pygame.transform.flip(q,True,False),(charcor[0] -35,charcor[1] + 26))
                pygame.display.flip()
                pygame.time.delay(30)
            if direction == "right":
                if charcor[0] + 100 >= 1024:
                    charcor= (980, charcor[1])
                else:
                    charcor= (charcor[0] + 100, charcor[1])
            if direction == "left":
                if charcor[0] - 100 <= 0:
                    charcor = (0,charcor[1])
                else:
                    charcor= (charcor[0] - 100, charcor[1])
            Teleporting.fadeout(300)
########################################################################            
    if pygame.mouse.get_pressed() == (1,0,0):
        if pygame.mouse.get_pos ()[0] >= 512:
            Rdummy = True
            Ldummy = False
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = random.randint(50000,200000)
        if pygame.mouse.get_pos ()[0] < 512:
            Rdummy = False
            Ldummy = True
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = random.randint(50000,200000)
    if pygame.mouse.get_pressed() == (0,0,1):
        if pygame.mouse.get_pos ()[0] >= 512:
            Rdummy = True
            Ldummy = False
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = 999999
        if pygame.mouse.get_pos ()[0] < 512:
            Rdummy = False
            Ldummy = True
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = 999999
    if pygame.mouse.get_pressed() == (1,0,1):
        if pygame.mouse.get_pos ()[0] >= 512:
            Rdummy = True
            Ldummy = False
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = 50000000
        if pygame.mouse.get_pos ()[0] < 512:
            Rdummy = False
            Ldummy = True
            dummycor = (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 43)
            dummyhp = 50000000
########################################################################
    try:
        if dummyhp <= 0:
            Rdummy = False
            Ldummy = False
            Fatality.play(loops=0, maxtime=0, fade_ms=0)
            for i in deathset:
                screen.blit (bg, (0,0))
                screen.blit (returning, (900,0))
                screen.blit (hpcount, (0,0))
                if direction == 'right':
                    screen.blit (S, (charcor))
                if direction == 'left':
                    screen.blit (S2, (charcor))
                if dummycor[0] < 512:
                    screen.blit (i, (dummycor))
                if dummycor[0] >= 512:
                    screen.blit (pygame.transform.flip (i, True, False), (dummycor))
                pygame.display.flip()
                pygame.time.delay (200)
            dummyhp = 'Deceased'
            Fatality.fadeout (300)
    except: dummyhp = 'N/A Click to Spawn'
########################################################################     
    emotes ()
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_z:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    laz.play(loops=0, maxtime=0, fade_ms=0)
                    for att in arset:
                        decrement=(random.randint (1000, 4000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] + 20) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] + 20):
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] + 20):
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        screen.blit (att, (charcor))
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0]:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Ldummy == True or Rdummy) == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0]):
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    laz.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    laz.play(loops=0, maxtime=0, fade_ms=0)
                    for att2 in alset:
                        decrease = (random.randint (1000, 4000))
                        text= font.render (str (decrease), 1, (255,63,0))
                        if att2 == AL1:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 147, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL2:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 921, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL3:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 936, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL4:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 921, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL5:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 915, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL6:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 875, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL7:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 745, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL8:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 718, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if Ldummy == (True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        if att2 == AL9:
                            screen.blit (bg, (0,0))
                            screen.blit (returning, (900,0))
                            screen.blit (hpcount, (0,0))
                            if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20) and (Ldummy == True or Rdummy == True):
                                if dummycor[0] < 512:
                                    screen.blit (M, (dummycor))
                                if dummycor[0] >= 512:
                                    screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                            if Ldummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (MH, (dummycor))
                            if Rdummy == True and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            screen.blit (att2, (charcor[0] - 677, charcor [1]))
                            if Ldummy == True or Rdummy == True:
                                if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20:
                                    screen.blit (text, Textcor)
                            pygame.display.flip()
                            pygame.time.delay (100)
                            if (Ldummy == True or Rdummy == True) and ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] - 20):
                                Textcor = (Textcor[0], Textcor[1] - 5)
                                if dummyhp - decrease <= 0:
                                    dummyhp = 0
                                if dummyhp - decrease > 0:
                                    dummyhp = dummyhp - decrease
                                hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    laz.fadeout (300)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_x:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    carn.play(loops=0, maxtime=0, fade_ms=0)
                    for edge in ceset:
                        decrement=(random.randint (600, 1300))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 250 and dummycor [0] > charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 250 and dummycor [0] > charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 250 and dummycor [0] > charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if edge == CE1 or edge == CE2 or edge == CE3 or edge == CE4 or edge == CE5:
                            screen.blit (edge, (charcor[0], charcor[1]))
                        else:
                            screen.blit (edge, (charcor[0], charcor[1] - 50))
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 250 and dummycor [0] > charcor[0]:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (20)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 250 and dummycor [0] > charcor[0]:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    carn.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    carn.play(loops=0, maxtime=0, fade_ms=0)
                    for edge in ceset:
                        if edge == CE1:
                            sub = 7
                        if edge == CE2:
                            sub = 57
                        if edge == CE3:
                            sub = 67
                        if edge == CE4:
                            sub = 74
                        if edge == CE5:
                            sub = 120
                        if edge == CE6:
                            sub = 368
                        if edge == CE7:
                            sub = 409
                        if edge == CE8:
                            sub = 276
                        if edge == CE9:
                            sub = 235
                        if edge == CE10:
                            sub = 166
                        if edge == CE11:
                            sub = 165
                        if edge == CE12:
                            sub = 261
                        if edge == CE13:
                            sub = 290
                        if edge == CE14:
                            sub = 302
                        if edge == CE15:
                            sub = 335
                        if edge == CE16:
                            sub = 335
                        if edge == CE17:
                            sub = 219
                        if edge == CE18:
                            sub = 213
                        if edge == CE19:
                            sub = 211
                        decrement=(random.randint (600, 1300))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 250 and dummycor [0] < charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 250 and dummycor [0] < charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 250 and dummycor [0] < charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if edge == CE1 or edge == CE2 or edge == CE3 or edge == CE4 or edge == CE5:
                            screen.blit (pygame.transform.flip(edge, True, False), (charcor[0]-sub, charcor[1]))
                        else:
                            screen.blit (pygame.transform.flip(edge, True, False), (charcor[0]-sub, charcor[1]-50))
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 250 and dummycor [0] < charcor[0]:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (20)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 250 and dummycor [0] < charcor[0]:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    carn.fadeout (300)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_a:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sla.play(loops=0, maxtime=0, fade_ms=0)
                    for x in slashset:
                        decrement=(random.randint (6000, 12000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if x == Slash3:
                            screen.blit (x, (charcor[0] - 70, charcor [1] - 47))
                        if x == Slash2:
                            screen.blit (x,(charcor[0]-15,charcor[1]))
                        if x == Slash1:
                            screen.blit (x, (charcor[0]-29,charcor[1]))
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and x == Slash3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and x == Slash3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    sla.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sla.play(loops=0, maxtime=0, fade_ms=0)
                    for x in slashset:
                        decrement=(random.randint (6000, 12000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if x == Slash3:
                            screen.blit (pygame.transform.flip(x,True,False), (charcor[0] -38, charcor [1] - 47))
                        if x == Slash2:
                            screen.blit (pygame.transform.flip(x,True,False),(charcor[0]+17,charcor[1]))
                        if x == Slash1:
                            screen.blit (pygame.transform.flip(x,True,False), (charcor[0]+17, charcor[1]))
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and x == Slash3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and x == Slash3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    sla.fadeout (300)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_s:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sli.play(loops=0, maxtime=0, fade_ms=0)
                    for y in sliceset:
                        decrement=(random.randint (10000, 20000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if y == Slice3:
                            screen.blit (y, (charcor[0] - 36, charcor [1] - 68))
                        if y == Slice2:
                            screen.blit (y, (charcor[0]-20,charcor[1]-62))
                        if y == Slice1:
                            screen.blit (y, (charcor[0]+1,charcor[1]-9))
                        if y == Trans2:
                            screen.blit (y,charcor)
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and y == Slice3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (80)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0] and y == Slice3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    sli.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    sli.play(loops=0, maxtime=0, fade_ms=0)
                    for y in sliceset:
                        decrement=(random.randint (10000, 20000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if y == Slice3:
                            screen.blit (pygame.transform.flip(y,True,False), (charcor[0]-72, charcor [1] - 69))
                        if y == Slice2:
                            screen.blit (pygame.transform.flip(y,True,False),(charcor[0]-95,charcor[1]-62))
                        if y == Slice1:
                            screen.blit (pygame.transform.flip(y,True,False), (charcor[0]-33, charcor[1]-9))
                        if y == Trans2:
                            screen.blit (pygame.transform.flip(y,True,False), charcor)
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and y == Slice3:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (80)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0] and y == Slice3:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    sli.fadeout (300)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_d:
                if direction == 'right':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    swi.play(loops=0, maxtime=0, fade_ms=0)
                    for z in swingset:
                        decrement=(random.randint (69999, 99999))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 100 and dummycor [0] > charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if z == Swing3:
                            screen.blit (z, (charcor[0]-57,charcor[1]-40))
                        if z == Swing2:
                            screen.blit (z, (charcor[0]-42,charcor[1]-21))
                        if z == Swing1:
                            screen.blit (z, (charcor[0]-37,charcor[1]-1))
                        if z == Swing4:
                            screen.blit (z, (charcor[0]-65, charcor[1] -10))
                        if z == Trans:
                            screen.blit(z,charcor)
                        if Ldummy == True or Rdummy == True:
                            if (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0] and z == Swing4:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] < charcor[0] + 130 and dummycor [0] > charcor[0] and z == Swing4:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    swi.fadeout (300)
                if direction == 'left':
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    swi.play(loops=0, maxtime=0, fade_ms=0)
                    for z in swingset:
                        decrement=(random.randint (69999, 99999))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if not ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 100 and dummycor [0] < charcor[0]) and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if Ldummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0]:
                            screen.blit (MH, (dummycor))
                        if Rdummy == True and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0]:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        if z == Swing3:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0], charcor[1]-40))
                        if z == Swing2:
                            screen.blit (pygame.transform.flip(z,True,False),(charcor[0]-2,charcor[1]-21))
                        if z == Swing1:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0]-2, charcor[1]-1))
                        if z == Swing4:
                            screen.blit (pygame.transform.flip(z,True,False), (charcor[0]-114, charcor[1]-10))
                        if z == Trans:
                            screen.blit(pygame.transform.flip(z,True,False),charcor)
                        if Ldummy == True or Rdummy == True:
                            if ((dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0]) and z == Swing4:
                                screen.blit (text, Textcor)
                        pygame.display.flip()
                        pygame.time.delay (100)
                        if (Ldummy == True or Rdummy == True) and (dummycor[1] > 640 and dummycor[1] < 730) and dummycor[0] > charcor[0] - 130 and dummycor [0] < charcor[0] and z == Swing4:
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                    swi.fadeout (300)
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_v:
                Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                naut.play(loops=0, maxtime=0, fade_ms=0)
                for j in ultimate:
                    if Ldummy == True or Rdummy == True:
                        if dummyhp > 4000000:
                            decrement=(random.randint (699999, 999999))
                        else:
                            decrement=(random.randint (19999, 39999))
                    text= font.render (str (decrement), 1, (255,63,0))
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    
                    if direction == "right":
                        screen.blit (alert, (charcor))
                    if direction == "left":
                        screen.blit (pygame.transform.flip(alert,True,False), (charcor))
                        
                    if Ldummy == True or Rdummy == True:
                        if j == Ult20 or j == Ult22 or j == Ult23 or j == Ult24 or j == Ult25 or j == Ult26 or j == Ult27 or j == Ult21 or j == Ult28:
                            if dummycor[0] < 512:
                                screen.blit (MH, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        else:
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "left":
                        screen.blit (j, (0,50))
                    if direction == "right":
                        screen.blit (pygame.transform.flip(j,True,False), (0,50))
                    if j == Ult20 or j == Ult22 or j == Ult23 or j == Ult24 or j == Ult25 or j == Ult26 or j == Ult27 or j == Ult21 or j == Ult28:
                        if (Ldummy == True or Rdummy == True):
                            screen.blit (text, Textcor)
                            Textcor = (Textcor[0], Textcor[1] - 5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))

                    pygame.display.flip()
                    pygame.time.delay (100)
                naut.fadeout (300)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_c:
                Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                for k in predemo:
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right":
                        screen.blit (k, (charcor[0], charcor[1] - 30))
                    if direction == "left":
                        screen.blit (pygame.transform.flip(k,True,False), (charcor[0], charcor[1] - 30)) 
                    pygame.display.flip()
                    pygame.time.delay (50)
                DemoSlash.play(loops=0, maxtime=0, fade_ms=0)
                if (Ldummy == True or Rdummy == True) and direction == "right" and dummycor[0] < charcor[0] + 500 and dummycor[0] > charcor[0]:
                    for l in demohit:
                        decrement=(random.randint (5000, 12000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if dummycor[0] < 512:
                            screen.blit (MH, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        screen.blit (l, (dummycor[0] - 40, dummycor[1] - 40))
                        screen.blit (text, Textcor)
                        Textcor = (Textcor[0], Textcor[1] - 5)
                        if dummyhp - decrement <= 0:
                            dummyhp = 0
                        if dummyhp - decrement > 0:
                            dummyhp = dummyhp - decrement
                        hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        pygame.display.flip()
                        pygame.time.delay (50)
                if (Ldummy == True or Rdummy == True) and direction == "left" and dummycor[0] > charcor[0] - 500 and dummycor[0] < charcor[0]:
                    for l in demohit:
                        decrement=(random.randint (5000, 12000))
                        text= font.render (str (decrement), 1, (255,63,0))
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if dummycor[0] < 512:
                            screen.blit (MH, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        
                        screen.blit (pygame.transform.flip(l,True,False), (dummycor[0] - 40, dummycor[1] - 40))
                        screen.blit (text, Textcor)
                        Textcor = (Textcor[0], Textcor[1] - 5)
                        if dummyhp - decrement <= 0:
                            dummyhp = 0
                        if dummyhp - decrement > 0:
                            dummyhp = dummyhp - decrement
                        hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        pygame.display.flip()
                        pygame.time.delay (50)
                DemoSlash.stop()
                for u in postdemo:
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (Ldummy == True or Rdummy == True) and direction == "right" and dummycor[0] < charcor[0] + 500 and dummycor[0] > charcor[0]:
                        if dummycor[0] < 512:
                            screen.blit (MH, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                    if (Ldummy == True or Rdummy == True) and direction == "left" and dummycor[0] > charcor[0] - 500 and dummycor[0] < charcor[0]:
                        if dummycor[0] < 512:
                            screen.blit (MH, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                    if direction == "left" and dummycor[0] < charcor[0]- 500 and (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right" and dummycor[0] > charcor[0]+ 500 and (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "left" and dummycor[0] > charcor[0] and (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right" and dummycor[0] < charcor[0] and (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == 'right':
                        if u == Demo5:
                            screen.blit (u, (charcor[0]-33,charcor[1] - 36))
                        if u == Demo6:
                            screen.blit (u, (charcor[0]-37,charcor[1] - 38))
                        if u == Demo7:
                            screen.blit (u, (charcor[0]-41,charcor[1] - 43))
                        if u == Demo8:
                            screen.blit (u, (charcor[0]-27,charcor[1] - 42))
                        if u == Demo9:
                            screen.blit (u, (charcor[0]-25,charcor[1] - 40))
                        if u == Demo10:
                            screen.blit (u, (charcor[0]-20,charcor[1] - 44))
                        if u == Demo11:
                            screen.blit (u, (charcor[0]-19,charcor[1] - 38))     
                    if direction == 'left':
                        if u == Demo5:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]-58,charcor[1] - 37))
                        if u == Demo6:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+4,charcor[1] - 39))
                        if u == Demo7:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+4,charcor[1] - 44))
                        if u == Demo8:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+4,charcor[1] - 43))
                        if u == Demo9:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+4,charcor[1] - 41))
                        if u == Demo10:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+3,charcor[1] - 45))
                        if u == Demo11:
                            screen.blit (pygame.transform.flip(u,True,False), (charcor[0]+3,charcor[1] - 39)) 
                    pygame.display.flip()
                    pygame.time.delay (50)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_f:
                Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                Shootspree = True
                Reset = True
                for c in preh:
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right":
                        if c == H1:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 17))
                        if c == H2:
                            screen.blit (c, (charcor[0]-64, charcor[1] - 34))
                        if c == H3:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 34))
                        if c == H4:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 33))
                        if c == H5:
                            screen.blit (c, (charcor[0]-64, charcor[1] - 34))
                        if c == H6:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 35))
                        if c == H7:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 52))
                        if c == H8:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 54))
                        if c == H9:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 56))
                        if c == H10:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 57))
                        if c == H11:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 59))
                        if c == H12:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 69))
                        if c == H13:
                            screen.blit (c, (charcor[0]-62, charcor[1] - 97))
                    if direction == "left":
                        if c == H1:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-5, charcor[1] - 17))
                        if c == H2:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-67, charcor[1] - 34))
                        if c == H3:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-71, charcor[1] - 34))
                        if c == H4:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-71, charcor[1] - 33))
                        if c == H5:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-72, charcor[1] - 34))
                        if c == H6:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-82, charcor[1] - 35))
                        if c == H7:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-82, charcor[1] - 52))
                        if c == H8:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-83, charcor[1] - 54))
                        if c == H9:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-82, charcor[1] - 56))
                        if c == H10:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-81, charcor[1] - 57))
                        if c == H11:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-81, charcor[1] - 59))
                        if c == H12:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-79, charcor[1] - 69))
                        if c == H13:
                            screen.blit (pygame.transform.flip(c,True,False), (charcor[0]-77, charcor[1] - 97)) 
                    pygame.display.flip()
                    pygame.time.delay (50)
                Hsound.play(loops=-1, maxtime=0, fade_ms=0)
                while Shootspree == True:
                    for event in pygame.event.get ():
                        if event.type == pygame.QUIT:
                            pygame.quit ()
                            sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit ()
                                sys.exit()
                    for v in shootset:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if direction == "right":
                            if v == HO1:
                                screen.blit (v, (charcor[0]-62, charcor[1] - 101))
                            if v == HO2:
                                screen.blit (v, (charcor[0]-61, charcor[1] - 100))
                            if v == HO3:
                                screen.blit (v, (charcor[0]-71, charcor[1] - 102))
                        if direction == "left":
                            if v == HO1:
                                screen.blit (pygame.transform.flip(v,True,False), (charcor[0]-76, charcor[1] - 101))
                            if v == HO2:
                                screen.blit (pygame.transform.flip(v,True,False), (charcor[0]-84, charcor[1] - 100))
                            if v == HO3:
                                screen.blit (pygame.transform.flip(v,True,False), (charcor[0]-95, charcor[1] - 102))
                        if direction == "right" and dummycor[0] > charcor[0] and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (MH, (dummycor))
                                if arrows[0] > dummycor[0]:
                                    screen.blit (Hhit,(random.randint(dummycor[0] - 10, dummycor[0] + 10),(random.randint(dummycor[1] - 10, dummycor[1] + 10))))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                                if arrows[0] > dummycor[0]:
                                    screen.blit (Hhit,(random.randint(dummycor[0] - 10, dummycor[0] + 10),(random.randint(dummycor[1] - 10, dummycor[1] + 10))))
                        if direction == "left" and dummycor[0] < charcor[0] and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (MH, (dummycor))
                                if arrows[0] < dummycor[0]:
                                    screen.blit (Hhit,(random.randint(dummycor[0] - 10, dummycor[0] + 10),(random.randint(dummycor[1] - 10, dummycor[1] + 10))))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                                if arrows[0] < dummycor[0]:
                                    screen.blit (Hhit,(random.randint(dummycor[0] - 10, dummycor[0] + 10),(random.randint(dummycor[1] - 10, dummycor[1] + 10))))
                        if direction == "right" and dummycor[0] < charcor[0] and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if direction == "left" and dummycor [0] > charcor[0] and (Ldummy == True or Rdummy == True):
                            if dummycor[0] < 512:
                                screen.blit (M, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                        if direction == 'right':
                            if Reset == True:
                                arrows= (charcor[0]+150,charcor[1]+30)
                                Reset = False
                            screen.blit (Ball,arrows)
                            if arrows[0] - 100 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 100, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 150 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 150, arrows [1] - 5))
                            if arrows[0] - 200 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 200, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 50)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 250 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 250, arrows [1] - 5))
                            if arrows[0] - 300 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 300, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 80)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 350 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 350, arrows [1] - 5))
                            if arrows[0] - 400 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 400, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 110)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 450 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 450, arrows [1] - 5))
                            if arrows[0] - 500 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 500, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 140)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 550 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 550, arrows [1] - 5))
                            if arrows[0] - 600 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 600, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 170)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 650 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 650, arrows [1] - 5))
                            if arrows[0] - 700 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 700, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] > charcor[0] and dummyhp != "Deceased" and arrows[0] > dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 200)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] - 750 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 750, arrows [1] - 5))
                            if arrows[0] - 800 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 800, arrows [1] + 5))
                            if arrows[0] - 850 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 850, arrows [1] - 5))
                            if arrows[0] - 900 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 900, arrows [1] + 5))
                            if arrows[0] - 950 > charcor [0]:
                                screen.blit (Ball,(arrows[0] - 950, arrows [1] - 5))
                            if arrows[0] >= 1024:
                                arrows= (900,charcor[1]+30)
                            else:
                                arrows = (arrows[0] + 50, arrows [1])                                
                        if direction == 'left':
                            if Reset == True:
                                arrows= (charcor[0]-150,charcor[1]+30)
                                Reset = False
                            screen.blit (pygame.transform.flip(Ball,True,False),arrows)
                            if arrows[0] + 100 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 100, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 150 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 150, arrows [1] - 5))
                            if arrows[0] + 200 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 200, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 50)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 250 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 250, arrows [1] - 5))
                            if arrows[0] + 300 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 300, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 80)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 350 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 350, arrows [1] - 5))
                            if arrows[0] + 400 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 400, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 110)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 450 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 450, arrows [1] - 5))
                            if arrows[0] + 500 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 500, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 140)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 550 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 550, arrows [1] - 5))
                            if arrows[0] + 600 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 600, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 170)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 650 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 650, arrows [1] - 5))
                            if arrows[0] + 700 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 700, arrows [1] + 5))
                                decrement=(random.randint (500, 1500))
                                text= font.render (str (decrement), 1, (255,63,0))
                                if dummycor[0] < charcor[0] and dummyhp != "Deceased" and arrows[0] < dummycor[0]:
                                    screen.blit (text,Textcor)
                                    Textcor = (dummycor[0] + 15, dummycor[1] - 200)
                                    if dummyhp - decrement <= 0:
                                        dummyhp = 0
                                    if dummyhp - decrement > 0:
                                        dummyhp = dummyhp - decrement
                                    hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            if arrows[0] + 750 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 750, arrows [1] - 5))
                            if arrows[0] + 800 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 800, arrows [1] + 5))
                            if arrows[0] + 850 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 850, arrows [1] - 5))
                            if arrows[0] + 900 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 900, arrows [1] + 5))
                            if arrows[0] + 950 < charcor [0]:
                                screen.blit (pygame.transform.flip(Ball,True,False),(arrows[0] + 950, arrows [1] - 5))
                            if arrows[0] <= 0:
                                arrows= (100,charcor[1]+30)
                            else:
                                arrows = (arrows[0] - 50, arrows [1])
                        pygame.display.flip()
                        pygame.time.delay (50)
                        try:
                            if dummyhp <= 0:
                                Rdummy = False
                                Ldummy = False
                                Fatality.play(loops=0, maxtime=0, fade_ms=0)
                                for i in deathset:
                                    screen.blit (bg, (0,0))
                                    screen.blit (returning, (900,0))
                                    screen.blit (hpcount, (0,0))
                                    if i == MD1 or i == MD4:
                                        if direction == 'right':
                                            screen.blit (HO1, (charcor[0]-62,charcor[1]-101))
                                        if direction == 'left':
                                            screen.blit (pygame.transform.flip(HO1,True,False), (charcor[0]-76, charcor[1] - 101))
                                    if i == MD2 or i == MD5:
                                        if direction == 'right':
                                            screen.blit (HO2, (charcor[0]-61,charcor[1]-100))
                                        if direction == 'left':
                                            screen.blit (pygame.transform.flip(HO2,True,False), (charcor[0]-84, charcor[1] - 100))
                                    if i == MD3 or i == MD6:
                                        if direction == 'right':
                                            screen.blit (HO3, (charcor[0]-71,charcor[1]-101))
                                        if direction == 'left':
                                            screen.blit (pygame.transform.flip(HO3,True,False), (charcor[0]-95, charcor[1] - 102))
                                    if dummycor[0] < 512:
                                        screen.blit (i, (dummycor))
                                    if dummycor[0] >= 512:
                                        screen.blit (pygame.transform.flip (i, True, False), (dummycor))
                                    pygame.display.flip()
                                    pygame.time.delay (200)
                                dummyhp = 'Deceased'
                                Fatality.fadeout (300)
                        except: dummyhp = 'N/A Click to Spawn'
                    if not event.type == KEYDOWN:
                        Shootspree = False
                        Hsound.fadeout(100)
                for p in posth:
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right":
                        if p == HE1:
                            screen.blit (p, (charcor[0]-62,charcor[1] - 95))
                        if p == HE2:
                            screen.blit (p, (charcor[0]-62,charcor[1] - 91))
                        if p == HE3:
                            screen.blit (p, (charcor[0]-62,charcor[1] - 78))
                        if p == HE4:
                            screen.blit (p, (charcor[0]-62,charcor[1] - 64))
                        if p == HE5:
                            screen.blit (p, (charcor[0]-61,charcor[1] - 21))
                    if direction == "left":
                        if p == HE1:
                            screen.blit (pygame.transform.flip (p,True,False), (charcor[0]-75,charcor[1] - 95))
                        if p == HE2:
                            screen.blit (pygame.transform.flip (p,True,False), (charcor[0]-74,charcor[1] - 91))
                        if p == HE3:
                            screen.blit (pygame.transform.flip (p,True,False), (charcor[0]-74,charcor[1] - 78))
                        if p == HE4:
                            screen.blit (pygame.transform.flip (p,True,False), (charcor[0]-71,charcor[1] - 64))
                        if p == HE5:
                            screen.blit (pygame.transform.flip (p,True,False), (charcor[0]-6,charcor[1] - 21))
                    pygame.display.flip()
                    pygame.time.delay (50)
########################################################################
    if charcor[1] == 640:
        if event.type == KEYDOWN:
            if event.key == K_g:
                Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                EAsfx.play(loops=0, maxtime=0, fade_ms=0)
                for e in preea:
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    if direction == "right":
                        screen.blit (e, (charcor))
                    if direction == "left":
                        if e == Trans3:
                            screen.blit (pygame.transform.flip(e, True, False), (charcor))
                        if e == EA1:
                            screen.blit (pygame.transform.flip(e, True, False), (charcor[0]-6,charcor[1]))
                        if e == EA2:
                            screen.blit (pygame.transform.flip(e, True, False), (charcor[0]-59,charcor[1]))
                        if e == EA3:
                            screen.blit (pygame.transform.flip(e, True, False), (charcor[0]-94,charcor[1]))
                    pygame.display.flip()
                    pygame.time.delay(50)
                EAcor = (dummycor[0]+4,dummycor[1] - 31)
                for b in ea:
                    decrement=(random.randint (10000, 20000))
                    text= font.render (str (decrement), 1, (255,63,0))
                    screen.blit (bg, (0,0))
                    screen.blit (returning, (900,0))
                    screen.blit (hpcount, (0,0))
                    if (b == EA4 or b == EA5 or b == EA6 or b == EA7 or b == EA8 or b == EA9 or b == EA10 or b == EA11 or b == EA12 or b == EA13 or b == EA14 or b == EA15 or b == EA16 or b == EA17 or b == EA18 or b == EA19 or b == EA20 or b == EA21 or b == EA22 or b == EA23 or b == EA24 or b == EA25 or b == EA26 or b == EA27 or b == EA28) and (Ldummy == True or Rdummy == True):
                        if dummycor[0] < 512:
                            screen.blit (M, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (M, True, False), (dummycor))
                    else:
                        if Ldummy == True or Rdummy == True:
                            if dummycor[0] < 512:
                                screen.blit (MH, (dummycor))
                            if dummycor[0] >= 512:
                                screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                            if random.randint (0,2) == 0:
                                screen.blit (EAball,EAcor)
                            elif random.randint (0,1) == 0:
                                screen.blit (EAball1,EAcor)
                            else:
                                screen.blit (EAball2,EAcor)
                            screen.blit (text,Textcor)
                            Textcor = (Textcor[0],Textcor[1] -5)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                            EAcor = (random.randint(EAcor[0]-2,EAcor[0]+2), EAcor[1] - 2)
                    if direction == "right":
                        screen.blit (EA3, (charcor))
                    if direction == "left":
                        screen.blit (pygame.transform.flip(EA3,True,False), (charcor[0]-94, charcor[1]))
                    if b == EA31:
                        screen.blit (b, (-90,-65))
                    elif b == EA34:
                        screen.blit (b, (-90,-44))
                    elif b == EA35:
                        screen.blit (b, (-90,-41))
                    elif b == EA37:
                        screen.blit (b, (-90,-53))
                    elif b == EA39:
                        screen.blit (b, (-90,-53))
                    else:
                        screen.blit (b, (-90,-40))
                    pygame.display.flip()
                    pygame.time.delay (35)
                EAsfx.fadeout(300)
                if Ldummy == True or Rdummy == True:
                    Textcor = (dummycor[0] + 15, dummycor[1] - 20)
                    EAE.play(loops=0, maxtime=0, fade_ms=0)
                    for u in EAEset:
                        screen.blit (bg, (0,0))
                        screen.blit (returning, (900,0))
                        screen.blit (hpcount, (0,0))
                        if direction == "right":
                            screen.blit (EA3, (charcor))
                        if direction == "left":
                            screen.blit (pygame.transform.flip(EA3,True,False), (charcor[0]-94, charcor[1]))
                        if dummycor[0] < 512:
                            screen.blit (MH, (dummycor))
                        if dummycor[0] >= 512:
                            screen.blit (pygame.transform.flip (MH, True, False), (dummycor))
                        screen.blit (u, (dummycor[0]-50,dummycor[1]-70))
                        if u == EAE2 or u == EAE3:
                            decrement=(random.randint (39999, 49999))
                            text= font.render (str (decrement), 1, (255,63,0))
                            screen.blit (text,Textcor)
                            Textcor = (Textcor[0], Textcor[1]-25)
                            if dummyhp - decrement <= 0:
                                dummyhp = 0
                            if dummyhp - decrement > 0:
                                dummyhp = dummyhp - decrement
                            hpcount = font.render ('Health of Dummy =' + str (dummyhp), 1, (255,255,0))
                        pygame.display.flip()
                        pygame.time.delay (65)
                    EAE.fadeout(300)










                    
                    



                    
