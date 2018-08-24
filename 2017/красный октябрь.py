import math
from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'красный октябрь'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        pentagons = pentagon(polygons)
        #movement
        if len(pentagons) != 0:
            if hero.health > hero.health / 4:
                for i in range(0, len(pentagons)):
                    if distance(
                            pentagons[i],
                            hero) == pentagons[i].radius + hero.radius + 90:
                        self.accelerate_towards(-pentagon.position[0],
                                                -pentagon.position[1])
                        if len(heroes) != 0:
                            mindisH = minDistHero(hero, heroes)
                            if distance(hero, mindisH) < 10:
                                self.accelerate_towards(
                                    -mindisH.position[0], -mindisH.position[1])
                    else:
                        self.accelerate_towards(
                            *minhealthpoly(polygons).position)
            else:
                self.accelerate_towards(*hero.position)
        else:
            self.accelerate_towards(*minhealthpoly(polygons).position)

        if hero.level < 16:
            self.shoot_at(*minhealthpoly(polygons).position)
        else:
            if len(heroes) != 0:
                self.shoot_at(*minHealthHero(heroes).position)
            else:
                self.shoot_at(*minhealthpoly(polygons).position)
        #elif len(bullets) != 0:
        #if distance(closebul(hero,bullets),hero) < 10:
        #self.shoot_at(*closebul(hero,bullets).position)
        if hero.health_regen_level < 8:
            self.level_up(Ability.HealthRegen)
        elif hero.max_health_level < 8:
            self.level_up(Ability.MaxHealth)
        elif hero.bullet_damage_level < 8:
            self.level_up(Ability.BulletDamage)
        elif hero.reload_level < 8:
            self.level_up(Ability.Reload)
        elif hero.bullet_speed_level < 5:
            self.level_up(Ability.BulletSpeed)


def distance(object1, object2):
    return math.sqrt((object1.position[0] - object2.position[0])**2 +
                     (object1.position[1] - object2.position[1])**2)


def center(polygons):
    res = ()
    xt = 0
    yt = 0
    for i in range(0, len(polygons)):
        xt = xt + polygons[i][0]
        yt = yt + polyhons[i][1]
    res.append(xt / len(polygons))
    res.append(yt / len(polygons))
    return res


def minhealthpoly(polygons):
    min = polygons[0]
    for i in range(0, len(polygons)):
        if polygons[i].health < min.health:
            min = polygons[i]
    return min


def minHealthHero(heroes):
    r = heroes[0]
    for i in range(0, len(heroes)):
        if r.health > heroes[i].health:
            r = heroes[i]
    return r


def closebul(hero, bullets):
    r = bullets[0]
    for i in range(0, len(bullets)):
        if distance(r, hero) > distance(bullets[i], hero):
            r = bullets[i]
    return r


def pentagon(polygons):
    pent = []
    for i in range(0, len(polygons)):
        if polygons[i].health == 300:
            pent.append(polygons[i])
    return (pent)


def minDistHero(hero, heroes):
    r = heroes[0]
    for i in range(0, len(heroes)):
        if distance(hero, heroes[i]) < distance(hero, r):
            r = heroes[i]
    return r
