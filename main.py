from glob import magic_check

from classes.game import Person,bcolors
from classes.magic import Magic
from classes.inventory import Item





fire=Magic("Fire",10,100,"black")
thunder=Magic("Thunder",10,100,"black")
blizzard=Magic("Blizzard",10,100,"black")
meteor=Magic("Meteor",20,200,"black")
quake=Magic("Quake",14,140,"black")

#create white magic
cure=Magic("Cure",12,120,"white")
cura=Magic("Cura",18,200,"white")

#create some Items
potion=Item("Potion","potion","Heals 50 HP",50)
hipotion=Item("Hi-Potion","potion","Heals 100 HP",100)
superpotion=Item("Super Potion","potion","Heals for 500 HP",500)
elixer=Item("Elixer","elixer","Fully restore HP/MP of one party member",9999)
hielixer=Item("MegaElixer","elixer","Fully Restore party's HP/MP",9999)
grenade=Item("grenade","attack","Deals 500 damage",500)

player_items=[{"item":potion,"quantity":15},{"item":hipotion,"quantity":5},{"item":superpotion,"quantity":5},{"item":elixer,"quantity":5},{"item":hielixer,"quantity":2},{"item":grenade,"quantity":5}]

player1=Person("Rishi",460,65,60,34,[fire,thunder,blizzard,meteor,cura,cure],player_items)
player2=Person("Raju",460,65,60,34,[fire,thunder,blizzard,meteor,cura,cure],player_items)
player3=Person("Shyam",460,65,60,34,[fire,thunder,blizzard,meteor,cura,cure],player_items)
enemy1=Person("octopus",1200,61,45,25,[],[])
enemy2=Person("imp",18250,65,30,12,[],[])
enemy3=Person("imp",1200,55,25,10,[],[])
enemies=[enemy1,enemy2,enemy3]

players=[player1,player2,player3]
running=True
i=0
print(bcolors.FAIL+bcolors.BOLD+ "An enemy Attack" + bcolors.ENDC)
while running:
       print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
       print("\n")
       for player in players:

              print(player.get_stats())
              print("\n")

       for player in players:

          player.choose_actions()
          choice=input("Choose Action:")
          index=int(choice)-1
          if index==0:
              dmg=player.generate_damage()
              enemy=player.choose_target(enemies)
              enemies[enemy].take_damage(dmg)
              print(enemies[enemy].name)
              print("You attacked for"+ enemies[enemy].name, "points of damage    Enemy HP:",enemies[enemy].get_hp())
              if enemies[enemy].get_hp()==0:
                  del enemies[enemy]
          elif index==1:
              player.choose_magic()
              magic_choice=int(input ("Choose Magic:"))-1
              if magic_choice==-1:
                     continue
              spell=player.magic[magic_choice]
              magic_dmg=spell.generate_dmg()
              current_mp=player.get_mp()
              if spell.cost>current_mp:
                     print(bcolors.FAIL + "\nNot enough MP\n" +bcolors.ENDC)
                     continue

              player.reduce_map(spell.cost)

              if spell.type=='white':
                     player.heal(magic_dmg)
                     print(bcolors.OKBLUE + "\n" +spell.name +"heals for",str(magic_dmg) + bcolors.ENDC)
              elif spell.type=="black":
                  enemy=player.choose_target(enemies)
                  enemies[enemy].take_damage(magic_dmg)
                  print(bcolors.OKBLUE + "\n" + spell.name +"deals", str(magic_dmg), "points of damage to" +enemies[enemy].name+bcolors.ENDC)
                  if enemies[enemy].get_hp()==):
                      del enemies[enemy]
          elif index==2:
              player.choose_item()
              item_choice=int(input("choose item:"))-1

              if item_choice==-1:
                     continue

              item=player.items[item_choice]["item"]
              if player.items[item_choice]["quantity"]==0:
                     print(bcolors.FAIL+"\n"+"None left...."+bcolors.ENDC)
                     continue
              player.items[item_choice]["quantity"]-=1

              if item.type=="potion":
                     player.heal(item.prop)
                     print(bcolors.OKGREEN + "\n" +item.name + "heals for ",str(item.prop),"HP",bcolors.ENDC)
              elif item.type=="elixer":
                     player.hp=player.maxhp
                     player.mp=player.maxmp
                     print(bcolors.OKGREEN + "\n" + item.name +"fully restore hp/mp" + bcolors.ENDC)
              elif item.type=="attack":
                     enemy=player.choose_target(enemies)
                     enemies[enemy].take_damage(item.prop)
                     print(bcolors.FAIL + "\n" +item.name +"deals",str(item.prop),"points of damage"+bcolors.ENDC)
                     if enemies[enemy].get_hp()==0:
                         del enemies[enemy]



       enemy_choice=1
       enemy_dmg=enemy[0].generate_damage()
       player1.take_damage(enemy_dmg)
       defeated_enemies=0
       defeated_players=0
       for enemy in enemies:
           if enemy.get_hp()==0:
               defeated_enemies +=1

        for player in players:
         if player.get_hp()==0:
           defeated_players +=1

        if defeated_enemies==2:
            print(bcolors.OKBLUE + "you win" + bcolors.ENDC)
            running = False

        elif defeated_players==2:
            print(bcolors.WARNING + "enemy won" + bcolors.ENDC)
            running = False


       print("enemy attacked for", enemy_dmg, "points of damage    Player HP:", player.get_hp())
       print("...............................................................................")
       print(bcolors.WARNING+"EnemyHP:",str(enemy.get_hp()),"/", str(enemy.get_max_hp())+bcolors.ENDC+"\n")




