from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient

class Client(GuiClient):
    def init(self):
        self.name = 'Game_Ai_V2.0' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
    
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("polygons:", polygons)
        print("heroes:", heroes)
        print("bullets:", bullets)
        print("My id",hero.id)
        print('-' * 79)

        #升級管控

        if hero.experience_to_level_up>=hero.experience:
            if hero.abilities.bullet_damage.level<4:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.health_regen.level<2:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.max_health.level<2:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.reload.level<4:
                self.level_up(Ability.Reload)
            elif hero.abilities.bullet_speed.level<4:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.movement_speed.level<3:
                self.level_up(Ability.MovementSpeed)
            elif hero.abilities.bullet_penetration.level<4:
                self.level_up(Ability.BulletPenetration)
            elif hero.abilities.bullet_damage.level<8:
                self.level_up(Ability.BulletDamage)
            elif hero.abilities.reload.level<8:
                self.level_up(Ability.Reload)
            elif hero.abilities.bullet_speed.level<8:
                self.level_up(Ability.BulletSpeed)
            elif hero.abilities.bullet_penetration.level<8:
                self.level_up(Ability.BulletPenetration)
            elif hero.abilities.health_regen.level<6:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.max_health.level<8:
                self.level_up(Ability.MaxHealth)
            elif hero.abilities.health_regen.level<8:
                self.level_up(Ability.HealthRegen)
            elif hero.abilities.movement_speed.level<8:
                self.level_up(Ability.MovementSpeed)

        #旗標設定

        flag_blocknear=False
        flag_enemynear=False
        flag_bossnear=False
        flag_wallnear=False
        flag_bulletnear=False
        flag_engagebattle=False

        #計數器設置

        i=0
        j=0
        k=0
        l=0
        m=0
        n=0

        
        #獲取座標值

        #自身座標
        x,y=hero.position

        #找尋鄰近方塊座標與距離，判定方塊過近與否
        xpoly,ypoly=0,0
        if polygons:
            xpoly,ypoly=polygons[0].position
            nearestblock=0
            i=0
            dist_poly=((x-xpoly)**2+(y-ypoly)**2)**0.5

            for p in polygons:
                xpoly,ypoly=p.position
                if (((x-xpoly)**2+(y-ypoly)**2)**0.5)<dist_poly:
                    dist_poly=((x-xpoly)**2+(y-ypoly)**2)**0.5
                    nearestblock=i
                i+=1

            xpoly,ypoly=polygons[nearestblock].position

            if dist_poly<300:
            	flag_blocknear=True

        #找尋目標方塊座標(低血量)
        xtarget,ytarget=0,0
        if polygons:
        	xtarget,ytarget=polygons[0].position
        	besttarget=0
        	j=0

        	for q in polygons:
        		if polygons[besttarget].health>polygons[j].health:
        			besttarget=j
        		j+=1

        	xtarget,ytarget=polygons[besttarget].position

        #找尋強敵座標
        xboss,yboss=0,0
        if heroes:
        	k=0
        	boss=0
        	realboss=0
        	mylevel=hero.level

        	for r in heroes:
        		if mylevel<heroes[k].level:
        			flag_bossnear=True
        			boss=k
        			if heroes[realboss].level<heroes[boss].level:
        				realboss=boss
        		k+=1

        	xboss,yboss=heroes[realboss].position

        #找尋對手座標
        xfoe,yfoe=0,0
        if heroes:
        	l=0
        	foe=0
        	flag_enemynear=True

        	for s in heroes:
        		if heroes[foe].health>heroes[l].health:
        			foe=l
        		l+=1

        	xfoe,yfoe=heroes[foe].position

        #判定離牆壁距離
        if x<300 or x>4700 or y<300 or y>3700:
        	flag_wallnear=True

        #判定最近子彈
        
        xbullet,ybullet=0,0
        m=0
        dist_bul=4000
        nearestbullet=0
        if bullets:
            for t in bullets:
            	if bullets[m].owner_id==hero.id:
            		m+=1
            		continue
            	else:
            		if (((x-xbullet)**2+(y-ybullet)**2)**0.5)<dist_bul:
            			dist_bul=(((x-xbullet)**2+(y-ybullet)**2)**0.5)
            		nearestbullet=m
            		m+=1


            xbullet,ybullet=bullets[nearestbullet].position

            if dist_bul<250:
            	flag_bulletnear=True

        #判定等級足夠打架
        if hero.level>=15:
        	flag_engagebattle=True





       	#控制射擊目標
       	if polygons:
       		self.shoot_at(xtarget,ytarget)

       	if flag_bossnear==True and heroes:
       		self.shoot_at(xboss,yboss)

        if flag_enemynear==True and flag_bossnear==False and heroes:
        	self.shoot_at(xfoe,yfoe)

        #控制移動方向
        self.accelerate_towards(2500,2000)
        if polygons:
        	self.accelerate_towards(xtarget,ytarget)

        if flag_enemynear==True and heroes:
        	if flag_engagebattle==True:
        		self.accelerate_towards(xfoe,yfoe)
        	if (((x-xfoe)**2+(y-yfoe)**2)**0.5)<300:
        		self.accelerate_towards(xfoe+(x-foe)*2,yfoe+(y-yfoe)*2)

        if flag_bulletnear==True and bullets:
        	self.accelerate_towards(x+(y-ybullet)*(-1),y+(x-xbullet))

        if flag_blocknear==True and polygons:
        	self.accelerate_towards(xpoly+(x-xpoly)*2,ypoly+(y-ypoly)*2)

        if flag_bossnear==True and heroes:
        	self.accelerate_towards(xboss+(x-xboss)*4,yboss+(y-yboss)*4)
        	if flag_blocknear==True:
        		self.accelerate_towards(x+(y-ypoly)*(-1),y+(x-xpoly))


        if flag_wallnear==True:
        	self.accelerate_towards(2500,2000)

Client.main()