from vikingsClasses import *
import random


soldier_names = ["Mar","Tayna","Gabriel","Elena"]
n_soldiers = len(soldier_names)

war = War()

#Create 4 Vikings
for i in range(0, n_soldiers):
    war.addViking(Viking(soldier_names[random.randint(0, n_soldiers-1)],100,random.randint(0,100)))

#Create 4 Saxons
for i in range(0, n_soldiers):
    war.addSaxon(Saxon(100,random.randint(0,100)))

print("WELCOME TO THE WAR BETWEEN VIKINGS AND SAXONS!\n")

round = 0
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    
    result_attack_viking = war.vikingAttack()
    print(result_attack_viking)

    result_attack_saxon = war.saxonAttack()
    print(result_attack_saxon)

    print(f"round: {round} // Viking army: {len(war.vikingArmy)} warriors",f"and Saxon army: {len(war.saxonArmy)} warriors")

    war_status = war.showStatus()
    print(f"\n{war_status}\n")

    round += 1