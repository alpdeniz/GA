#!/usr/local/bin/python
import random as r
import score
class Dna():
   def __init__(self):
      self.nofgenomes=4
      self.dna=[]
      self.fit=0
   def randomdna(self):
      self.dna.append(r.uniform(6,17))
   #   self.dna.append(r.uniform(0.28,0.48))
      self.dna.append(r.uniform(1.1,1.8))
      self.dna.append(r.uniform(1.1,2))
      self.dna.append(r.uniform(1.1,3.2))      
   def adddna(self,genes):
      for i in range(len(genes)):
         self.dna.append(genes[i])
   def mutate(self):
      dna=self.dna
      a=r.randint(0,self.nofgenomes-1)
      dna[a]=r.uniform(1.1,17)
#      print "mutation @"+str(a+1)
         
   def fitness(self):
      ng = self.nofgenomes
      dna=self.dna
#         
      self.fit = score.score(dna[0],dna[1],dna[2],dna[3])[0]
      return self.fit
      
   def showdna(self):
      dna=self.__class__.dna
      for i in range(5):
         print dna[i] , i+1
              
class Generation():
   def choose(self,dnas):  
      totalfitness = sum(dna.fit for dna in dnas ) 
      fslice = totalfitness * r.random()        
      cfslice = 0
      for e in dnas:
          cfslice = cfslice + e.fit
          
          if cfslice > fslice:
              dnas.remove(e)
              return e
              
   def breed(self,mum_dna,dad_dna):
      #crossover location
      cp=r.randint(1,len(mum_dna)-1)
      baby1=Dna()
      baby2=Dna()
      babym1=Dna()
      babym2=Dna()
      for i in range(cp):
         baby1.dna.append(mum_dna[i])
         baby2.dna.append(dad_dna[i])
      for j in range(len(mum_dna)-cp):
         baby1.dna.append(dad_dna[j+cp])
         baby2.dna.append(mum_dna[j+cp])
      baby1.fitness()
      baby2.fitness()        

      babym1.dna=baby1.dna
      babym2.dna=baby2.dna

#if r.random() < mutationrate:
      babym1.mutate()
  #    if r.random() < mutationrate:
      babym2.mutate()    
      babym1.fitness()
      babym2.fitness()  
      dnas.append(baby1)
      dnas.append(baby2)  
      dnas.append(babym1)
      dnas.append(babym2)  
        
      
dnas=[] 
mutationrate=0.1
population=400
mum=[]
dad=[]  
#initial population 
for i in range(population):  
   dnas.append(Dna())
   dnas[i].randomdna()
   dnas[i].fitness()
generation=0

for i in range(10000):      
  newpop = Generation()
  fittestmum=max(dnas, key=lambda dna: dna.fit)
  dnas.remove(fittestmum)
  fittestdad=max(dnas, key=lambda dna: dna.fit)
  dnas.remove(fittestdad)
  for parents in range(population/20-1):
     mum.append(newpop.choose(dnas))
     dad.append(newpop.choose(dnas))  

  del dnas[:] 
  dnas.append(fittestmum)
  dnas.append(fittestdad)
  newpop.breed(fittestmum.dna,fittestdad.dna)
  for parents in range(population/20-1):
    newpop.breed(mum[parents].dna,dad[parents].dna)
  if i % 10 == 0:
     print max(dnas, key=lambda dna: dna.fit).fit, 'generation :', generation
  generation+=1
a=max(dnas, key=lambda dna: dna.fit)
b=score.score(a.dna[0],a.dna[1],a.dna[2],a.dna[3])
print b,a.dna
#Ain = raw_input("Enter core inlet area: ")
Thrust=1.5*b[3]
print Thrust
#for baby in dnas:
 # print baby.fit
