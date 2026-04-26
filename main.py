import pygame, heapq, os
from abc import ABC, abstractmethod

#SINGLETON PATTERN
# Uztikrina, kad visoje programoje būtų tik vienas Logger objektas. Jame visa informacija saugoma
class Logger:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.f = "log.txt"
        return cls._instance

    def log(self, msg):                                  #neistirina seno teksto, prideda nauja teksta
        with open(self.f, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

    def last(self):                                       
        if not os.path.exists(self.f): return "Laukia..."   #rodo paskutini atlikta veiksma ekrane naudotojui
        with open(self.f, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines[-1].strip() if lines else "..."

#ABSTRAKCIJA IR ENKAPSULIACIJA
class MapObject(ABC): # ABC - abstrakti bazine klase. Tai yra kaip sablonas, kuri gali paveldeti kitos klases
    def __init__(self, x, y, name):
        self._x = x  #Enkapsuliacija. Duomenys privatus (apsaugoti). Negalima tiesiogiai prieiti prie koord., kad kodas nepakeistu daiktu vietu.
        self._y = y
        self.name = name 

    @property #per sita getteri koordinates pasiimsiu
    def pos(self): return (self._x, self._y)

    @abstractmethod #privercia vaikines klases tureti draw metoda (zemelapi kiekvienas objektas savaip nusipies)
    def draw(self, s, f): pass

#PAVELDIMUMAS IR POLIMORFIZMAS
class Station(MapObject): #MapObject yra tevine klase, visos kitos vaikines. Jos paveldi viska, ka turi tevine klase. PAVELDIMUMAS
    def __init__(self, x, y, name, clr, is_p=True):
        super().__init__(x, y, name)
        self.clr, self.is_p, self.act = clr, is_p, True

    def draw(self, s, f): #Polimorfizmas - skirtingi objektai i ta pati metoda reaguoja savaip. Komanda ta pati - veiksmas skirtingas
        c = self.clr if self.act else (200, 50, 50)  #pristatymo spalva
        pygame.draw.rect(s, c, (self._x*25, self._y*25, 25, 25)) #staciakampiu piesimas (25px)
        lbl = "" if self.is_p else f"{self.name}"
        if lbl:
            s.blit(f.render(lbl, 1, (255,255,255)), (self._x*25+9, self._y*25+4)) #nupiesiami skaiciai 1-4 ant pristatymo vietu

#KOMPOZICIJA
class Navigator: #Kelio paieska :pp visa sita funkcija suranda optimaliausia kelia
    def find(self, start, goal, obs):
        q, came, g = [(0, start)], {}, {start: 0} 
        while q:
            curr = heapq.heappop(q)[1]
            if curr == goal:
                path = []
                while curr in came: path.append(curr); curr = came[curr]
                return path[::-1]
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                n = (curr[0]+d[0], curr[1]+d[1])
                if 0<=n[0]<50 and 0<=n[1]<30 and n not in obs:
                    if n not in g or g[curr]+1 < g[n]:
                        g[n]=g[curr]+1; came[n]=curr
                        h = abs(n[0]-goal[0]) + abs(n[1]-goal[1])
                        heapq.heappush(q, (g[n]+h, n))
        return []

class AGV:
    def __init__(self, pos):
        self.pos, self.path, self.job = list(pos), [], None  #agv vieta i sarasa dedama, taip jo busima vieta atnaujinama  #Jei navigatoriaus nebus, agv irgi nebus
        self.nav = Navigator() #Kompozicija - kai vienas objektas valdo kito objekto gyvavimo ciklą. Jei pagrindinis objektas sunaikinamas, išnyksta ir jo dalys.

#ZEMELAPISSSS
pygame.init(); sc = pygame.display.set_mode((1250, 850)); font = pygame.font.SysFont("Arial", 14, True)
log, agv = Logger(), AGV((49, 12))
ps = [Station(22,0,"1",(50,50,200)), Station(14,29,"2",(50,50,200)), Station(39,29,"3",(50,50,200))]
ds = [Station(3,7,"1",(100,150,100),0), Station(19,17,"2",(100,150,100),0), Station(32,11,"3",(100,150,100),0), Station(47,2,"4",(100,150,100),0)]
q, obs, btns = [], set(), [pygame.Rect(250+i*110, 785, 100, 40) for i in range(4)]

rs = [(range(16,26), range(14,17)), (range(19,22), range(10,17)), (range(20,24), range(14,20)),
      (range(29,36), range(12,15)), (range(30,32), range(11,12)), (range(33,34), range(11,12)),
      (range(29,33), range(18,21)), (range(26,33), range(21,23)), (range(33,35), range(20,23)),
      (range(38,43), range(15,18)), (range(48,50), range(15,17)), (range(47,50), range(13,15)),
      (range(48,50), range(10,12)), (range(43,50), range(27,30)), (range(40,50), range(28,30)),
      (range(27,39), range(29,30)), (range(15,26), range(27,30)), (range(19,22), range(22,30)),
      (range(0,14), range(28,30)), (range(5,15), range(20,23)), (range(7,11), range(15,20)),
      (range(2,6), range(8,15)), (range(8,11), range(1,6)), (range(14,22), range(0,4)),
      (range(23,38), range(0,2)), (range(34,38), range(0,8)), (range(40,48), range(3,7)), (range(28,34), range(2,6))]
for rx, ry in rs: [obs.add((x,y)) for x in rx for y in ry]

while True:
    sc.fill((20, 20, 25)); cp = tuple(agv.pos) #background ir dabartine agv pozicija
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            for i, r in enumerate(btns):
                if r.collidepoint(e.pos) and ds[i].act:
                    ds[i].act = False; q.append(ds[i])
                    log.log(f"Važiuojama pildyti į {i+1}")


    if agv.path: agv.pos = list(agv.path.pop(0)) #visa vaziavimo logika
    else:
        if agv.job and cp == agv.job.pos: #atvyko i tiksla
            agv.job.act = True; log.log(f"Viskas pildoma / papildyta"); agv.job = None
        elif agv.job and any(cp == p.pos for p in ps): #paeme krovini, veza pildyt
            agv.path = agv.nav.find(cp, agv.job.pos, obs)
        elif not agv.job and q: #jei yra dar darbu, toliau daro
            agv.job = q.pop(0); agv.path = agv.nav.find(cp, ps[0].pos, obs)
        elif not agv.job and cp != (49, 12): #nera darbo, grizta i baze
            agv.path = agv.nav.find(cp, (49, 12), obs)

    #Atvaizdavimas
    for x, y in obs: pygame.draw.rect(sc, (50, 50, 60), (x*25, y*25, 24, 24))
    for o in ps + ds: o.draw(sc, font)
    pygame.draw.rect(sc, (255, 215, 0), (agv.pos[0]*25+4, agv.pos[1]*25+4, 17, 17))
    
    #UI
    pygame.draw.rect(sc, (30, 30, 40), (0, 750, 1250, 100))
    sc.blit(font.render(f"Log: {log.last()}", 1, (0, 255, 0)), (20, 765))
    for i, r in enumerate(btns):
        pygame.draw.rect(sc, (60, 60, 75), r, border_radius=5)
        sc.blit(font.render(f"Panaudoti {i+1}", 1, (255,255,255)), (r.x+12, r.y+12))

    pygame.display.flip(); pygame.time.Clock().tick(30)
