from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '中華台北'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):

        if bullets:
            minR = 99999
            minB = None
            for b in bullets:
                r = (b.position[0])**2 + (b.position[1])**2
            if r <= minR:
                minR = r
                minB = b
                self.shoot_at(*minB.position)

        #Hero Detection
        minL = 999
        minH = None
        for h in heroes:
            l = h.level
            if l <= minL:
                minL = l
                minH = h

        minD = 9999999
        minP = None
        for p in polygons:
            x = (p.position[0] - hero.position[0])**2
            y = (p.position[1] - hero.position[1])**2
            d = x + y
            if d <= minD:
                minD = d
                minP = p
        if heroes:
            self.shoot_at(*h.position)
        elif polygons:
            self.shoot_at(*minP.position)

        #Level up
        if hero.abilities.health_regen.level < 1:
            self.level_up(Ability.HealthRegen)
        elif hero.abilities.reload.level < 8:
            self.level_up(Ability.Reload)
        elif hero.abilities.bullet_damage.level < 6:
            self.level_up(Ability.BulletDamage)
        elif hero.abilities.bullet_speed.level < 6:
            self.level_up(Ability.BulletSpeed)
        elif hero.abilities.bullet_penetration.level < 6:
            self.level_up(Ability.BulletPenetration)
        else:
            self.level_up(Ability.MovementSpeed)
            self.level_up(Ability.HealthRegen)
            self.level_up(Ability.MaxHealth)
            self.level_up(Ability.BodyDamage)


Client.main()
