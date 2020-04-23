#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append(".")

cIns=2
cDel=2
filename='Instances_genom_1/Instances_genome/Inst_0000010_8.adn'
#f=open(filename)

#x=['A','T','T','G','T','A']
#y=['A','T','C','T','T','A']
#x=['A','G','T','A','C','G','C','A']
#y=['T','A','T','G','C']

print "------------------------------------------ Initialisation -----------------------------------"

def c_sub(a,b):
	if( (a=='A' and b=='T') or (a=='T' and b=='A') or (a=='G' and b=='C') or (a=='C' and b=='G') ):
		return 3
	if( a==b ):
		return 0
	return 4
	
def construireTab(filename):
	f = open(filename)
	n = f.readline()
	m = f.readline()
	chaineX = f.readline()
	chaineY = f.readline()
	x=[]
	y=[]
	for x1 in chaineX: 
		if(x1!= " " and x1!="\n"):
			x.append(x1)
	for y1 in chaineY:
		if(y1!=" " and y1!="\n"):
			y.append(y1)
	f.close()
	return (x,y)
	

t=construireTab(filename)
x=t[0]
y=t[1]
print "x=",x
print "y=",y,"\n"

print "------------------------------------------ Tâche A -----------------------------------"

def dist_naif_rec(x,y,i,j,c,dist):
	"""
	x et y deux mots
	i un indice dans [0..|x|],j un indice dans [0..|y|]
	c le coût de l'alignement de (x[1..i],y[1..j]) 
	dist le coût du meilleur alignement de (x,y) connu avant cet appel
	"""
	
	if(i==len(x)-1 and j==len(y)-1):
		if(c<dist):
			dist=c
	else:
		if(i<len(x)-1 and j<len(y)-1):			
			dist=dist_naif_rec(x,y,i+1,j+1,c+c_sub(x[i+1],y[j+1]),dist)

		if(i<len(x)-1):
			dist=dist_naif_rec(x,y,i+1,j,c+2,dist)
		
		if(j<len(y)-1):
			dist=dist_naif_rec(x,y,i,j+1,c+2,dist)		
	return dist


def dist_naif(x,y):
	return dist_naif_rec(x,y,-1,-1,0,10000000)
	

d=dist_naif(x,y)
print "exemple:",filename
print "le resultat de dist_naif=",d,"\n"
print "------------------------------------------ Tâche B -----------------------------------"

def dist_1(x,y):
	n=len(x) #ligne
	m=len(y) #colonne
	print n,m
	tab=[[0 for j in range(m+1)]  for i in range(n+1)] #creation d'un tableau(matrice) de taille n*m 
	tab[0][0]=0
	#print tab
	#initialisation du tableau
	for i in range(1,n+1):          # la colonne 0
		tab[i][0]=i*cDel      #D(i,0)
	for j in range(1,m+1):          # la ligne 0
		tab[0][j]=j*cIns      #D(0,j)  
	
	for i1 in range(1,n+1):
		for j1 in range(1,m+1):
			#print i1,j1
			#print tab[i1-1][j1],tab[i1][j1-1],tab[i1-1][j1-1]
			case1=tab[i1-1][j1]  #la case en haut 
			case2=tab[i1][j1-1]  #la case à gauche
			case3=tab[i1-1][j1-1]#la case en haut à gauche
			tab[i1][j1] = min(case1+cIns, case2+cDel, case3+c_sub(x[i1-1],y[j1-1]))
	return tab[n][m]


d=dist_1(x,y)
print "le resultat de dist_1 est :",d,"\n"





def dist_1bis(x,y): ### uniquement pour obtenir un tab de sol1
	n=len(x) #ligne
	m=len(y) #colonne
	print n,m
	tab=[[0 for j in range(m+1)]  for i in range(n+1)] #creation d'un tableau(matrice) de taille n*m 
	tab[0][0]=0
	#print tab
	#initialisation du tableau
	for i in range(1,n+1):          # la colonne 0
		tab[i][0]=i*cDel      #D(i,0)
	for j in range(1,m+1):          # la ligne 0
		tab[0][j]=j*cIns      #D(0,j)  
	
	for i1 in range(1,n+1):
		for j1 in range(1,m+1):
			#print i1,j1
			#print tab[i1-1][j1],tab[i1][j1-1],tab[i1-1][j1-1]
			case1=tab[i1-1][j1]  #la case en haut 
			case2=tab[i1][j1-1]  #la case à gauche
			case3=tab[i1-1][j1-1]#la case en haut à gauche
			tab[i1][j1] = min(case1+cIns, case2+cDel, case3+c_sub(x[i1-1],y[j1-1]))
	return tab

def sol_1(x,y,t):
	tmpX=[]
	tmpY=[]
	alX=[]
	alY=[]
	i=len(x) #ligne
	j=len(y) #colonne
	
	while(i!=0 and j!=0):
	
		#print "i=",i,"j=",j
		c=tab[i][j]
		case1=tab[i-1][j]  #la case en haut 
		case2=tab[i][j-1]  #la case à gauche
		case3=tab[i-1][j-1]#la case en haut à gauche
		
		#on cherche la case precedente  
		if(c-case1==cIns):
			tmpX.append(x[i-1])
			tmpY.append('-')
			i=i-1

		if(c-case2==cDel):
			tmpX.append('-')
			tmpY.append(y[j-1])
			j=j-1
			
		if(c-case3==c_sub(x[i-1],y[j-1])):
			#if(c_sub(x[i-1],y[j-1]==0):
			
			tmpX.append(x[i-1])
			tmpY.append(y[j-1])
			i=i-1
			j=j-1
	
	#on inverse l'ordre du tab trouvé
	for i in reversed(tmpX):
		alX.append(i)

	for j in reversed(tmpY):
		alY.append(j)
	
	return (alX,alY)

#tab=dist_1bis(x,y)
#sol=sol_1(x,y,tab)
#print "alignement optimal = ",sol


def prog_dyn(x,y):
	t=dist_1(x,y)
	sol=sol_1(x,y,t)
	
	return (t,sol)
	
print "------------------------------------------ Tâche C --------------------------------"	
def dist_2(x,y):
	n=len(x) #ligne
	m=len(y) #colonne
	print n,m
	vide=[0 for j in range(m+1)] 
	tab=[[0 for j in range(m+1)]  for i in range(2)] #creation d'un tableau(matrice) de taille n*m 
	tab[0][0]=0

	#initialisation du tableau
	for j in range(1,m+1):          # la ligne 0
		tab[0][j]=j*cIns      #D(0,j)  
	
	for i1 in range(1,n+1):
		tab[1][0]=cDel*i1
		for j1 in range(1,m+1):
			case1=tab[0][j1]  #la case en haut 
			case2=tab[1][j1-1]  #la case à gauche
			case3=tab[0][j1-1]#la case en haut à gauche
			tab[1][j1] = min(case1+cIns, case2+cDel, case3+c_sub(x[i1-1],y[j1-1]))

		for j2 in range(0,m+1):
			tab[0][j2]=tab[1][j2]
		
		tab[1]=vide
	return tab	
	
	
tab1=dist_2(x,y)
print "le resultat de dist_1 est :",tab1,"\n"	

print "------------------------------------------ Tâche D -----------------------------------"

def mots_gap(k):
	mot=['-' for i in range(k)] 
	return mot


mt=mots_gap(5)	
print "test de mots_gap(5)est: ", mt

def paire_concordante(a): #a est une lettres
	if(a=='A'):
		return 'T'
		
	if (a=='T'):
		return 'A'
	
	if (a=='G'):
		return 'C'
	
	if(a=='C'):
		return 'G'


	
l=['T']
m=['A','C']

	
def align_lettre_mot(lettre,mot):

	if lettre==mot:
		return (lettre,mot)
	
	if lettre[0] in mot:
		for i in range(len(mot)-1):
			i=mot.index(lettre[0])
			alignX=['-' for j in range(len(mot))]
			alignX[i]=lettre[0]
			return (alignX,mot)
		
	else:
		if (paire_concordante(lettre[0]) in mot):
			i=mot.index(paire_concordante(lettre[0]))
			alignX=['-' for j in range(len(mot))]
			alignX[i]=lettre[0]

			return (alignX,mot)
		else:
			alignX=['-' for j in range(len(mot))] 
			alignX[0]=lettre[0]
			return (alignX,mot)	
						
		
			
t1=align_lettre_mot(l,m)				
print "test avec lettre: ",l,"mot:",m,"\n"				


def coupure(x,y):
	n=len(x) #ligne
	m=len(y) #colonne 
	vide=[0 for j in range(m+1)] 
	tab=[[0 for j in range(m+1)]  for i in range(2)] #creation d'un tableau(matrice) de taille n*m 
	tab[0][0]=0
	
	tabI=[[0 for j in range(m+1)]  for i in range(2)]  # tableau I qui indique le chemin d'alignement
	#print "tabi=",tabi
	
	#initialisation du tableau
	for j in range(1,m+1):          # la ligne 0
		tab[0][j]=j*cIns      #D(0,j)  
	
	for i1 in range(1,n+1):
		tab[1][0]=cDel*i1
		tabI[1][0]=0
		for j1 in range(1,m+1):
			case1=tab[0][j1]  #la case en haut 
			case2=tab[1][j1-1]  #la case à gauche
			case3=tab[0][j1-1]#la case en haut à gauche
			tab[1][j1] = min(case1+cIns, case2+cDel, case3+c_sub(x[i1-1],y[j1-1]))
			if(i1==n/2):
				#tabI[1][0]=0
				tabI[1][j1]=j1
			
			if(i1>n/2):
				#print "i1=",i1,"j1=",j1,"tabI=",tabI[1]
				if(tab[1][j1]-case2==cDel): 
					#print "tabI[1][j1-1]=",tabI[1][j1-1]
					tabI[1][j1]=tabI[1][j1-1]
				elif(tab[1][j1]-case1==cIns): 
					#print "",tabI[0][j1]
					tabI[1][j1]=tabI[0][j1]
				elif(tab[1][j1]-case3==c_sub(x[i1-1],y[j1-1])): 
					#print "tabI[0][j1-1]=",tabI[0][j1-1]
					tabI[1][j1]=tabI[0][j1-1]
	
		for j2 in range(0,m+1):
			tab[0][j2]=tab[1][j2]
			if(i1>=n/2):
				tabI[0][j2]=tabI[1][j2]
		
		
		tab[1]=vide
		tabI[1]=[0 for j in range(m+1)]
		#print "tabI a la fin=",tabI
	return tabI[0][m]
	
	
tt=coupure(x,y)
print"coupure j liée à i est: ",tt,"\n"	


def sol_2(x,y):
	if(len(x)==1 and len(y)!=0):
		return align_lettre_mot(x,y)
		
	if(len(y)==0):
		return (x,mots_gap(len(x)))	
		
	else:
		i=len(x)/2
		j=int(coupure(x,y))
		
		(alX1,alY1) = sol_2(x[:i],y[:j]) #diviser pour regner
		(alX2,alY2) = sol_2(x[i:],y[j:])

	
	return (alX1+alX2, alY1+alY2)


s2=sol_2(x,y)
print "le résultat de sol_2 est :",s2,"\n"

















