from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient

import random
import math


class Client(HeadlessClient):
    def init(self):
        self.name = 'NYKD - 54'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        if heroes:
            x, y = heroes[0].position

            for m in heroes:
                if hero.level > m.level:
                    if hero.health > m.health:
                        self.accelerate_towards(x, y)
                        self.shoot_at(*heroes[0].position)
                    elif hero.health <= m.health:
                        self.accelerate_towards(-x, y)
                        self.shoot_at(*heroes[0].position)
                elif hero.level <= m.level:
                    self.accelerate_towards(-x, -y)
                    self.shoot_at(*heroes[0].position)

        elif polygons:
            j, k = polygons[0].position
            o, p = hero.position
            polygonsdict = {}
            polygonsdistance = []

            for n in polygons:
                distance = (((o - j)**2 + (p - k)**2))**0.5
                polygonsdict[distance] = (j, k)
                polygonsdistance.append(distance)
            polygonsdistance.sort()
            target, name = polygonsdict[polygonsdistance[0]]
            self.shoot_at(j, k)
            self.accelerate_towards(j, k)

        elif bullets:
            a, b = bullets[0].position
            o, p = hero.position
            bulletsdict = {}
            bulletsdistances = []

            for n in bullets:
                distances = (((o - a)**2 + (p - b)**2))**0.5
                bulletsdict[distances] = (a, b)
                bulletsdistances.append(distances)
            bulletsdistances.sort()
            target, name = bulletsdict[bulletsdistances[0]]
            self.shoot_at(a, b)
            self.accelerate_towards(-a, b)

        #技能點
        if 57 > hero.skill_points:
            self.level_up(Ability.Reload)
            if 57 > hero.skill_points:
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
                                        self.level_up(
                                            Ability.BulletPenetration)


Client.main()
