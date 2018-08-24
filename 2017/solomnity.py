from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random
import math


class Client(HeadlessClient):
    def init(self):
        self.name = 'solomnity'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        for n in range(0, 2):
            if hero.health_regen_level < 2:
                self.level_up(Ability.HealthRegen)

        for i in range(0, 8):  ##點技能
            self.level_up(Ability.Reload)
            self.level_up(Ability.BulletPenetration)
            self.level_up(Ability.BulletDamage)
            self.level_up(Ability.MaxHealth)
            self.level_up(Ability.BulletSpeed)
            self.level_up(Ability.MovementSpeed)
            self.level_up(Ability.HealthRegen)
            self.level_up(Ability.BodyDamage)

        ##flag=0
        if hero.health > 0.7 * hero.max_health:
            self.accelerate(1.5 * 3.14)
        s = 0
        heroes_level = []
        dist = []  ##  與方塊的距離
        ##distance=(((hero.position[0])-(polygons[0].position[0]))**2+((hero.position[1])-(polygons[0].position[1]))**2)**0.5
        #dist_min_polygons=polygons[0]
        if len(heroes) > 0:
            for m in range(0, len(heroes)):
                heroes_level.append(heroes[m].level)
                heroes_levelmin_value = min(heroes_level)
                heroes_levelmax_value = max(heroes_level)
            for s in range(0, len(heroes)):
                if heroes_levelmin_value == heroes[s].level:
                    heroes_levelmin = heroes[s]
                    break
            for v in range(0, len(heroes)):
                if heroes_levelmax_value == heroes[v].level:
                    heroes_levelmax = heroes[v]
                    break

            x_min = hero.position[0] - heroes_levelmin.position[0]
            y_min = hero.position[1] - heroes_levelmin.position[1]
            if x_min != 0:
                tan_min = math.tan(y_min / x_min)
            x_max = hero.position[0] - heroes_levelmax.position[0]
            y_max = hero.position[1] - heroes_levelmax.position[1]
            if x_max != 0:
                tan_max = math.tan(y_max / x_max)

        #for each in range(0,len(polygons)-1):##生命比例最低的方塊
        #if  len(polygons)>1:
        #if polygons[each].health/polygons[each].max_health>polygons[each+1].health/polygons[each+1].max_health:
        #polygons_healthmin=polygons[each+1]
        #elif len(polygons)==1:
        #polygons_healthmin=polygons[each]
        #if len(polygons)>0:
        #for l in range(0,len(polygons)):##距離最近的方塊的距離
        #dist.append((((hero.position[0])-(polygons[l].position[0]))**2+((hero.position[1])-(polygons[l].position[1]))**2)**0.5)
        #dist_min=min(dist)
        #for j in range(0,len(polygons)):##找出距離最近的方塊
        #if dist_min==(((hero.position[0])-(polygons[j].position[0]))**2+((hero.position[1])-(polygons[j].position[1]))**2)**0.5:
        #dist_min_polygons=polygons[j]
        #else:
        #dist_min_polygons=polygons[0]

        ##if dist_min_polygons and dist_min<3000: ##and flag==0:
        ##x=hero.position.x-dist_min_polygons.position.x
        ##y=hero.position.y-dist_min_polygons.position.y
        ##tan=math.tan(y/x)
        ##self.accelerate(tan)


##防碰撞系統
#if heroes and  heroes[0].level<hero.level :##and hero.health>0.3*hero.max_health:
##追擊機制
##flag=1## 無視碰撞
#self.shoot_at(*heroes[0].position)
#self.accelerate_towards(*heroes_levelmin.position)
#if heroes and heroes[0].level>hero.level :##or hero.health<0.3*hero.max_health):
#self.shoot_at(*heroes[0].position)

#self.accelerate(tan_max)
#self.accelerate(direction)
#self.shoot_at(*heroes_levelmax.position)

#if heroes and hero.level<20: ##and heroes[0].health/heroes[0].max_health<0.4:
##低等級碰運氣
##flag=1##無視碰撞
#self.shoot_at(*heroes[0].position)
#self.accelerate_towards(*heroes[0].position)
#if heroes and hero.level>20 :##or heroes[0].health/heroes[0].max_health>0.4):
#self.shoot_at(*heroes[0].position)
#self.accelerate_towards(*heroes[0].position)
#if heroes and heroes[0].health<hero.health:
#self.shoot_at(*heroes[0].position)
#self.accelerate_towards(*heroes[0].position)
#if heroes and heroes[0].health>hero.health:
#self.shoot_at(*heroes[0].position)
##self.accelerate_towards(*heroes[0].position)

        if heroes:
            self.shoot_at(*heroes[0].position)
            #self.accelerate_towards(*heroes[0].position)
        #if heroes and hero.health<0.2*hero.max_health:
        #self.shoot_at(*heroes[0].position)
        #self.accelerate_towards(-heroes[0].position[0],-heroes[0].position[1])

        if polygons and not heroes:
            self.shoot_at(*polygons[len(polygons) - 1].position)
        #if dist_min_polygons and not heroes: ##eat polygons
        #self.shoot_at(*dist_min_polygons.position)
        #if hero.health>0.8*hero.max_health:
        #self.accelerate_towards(*dist_min_polygons.position)

        ##elif polygons_healthmin :
        ##if distance>100 :
        ##吃方塊
        ##flag=1
        ##self.shoot_at(*polygons_healthmin.position)
        ##self.accelerate_towards(*polygons_healthmin.position)
        ##if dist_min<300:
        ##flag=0
        ##elif polygons_healthmin and distance<100:
        ##防止與方塊碰撞
        ##flag=0
        ##self.shoot_at(*polygons_healthmin.position)
        ##x=hero.position.x-polygons_healthmin.position.x
        ##y=hero.position.y-polygons_healthmin.position.y
        ##tan=math.tan(y/x)
        ##self.accelerate(tan)
        #else:
        ##防沒事可做
        ##flag=0
        #self.accelerate(3.14)

Client.main()
