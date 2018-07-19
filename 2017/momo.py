from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero

from thegame.gui import GuiClient

import random





class Client(GuiClient):




    def init(self):

        self.name = 'momo' # 設定名稱




    def action(self, hero, heroes, polygons, bullets):

        print("I'm", hero)

        print(

            f'level: {hero.level}',

            f'experience: {hero.experience}/{hero.experience_to_level_up}'

        )

        print("I'm surrounded by these polygons:", polygons)

        print("I'm surrounded by these heroes:", heroes)

        print("I'm surrounded by these bullets:", bullets)

        print('-' * 79)


        if heroes:
            self.accelerate_towards(*heroes[0].position)
            self.shoot_at(*heroes[0].position)
        else:
            self.accelerate_towards(random.randint(0, 5000),random.randint(0,4000))
            self.shoot_at(*polygons[0].position)
        for i in range(200):
            self.level_up(Ability.BodyDamage)
            self.level_up(Ability.Reload)
            self.level_up(Ability.HealthRegen)
            self.level_up(Ability.BulletDamage)
            self.level_up(Ability.MaxHealth)
            self.level_up(Ability.BulletSpeed)






Client.main()