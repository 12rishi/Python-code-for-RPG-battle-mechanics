import random
from .magic import  Magic

class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[93m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp=hp
        self.hp=hp
        self.mp=mp
        self.maxmp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.items=items
        self.actions=["Attack","Magic","Items"]
        self.name=name

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    # def generate_spell_damage(self,i):
    #     mgl=self.magic[i]["dmg"]-5
    #     mgh=self.magic[i]["dmg"]+5
    #     return random.randrange(mgl,mgh)
    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
    def get_hp(self):
        return self.hp
    def get_mp(self):
        return  self.mp
    def get_max_hp(self):
        return self.maxhp
    def get_max_mp(self):
        return self.maxmp
    def reduce_map(self,cost):
        self.mp-=cost

    # def get_spell_name(self,i):
    #     return self.magic[i]["name"]

    # def get_spell_mp_cost(self,i):
    #     return self.magic[i]["cost"]
    def choose_actions(self):
        i=1
        print("Actions:")
        for item in self.actions:
            print(str(i) + ":",item)
            i+=1

    def choose_magic(self):
        i=1
        print("Magic:")
        for spell in self.magic:
            print(str(i) + ":",spell.name,"cost:",str(spell.cost))
            i+=1

    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def choose_item(self):
        i=1

        print(bcolors.OKGREEN+bcolors.BOLD+"Items"+bcolors.ENDC)
        for item in self.items:
            print(str(i) + ".",item["item"].name, ":", item["item"].description," (x5) ")
            i+=1

    def choose_target(self,enemies):
        i=1
        print("\n"+bcolors.FAIL+bcolors.BOLD+" TARGET:"+bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print(" " + str(i) + " " + enemy.name)
                i += 1




        choice=int(input("choose target:"))-1
        return choice

    def get_stats(self):
        print("\n\n")
        print("NAME                                                  HP                                                                   MP")
        print("                                                  _________________________                                            __________")
        print( self.name+":"+str(self.hp)+"/"+str(self.maxhp)+" |█████████████████████████|   "+   str(self.mp)+"/"+str(self.maxmp)+"|██████████|")
