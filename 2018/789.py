from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '789'

    def action(self, hero, heroes, polygons, bullets):
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
        dis = []
        for p in polygons:
            d = distance(p.position, hero.position)
            if p.health >= 150:
                d = 99999999999
        dis.append(d)
        m = min(dis)
        i = dis.index(m)
        self.shoot_at(*polygons[i].position)
        self.accelerate_towards(*polygons[i].position)

        attack = [hh for hh in heroes if hh.health < 700]
        if len(attack) > 0 and polygons[i].health > 800:
            self.accelerate_towards(*attack[0].position)
            self.shoot_at(*attack[0].position)
        else:
            self.shoot_at(*polygons[i].position)
            self.accelerate_towards(*polygons[i].position)

        if hero:
            self.level_up(Ability.HealthRegen)
            if hero:
                self.level_up(Ability.Reload)
                if hero:
                    self.level_up(Ability.BulletSpeed)


Client.main()
