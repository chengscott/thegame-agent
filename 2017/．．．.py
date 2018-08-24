from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '．．．'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BulletSpeed)
        for a in range(0, len(bullets)):
            if ((bullets[a].position[0] - hero.position[0])**2 +
                (bullets[a].position[1] - hero.position[1])**2)**0.5 < 10:
                self.accelerate_towards(polygons[0].position[0],
                                        polygons[0].position[1])
                if ((bullets[a].position[0] - hero.position[0])**2 +
                    (bullets[a].position[1] - hero.position[1])**2)**0.5 >= 10:
                    break
            for i in range(0, len(heroes)):
                if ((heroes[i].position[0] - hero.position[0])**2 +
                    (heroes[i].position[1] - hero.position[1])**2)**0.5 < 10:
                    self.accelerate_towards(3000, 200)
                    self.shoot_at(*heroes[i].position)
                    if polygons:
                        self.shoot_at(*polygons[1].position)
                    if ((heroes[i].position[0] - hero.position[0])**2 +
                        (heroes[i].position[1] - hero.position[1])**
                            2)**0.5 >= 10:
                        break

                else:
                    self.accelerate_towards(2500, 200)
            else:
                self.accelerate_towards(2500, 200)
        self.shoot_at(polygons[2].position[0], polygons[2].position[1])
        self.level_up(Ability.MovementSpeed)
        self.level_up(Ability.BulletDamage)


Client.main()
