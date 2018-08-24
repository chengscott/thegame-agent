from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
s = 0


class Client(HeadlessClient):
    def init(self):
        self.name = 'Halloween'  # 設定名稱
        self.s = 0
        self.gg = 10000
        self.ap = 0

    def action(self, hero, heroes, polygons, bullets):

        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        self.gg = 10000
        k = 0
        l = 0
        h = 0
        z = 0
        self.s = 0
        self.ap = 0
        x, y = hero.position

        def dist(a, b):
            return ((a - x)**2 + (b - y)**2)**0.5

        def strong():
            for i in range(len(heroes)):
                if hero.level - heroes[i].level <= 0 and dist(
                        *heroes[i].position) < 1500:
                    if self.gg >= dist(*heroes[i].position):
                        self.gg = dist(*heroes[i].position)
                        self.s = i
            if self.s == 0:
                return False
            else:
                return True

        self.gg = 10000

        def kill():
            for i in range(len(heroes)):
                if heroes[i].health / heroes[i].abilities.max_health.value < 0.1 and dist(
                        *heroes[i].position) < 300:
                    if self.gg > (heroes[i].health /
                                  heroes[i].abilities.max_health.value):
                        self.gg = (heroes[i].health /
                                   heroes[i].abilities.max_health.value)
                        self.ap = i
            if self.ap == 0:
                return False
            else:
                return True

        if hero.abilities.health_regen.level <= 2:
            self.level_up(Ability.HealthRegen)
        if hero.abilities.movement_speed.level <= 8:
            for i in range(8):
                self.level_up(Ability.MovementSpeed)
        if hero.abilities.reload.level <= 3:
            for i in range(4):
                self.level_up(Ability.Reload)
                if hero.abilities.reload.level >= 3:
                    break
        if hero.abilities.max_health.level <= 2:
            for i in range(2):
                self.level_up(Ability.MaxHealth)
                if hero.abilities.max_health.level >= 3:
                    break
        if hero.abilities.health_regen.level <= 6:
            for i in range(2):
                self.level_up(Ability.HealthRegen)
        u = 10000
        k = 0
        l = 0
        h = 0
        z = 0
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.Reload)
        self.level_up(Ability.BulletSpeed)
        self.level_up(Ability.BulletDamage)
        self.level_up(Ability.BulletPenetration)
        self.level_up(Ability.BodyDamage)
        if heroes:
            for i in range(len(heroes)):
                if (u > dist(*heroes[i].position)):
                    u = dist(*heroes[i].position)
                    k = i
            u = 10000
            for i in range(len(heroes)):
                if u > heroes[i].level:
                    u = heroes[i].level
                    l = i
        u = 10000
        if polygons:
            for i in range(len(polygons)):
                if (u > dist(*polygons[i].position)):
                    u = dist(*polygons[i].position)
                    h = i

        u = 10000
        if bullets:
            for i in range(len(bullets)):

                if (u > dist(*bullets[i].position)):
                    u = dist(*bullets[i].position)
                    z = i
        if heroes:
            c, d = heroes[k].position  #最近
            v, t = heroes[l].position  #最弱
            o, p = heroes[self.s].position  #最強的最近
            f, g = heroes[self.ap].position  #血小於10%
        if polygons:
            q, w = polygons[h].position  #最近
        if bullets:
            r, t = bullets[z].position  #

        if heroes and kill():
            self.accelerate_towards(f, g)
            self.shoot_at(*heroes[self.ap].position)

        elif x <= 100 or y <= 100 or x >= 4900 or y >= 3900:
            self.accelerate_towards(2500, 2000)
            if polygons:
                self.shoot_at(*polygons[h].position)
        elif heroes and dist(
                *heroes[l].position
        ) <= 300 and hero.level - heroes[l].level >= 2 and hero.health / hero.abilities.max_health.value >= 0.4:
            if dist(*heroes[l].position) > 300:
                self.accelerate_towards(v, t)
                self.shoot_at(*heroes[l].position)
            else:
                self.accelerate_towards(2 * x - v, 2 * y - t)
                self.shoot_at(*heroes[l].position)

        elif heroes and strong():
            if polygons and dist(*polygons[h].position) < dist(
                    *heroes[self.s].position):
                self.shoot_at(*heroes[self.s].position)
                self.accelerate_towards(2 * x - o, 2 * y - p)
            elif polygons:
                self.shoot_at(*polygons[h].position)
                self.accelerate_towards(2 * x - o, 2 * y - p)
            else:
                self.shoot_at(*heroes[self.s].position)
                self.accelerate_towards(2 * x - o, 2 * y - p)

        elif polygons and dist(*polygons[h].position) < 50:
            self.accelerate_towards(x + (x - q) * 0.3, y + (y - q) * 0.3)
            self.shoot_at(*polygons[h].position)

        elif bullets and dist(*bullets[z].position) < 60:
            self.accelerate_towards(x + (y - t) * 0.7, y - (x - r) * 0.7)
            if polygons:
                self.shoot_at(*polygons[h].position)

        #elif heroes and polygons and hero.health/hero.abilities.max_health.value<=0.4 and  dist(*heroes[k].position)>=800 :
        #self.shoot_at(*polygons[h].position)
        #elif heroes and hero.health/hero.abilities.max_health.value<=0.4 and  dist(*heroes[k].position)<=800 :
        #self.shoot_at(*heroes[k].position)
        #self.accelerate_towards(2*x-c+100,2*y-d)

        elif polygons and dist(*polygons[h].position) < 800:
            if dist(*polygons[h].position) > 500:
                self.accelerate_towards(q - 60, w - 60)
                self.shoot_at(*polygons[h].position)
            else:
                self.accelerate_towards(2 * x - q, 2 * y - w)
                self.shoot_at(*polygons[h].position)
        elif not polygons or dist(*polygons[h].position) > 800:
            self.accelerate_towards(x + 100, y + 100)
            self.accelerate_towards(x - 200, y - 100)


Client.main()
