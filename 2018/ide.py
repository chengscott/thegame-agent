from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'ide'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        a, b = hero.position
        ch = []
        if hero.level >= 15:
            if heroes:
                for i in range(len(heroes)):
                    x, y = heroes[i].position
                    self.shoot_at(x, y)
            else:
                for i1 in range(len(polygons)):
                    x1, y1 = polygons[i1].position
                    r1 = (x1 - a)**2 + (y1 - b)**2
                    ch.append(r1)
                d1 = min(ch)
                i1 = ch.index(d1)
                x1, y1 = polygons[i1].position
                self.shoot_at(x1, y1)
                if polygons[i1].edges != 5:
                    self.accelerate_towards(x1, y1)
        else:
            for i1 in range(len(polygons)):
                x1, y1 = polygons[i1].position
                r1 = (x1 - a)**2 + (y1 - b)**2
                ch.append(r1)
            d1 = min(ch)
            i1 = ch.index(d1)
            x1, y1 = polygons[i1].position
            self.shoot_at(x1, y1)
            if polygons[i1].edges != 5:
                self.accelerate_towards(x1, y1)

        if hero.skill_points != 0:
            for isk in range(3):
                self.level_up(6)
            for jsk in range(5):
                self.level_up(0)
            self.level_up(2)
            self.level_up(2)
            for jsk in range(3):
                self.level_up(5)
            for ksk in range(100):
                self.level_up(0)
                self.level_up(0)
                self.level_up(0)
                self.level_up(5)
                self.level_up(6)
                self.level_up(5)
                self.level_up(2)
                self.level_up(2)
                self.level_up(5)


Client.main()
