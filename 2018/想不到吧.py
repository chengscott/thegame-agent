from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '想不到吧'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        if hero.level > 1:
            self.accelerate_towards(300, 400)

        if 8 > hero.level > 1:
            self.level_up(Ability.HealthRegen)

        if 16 > hero.level > 8:
            self.level_up(Ability.MovementSpeed)

        if 24 > hero.level > 16:
            self.level_up(Ability.Reload)

        if 30 > hero.level > 24:
            self.level_up(Ability.BulletSpeed)

        if 35 > hero.level > 30:
            self.level_up(Ability.BulletPenetration)
        if 40 > hero.level > 35:
            self.level_up(Ability.BulletDamage)

        if polygons:
            x, y = polygons[0].position

            for j in polygons:
                polygonsdict = {}
                polygonsdistance = []
            for i in polygons:
                x1, y1 = i.position
                distance = (((x - x1)**2 + (y - y1)**2))**0.5
                polygonsdict[distance] = (x1, y1), i
                polygonsdistance.append(distance)
            polygonsdistance.sort()
            target, name = polygonsdict[polygonsdistance[0]]
            xtarget, ytarget = target
            self.accelerate_towards(xtarget, ytarget)
            self.shoot_at(xtarget, ytarget)
            if hero.health < name.health:
                self.accelerate_towards(-abs(x - xtarget), -abs(y - ytarget))
                self.shoot_at(x, y)

        if heroes:
            a, b = heroes[0].position
            for i in heroes:
                if i.health > hero.health:
                    self.accelerate_towards(-a, -b)
                    self.shoot_at(a, b)
                else:
                    self.shoot_at(a, b)


Client.main()
