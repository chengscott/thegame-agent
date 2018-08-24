from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import math


class Client(HeadlessClient):
    def init(self):
        self.name = 'XD'  # 設定名稱

    def action(self, hero, heroes, bullets, polygons):
        def distance(p1, p2):
            (x1, y1), (x2, y2) = p1, p2
            return (x1 - x2)**2 + (y1 - y2)**2

        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        hx, hy = hero.position
        dis = []
        if polygons:
            for p in polygons:
                px, py = p.position
                dp = distance(p.position, hero.position)
                dis.append(dp)
        # dis
            dp = min(dis)
            i = dis.index(dp)
            self.shoot_at(*polygons[i].position)
            self.accelerate(-math.atan2(hy - py, hx - px))
            self.accelerate(3.14 / 2)
        else:
            self.accelerate_towards(2500, 2000)

        dist = []
        if heroes:

            for h in heroes:
                hsx, hsy = h.position
                dh = distance(h.position, hero.position)
                dist.append(dh)

        if dist:
            dh = min(dist)
            hsx, hsy = h.position
            self.shoot_at(*h.position)
            self.accelerate(-math.atan2(hy - hsy, hx - hsx))

        if hero.skill_points != 0:
            self.level_up(3)
            self.level_up(3)
            self.level_up(6)
            self.level_up(6)
            self.level_up(7)
            self.level_up(1)
            self.level_up(2)
            self.level_up(4)
            self.level_up(5)
            self.level_up(0)


Client.main()
