from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = ' 大便 '  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        #Protection Before 18
        if hero.level < 19:
            #if polygons == []:
            #self.accelerate_towards (hero.position[0] - 1600, hero.position[1] - 1600)
            #Polygon Detection
            minD = 9999999
            minP = None
            for p in polygons:
                x = (p.position[0] - hero.position[0])**2
                y = (p.position[1] - hero.position[1])**2
                d = x + y
                if d <= minD:
                    minD = d
                    minP = p
            if polygons:
                #self.accelerate_towards (minP.position[0] + 5 * hero.radius, minP.position[1] + 5 * hero.radius)
                self.shoot_at(*minP.position)

            if bullets:
                minR = 99999
                minB = None
                for b in bullets:
                    r = (b.position[0])**2 + (b.position[1])**2
                if r <= minR:
                    minR = r
                    minB = b
                    self.shoot_at(*minB.position)
        else:
            #Hero Detection
            minL = 999
            minH = None
            for h in heroes:
                l = h.level
                if l <= minL:
                    minL = l
                    minH = h
            if heroes:
                self.shoot_at(*h.position)

                #if heroes:
                #self.accelerate_towards (h.position[0] + 2 * hero.radius, h.position[1] + 2 * hero.radius)

                #if hero.position == (h.position[0] + 2 * hero.radius, h.position[1] + 2 * hero.radius):
                #r = (h.position[0] - hero.position[0])**2 + (h.position[1] - hero.position[1])**2
                # a = (h.position[0] - hero.position[0])/r**0.5
                #b = (h.position[1] - hero.position[1])/r**0.5
                # self.accelerate_towards (hero.position[0] - b, hero.position[1] + a)
                # self.shoot_at (*h.position)

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
