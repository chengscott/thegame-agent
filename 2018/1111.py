from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '1111'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        mx, my = hero.position
        p_dis = []
        h_dis = []
        b_dis = []
        upgrade_list = [
            Ability.HealthRegen, Ability.MaxHealth, Ability.BodyDamage,
            Ability.BulletSpeed
        ]
        if hero.skill_points > 0:
            if hero.abilities.health_regen.level < 2:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.max_health.level < 2:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.reload.level < 4:
                self.level_up(Ability.Reload)
            elif hero.abilities.bullet_damage.level < 4:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.bullet_speed.level < 4:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.reload.level < 8:
                self.level_up(Ability.Reload)
            elif hero.abilities.health_regen.level < 4:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.max_health.level < 4:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.movement_speed.level < 4:
                self.level_up(Ability.MovementSpeed)
            elif hero.abilities.bullet_damage.level < 8:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.movement_speed.level < 8:
                self.level_up(Ability.MovementSpeed)
            else:
                self.level_up(upgrade_list[hero.level % 4])

        ##
        if polygons:
            for t in range(len(polygons)):
                px, py = polygons[t].position
                d = ((px - mx)**2 + (py - my)**2)**0.5
                p_dis.append(d)
                ax, ay = polygons[p_dis.index(min(p_dis))].position
            self.shoot_at(ax, ay)
            if min(p_dis) > 300:
                self.accelerate_towards(ax, ay)
        ## 判斷視野內玩家與本體的距離
        if heroes:
            for i in range(len(heroes)):
                hx, hy = heroes[i].position
                d = ((hx - mx)**2 + (hy - my)**2)**0.5
                h_dis.append(d)
            ## 如果距離過近，則用反方向遠離
            if min(h_dis) < 500 and hero.level < heroes[h_dis.index(
                    min(h_dis))].level:
                ex, ey = heroes[h_dis.index(min(h_dis))].position
                cx, cy = heroes[h_dis.index(min(h_dis))].velocity
                self.accelerate_towards(mx - cy, mx + cx)
            elif min(h_dis) < 500 and hero.level > heroes[h_dis.index(
                    min(h_dis))].level and hero.level > 30:
                ex, ey = heroes[h_dis.index(min(h_dis))].position
                cx, cy = heroes[h_dis.index(min(h_dis))].velocity
                self.accelerate_towards(ex + 5 * cx, ey + 5 * cy)
            if min(h_dis) < 500 and hero.level > 10:
                ex, ey = heroes[h_dis.index(min(h_dis))].position
                cx, cy = heroes[h_dis.index(min(h_dis))].velocity
                self.shoot_at(ex + 5 * cx, ey + 5 * cy)

        if bullets:
            for s in range(len(bullets)):
                if bullets[s].owner_id != hero.id:
                    bx, by = bullets[s].position
                    d = ((bx - mx)**2 + (by - my)**2)**0.5
                    b_dis.append(d)
                else:
                    b_dis.append(500)
            if min(b_dis) < 80:
                dx, dy = bullets[b_dis.index(min(b_dis))].velocity
                self.accelerate_towards(-5 * dy + mx, 5 * dx + my)


Client.main()
