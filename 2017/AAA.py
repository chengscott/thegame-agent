from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'AAA'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        for i in range(0, hero.level * 2):  #點技能
            if hero.abilities.health_regen.level <= 4:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.max_health.level <= 3:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.body_damage.level <= 3:
                self.level_up(Ability.BodyDamage)
            elif hero.abilities.reload.level <= 3:
                self.level_up(Ability.Reload)
            elif hero.abilities.movement_speed.level <= 2:
                self.level_up(Ability.MovementSpeed)
            elif hero.abilities.bullet_damage.level <= 3:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.bullet_speed.level <= 3:
                self.level_up(Ability.BulletSpeed)

            else:
                self.level_up(Ability.HealthRegen)
                self.level_up(Ability.MaxHealth)
                self.level_up(Ability.BodyDamage)
                self.level_up(Ability.Reload)
                self.level_up(Ability.BulletSpeed)
                self.level_up(Ability.BulletDamage)
                self.level_up(Ability.BulletPenetration)

        if hero.position[0] - hero.radius * 2 <= 0 or hero.position[0] + hero.radius * 2 >= 5000 or hero.position[1] - hero.radius * 2 <= 0 or hero.position[1] + hero.radius * 2 >= 4000:
            self.accelerate_towards(2500, 2000)

        if hero.abilities.health_regen.level <= 4 or hero.abilities.max_health.level <= 3 or hero.abilities.body_damage.level <= 4 or hero.abilities.reload.level <= 3:  #能力不足

            if heroes:
                for l in range(0, len(heroes)):
                    if (
                        (heroes[l].position[0] - hero.position[0])**2 +
                        (heroes[l].position[1] - hero.position[1])**2
                    )**0.5 <= (
                        (heroes[0].position[0] - hero.position[0])**2 +
                        (heroes[0].position[1] - hero.position[1])**2)**0.5:
                        heroes[0] = heroes[l]
                        #躲敵人
                        X2P3 = hero.position[0] + heroes[0].velocity[0]
                        X2N3 = hero.position[0] - heroes[0].velocity[0]
                        Y2P3 = hero.position[1] + heroes[0].velocity[1]
                        Y2N3 = hero.position[1] - heroes[0].velocity[1]
                        X43 = heroes[0].position[0] + heroes[0].velocity[0]
                        Y43 = heroes[0].position[1] + heroes[0].velocity[1]
                        if ((hero.position[0] - heroes[0].position[0])**2 +
                            (hero.position[1] - heroes[0].position[1])**2) < (
                                (X2P3 - X43)**2 + (Y2N3 - Y43)**2):
                            self.accelerate_towards(X2P3, Y2N3)
                        else:
                            self.accelerate_towards(X2N3, Y2P3)

            if polygons:
                for j in range(1, len(polygons)):
                    if ((polygons[j].position[0] - hero.position[0])**2 +
                        (polygons[j].position[1] - hero.position[1])**2) <= (
                            (polygons[0].position[0] - hero.position[0])**2 +
                            (polygons[0].position[1] - hero.position[1])**2):
                        polygons[0] = polygons[j]
                        self.shoot_at(*polygons[0].position)
                        X2P = hero.position[0] + polygons[0].velocity[0]
                        X2N = hero.position[0] - polygons[0].velocity[0]
                        Y2P = hero.position[1] + polygons[0].velocity[1]
                        Y2N = hero.position[1] - polygons[0].velocity[1]
                        X4 = polygons[0].position[0] + polygons[0].velocity[0]
                        Y4 = polygons[0].position[1] + polygons[0].velocity[1]
                        if ((hero.position[0] - polygons[0].position[0])**2 +
                            (hero.position[1] - polygons[0].position[1])**
                                2) < ((X2P - X4)**2 + (Y2N - Y4)**2):
                            self.accelerate_towards(X2P, Y2N)
                        else:
                            self.accelerate_towards(X2N, Y2P)

            if bullets:
                for i in range(1, len(bullets)):
                    if ((bullets[i].position[0] - hero.position[0])**2 +
                        (bullets[i].position[1] - hero.position[1])**2)**0.5 < (
                            (bullets[0].position[0] - hero.position[0])**2 +
                            (bullets[0].position[1] - hero.position[1])**
                            2)**0.5 and bullets[i].owner_id != self.name:
                        bullets[0] = bullets[i]
                        X2P2 = hero.position[0] + bullets[0].velocity[0]
                        X2N2 = hero.position[0] - bullets[0].velocity[0]
                        Y2P2 = hero.position[1] + bullets[0].velocity[1]
                        Y2N2 = hero.position[1] - bullets[0].velocity[1]
                        X42 = bullets[0].position[0] + bullets[0].velocity[0]
                        Y42 = bullets[0].position[1] + bullets[0].velocity[1]
                        if ((hero.position[0] - bullets[0].position[0])**2 +
                            (hero.position[1] - bullets[0].position[1])**2) < (
                                (X2P2 - X42)**2 + (Y2N2 - Y42)**2):
                            self.accelerate_towards(X2P2, Y2N2)
                        else:
                            self.accelerate_towards(X2N2, Y2P2)
        else:

            if heroes:
                for l in range(0, len(heroes)):
                    if (
                        (heroes[l].position[0] - hero.position[0])**2 +
                        (heroes[l].position[1] - hero.position[1])**2
                    )**0.5 <= (
                        (heroes[0].position[0] - hero.position[0])**2 +
                        (heroes[0].position[1] - hero.position[1])**2)**0.5:
                        heroes[0] = heroes[l]

                        if hero.health > hero.max_health / 2 and hero.health - heroes[0].body_damage * 20 > 0:
                            self.accelerate_towards(heroes[0].position[0],
                                                    heroes[0].position[1])
                            self.shoot_at(*heroes[0].position)
                        elif hero.health > hero.max_health / 2 and hero.health - heroes[0].body_damage * 20 < 0:
                            self.shoot_at(*heroes[0].position)
                            X2P3 = hero.position[0] + heroes[0].velocity[0]
                            X2N3 = hero.position[0] - heroes[0].velocity[0]
                            Y2P3 = hero.position[1] + heroes[0].velocity[1]
                            Y2N3 = hero.position[1] - heroes[0].velocity[1]
                            X43 = heroes[0].position[0] + heroes[0].velocity[0]
                            Y43 = heroes[0].position[1] + heroes[0].velocity[1]
                            if ((hero.position[0] - heroes[0].position[0])**2 +
                                (hero.position[1] - heroes[0].position[1])**
                                    2) < ((X2P3 - X43)**2 + (Y2N3 - Y43)**2):
                                self.accelerate_towards(X2P3, Y2N3)
                            else:
                                self.accelerate_towards(X2N3, Y2P3)

                        else:
                            X2P3 = hero.position[0] + heroes[0].velocity[0]
                            X2N3 = hero.position[0] - heroes[0].velocity[0]
                            Y2P3 = hero.position[1] + heroes[0].velocity[1]
                            Y2N3 = hero.position[1] - heroes[0].velocity[1]
                            X43 = heroes[0].position[0] + heroes[0].velocity[0]
                            Y43 = heroes[0].position[1] + heroes[0].velocity[1]
                            if ((hero.position[0] - heroes[0].position[0])**2 +
                                (hero.position[1] - heroes[0].position[1])**
                                    2) < ((X2P3 - X43)**2 + (Y2N3 - Y43)**2):
                                self.accelerate_towards(X2P3, Y2N3)
                            else:
                                self.accelerate_towards(X2N3, Y2P3)
            elif polygons:
                for j in range(1, len(polygons)):
                    if ((polygons[j].position[0] - hero.position[0])**2 +
                        (polygons[j].position[1] - hero.position[1])**2) < (
                            (polygons[0].position[0] - hero.position[0])**2 +
                            (polygons[0].position[1] - hero.position[1])**2):
                        polygons[0] = polygons[j]
                        if hero.health - polygons[0].body_damage * 20 <= 0 or hero.health < hero.max_health / 3:
                            self.shoot_at(*polygons[0].position)
                        X2P = hero.position[0] + polygons[0].velocity[0]
                        X2N = hero.position[0] - polygons[0].velocity[0]
                        Y2P = hero.position[1] + polygons[0].velocity[1]
                        Y2N = hero.position[1] - polygons[0].velocity[1]
                        X4 = polygons[0].position[0] + polygons[0].velocity[0]
                        Y4 = polygons[0].position[1] + polygons[0].velocity[1]
                        if ((hero.position[0] - polygons[0].position[0])**2 +
                            (hero.position[1] - polygons[0].position[1])**
                                2) < ((X2P - X4)**2 + (Y2N - Y4)**2):
                            self.accelerate_towards(X2P, Y2N)
                        else:
                            self.accelerate_towards(X2N, Y2P)
                    else:
                        self.accelerate_towards(polygons[0].position[0],
                                                polygons[0].position[1])
                        self.shoot_at(*polygons[0].position)

            if bullets:
                for i in range(1, len(bullets)):
                    if ((bullets[i].position[0] - hero.position[0])**2 +
                        (bullets[i].position[1] - hero.position[1])**2)**0.5 < (
                            (bullets[0].position[0] - hero.position[0])**2 +
                            (bullets[0].position[1] - hero.position[1])**
                            2)**0.5 and bullets[i].owner_id != self.name:
                        bullets[0] = bullets[i]
                        X2P2 = hero.position[0] + bullets[0].velocity[0]
                        X2N2 = hero.position[0] - bullets[0].velocity[0]
                        Y2P2 = hero.position[1] + bullets[0].velocity[1]
                        Y2N2 = hero.position[1] - bullets[0].velocity[1]
                        X42 = bullets[0].position[0] + bullets[0].velocity[0]
                        Y42 = bullets[0].position[1] + bullets[0].velocity[1]
                        if ((hero.position[0] - bullets[0].position[0])**2 +
                            (hero.position[1] - bullets[0].position[1])**2) < (
                                (X2P2 - X42)**2 + (Y2N2 - Y42)**2):
                            self.accelerate_towards(X2P2, Y2N2)
                        else:
                            self.accelerate_towards(X2N2, Y2P2)


Client.main()
