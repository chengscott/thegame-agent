from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):
    def init(self):
        self.name = 'aaabb' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        def distance_square(p1, p2):
            (x1, y1), (x2, y2) = p1, p2
            return  (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        
    
        dish=[]
        disp=[]
        disb=[]
        if heroes :
       
            for i in heroes:
                dh= distance_square(i.position,hero.position)
                dish.append(dh)
            dis = min(dish)
            i = dish.index(dis)
            x, y = heroes[i].position
            self.accelerate_towards(y,x)
            self.shoot_at(*heroes[i].position)
        else:
        
            if polygons :
                for j in polygons:
                    dp= distance_square(j.position,hero.position)
                    disp.append(dp)
                dispp = min(disp)
                j = disp.index(dispp)
                x1,y1 = polygons[j].position
                self.accelerate_towards(y1,x1)
                self.shoot_at(*polygons[j].position)
        
        
            if bullets :
                for k in bullets:
                    db= distance_square(k.position,hero.position)
                    disb.append(db)
                disbb = min(disb)
                k = disb.index(disbb)
                x2,y2 = bullets[k].position
                self.accelerate_towards(y2,x2)
                self.shoot_at(*polygons[0].position)
        
        self.level_up(Ability.HealthRegen)
        self.level_up(Ability.MovementSpeed)
        self.level_up(Ability.MaxHealth)
        self.level_up(Ability.BodyDamage)
        self.level_up(Ability.BulletSpeed) 
        self.level_up(Ability.BulletPenetration) 
        self.level_up(Ability.BulletDamage)
        self.level_up(Ability.Reload)
        


Client.main()