#!/usr/local/bin/python
import random as r
def score(Bypass,pf,pfi,pic):
  M0=0.8
  Pa=101325
  density=1.2
  Ta=273.15+15
  gamma=1.4
  R=287
#  Ain=3.14*Rin**2
  U0=M0*(gamma*R*Ta)**0.5
  mcore=density*U0
  mtotal=mcore*(Bypass+1)
  Cpc=1004.5
  Cpt=1153
  pch=10.5
  Qhv=43200000
  T04=1560
  pb=0.995
#T02=T0a - inlet total temperature
  T02=Ta*(1+(gamma-1)/2*M0**2)

#fan temperature ratio - pf = fan pressure ratio
  tf=1+(pf**((gamma-1)/gamma)-1)
  tfi=1+(pfi**((gamma-1)/gamma)-1)
  tic=1+(pic**((gamma-1)/gamma)-1)
#diffuser total pressure ratio  
  pd=(T02/Ta)**(gamma/(gamma-1))
 # print 'Inlet:',Ta,'Total temp:',T02,'Total Press:',Pa*pd
#after fan total temp
  T08=tf*T02
 # print 'Bypass Temp:',T08
  T02a=tfi*T02
  #print 'Core After Fan:',T02a,'K, ',Pa*pd*pfi,'Pa'
#compressor total temperature ratio
  tch=1+(pch**((gamma-1)/gamma)-1)
  T03=tch*tic*T02a
  P03=Pa*pd*pfi*pic*pch
 # print 'After Comp Total temp:', T03, 'Total press:',P03
#combustor
  f=(Cpt*T04-Cpc*T03)/Qhv
  #f=((T04/T03)-1)/((Qhv/(Cpc*T03))-(T04/T03))
 # print 'Temp:',T04,'Press:',P03*pb,'Fuel flow:',f
#HP Turbine
  tth=1-((T02a*(tch-1)/T04)*(Cpc/Cpt))
  T04b=T04*tth
  pth=(tth)**(gamma/(gamma-1))
#LP Turbine
  ttl=1-((Bypass*T02*(tf-1)+T02a*(tic-1)+T02*(tfi-1))/T04b)*(Cpc/Cpt)
  if ttl < 0:
     return [0]
  #TurbineTratio=1-((T08/T02)*((T03/T08)-1)+(Bypass+1)*((T08/T02)-1))/((1+f)*(T04/T02))
  T05=T04b*ttl
  #T05=TurbineTratio*T04
 # print ttl*tth, TurbineTratio
  ptl=(ttl)**(gamma/(gamma-1))
  pth=(tth)**(gamma/(gamma-1))
  pt=(T05/T04)**(gamma/(gamma-1))
  P05=Pa*pd*pfi*pic*pch*pb*pt
 # print 'Temp:',T05,'Press:',P05, 'LPT P ratio:',ptl,'HPT:',pth, 'Total P decrease:',pt

  p0nh=pt*pic*pch*pfi*pd
  p0nc=pf*pd
  if (1/p0nh)**((gamma-1)/(gamma))>1:
     return [0]
  if (2*Cpc*T08*(1-(1/p0nc)**((gamma-1)/(gamma))))<0:
     return [0]
  Ueh=(2*Cpt*T05*(1-(1/p0nh)**((gamma-1)/(gamma))))**0.5
  Uec=(2*Cpc*T08*(1-(1/p0nc)**((gamma-1)/(gamma))))**0.5
  
  GT=((1+f)*Ueh+Bypass*Uec)*mcore
  RDrag=(1+Bypass)*U0*mcore
  T=GT-RDrag
 # print 'Net Thrust:', T,'Hot stream:',Ueh,'Bypass:',Uec
  SpT=T/mtotal
  TSFC=mcore*f/T
  SFC=mcore*f/mtotal
  eff=U0*T/(mcore*f*Qhv)
#  print 'f:',f,'TSFC:',TSFC*3600,'SpFuel:',SFC,'Eff:',eff,'SpThrust:',SpT,'GThrust:',GT,'Thrust:',T,'Core mass:',mcore
  return [T*eff/TSFC-10*ttl,Ueh,Uec,T,f,TSFC]




