from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
from math import hypot, pi, sin, asin, atan2


class Client(HeadlessClient):
    def init(self):
        self.name = 'OAQ'

    def action(self, hero, heroes, polygons, bullets):
        if hero.skill_points:
            for i in range(8):
                self.level_up(Ability.BulletDamage)
                self.level_up(Ability.HealthRegen)
                self.level_up(Ability.MaxHealth)
                self.level_up(Ability.Reload)
                self.level_up(Ability.BodyDamage)
                self.level_up(Ability.BulletSpeed)
            for i in range(8):
                self.level_up(Ability.BulletPenetration)
                self.level_up(Ability.MovementSpeed)

        def cp(target):
            if target.health == 0: return 9999999
            tx, ty = target.position
            hx, hy = hero.position
            return target.rewarding_experience / (
                (target.health / hero.bullet_damage) *
                (target.body_damage / hero.body_damage) *
                (hypot(tx - hx, ty - hy) / hero.bullet_speed + hero.reload))

        def shouldMove():
            return hero.health >= hero.max_health * 0.8 or (
                hero.health >= hero.max_health * 0.6
                and hero.health_regen_cooldown)

        def shoot_object(target):
            vx, vy = target.velocity
            dx = target.position.x - hero.position.x
            dy = target.position.y - hero.position.y
            phi = atan2(vy, vx) - atan2(dx, dy)
            u = hypot(vx, vy)
            v = hero.bullet_speed
            if u < v:
                theta0 = asin(u / v * sin(phi))
                #theta1 = -asin(u/v*sin(phi)) + pi
                self.shoot(atan2(dy, dx) + theta0)

        pv = 0
        if polygons:
            pm = max(polygons, key=cp)
            pv = cp(pm)
            self.shoot_at(*pm.position)
            if shouldMove():
                self.accelerate_towards(*pm.position)
        allies = [x for x in heroes if x.name.startswith('OA')]
        if allies:
            self.accelerate_towards(allies[0].position[0] + 20,
                                    allies[0].position[1] + 20)
        enemies = [
            x for x in heroes if not x.name.startswith('OA')
            and hypot(*x.velocity) < hero.bullet_speed * 0.9
        ]
        if enemies:
            hm = max(enemies, key=cp)
            hv = cp(hm)
            if pv < hv:
                #self.shoot_at(*hm.position)
                shoot_object(hm)
                if shouldMove():
                    self.accelerate_towards(*hm.position)


Client.main()
