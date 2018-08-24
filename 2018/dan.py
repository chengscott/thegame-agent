from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import time


class Client(HeadlessClient):
    def init(self):
        self.name = 'dan'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):

        ##打多邊形，在與多邊形距離為300以外的範圍朝多邊形前進
        he = []
        c, d = hero.position  #自己的位子
        if polygons:
            for g in range(len(polygons)):

                e, f = polygons[g].position
                dis2 = ((c - e)**2 + (d - f)**2)**0.5
                he.append(dis2)
            a = min(he)
            print(a)
            g = he.index(a)
            self.shoot_at(*polygons[g].position)
            h1, h2 = polygons[g].position
            if a >= 300:
                self.accelerate_towards(h1, h2)

        dis_dic = []
        if heroes:
            self.shoot_at(*heroes[0].position)
            self.accelerate_towards(*heroes[0].position)
            for i in range(len(heroes)):

                a, b = heroes[i].position
                dis = ((a - c)**2 + (b - d)**2)**0.5
                dis_dic.append(dis)
            d = min(dis_dic)
            i = dis_dic.index(d)
            x, y = heroes[i].position

            if hero.level < heroes[i].level:
                self.accelerate_towards(2 * c - x, 2 * d - y)
            else:
                if d >= 300:
                    self.accelerate_towards(x, y)

            close = heroes[i].position

        bul = []

        if bullets:
            for p in range(len(bullets)):
                if bullets[p].owner_id != hero.id:
                    a1, b1 = bullets[p].position
                    dis1 = ((a1 - c)**2 + (b1 - d)**2)**0.5
                    bul.append(dis1)
                else:
                    bul.append(500)
            o = min(bul)
            r = bul.index(o)
            a2, b2 = bullets[p].position

            if d < 200:
                self.accelerate_towards(-5 * a2 + c, -5 * b2 + d)

        if hero.level < 20:
            if hero.health_regen_level < 2:
                self.level_up(Ability.HealthRegen)
            elif hero.movement_speed_level < 4:
                self.level_up(Ability.MovementSpeed)
            elif hero.reload_level < 4:
                self.level_up(Ability.Reload)
            elif hero.health_regen_level < 4:
                self.level_up(Ability.HealthRegen)
            elif hero.bullet_damage_level < 4:
                self.level_up(Ability.BulletDamage)
            elif hero.max_health_level < 4:
                self.level_up(Ability.MaxHealth)

        self.level_up(Ability.MovementSpeed)
        self.level_up(Ability.Reload)
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BulletDamage)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.BulletSpeed)

        self.level_up(Ability.BulletPenetration)


Client.main()
