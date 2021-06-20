star=['水瓶','雙魚','牡羊','金牛','雙子','巨蟹','獅子','處女','天秤','天蠍','射手','魔羯']
a,b=input('輸入月 日:').split(' ')
a=int(a)
b=int(b)
if((a==1 and b>=21 and b<=31) or (a==2 and b>=1 and b<=18)):
    print(star[0])
elif((a==2 and b>=19 and b<=29) or (a==3 and b>=1 and b<=20)):
    print(star[1])
elif((a==3 and b>=21 and b<=31) or (a==4 and b>=1 and b<=20)):
    print(star[2])
elif((a==4 and b>=21 and b<=30) or (a==5 and b>=1 and b<=21)):
    print(star[3])
elif((a==5 and b>=22 and b<=31) or (a==6 and b>=1 and b<=21)):
    print(star[4])
elif((a==6 and b>=22 and b<=30) or (a==7 and b>=1 and b<=22)):
    print(star[5])
elif((a==7 and b>=23 and b<=31) or (a==8 and b>=1 and b<=23)):
    print(star[6])
elif((a==8 and b>=24 and b<=31) or (a==9 and b>=1 and b<=23)):
    print(star[7])
elif((a==9 and b>=24 and b<=30) or (a==10 and b>=1 and b<=23)):
    print(star[8])
elif((a==10 and b>=24 and b<=31) or (a==11 and b>=1 and b<=22)):
    print(star[9])
elif((a==11 and b>=23 and b<=30) or (a==12 and b>=1 and b<=21)):
    print(star[10])
elif((a==12 and b>=22 and b<=31) or (a==1 and b>=1 and b<=20)):
    print(star[11])