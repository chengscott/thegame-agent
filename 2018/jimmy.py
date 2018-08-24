from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'jimmy'

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 100)

        hx, hy = hero.position
        dis = []
        lev = []
        hp = []

        if polygons:
            for i in polygons:
                a, b = i.position
                r = (hx - a)**2 + (hy - b)**2
                dis.append(r)
            d = min(dis)
            n = dis.index(d)
            x, y = polygons[n].position
            self.shoot_at(x, y)
            if hero.health / hero.max_health >= 0.6 and heroes == []:
                self.accelerate_towards(x, y)

        if heroes:
            for i in heroes:
                l = i.level
                lev.append(l)
            sl = max(lev)
            n = lev.index(sl)
            x, y = heroes[n].position
            if hero.level - heroes[n].level <= 0:
                if hx - x > 0:
                    xbar = x + 2000
                else:
                    xbar = x - 2000
                if hy - y > 0:
                    ybar = y + 2000
                else:
                    ybar = y - 2000
                self.accelerate_towards(xbar, ybar)
            else:
                for i in heroes:
                    o = i.health
                    hp.append(o)
                d = min(hp)
                n = hp.index(d)
                x, y = heroes[n].position
                self.shoot_at(x, y)
                if hero.health / heroes[n].health >= 1.2 and hero.health / hero.max_health >= 0.3:
                    self.accelerate_towards(x, y)

        if polygons == [] and heroes == []:
            self.accelerate_towards(2000, 2000)

        if hero.abilities.health_regen.level < 2:
            self.level_up(Ability.HealthRegen)
        elif hero.abilities.body_damage.level < hero.abilities.health_regen.level:
            self.level_up(Ability.BodyDamage)
        elif hero.abilities.max_health.level < hero.abilities.body_damage.level:
            self.level_up(Ability.MaxHealth)
        else:
            if hero.abilities.bullet_speed.level < 2:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.bullet_damage.level < hero.abilities.bullet_speed.level:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.reload.level < hero.abilities.bullet_damage.level:
                self.level_up(Ability.Reload)
            else:
                if hero.abilities.movement_speed.level < 2:
                    self.level_up(Ability.MovementSpeed)
                else:
                    if hero.abilities.health_regen.level < 5:
                        self.level_up(Ability.HealthRegen)
                    elif hero.abilities.body_damage.level < hero.abilities.health_regen.level:
                        self.level_up(Ability.BodyDamage)
                    elif hero.abilities.max_health.level < hero.abilities.body_damage.level:
                        self.level_up(Ability.MaxHealth)
                    else:
                        if hero.abilities.movement_speed.level < 7:
                            self.level_up(Ability.MovementSpeed)
                        else:
                            if hero.abilities.health_regen.level < 7:
                                self.level_up(Ability.HealthRegen)
                            elif hero.abilities.body_damage.level < hero.abilities.health_regen.level:
                                self.level_up(Ability.BodyDamage)
                            elif hero.abilities.max_health.level < hero.abilities.body_damage.level:
                                self.level_up(Ability.MaxHealth)
                            else:
                                if hero.abilities.bullet_speed.level < 4:
                                    self.level_up(Ability.BulletSpeed)
                                elif hero.abilities.bullet_damage.level < hero.abilities.bullet_speed.level:
                                    self.level_up(Ability.BulletDamage)
                                elif hero.abilities.reload.level < hero.abilities.bullet_damage.level:
                                    self.level_up(Ability.Reload)
                                else:
                                    if hero.abilities.bullet_penetration.level < 3:
                                        self.level_up(
                                            Ability.BulletPenetration)
                                    else:
                                        if hero.abilities.health_regen.level < 8:
                                            self.level_up(Ability.HealthRegen)
                                        elif hero.abilities.body_damage.level < hero.abilities.health_regen.level:
                                            self.level_up(Ability.BodyDamage)
                                        elif hero.abilities.max_health.level < hero.abilities.body_damage.level:
                                            self.level_up(Ability.MaxHealth)
                                        else:
                                            if hero.abilities.movement_speed.level < 7:
                                                self.level_up(
                                                    Ability.MovementSpeed)
                                            else:
                                                if hero.abilities.bullet_speed.level < 6:
                                                    self.level_up(
                                                        Ability.BulletSpeed)
                                                elif hero.abilities.bullet_damage.level < hero.abilities.bullet_speed.level:
                                                    self.level_up(
                                                        Ability.BulletDamage)
                                                elif hero.abilities.reload.level < hero.abilities.bullet_damage.level:
                                                    self.level_up(
                                                        Ability.Reload)
                                                else:
                                                    if hero.abilities.bullet_penetration.level < 5:
                                                        self.level_up(
                                                            Ability.
                                                            BulletPenetration)
                                                    else:
                                                        if hero.abilities.bullet_speed.level < 8:
                                                            self.level_up(
                                                                Ability.
                                                                BulletSpeed)
                                                        elif hero.abilities.bullet_damage.level < hero.abilities.bullet_speed.level:
                                                            self.level_up(
                                                                Ability.
                                                                BulletDamage)
                                                        elif hero.abilities.reload.level < hero.abilities.bullet_damage.level:
                                                            self.level_up(
                                                                Ability.Reload)
                                                        else:
                                                            if hero.abilities.bullet_penetration.level < 8:
                                                                self.level_up(
                                                                    Ability.
                                                                    BulletPenetration
                                                                )


Client.main()
