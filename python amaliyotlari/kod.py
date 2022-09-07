


def tubmi(x):
    """bU  FUNKSIYA SONNI TUB LIKKKA TEKSHIRADI"""
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    if x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True





def  sanoq(min,max,qadam=''):
    """bU FUNKSIYA RANGE FUNKSIYASI BILANN BIR XIL ISHLAYDI"""
    top=[]
    if min<max:
        while(min<max):
            if qadam :
                top.append(min)
                min+=qadam
            else:
                top.append(min)
                min+=1 
    else:
        while(min>max):
            if qadam :
                top.append(min)
                min+=qadam
            else:
                top.append(min)
                min+=1 
    return top 



def pifagor(katet1,katet2):
    """Bu  funksiya pifagor teoremasi"""
    c = (((katet1)**2+(katet2)**2))**(1/2)
    return c




def ekuB(son1,son2):
    """bu funksiya EKUB ni xisoblaydi"""
    while son1 != 0 and son2 != 0:
        if son1 > son2:
            son1 %= son2
        else:
            son2 %= son1
    y = son1+son2
    return y


def ekuK(son1,son2):
    """bu funksiya EKUB ni xisoblaydi"""
    kopay=son1*son2
    while son1 != 0 and son2 != 0:
        if son1 > son2:
            son1 %= son2
        else:
            son2 %= son1
    y = son1+son2
    x = kopay//y
    return x




def faktariyal(x):
    """Bu funksiya faktatiyalni xisoblaydi"""
    fac = 1
    for n in sanoq(1, x+1):
        fac*=n
    return fac

# from random import *
# def suniy(x):
#     """Bu fuksiya oyinnni o'z ichiga  jamlagan funksiya xisoblanadi """
#     taxminiy = randint(1,x);
#     print(f"Man 1 dan {x} gacha bir son o'yladim \
# shuni topishga  xarakat qilib ko'ring ? ")
#     urunish = 0
#     while True:
#         urunish += 1
#         savol = int(input("Man nechini o'yladim ? > "))
#         if taxminiy < savol:
#             print(f" Xato {savol} dan kichikroq son kiritib ko'ring ")
#         elif taxminiy > savol:
#             print(f" Xato {savol} dan kattaroq son kiritib ko'ring ")
#         else:
#             break
#     print("Siz to'g'ri topdiz 😊")
print(ekuB(15,10))

#
