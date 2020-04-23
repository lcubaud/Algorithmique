#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import ALGOO
import tacheJPP
sys.path.append(".")

#x=['A','T','T','G','T','A']
#y=['A','T','C','T','T','A']

filename=['Instances_genome/Inst_0000010_44.adn',
'Instances_genome/Inst_0000010_7.adn',
'Instances_genome/Inst_0000010_8.adn',
'Instances_genome/Inst_0000012_13.adn',
'Instances_genome/Inst_0000012_32.adn',
'Instances_genome/Inst_0000012_56.adn',
'Instances_genome/Inst_0000013_45.adn',
'Instances_genome/Inst_0000013_56.adn',
'Instances_genome/Inst_0000013_89.adn',
'Instances_genome/Inst_0000014_7.adn',
'Instances_genome/Inst_0000014_23.adn',
'Instances_genome/Inst_0000014_83.adn',
'Instances_genome/Inst_0000015_2.adn',
'Instances_genome/Inst_0000015_4.adn',
'Instances_genome/Inst_0000015_76.adn',
'Instances_genome/Inst_0000020_8.adn',
'Instances_genome/Inst_0000020_17.adn',
'Instances_genome/Inst_0000050_3.adn',
'Instances_genome/Inst_0000100_7.adn',
'Instances_genome/Inst_0000500_3.adn',
'Instances_genome/Inst_0001000_7.adn',
'Instances_genome/Inst_0002000_3.adn',
'Instances_genome/Inst_0003000_1.adn',
'Instances_genome/Inst_0005000_4.adn',
'Instances_genome/Inst_0008000_32.adn',
'Instances_genome/Inst_0010000_7.adn',
'Instances_genome/Inst_0015000_3.adn',
'Instances_genome/Inst_0020000_30.adn',
'Instances_genome/Inst_0050000_6.adn',
'Instances_genome/Inst_0100000_3.adn',]

print "------TACHE A----------------"
for i in range(0,6):
	f=open(filename[i])
	t=ALGOO.construireTab(filename[i])
	x=t[0]
	y=t[1]
	start_time = time.time()
	ALGOO.tacheA(x,y)
	print("Temps d execution : %s secondes ---" % (time.time() - start_time))
	if (time.time() - start_time) > 60:
		print "coucou"

print "------TACHE B----------------"
for i in range(25,27):
	f=open(filename[i])
	t=ALGOO.construireTab(filename[i])
	x=t[0]
	y=t[1]
	start_time = time.time()
	ALGOO.tacheB(x,y)
	print("Temps d execution : %s secondes ---" % (time.time() - start_time))
	if (time.time() - start_time) > 600:
		print "plus de 10mins"


print "-----TACHE C----------------"
for i in [1,4,8,12,15,18,20,21,22,23,24,25,26,27,28]:
	f=open(filename[i])
	t=ALGOO.construireTab(filename[i])
	x=t[0]
	y=t[1]
	start_time = time.time()
	tab=ALGOO.tacheC(x,y)
	print("Temps d execution : %s secondes ---" % (time.time() - start_time))
	if (time.time() - start_time) > 600:
		print "plus de 10mins"



print "----------TACHE D---------------"
x=['A','T','T','G','T','A']
y=['A','T','C','T','T','A']

for i in range(0,1):
	f=open(filename[i])
	t=ALGOO.construireTab(filename[i])
	x=t[0]
	y=t[1]
	start_time = time.time()
	alX=ALGOO.sol_2(x,y)
	print alX
	print("Temps d execution : %s secondes ---" % (time.time() - start_time))
	if (time.time() - start_time) > 600:
		print "plus de 10mins"
#ALGOO.afficherAlignement(alX,alY)
