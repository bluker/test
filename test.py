mk6ch0={'50':1547,'100':1493,'150':1438,'200':1381,'250':1321,'300':1256,'350':1183,'400':1097,'450':979}
mk6ch1={'150':1556,'200':1541,'250':1527,'300':1512,'350':1497,'400':1482,'450':1466,'500':1451,'550':1436,'600':1420,'650':1404,'700':1388,'750':1372,'800':1355,'850':1338,'900':1321,'950':1303,
'1000':1285,'1050':1266,'1100':1247,'1150':1227,'1200':1207,'1250':1186,'1300':1163,'1350':1140,'1400':1115,'1450':1088,'1500':1059,'1550':1027,'1600':991,'1650':947,'1700':886}
mk6ch2={'250':1559,'300':1551,'350':1543,'400':1535,'450':1527,'500':1519,'550':1510,'600':1502,'650':1494,'700':1485,'750':1477,'800':1468,'850':1460,'900':1451,'950':1443,'1000':1434,'1050':1425,
'1100':1417,'1150':1408,'1200':1399,'1250':1390,'1300':1381,'1350':1371,'1400':1362,'1450':1353,'1500':1343,'1550':1334,'1600':1324,'1650':1314,'1700':1304,'1750':1294,'1800':1284,'1850':1274,
'1900':1263,'1950':1252,'2000':1242,'2050':1230,'2100':1219,'2150':1207,'2200':1196,'2250':1184,'2300':1171,'2350':1158,'2400':1145,'2450':1132,'2500':1118,'2550':1103,'2600':1088,'2650':1072,
'2700':1056,'2750':1038,'2800':1019,'2850':999,'2900':978,'2950':954,'3000':926,'3050':893,'3100':848}
mk6ch0gd ={'50':5,'100':9,'150':14,'200':20,'250':27,'300':36,'350':49,'400':69,'450':112}
mk6ch1gd ={'150':1,'200':1,'250':2,'300':2,'350':3,'400':3,'450':3,'500':4,'550':4,'600':5,'650':5,'700':6,'750':6,'800':7,'850':8,'900':8,'950':9,'1000':10,'1050':11,'1100':12,'1150':13,'1200':14,
'1250':15,'1300':17,'1350':19,'1400':21,'1450':24,'1500':27,'1550':32,'1600':39,'1650':49,'1700':71}
mk6ch2gd ={'250':1,'300':1,'350':1,'400':1,'450':1,'500':1,'550':1,'600':1,'650':1,'700':2,'750':2,'800':2,'850':2,'900':2,'950':2,'1000':2,'1050':2,'1100':3,'1150':3,'1200':3,'1250':3,'1300':3,
'1350':3,'1400':4,'1450':4,'1500':4,'1550':4,'1600':4,'1650':4,'1700':5,'1750':5,'1800':5,'1850':5,'1900':6,'1950':6,'2000':6,'2050':7,'2100':7,'2150':7,'2200':8,'2250':8,'2300':9,'2350':9,'2400':10,
'2450':10,'2500':11,'2550':12,'2600':13,'2650':14,'2700':15,'2750':16,'2800':18,'2850':20,'2900':22,'2950':26,'3000':31,'3050':39,'3100':54}
mk6ch0hf = {'50':7.3,'100':3.7,'150':2.5,'200':1.9,'250':1.5,'300':1.3,'350':1.1,'400':0.9,'450':0.8} #50增量
mk6ch1hf = {'450':5.6,'700':3.6,'950':2.7,'1200':2.1,'1450':1.7,'1700':1.3} #250增量
mk6ch2hf = {'1700':3.7,'1900':3.3,'2100':2.9,'2300':2.7,'2500':2.4,'2700':2.2,'2900':1.9,'3100':1.6} #200增量
mk6ch1qy = {'450':0.6,'700':0.9,'950':1.3,'1200':1.7,'1450':2,'1700':2.3} #250增量 
mk6ch2qy = {'250':0.5,'400':0.8,'550':1.2,'700':1.5,'850':1.9,'1000':2.2,'1150':2.5,'1300':2.9,'1450':3.2,'1600':3.6,'1750':3.9,'1900':4.3,'2050':4.6,'2200':5,'2350':5.4,'2500':5.7,'2650':6,'2800':6.4,
'2950':6.6,'3100':6.8} #150增量
#海拔2000至5000米大气压字典 200增量
qybiao = {'2000':795,'2200':775,'2400':756,'2600':738,'2800':719,'3000':701,'3200':684,'3400':666,'3600':649,'3800':633,'4000':617,'4200':601,'4400':585,'4600':570,'4800':555,'5000':540} 


jxpd = 1
lspd = 2
while jxpd>0:
    jl = int(input("输入距离"))
    if jl<50 or jl>3100:
        print("射程超限")
    elif jl<150 and jl>=50:
        ch = 0
    elif jl<250 and jl>=150:
        ch = 1
    elif jl<3100 and jl>=250:
        ch = 2
    elif jl==3100:
        print("848,你这距离太悬了，建议别打")
        ch = 2
    else:
        print("bug")
    if lspd == 1:
        ch = float(input("隐藏选项，你想要几号装药?(0,1,2)"))
    print(int(ch),"几号装药")
    chb = ch
    if ch==0:
        ch = mk6ch0
        csjl = 50
        cha = mk6ch0gd
        chd = mk6ch0hf
    elif ch==1:
        ch = mk6ch1
        csjl = 150
        cha = mk6ch1gd
    elif ch==2:
        ch = mk6ch2
        csjl = 250
        cha = mk6ch2gd
    lmsj = jl-csjl
    while lmsj>=50:
        csjl =csjl+50
        lmsj = jl-csjl
        
    strcsjl =str(csjl)       
    qbc = ch.get(strcsjl)
    f1 = int(csjl)         #整数化初始射程
    f2 = f1+50           #前距离加50分划就是后距离
    f3 = str(f2)        #后距离化为字符串，好搜
    hbc = ch.get(f3)      #查找字典后距离对应的标尺
    f5 = qbc-hbc             #标尺差计算，要求高射界
    f6 = f5/50          #标尺差除分度值
    f7 = qbc-f6*lmsj       #前标尺减移动一米需要改变的密位乘距离减前距离
    print(qbc,round(f7),hbc,"三个距离标尺")
    jlc2 = 50
    bcc = f5
    jdms = "1"

#高度计算模块依赖距离标尺计算
 #未来会改为射界限制触发器?
    shuru3 = input('前方是高度计算，按1跳过，按2继续')
    if shuru3 =='1':
        gdjg = f7
        qbcb = qbc
        hbcb = hbc
        print(round(qbcb),round(gdjg),round(hbcb),"您跳过了高度计算")
    else:
        wg1 = input('我的高度')
        dg1 = input('敌人高度')
        wg2 =int(wg1)
        dg2 =int(dg1)
        if wg2>dg2:
            shuru2 = '高打低'
            gdc1 = wg2-dg2
        elif wg2<dg2:
            shuru2 = '低打高'
            gdc1 = dg2-wg2
        elif wg2 ==dg2:
            print("你小子挺闲,没高度差")
            shuru2 = '高打低'
            gdc1 = 0
        else:
            print("你很厉害，我的程序被你整出了bug")
        gdxza = cha.get(strcsjl)
        gdxzb = cha.get(f3)
        if gdxza==gdxzb:
            gdxz = gdxza
        elif gdxza!=gdxzb:
            gdmwc = gdxzb-gdxza
            gdxz = gdxza+gdmwc/50*lmsj
        print(gdxz)
        mwxz =gdxz/100*gdc1
        if shuru2 =='高打低':
            gdjg = f7+mwxz #前标尺，标尺，后标尺一起算
            hbcb = hbc+mwxz
            qbcb = qbc+mwxz
        elif shuru2 =='低打高':
            gdjg = f7-mwxz
            hbcb = hbc-mwxz
            qbcb = qbc-mwxz
        else:
            print("程序出bug了，请汇报")
        print(round(qbcb),round(gdjg),round(hbcb),"高度标尺")
    if qbcb>=1564: #废弃的射界限制触发器，未来可能重启?
        print("遇到装药极限射程，请以最新结果为准，重新输入数据")
        lspd = 1
    else:
        jxpd = jxpd-1
#大气压模块，可以单独使用，去和其他程序整合
if shuru3 =='2': #判断用户有没有跳过高度修正模块，全自动大气压计算依赖高度修正模块
    print("大气压全自动计算可用")    
    if wg2<=0: #如果我的高度低于海平面
        cgbc2 = gdjg
        dqy = 1013.4
    else:
        if wg2<=2000:
            beishu = wg2/12 #海拔2000米以下，每上升12米大气压下降1毫米汞柱 简单的数学运算
            gongzhu = 1013.25/760
            dqypy = beishu*gongzhu
            dqy = 1013.25-dqypy
            print(dqy,"自动计算出的大气压")
        elif wg2>2000 and wg2<=5000:
            csjl = 2000
            lmsj = wg2-csjl
            while lmsj>=200:
                csjl =csjl+200
                lmsj = wg2-csjl
            strcsjlb =str(csjl)
            qqy = qybiao.get(strcsjlb)
            qya = int(csjl)         #整数化初始射程
            qyb = qya+200           
            qyc = str(qyb)        #后距离化为字符串，好搜
            hqy = qybiao.get(qyc)      #查找字典后距离对应的标尺
            bqyc = qqy-hqy             
            qyd = bqyc/200          #标尺差除分度值
            dqy = qqy-qyd*lmsj+10       
            print(dqy,"自动计算出的大气压")
        elif wg2>5000:
            gdpya = wg2-5000
            dqy = 540-gdpya/100*5.2
            print(dqy,"自动计算出的大气压，因为海拔大于五千，所以可能不准")
        else:
            print("自动气压计算bug")
    if chb==0: #根据装药调射表字典 以前需要手动输入大气压和修正米 现在自动完成
        dqym = 0.1
        print(dqym)
    elif chb==1:
        csjl = 450
        lmsj = jl-csjl
        while lmsj>=250:
            csjl =csjl+250
            lmsj = jl-csjl
        che = mk6ch1qy
        csjlstr = str(csjl)
        dqym = che.get(csjlstr)
        print(dqym)
    elif chb==2:
        csjl = 250
        lmsj = jl-csjl
        while lmsj>=150:
            csjl =csjl+150
            lmsj = jl-csjl
        che = mk6ch2qy
        csjlstr = str(csjl)
        dqym = che.get(csjlstr)
        print(dqym)
    else:
        print("大气压模块装药判断错误")
    bzdqy = 1013.25
    if dqy>bzdqy:
        chazhi = dqy-bzdqy
        bfs = chazhi/bzdqy*100 #计算气压变化了百分之多少
        xzm = bfs*dqym   #百分数乘修正米等于要修的米数
        slm = jlc2/bcc
        xzmil = xzm/slm  #修正米数转化为密位
        cgbc2 = gdjg-xzmil
        qbcc = qbcb-xzmil
        hbcc = hbcb-xzmil
        print(round(qbcc),round(cgbc2),round(hbcc),"标尺")        
    elif dqy<bzdqy:
        chazhi = bzdqy-dqy
        bfs = chazhi/bzdqy*100
        xzm = bfs*dqym
        slm = jlc2/bcc
        xzmil = xzm/slm
        cgbc2 = gdjg+xzmil
        qbcc = qbcb+xzmil
        hbcc = hbcb+xzmil
        print(round(qbcc),round(cgbc2),round(hbcc),"标尺")
    else:
        print("bug")
else:
    print("跳过了大气压计算")
    cgbc2 = gdjg #如果跳过大气压，保证后面不出错
    hbcc = hbcb
    qbcc = qbcb
#给用户1mps横风修正参考值    
if chb==0: #装药判断做反应 相当于照搬计算公式但射表数据字典给
    fp1 = chd.get(strcsjl)
    print(fp1,"1米每秒侧风修正密位")
elif chb==1:
    csjl = 450
    lmsj = jl-csjl
    while lmsj>=250:
        csjl =csjl+250
        lmsj = jl-csjl
    chd = mk6ch1hf
    csjlstr = str(csjl)
    fp1 = chd.get(csjlstr)
    print(fp1,"1米每秒侧风修正密位")
elif chb==2:
    csjl = 1700
    lmsj = jl-csjl
    while lmsj>=200:
        csjl =csjl+200
        lmsj = jl-csjl
    chd = mk6ch2hf
    csjlstr = str(csjl)
    fp1 = chd.get(csjlstr)
    print(fp1,"1米每秒侧风修正密位，参考，数据较保守")
else:
    print("风偏模块装药判断错误")
    
#炸点修正量模块，目前只提供修多少，只计算量，不算方向，需要人类自己算，不提供方向也有好处，省事，少了适配兼容
bla = 2 #多次修正
while bla >1:
    print("下方是炸点修正模块，修正量程序告诉你，往哪修自己想")    
    pc1 = input("输入前后偏差距离\n输入 jc 可以使用夹叉法\n输入 pc 可以用带方向的偏差法")
    if pc1=='jc':
        print("夹叉法试射，只能在观炮夹角小于30度时使用，最好火炮，观察员，目标按顺序连成三点一线，注意观测第三发炮弹")
        jcsx = int(input("输入基础射向"))
        b3a = 1
        cgbc = hbcc #与气压模块的后标尺连接 如果炸点修正模块挨着的模块不是高度模块，需要改
        cgsx = jcsx
        xzcishu = 0
        fxbei = 1
        zuicjc = input("手动输入最初夹叉，按enter键跳过，如果跳过，最初夹叉为50米")
        if bool(zuicjc):
            zuicjc = float(zuicjc)
            hzuicjc = float(zuicjc)
        else:
            zuicjc = 50
            hzuicjc = 50
        while b3a>0:
            fx = input("远弹按w，近弹按s，炸点偏左按a，偏右按d，用wasd表示方向，按1退出夹叉法计算")
            if xzcishu!=0 and fxbei!=fx: #判断方向符号不同是否形成对立 比如前后对立 但右前不是
                if fx in "ws" and fxbei in "ws": #判断前后对立
                    zuicjc = zuicjc/2 #如果对立，最初夹叉除2
                    hzuicjc = hzuicjc
                elif fx in "ad" and fxbei in "ad": #判断左右对立
                    zuicjc = zuicjc
                    hzuicjc = hzuicjc/2
                else:
                    print("调试") #调试用的，不用管它
            s1m = jlc2/bcc    
            h1m = jl/1000
            sxzL = zuicjc/s1m
            hxzL = hzuicjc/h1m
            if fx=="w":
                cgbc = cgbc+sxzL
            elif fx=="s":
                cgbc = cgbc-sxzL
            elif fx=="a":
                cgsx = cgsx+hxzL
            elif fx=="d":
                cgsx = cgsx-hxzL
            else:
                b3a = 0
                bla = 0
                print("你退出了夹叉法计算")
            if cgsx<0: #过0判断
                cgsx = 6400+cgsx
            elif cgsx>6400:
                cgsx = cgsx-6400
            fxbei = fx
            xzcishu = xzcishu+1
            if b3a>0:
                print(round(cgsx),"修正后的射向")
                print(round(cgbc),"修正后的标尺")
                print(zuicjc,hzuicjc)
    elif pc1=='pc':
        print("进入偏差法计算，注意观测第三发炮弹")
        jcsx = int(input("输入基础射向"))
        cgbc = hbcc #连接前一个模块的结果
        cgsx = jcsx
        b4a = 1
        print("提示：远弹按w，近弹按s，炸点偏左按a，偏右按d，用wasd表示方向，使用-分开方向和距离，例如w-100，表示远弹，误差100米")
        while b4a>0:
            pca = input("输入纵向偏差，例如w-100，按1退出偏差法计算")
            if pca=="1":
                b4a = 0
                bla = 0
                print("你退出了带方向的偏差法计算")
            else:
                pcb = input("输入横向偏差，例如a-50")
                zfg = pca.split("-",1) #字符串切割
                hfg = pcb.split("-",1)
                fxa = zfg[0]
                fxb = hfg[0]
                zpc = int(zfg[1])
                hpc = int(hfg[1])
                s1m = jlc2/bcc    
                h1m = jl/1000
                print(s1m,"竖一密几")
                print(h1m,"横一密几")
                sxzL = zpc/s1m
                hxzL = hpc/h1m
                if fxa=="w":
                    cgbc = cgbc+sxzL
                elif fxa=="s":
                    cgbc = cgbc-sxzL
                else:
                    print("bug5")
                if fxb=="a":
                    cgsx = cgsx+hxzL
                elif fxb=="d":
                    cgsx = cgsx-hxzL
                else:
                    print("bug6")
                if cgsx<0: #过0判断
                    cgsx = 6400+cgsx
                elif cgsx>6400:
                    cgsx = cgsx-6400
                print(round(cgsx),"修正后的射向")
                print(round(cgbc),"修正后的标尺")
    
    else:               
        pc2 = input("左右偏差距离")    
        pc3 = int(pc1)
        pc4 = int(pc2)
        s1m = jlc2/bcc    #距离差除标尺差就是前后方向一密位动几米，我简称为一密几，意思是一密位移动几米
        h1m = jl/1000    #距离除一千就是横向一密位动几米
        sxzl = pc3/s1m    #想修正的距离除一密几就是要变的密位
        hxzl = pc4/h1m
        print(s1m,"竖一密几")
        print(h1m,"横一密几")
        print(sxzl,"前后修正量+-")
        print(hxzl,"左右修正量+-")
        #多次修正模块
        blb = input("还需要炸点修正吗？ 跳过扣1，多次修正扣2")
        if blb=="1":
            bla = 0
            print("你跳过了多次修正")
        elif blb=="2":
            bla+1    
