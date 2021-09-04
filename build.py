from src.hardware import Tangent_Assembly, Assembly_Builder, DeadEnd_Assembly
from src.tower import TowerBuilder, Tangent, DeadEnd, IndividualTower, Tline

'''
Notes:
    - type of structure i.e.: lattice, tubular, etc..    
    - drawing number
    - The idea is you make XX number of tower types and YY assembly types
    and you can combine in them in various combinations
    - For example tangent is a class AD may be an instance of the 
    tangent class 
    - How do I create an tower number instance of the Tangent instance?
'''
ad_assembly = Assembly_Builder.createAssembly(Tangent_Assembly)
ad_assembly.shackle = '30k'
ad_assembly.clevis = 'y-clevis'
ad_assembly.clamp = 'basic'
ad_assembly.insulator = '139kV'

de_assembly = Assembly_Builder.createAssembly(DeadEnd_Assembly)
de_assembly.shackle = '60k'
de_assembly.clevis = 'y-clevis'
de_assembly.clamp = 'de_clamp'
de_assembly.insulator = '138kV'

tangent = TowerBuilder.createTower(Tangent, 'AD + 3')
deadend = TowerBuilder.createTower(DeadEnd, 'DD + 2')

t1 = IndividualTower(1, tangent)
t1.add_hardware(6, ad_assembly)

t2 = IndividualTower(2, deadend)
t2.add_hardware(6, de_assembly)

t3 = IndividualTower(tangent, 30)
t3.add_hardware(6, ad_assembly)
t3.towerNumber = 3 # update tower number after instantiation

t4 = IndividualTower(4, tangent)
t4.add_hardware(6, ad_assembly)

#for t in [t1,t2,t3,t4]:
#    for i in range(6):
#        print(f'tower number {t.towerNumber} hardware assembly: {i}')
#        print(t.hardware[i].clamp)
#        print(t.hardware[i].clevis)
#        print(t.hardware[i].insulator)
#        print(t.hardware[i].shackle)
        
line = Tline()
line.line_name = 'Eldorado'
line.addTower(t1)
line.addTower(t2)
print("\n")

print(line.line_name)
print(line.length())
print(line.display())



    
