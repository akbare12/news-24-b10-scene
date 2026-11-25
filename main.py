import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
SB='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SN='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SNB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
CREAM=(247,242,231); INK=(20,20,20); NAVY=(26,42,74); RED=(176,30,36); GREY=(90,88,82); LGREY=(232,226,212); GOLD=(196,148,40); GREEN=(34,120,60); BLUE=(30,90,160); ORANGE=(200,110,20); PURPLE=(110,60,140); YELLOW=(180,150,20)
img=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(img)
def T(x,y,s,f,fill=INK,anchor='la'):
    d.text((x,y),s,font=f,fill=fill,anchor=anchor)
def WR(s,f,mw):
    words=s.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=f)<=mw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def PARA(x,y,s,f,mw,lh,fill=INK,maxl=99):
    ls=WR(s,f,mw)[:maxl]
    for i,l in enumerate(ls): T(x,y+i*lh,l,f,fill)
    return y+len(ls)*lh
def CHIP(x,y,s,c):
    f=F(SNB,8); w=d.textlength(s,font=f)+10; d.rounded_rectangle([x,y,x+w,y+13],2,fill=c); T(x+5,y+1,s,f,(255,255,255)); return x+w+4
def SCENE(x,y,w,h,kind):
    d.rectangle([x,y,x+w,y+h],fill=NAVY if kind!=2 else (40,40,60))
    if kind==1:
        d.rectangle([x,y+h-22,x+w,y+h],fill=(30,30,40))
        for i,bx in enumerate([x+8,x+52,x+96,x+150,x+205,x+258]):
            bh=[38,58,48,95,62,42][i]; d.rectangle([bx,y+h-22-bh,bx+34,y+h-22],fill=(70,80,110) if i!=3 else (150,160,190))
            for wy in range(0,bh-6,10):
                for wx in range(4,30,9): d.rectangle([bx+wx,y+h-22-bh+4+wy,bx+wx+4,y+h-22-bh+8+wy],fill=(255,210,90))
        d.rectangle([x+150,y+h-22-95,x+184,y+h-22],fill=(200,205,215)); d.polygon([(x+150,y+h-22-95),(x+167,y+h-22-96),(x+184,y+h-22-95)],fill=(200,205,215)); d.rectangle([x+165,y+h-22-96,x+169,y+h-22-86],fill=RED)
        d.ellipse([x+w-52,y+8,x+w-30,y+30],fill=(255,200,80)); d.polygon([(x+w-70,y+34),(x+w-58,y+22),(x+w-46,y+34)],fill=(120,120,130)); d.line([x+w-70,y+34,x+w-46,y+34],fill=(120,120,130),width=2)
        for ex,ey,er in [(x+158,y+h-70,14),(x+172,y+h-58,10),(x+146,y+h-52,8)]: d.ellipse([ex-er,ey-er,ex+er,ey+er],fill=(255,140,40)); d.ellipse([x+158-6,y+h-70-6,x+158+6,y+h-70+6],fill=(255,220,80))
    elif kind==2:
        d.rectangle([x,y+h-20,x+w,y+h],fill=(25,25,35)); d.rectangle([x+20,y+18,x+w-20,y+78],fill=(120,30,30)); d.rectangle([x+20,y+18,x+w-20,y+34],fill=(160,40,40))
        for i in range(5): d.rectangle([x+34+i*52,y+44,x+54+i*52,y+70],fill=(220,200,160))
        for i in range(3): d.rectangle([x+40+i*90,y+86,x+120+i*90,y+96],fill=(220,210,190))
        d.rectangle([x+130,y+8,x+190,y+16],fill=GOLD); T(x+132,y+8,'PARTY HQ',F(SNB,7),(255,255,255))
        d.rectangle([x+w-70,y+88,x+w-16,y+104],fill=(255,255,255)); d.line([x+w-66,y+96,x+w-20,y+96],fill=RED,width=2)
    elif kind==3:
        d.rectangle([x,y+h-24,x+w,y+h],fill=(40,40,50)); d.polygon([(x+20,y+h-24),(x+20,y+34),(x+70,y+18),(x+120,y+34),(x+120,y+h-24)],fill=(210,205,195)); d.polygon([(x+52,y+18),(x+70,y+6),(x+88,y+18)],fill=(180,30,30))
        for cx in [34,58,82,106]:
            d.rectangle([cx,y+44,cx+8,y+h-24],fill=(120,110,95))
        d.rectangle([x+w-110,y+52,x+w-30,y+70],fill=(150,110,50)); d.rectangle([x+w-100,y+40,x+w-40,y+52],fill=(90,60,30)); d.rectangle([x+w-72,y+30,x+w-68,y+40],fill=(90,60,30))
        d.ellipse([x+w-120,y+14,x+w-100,y+34],fill=(255,210,90)); d.rectangle([x+150,y+84,x+210,y+98],fill=(60,60,80)); T(x+152,y+86,'HUAWEI',F(SNB,9),(255,255,255))
# continents as (lon,lat) polygons, equirectangular
CONT=[([(-168,66),(-155,71),(-140,70),(-125,70),(-110,68),(-95,69),(-80,68),(-70,62),(-60,52),(-55,47),(-65,44),(-70,42),(-75,38),(-80,32),(-84,30),(-90,21),(-97,16),(-105,20),(-112,28),(-120,38),(-125,49),(-135,58),(-150,60),(-165,60)]),([(-80,10),(-60,8),(-50,0),(-35,-8),(-40,-20),(-50,-30),(-65,-40),(-70,-55),(-75,-35),(-80,-15)]),([(-10,36),(0,44),(-5,48),(0,51),(5,53),(10,57),(18,56),(25,60),(30,70),(40,68),(45,60),(30,50),(28,45),(20,40),(12,38),(0,36)]),([(-17,15),(-10,30),(0,36),(10,37),(20,32),(32,31),(35,28),(43,12),(51,11),(48,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-30),(12,-18),(9,-2),(9,4),(-8,5)]),([(40,68),(60,70),(80,73),(100,76),(120,73),(140,72),(160,70),(178,66),(170,60),(160,55),(140,45),(130,42),(127,38),(120,30),(110,20),(105,10),(100,8),(95,15),(90,22),(80,15),(75,8),(70,20),(60,25),(50,28),(45,30)]),([(113,-22),(122,-14),(132,-12),(142,-11),(150,-22),(153,-27),(150,-37),(140,-38),(130,-32),(120,-34)])]
def MAP(x,y,w,h,pins):
    d.rectangle([x,y,x+w,y+h],fill=(210,225,235)); d.rectangle([x,y,x+w,y+h],outline=NAVY,width=1)
    for poly in CONT:
        pts=[(x+(lon+180)/360*w, y+(90-lat)/180*h) for lon,lat in poly]; d.polygon(pts,fill=(120,160,110),outline=(80,120,85))
    for n,la,lo in pins:
        px=x+(lo+180)/360*w; py=y+(90-la)/180*h; d.ellipse([px-7,py-7,px+7,py+7],fill=RED,outline=(255,255,255)); T(px,py-5,str(n),F(SNB,7),(255,255,255),anchor='mm')
def STRIP(x,y,w,h,kind):
    cols=[(30,45,80),(120,50,40),(40,90,70),(140,110,30),(90,60,120),(40,110,110),(160,90,40),(80,80,100),(60,120,90),(110,40,60)]; bg=cols[kind%10]; d.rectangle([x,y,x+w,y+h],fill=bg)
    if kind==0:
        d.rectangle([x,y+h-8,x+w,y+h],fill=(20,20,30))
        for i in range(6):
            bx=x+6+i*30; d.rectangle([bx,y+h-30,bx+16,y+h-8],fill=(200,200,210)); d.rectangle([bx+4,y+h-38,bx+12,y+h-30],fill=(120,120,130))
        d.polygon([(x+w-40,y+10),(x+w-28,y+4),(x+w-16,y+10)],fill=(60,60,70)); d.ellipse([x+w-34,y+16,x+w-26,y+24],fill=(255,180,60))
    elif kind==1:
        d.ellipse([x+w/2-16,y+4,x+w/2+16,y+36],fill=GOLD,outline=(255,255,255),width=2); d.rectangle([x+w/2-4,y+36,x+w/2+4,y+44],fill=GOLD)
        d.rectangle([x+8,y+h-14,x+70,y+h-6],fill=(0,120,60)); d.rectangle([x+w-70,y+h-14,x+w-8,y+h-6],fill=(200,40,40))
    elif kind==2:
        d.polygon([(x+10,y+h-6),(x+40,y+8),(x+70,y+h-6)],fill=(90,120,160)); d.rectangle([x+80,y+h-16,x+150,y+h-6],fill=(60,60,70)); d.rectangle([x+85,y+h-26,x+145,y+h-16],fill=(200,200,210))
        d.ellipse([x+w-30,y+6,x+w-10,y+26],fill=(255,200,80))
    elif kind==3:
        d.line([x+6,y+h-8,x+w-6,y+8],fill=(255,255,255),width=3); d.line([x+6,y+h-8,x+w-6,y+8],fill=(255,60,60),width=1)
        for i,px in enumerate([30,70,110,150]): d.ellipse([x+px,y+h-14-i*6,x+px+6,y+h-8-i*6],fill=(255,255,255))
        T(x+8,y+2,'50,018',F(SNB,11),(255,255,255))
    elif kind==4:
        d.rectangle([x+10,y+8,x+w-10,y+18],fill=(200,40,40)); d.rectangle([x+20,y+24,x+w-20,y+34],fill=(40,40,50))
        for i in range(4): d.rectangle([x+24+i*38,y+26,x+52+i*38,y+32],fill=(255,210,90))
        d.ellipse([x+w-24,y+6,x+w-8,y+22],fill=(255,80,80))
    elif kind==5:
        d.polygon([(x+30,y+30),(x+60,y+8),(x+90,y+30),(x+75,y+30),(x+60,y+20),(x+45,y+30)],fill=(120,120,130)); d.rectangle([x+50,y+28,x+70,y+38],fill=(60,60,70))
        d.polygon([(x+110,y+34),(x+140,y+10),(x+170,y+34)],fill=(140,140,150))
    elif kind==6:
        d.rectangle([x+14,y+10,x+70,y+30],fill=(220,220,220)); d.rectangle([x+80,y+10,x+w-14,y+30],fill=(180,180,190))
        for i in range(5): d.ellipse([x+22+i*10,y+16,x+28+i*10,y+24],fill=NAVY)
        d.rectangle([x+14,y+34,x+w-14,y+40],fill=(150,30,30))
    elif kind==7:
        d.rectangle([x+20,y+6,x+w-20,y+30],fill=(200,60,40)); d.rectangle([x+20,y+30,x+w-20,y+38],fill=(120,30,20))
        for i in range(4): d.rectangle([x+30+i*36,y+12,x+56+i*36,y+24],fill=(255,255,255))
    elif kind==8:
        d.polygon([(x+10,y+h-6),(x+50,y+6),(x+90,y+h-6)],fill=(150,120,80)); d.rectangle([x+110,y+14,x+170,y+34],fill=(200,200,210)); d.rectangle([x+120,y+6,x+160,y+14],fill=(180,40,40))
    else:
        d.polygon([(x+20,y+h-6),(x+60,y+4),(x+100,y+h-6)],fill=(200,200,210)); d.ellipse([x+130,y+8,x+170,y+40],fill=(200,220,255),outline=(255,255,255),width=2); d.line([x+130,y+24,x+170,y+24],fill=(100,140,200),width=2)
# ---- HEADER ----
d.rectangle([0,0,W,10],fill=RED); T(16,14,'THE WORLD ON ONE DAY',F(SNB,10),RED); T(1008,14,'38 STORIES  ·  7 REGIONS  ·  14 FIELDS  ·  ALL FROM TUESDAY 24 NOVEMBER 2026',F(SNB,9),NAVY,anchor='ra')
T(16,28,'Tuesday 24 November 2026',F(SB,34),INK); T(16,64,'One day of world news, one picture  —  wires read up to 23:00 UTC',F(SNB,10),GREY)
T(16,80,'Riyadh tower hit again  ·  Shanghai party chief probed  ·  Huawei guilty on 10 of 12 counts',F(SB,12),RED)
# region bar
REG=[('Europe',7,(60,90,160)),('Middle East',8,(176,30,36)),('Asia',9,(200,120,20)),('Africa',5,(34,120,60)),('Americas',5,(110,60,140)),('World / Space',4,(40,110,110))]
bx=16; tot=sum(n for _,n,_ in REG)
for name,n,c in REG:
    w=int(992*n/tot); d.rectangle([bx,98,bx+w,116],fill=c); T(bx+w/2,101,f'{name} {n}',F(SNB,9),(255,255,255),anchor='ma'); bx+=w
# UTC strip
T(16,122,'THE DAY IN UTC',F(SNB,9),RED); UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi hot-pot blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
ux=16
for t,ev in UTC:
    T(ux,134,t,F(SNB,10),RED); PARA(ux,146,ev,F(SN,8),128,10,INK,2); ux+=142
d.line([16,168,1008,168],fill=NAVY,width=1)
# numbers strip
T(16,174,'THE DAY IN NUMBERS',F(SNB,9),RED); NUMS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow, first over 50k'),('+8.99%','Taiex record'),('25','killed / missing, Yemen'),('26','Cikande fire toll')]
nx=16
for v,lab in NUMS:
    T(nx,186,v,F(SB,17),NAVY); T(nx,206,lab,F(SN,8),GREY); nx+=166
d.line([16,222,1008,222],fill=NAVY,width=1)
# ---- HEROES ----
HEROS=[(1,'1  RIYADH · MIDDLE EAST',GREEN,'CONFIRMED','Houthi drone hits Riyadh\'s tallest tower again, 11 hurt','Drone hits the PIF tower — the 2nd strike on it in a week. 11 hurt: 2 Saudi, 2 Indian, 3 Nepali, 4 Egyptian. (Saudi officials · AP)'),(2,'2  SHANGHAI · ASIA',BLUE,'OFFICIAL','China probes Shanghai party chief Chen Jining','Chen Jining, 62, probed for "serious violations" — the 4th Politburo member to fall in a probe this year. (CCDI)'),(3,'3  NEW YORK · US / TECH',ORANGE,'CONFIRMED','Huawei guilty on 10 of 12 counts','US jury convicts Huawei of trade-secret theft and bank fraud on 10 of 12 counts; cleared of racketeering. Sentence Sep 2027; Huawei to appeal. (US court)')]
hx=16
for kind,kick,col,chip,hl,deck in HEROS:
    SCENE(hx,228,320,118,kind); T(hx,350,kick,F(SNB,9),col); CHIP(hx+262,350,chip,col)
    PARA(hx,366,hl,F(SB,15),320,17,INK,2); PARA(hx,402,deck,F(SN,9),320,11,GREY,3); hx+=336
d.line([16,452,1008,452],fill=NAVY,width=1)
CARDS=[(0,'4  ZAPORIZHZHIA · EUROPE',GREEN,'REPORTED','Russian attacks kill 9 across Ukraine in a day','9 killed, 81 hurt; 96 drones launched, 73 shot down or jammed. (Ukraine officials)'),(1,'5  CAS · AFRICA / SPORT',BLUE,'OFFICIAL','CAS hands Senegal back the AFCON title','Morocco forfeit 3–0, so Senegal win 1–0 and take the title back. (CAS)'),(2,'6  HORMUZ · MIDDLE EAST',ORANGE,'REPORTED','IRGC attacks container ship in Hormuz','Ship attacked 18:58 UTC; navigation disabled, exclusion zone north of Khasab, Oman. (UKMTO)'),(3,'7  NEW YORK · MARKETS',GREEN,'CONFIRMED','Dow closes above 50,000 for the first time','Dow 50,018. Nasdaq −1.5% on chip slide; Taiex +8.99% record 40,122. (Market close)'),(4,'8  REDMOND · TECH',ORANGE,'REPORTED',"Microsoft declares 'Code Red' after historic outage",'After a 24-hour outage, the worst in Exchange Online history: 1-hour recovery goal, 5 workstreams. (Reuters)'),(5,'9  ESKISEHIR · EUROPE',ORANGE,'REPORTED','Turkish military helicopter crash kills 5','AS-532 helicopter crashes in Eskisehir; 5 killed. 19:52 UTC. (Turkish officials)'),(6,'10  CARTAGENA · AMERICAS',ORANGE,'REPORTED','Supermarket hostages: 25 held in Cartagena','25 held; 5 elderly women freed; airport landings halted ~45 minutes. 17:35 UTC. (Colombia officials)'),(7,'11  ADEN · MIDDLE EAST',ORANGE,'REPORTED','Houthis advance within 60 km of Aden','Houthi forces advance to within 60 km of Aden, Yemen. 16:51 UTC. (Wires)'),(8,'12  LAHJ · MIDDLE EAST',ORANGE,'REPORTED','Saudi strikes kill 25, wound 6 in Yemen','Strikes on a bus and truck in Wadi Maabaq, Lahj: 25 killed or missing, 6 hurt. 10:42 UTC. (Yemen officials)'),(9,'13  JIUQUAN · SPACE',BLUE,'OFFICIAL','China names first foreign astronaut for Tiangong','Shenzhou-24 crew: Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan — the first foreigner on Tiangong. (CMSA)')]
for r in range(2):
    for c in range(5):
        i=r*5+c; kind,kick,col,chip,hl,deck=CARDS[i]; x=16+c*200; y=458+r*118
        d.rectangle([x,y,x+192,y+112],fill=(255,255,255),outline=LGREY); STRIP(x+4,y+4,184,34,kind); T(x+6,y+42,kick,F(SNB,7),col); CHIP(x+128,y+42,chip,col)
        PARA(x+6,y+58,hl,F(SNB,9),180,10,INK,2); PARA(x+6,y+80,deck,F(SN,8),180,9,GREY,2)
# ---- MAP + ALSO ----
T(16,700,'THE WORLD — WHERE IT HAPPENED',F(SNB,10),NAVY)
PINS=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74.0),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.3),(7,42.2,-73.2),(8,47.7,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,14.9,47.4),(13,39.7,98.5)]
MAP(16,716,470,168,PINS); T(16,888,'Pins 1–13 = stories 1–13 above.  Red = Middle East · Blue = Asia · Green = Europe',F(SN,8),GREY)
T(500,700,'ALSO ON TUESDAY — 25 MORE STORIES',F(SNB,10),NAVY)
ALSO=['14 Ankara: Haftar visits Turkey, first time','15 London: UK sanctions Houthis + 4 officials','16 Villavicencio: car bomb injures 23','17 Gaza: Israel kills Hamas security chief','18 Baghdad: Iraq takes federal control of Kurdish oilfields','19 Gaza: meningitis epidemic alert — 272 cases in Oct','20 DR Congo: Cessna 208 missing, rebels claim shootdown','21 Hanoi: hot-pot blast kills at least 6','22 Gulf of Finland: Ukraine hits Russian ship Sparta II','23 Kuala Lumpur: Malaysia to return migrants to Myanmar','24 Ulleungdo: S. Korea shelter order, Russian jets in ADIZ','25 Dhaka: Hasina plans return on 16 Dec','26 The Hague: 14 nations endorse ICJ Myanmar ruling','27 Jakarta: Indonesia nominates 2 VP candidates','28 Beijing: China sentences official Ma to death for spying','29 Brussels: NATO vows defence against space threat','30 Mexico City: US drone aided El Chapo Isidro capture','31 San Salvador: Bukele names 3 soldiers killed in Haiti','32 Ottawa: Pentagon rebukes Canada — 41.9% air fleet ready','33 Washington: US adds Megaspeed to trade blacklist','34 Kyiv: Zelensky urges Ukraine–Russia–US–Europe talks','35 Ras Al Khaimah: bus–truck crash kills 13','36 London: England record 5,258 heat deaths, summer 2026','37 Kourou: Ariane 6 lofts 36 Amazon satellites','38 Cikande: factory-fire toll rises to 26']
for j,a in enumerate(ALSO):
    col=j%2; row=j//2; T(500+col*254,716+row*13,a,F(SN,8),INK)
# ---- DATE CHECK ----
d.rectangle([16,900,1008,976],fill=(255,235,235),outline=RED,width=1)
T(24,906,'DATE CHECK',F(SNB,10),RED)
PARA(24,920,'Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.',F(SNB,9),968,11,INK,1)
PARA(24,934,'LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) · Nvidia brings back Huang, +31% (Mon 23 Nov) · EU 22nd sanctions package (Mon 23 Nov) · COP31 ends with no deal (Sun 22 Nov) · corvette Merkury sinks (Sat 22 Nov) · El Chapo Isidro arrested (Fri 20 Nov) · Cikande fire starts (Sat 21 Nov) · Trump hush-money appeal ruling (Mon 23 Nov).',F(SN,8),968,10,INK,2)
PARA(24,956,'NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) · MPR session picks VP (11 Dec) · Huawei sentence (Sep 2027) · Hasina returns (16 Dec).',F(SN,8),968,10,INK,1)
T(16,984,'Sources: dailysummaryof.com/world/2026-11-24 · Reuters · AP · CCDI · CAS · CMSA · UKMTO · market close.',F(SN,8),GREY)
T(16,996,'CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side\'s claim.  Scenes are drawn illustrations, not photographs.',F(SN,8),GREY)
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); img.save(OUT)
print('saved',OUT,img.size,os.path.getsize(OUT))
