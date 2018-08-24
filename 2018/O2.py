from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import math


class Client(HeadlessClient):
    def init(self):
        self.name = 'O2'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        def distance(p1, p2):
            (x1, y1), (x2, y2) = (p1, p2)
            return (x1 - x2)**2 + (y1 - y2)**2

        if hero.health < 50:
            self.accelerate_towards(0.001, -1)

        dis = []
        if polygons:
            for h in polygons:
                sh = distance(h.position, hero.position)
                dis.append(sh)
            att = min(dis)
            i = dis.index(att)
            self.shoot_at(*polygons[i].position)
            x, y = hero.position
            xh, yh = polygons[i].position
            if distance(hero.position, polygons[i].position) > 50000:
                self.accelerate_towards(*polygons[i].position)
            elif hero.abilities.bullet_speed.level >= 6 and distance(
                    hero.position, polygons[i]
                    .position) < 50000 and hero.health_regen_level > 50:
                self.accelerate_towards(*polygons[i].position)
            else:
                self.accelerate(-math.atan2(y - yh, x - xh))

        dist = []
        if heroes:
            for k in heroes:
                sk = distance(k.position, hero.position)
                dist.append(sk)
            atta = min(dist)
            t = dist.index(atta)
            self.shoot_at(*heroes[t].position)
            x, y = hero.position
            xt, yt = heroes[t].position
            if (distance(hero.position, heroes[t].position) > 50000
                    and hero.health_regen_level > 50
                ) or hero.level > heroes[t].level:
                self.accelerate_towards(*heroes[t].position)
            elif hero.abilities.max_health.level < heroes[t].abilities.max_health.level:
                self.accelerate(-math.atan2(0.001, 1))
            elif hero.health > heroes[t].health:
                self.accelerate_towards(*heroes[t].position)

        if hero.skill_points != 0:
            self.level_up(7)
            self.level_up(3)
            self.level_up(0)
            self.level_up(6)
            self.level_up(6)
            self.level_up(7)
            self.level_up(1)
            self.level_up(2)
            self.level_up(4)
            self.level_up(5)
