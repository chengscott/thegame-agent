from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient

import random
import math

class Client(GuiClient):

    def init(self):
        self.name = 'J chou mu tan' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)


        if heroes:

            o, p  = hero.position
            heroesdict = {}
            heroesdistance = []

            for m in heroes:
                c ,d  = m.position
                distance = (((o - c) ** 2 + (p - d) ** 2)) ** 0.5
                heroesdict[distance] = (c, d) , m
                heroesdistance.append(distance)
            heroesdistance.sort()
            htarget, hname = heroesdict[heroesdistance[0]]


            if hero.level > hname.level:
                if hero.health > hname.health:
                    self.accelerate_towards(c, d)
                    self.shoot_at(*hname.position)
                elif hero.health <= hname.health:
                    self.accelerate_towards(-c, d)
                    self.shoot_at(*hname.position)
            elif hero.level <=  m.level:
                self.accelerate_towards(-c, -d)
                self.shoot_at(*hname.position)


        elif polygons:

            o, p  = hero.position
            polygonsdict = {}
            polygonsdistance = []

            for n in polygons:
                j, k  = n.position
                distance = (((o - j) ** 2 + (p - k) ** 2)) ** 0.5
                polygonsdict[distance] = (j, k) , n
                polygonsdistance.append(distance)
            polygonsdistance.sort()
            target, name = polygonsdict[polygonsdistance[0]]
            xtarget , ytarget = target
            if hero.health > name.health:
                self.accelerate_towards(xtarget , ytarget)
                self.shoot_at(*name.position)
            else :
                self.accelerate_towards(-xtarget , -ytarget)
                self.shoot_at(*name.position)



        elif bullets:
            a, b = bullets[0].position
            o, p  = hero.position
            bulletsdict = {}
            bulletsdistances = []

            for n in bullets:
                distances = (((o - a) ** 2 + (p - b) ** 2)) ** 0.5
                bulletsdict[distances] = (a, b)
                bulletsdistances.append(distances)
            bulletsdistances.sort()
            target, name = bulletsdict[bulletsdistances[0]]
#            self.shoot_at(a, b)
            self.accelerate_towards(-a, b)

        #技能點
        if  65 > hero.skill_points:
            self.level_up(Ability.Reload)
            if  57 > hero.skill_points:
                self.level_up(Ability.HealthRegen)
                if 49 > hero.skill_points:
                    self.level_up(Ability.BulletDamage)
                    if 41 > hero.skill_points:
                        self.level_up(Ability.BulletSpeed)
                        if 33 > hero.skill_points:
                            self.level_up(Ability.MaxHealth)
                            if 25 > hero.skill_points:
                                self.level_up(Ability.BodyDamage)
                                if 17 > hero.skill_points:
                                    self.level_up(Ability.MovementSpeed)
                                    if 9 > hero.skill_points:
                                        self.level_up(Ability.BulletPenetration)




Client.main()