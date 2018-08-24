from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = 'OUO'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):

        print('-' * 79)
        hx, hy = hero.position
        hhx, hhy = (0, 0)
        dis = []
        currentper = hero.health / hero.max_health
        id = 0
        '''if hx>4500:
            if hy>3500: #right top
                self.accelerate_towards(hx-1000,hy-1000)
            elif hy<500: #right down
                self.accelerate_towards(hx-1000,hy+1000)
            else: #right
                self.accelerate_towards(hx-1000,hy)
        elif hx<500:
            if hy>3500: #left top
                self.accelerate_towards(hx+1000,hy-1000)
            elif hy<500: #left down
                self.accelerate_towards(hx+1000,hy+1000)
            else: #left
                self.accelerate_towards(hx+1000,hy)
        else:
            if hy>3500: #top
                self.accelerate_towards(hx,hy-1000)
            elif hy<500: #down
                self.accelerate_towards(hx,hy+1000)'''

        if heroes:

            if hero.level >= 9:
                for h in heroes:
                    x, y = h.position
                    d = (x - hx)**2 + (y - hy)**2
                    dis.append(d)
                d = min(dis)
                p = dis.index(d)
                if heroes[p].health > hero.abilities.max_health.value or (
                        heroes[p].level - hero.level) >= 10:
                    hhx, hhy = heroes[p].position
                    if hx > 4500:
                        if hy > 3500:  #right top
                            self.accelerate_towards(hx - 1000, hy - 1000)
                        elif hy < 500:  #right down
                            self.accelerate_towards(hx - 1000, hy + 1000)
                        else:  #right
                            self.accelerate_towards(hx - 1000, hy)
                    elif hx < 500:
                        if hy > 3500:  #left top
                            self.accelerate_towards(hx + 1000, hy - 1000)
                        elif hy < 500:  #left down
                            self.accelerate_towards(hx + 1000, hy + 1000)
                        else:  #left
                            self.accelerate_towards(hx + 1000, hy)
                    else:
                        if hy > 3500:  #top
                            self.accelerate_towards(hx, hy - 1000)
                        elif hy < 500:  #down
                            self.accelerate_towards(hx, hy + 1000)
                        else:
                            if hhx >= hx:
                                if hhy >= hy:  # enemy is right top
                                    self.accelerate_towards(hx - 800, hy - 800)
                                else:  #enemy is right down
                                    self.accelerate_towards(hx - 800, hy + 800)
                            else:
                                if hhy >= hy:  # enemy is left top
                                    self.accelerate_towards(hx + 800, hy - 800)
                                else:  #enemy is left down
                                    self.accelerate_towards(hx + 800, hy + 800)

                else:
                    self.shoot_at(*heroes[p].position)
                    hhx, hhy = heroes[p].position
                    if currentper < 0.3:
                        if hhx >= hx:
                            if hhy >= hy:  # enemy is right top
                                self.accelerate_towards(hhx - 50, hhy - 50)
                            else:  #enemy is right down
                                self.accelerate_towards(hhx - 50, hhy + 50)
                        else:
                            if hhy >= hy:  # enemy is left top
                                self.accelerate_towards(hhx + 50, hhy - 50)
                            else:  #enemy is left down
                                self.accelerate_towards(hhx + 50, hhy + 50)
                    else:
                        self.accelerate_towards(*heroes[p].position)
            else:
                if polygons:
                    for i in polygons:
                        x, y = i.position
                        d = (x - hx)**2 + (y - hy)**2
                        dis.append(d)
                    d = min(dis)
                    p = dis.index(d)
                    self.shoot_at(*polygons[p].position)
                    if hero.abilities.body_damage.level == 8 and currentper > 0.3:
                        self.accelerate_towards(*polygons[p].position)
                    else:
                        self.accelerate_towards(polygons[p].position[0] - 150,
                                                polygons[p].position[1] - 150)
                else:
                    self.accelerate_towards(2500, 2000)
        else:
            if polygons:
                for i in polygons:
                    x, y = i.position
                    d = (x - hx)**2 + (y - hy)**2
                    dis.append(d)
                d = min(dis)
                p = dis.index(d)
                self.shoot_at(*polygons[p].position)
                if hero.abilities.body_damage.level == 8 and currentper > 0.3:
                    self.accelerate_towards(*polygons[p].position)
                else:
                    self.accelerate_towards(polygons[p].position[0] - 150,
                                            polygons[p].position[1] - 150)
            else:
                self.accelerate_towards(2500, 2000)

        self.level_up(Ability.BodyDamage)
        if hero.abilities[Ability.BodyDamage].level == 8:
            self.level_up(Ability.HealthRegen)
            if hero.abilities[Ability.HealthRegen].level == 8:
                self.level_up(Ability.MovementSpeed)
                if hero.abilities[Ability.MovementSpeed].level == 4:
                    self.level_up(Ability.MaxHealth)
                    if hero.abilities[Ability.MaxHealth].level == 8:
                        self.level_up(Ability.MovementSpeed)
                        if hero.abilities[Ability.MovementSpeed].level == 8:
                            self.level_up(Ability.Reload)
                            if hero.abilities[Ability.Reload].level == 8:
                                self.level_up(Ability.BulletSpeed)
                                if hero.abilities[
                                        Ability.BulletSpeed].level == 8:
                                    self.level_up(Ability.BulletDamage)
                                    if hero.abilities[
                                            Ability.BulletDamage].level == 8:
                                        self.level_up(
                                            Ability.BulletPenetration)


Client.main()
