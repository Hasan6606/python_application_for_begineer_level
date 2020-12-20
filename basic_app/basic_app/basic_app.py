print("Hasan Hüseyin AYGAR")  #bu satırda ise print metodu dahilinde "" bu iki ifade arasında yazılı olan metini ekrana yazdırır.
 #  '#' bu ifade sayesinde ise yorum satırı ekleriz ki daha verimli çalışmalar ve başka kişiler algoritmamızı daha iyi anlamaları için kullanılır.
 
"""
Çok satırlı yorumlarınızda ise üst ve alt kısıma üç adet çift tırnak koyarak oluşturabilirsiniz.
"""
# ctrl+k+c yaparak seçilen kısımıda yorum satırı yapabilirsiniz.
# ctrl+k+u yaparak seçilen kısımıda yorum satırı kaldırabilirsiniz.
#Matematiksel İşlem Operatörleri
# *(Çarpma),/(Bölme),+(Toplama),-(Çıkarma),%(Mod Alma)
#print(2+2.5) #bu satırda belirtmiş olduğumuz basit bir matematiksel işlemleri hesaplayıp ekran çıktısı olarak yansıtır.
#print(2*3+4) #bu satırda ise ifade ettiğimiz matematiksel işlemde program derleyicisinin matematiksel işlem önceliğini dikkate alarak işlem yapılmıştır.

###------Değişkenler------



# Değişkenler kullanıcıdan alınan girdileri sayısal veya metinsel olabilir.Programın arka planında tanımlamış oldumuz değişkenlerde tutar ve girdisine göre programın mantığı çerçevesinde bir çıktı olarak atamasına sebep olur.
# Değişkenlerde türkçe karakter(i,ö,ç,ğ,ü) kullanmamalısınız.
#Grup çalışması yapılan programlarda değişkne isimleri net ve anlaşılır olmalı ki kod yapınıza bakan kişi değişkeninizin mantığını daha iyi anlamalıdır.
#Büyük küçük harf duyarlılığı mevucttur.Yani (AGE=20) ve (age=20).Her ikisinin değerleri aynı olsada ikiside farklı isimlendirilmiş değişkenlerdir.
#Değişkenler arasında boşluk OLAMAZ.



#numberr=30 # 'numberr'adlı değişkenimizin içine 30 sayısını atadık.Bu değişkenimiz int (tamsayı) türünden değişkendir.
#numberr2=5.7# 'numberr2'adlı değişkenimizin içine 5.7 sayısını atadık.Bu değişkenimiz float (ondalıklı sayı) türünden değişkendir.
#numberr+=20  #burda ise 'numberr' adlı değişkenimize 20 değer eklemiş olduk.(numberr =numberr + 20)==(numberr+=20) sonuçları aynı olan işlemlerdir.
#ispython= True #Burda ise 'ispython' adında  bool türünden değişken değerinin 'True' olarak atadık.Bu değişken türünde ise boolen cebri ile alakalı işlemlerinizde bu türü kullanabilirsiniz.
#print(numberr)


#String Harf veya Kelime Çekme
#name="hasan" # 'name'adlı değişkenimizin içine 'hasan' kelimesini atadık.Bu değişkenimiz string (metinsel) türünden değişkendir.
#surname=' aygar' # 'surname'adlı değişkenimizin içine 'aygar' kelimesini atadık.Bu değişkenimiz string (metinsel) türünden değişkendir.
#print(name+surname) #Bu satırda ise yukarıda name ve surname adlı metinleri yan yana birleştirmek için değişken isimlerini print içine yazıp arasına + sembolünü eklerseniz iki farkli metinsel değişkeni ekrana yazdırabilirsiniz.
#print(name +'\n'+surname) #Bu satırda ise '\n' ifadesini kullandığımız yerden sonraki kısmı yeni bir satırda yazdırmasını sağlar.
#print(len(name))#Bu satırda ise "len(name)" yapısıyla name değişkeninin kaç karaktere sahip olduğunu öğrenmiş olduk.
#print(name[2]) #Bu satırda ise "name" adlı değişkenimizin içindeki 2. İNDİS değerini alıp yazdırırız.İndis numaraları 0 dan başlar bunu unutmamalıyız.
#print(name[2:4]) #Bu satırda ise "name" adlı değişkenimizin içindeki 2.-4. İNDİS  değerini dahil ederek alıp yazdırırız.
#print("My name is {0} {1}".format(name,surname)) #Bu satırda ise 'name ve surname' adlı değişkenleri print içindeki metinin yanına {} koyup buraya değişken geleceğini belirtiyoruz.Süslü parantez içindeki İNDİS numarasına göre sıralı olarak yazdırırız yada yazmazsanız dahi defult olarak parantez içindeki değişkenleri sol baştan sırasına göre yazdırır, sonra ".format()" yapısındaki parantez içine gelicek değişkeni tanımlıyıp ekrana farklı ve kısa yoldan yazdırabilirsiniz.
#resultt=200/700
#print("the result is {r:1.3}".format(r=resultt))#Burda ise yukarıdaki 'resultt' değişkenindeki işlemini ekranama ".format()" ile yazdırdık ama burda 'resultt' değişkenini 'r' harfinin içine atadık sonra '{r:1.3}' ifadesi ile yazdıracağımız ifadenin ilk kısmında bir basamak ve virgülden sonraki üç basamağını yazdırdık.
#print(f'My name is {name} {surname}') #Bu satırdaki kodda ise " " ifadenin başına 'f' yazıp süslü parantezlerin içine yazdırmak istediğimiz değişkenlerin ismini yazıp bu yöntemlede ekrana değişkenlerinizi yazdırabilirsiniz.

# --String Methodları---


#message="Hello,I am hasan."
#message=message.upper()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin içindeki karakterilerin hepsini büyük harflerle yazdırmak için "upper()" kullandık.
#message=message.lower()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin içindeki karakterilerin hepsini küçük harflerle yazdırmak için "lower()" kullandık.
#message=message.title()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin içindeki her kelimenin ilk harfini büyük harfle  yazdırmak için "title()" kullandık.
#message=message.capitalize()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin içindeki ilk kelimenin ilk harfini büyük yazdırmak için "capitalize()" kullandık.
#message=message.strip()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin başındaki boşluk karakterini silmek  için "strip()" kullandık.
#message=message.split()#Burdaki kodumuzda ise yukarıdaki 'message' değişkeninin boşlukları referans alarak içindeki kelimeleri dizi elemanları gösterir gibi yazdırmak   için "split()" kullandık.İstenildiği dahilinde () içine  referans almasını istediğimiz karakteri "" içinde yazarsanızda parçalayabilirsiniz.
#message=' '.join(message)#Burdaki yukarıdaki parçalanmış eski durumuna getirmek için (''.join(message)) kullanılır ' ' bu ifadenin içine ne yazarsanız arasına ne koyarsanız onu aralara yazarak eski cümleye dönüştürür.Eğer aradığınız kelime yoksa -1 değeri atar.
#index=message.find('hasan')#Burdaki kodda ise 'message' değişkeninde ' ' arasında yazılan kelimenin kaçıncı İNDİSİNDE başladığını "index" değişkenine atar.
#indexx=message.startswith("H") #Burdaki kodda 'message' adlı değişkenin 'H' harfiyle başlamasını kontrol ederiz eğer H harfiyle başlarsa TRUE değerini atar başlamazsa FALSE değerini atar.
#indexx2=message.endswith("H") #Burdaki kodda 'message' adlı değişkenin 'H' harfiyle bitmesini kontrol ederiz eğer H harfiyle biterse TRUE değerini atar başlamazsa FALSE değerini atar.
#indexx3=message.replace('hasan','Ahmet') #Bu kodda ise ilk ' ' kısımdaki kelimeyi ikinci kısımdaki ' ' yazılanı değiştirir. 
#print(index)
#print(indexx)
#print(indexx2)
#print(indexx3)



#INPUT
#x=input('Lütfen birinci sayıyı giriniz:') #Burda ise kullanıcıya parantez içindeki mesajı yazdırıp ve girilen değeri metinsel olarak 'x' isimli değişkende tutmaktadır.
#y=input('Lütfen ikinci sayıyı giriniz:')  #Burda ise kullanıcıya parantez içindeki mesajı yazdırıp ve girilen değeri metinsel olarak 'y' isimli değişkende tutmaktadır.
#print(type(x)) #Burda ise x değişkeninin türünü ekrana yazdırıcaz.
#print(type(y)) #Burda ise y değişkeninin türünü ekrana yazdırıcaz.
#toplam=int(x)+int(y) #Bu satırda kullanıcıdan alınan değeri metinsel olarak aldığımız için sayısal tür yapıp 'toplam' adındaki değişkene sayıların toplamını atmış olduk.
#print(toplam)  #Burda ise 'toplam' adındaki değişkeni ekrana yazdırdık.




#DEĞİŞKEN DÖNÜŞÜM
#x=5.4
#y=3
#y=float(y)# Bu satırda ise tam sayı değerine sahip olan 'y' değişkenini float türüne değiştirip tekrardan 'y' değişkenine atadık.Ekran çıktısı olarak '3.0' yazdırması float türüne dönüştürmemizden dolayıdır.
#x=int(x) # Bu satırda ise ondalık sayı  değerine sahip olan 'x' değişkenini int türüne değiştirip tekrardan 'x' değişkenine atadık.Ekran çıktısı olarak '5' yazdırması int türüne dönüştürmemizden dolayıdır.Ondalık kısmını almaz sadece tam sayı kısmını alır.
#print(y) #Ekrana 'x' değişkeni yazdırdık.
#print(x) #Ekrana 'y' değişkeni yazdırdık.
 
#SET
#benim_listem=["bir",2,True,5.6] #"benim_listem" adlı bir liste tanımlayıp içine değerler atadık.
#print(benim_listem[1]) #Burda ise "benim_listem" adlı listenin 1. indisindeki "2" ifadesini ekrana yazdırdık.
#benim_Listem=[6,"nine","ein"] #"benim_Listem" adlı bir liste tanımlayıp içine değerler atadık.
#liste_toplam=benim_listem+benim_Listem #"liste_toplam" adlı değişkenin içine "benim_listem+benim_Listem" ifadesiyle iki listeyi birleştirip tek bir liste haline getirdik.
#print(liste_toplam) #"liste_toplam" ifadesini yazdırdık.

#TUPLE
#tuple=(1,"iki",3) #Yan taraftaki tuple nesnesi sadece count ve index metodlarını kullanabilirsiniz.Eleman ekleme veya silme gibi değişiklik işlemleri yapamazsınız.
#print(tuple[1]) #tuple daki 1. indisindeki elemanı ekrana yazdırmış olduk.
#print( 3 in tuple)#Burdaki kod yapısında ise tuple içinde 3 var mı diye sorgulatıyoruz.Sonuç boolen(true,false) olarak değer atar.

#SET
#thisset = {"apple", "banana", "cherry"} #içinde elemanları olan set yapısını tanımlaadık.
#thisset.add("watermelon") #set yapısının içine rastgele bir indisin içine "watermelon" ekler.
#thisset.update(["MOUSE","KEYBOARD","HEADPHONE"])#Burda set yapısında güncelleme yaparak çoklu ekleme ya da çoklu değişiklik yaptık.
#thisset2={1,2,3} #"thisset2" adlı farklı bir set tanımladık.
#thisset3=thisset.union(thisset2) #".union()" yapısı sayesinde iki set yapsını karşık indislere atıyarak yeni bir set yapısı tanımladık. 
#print(thisset3) #Yeni set yapımızı ekrana yazdırdık.

#for x in thisset: #Bu for döngüsü bulunduğu satırdaki şartlar sağlandığı sürece alttaki kod yapısını çalıştırır.
 # print(x)
  #break #Bu ifade ise for döngüsünün algoritması bu ifadeyi gördüğü yere kadar olan tüm kod satırlarını çalıştırır.

#

#Dictionary

#ogrenciler={} #Burda 'ogrenciler' adında bir dictionary tanımladık.
##Alltaki dört satırda ise kullanıcadan öğrenci bilgilerini input yardımıyla sol taraftaki değişkenlere atamasını sağladık.
#ogrno=input("Öğrenci Numarsını giriniz:")
#ograd=input("Öğrenci Adını  giriniz:")
#ogrsoyad=input("Öğrenci Soyadını giriniz:")
#ogrtn=input("Öğrenci Telefon Numarsını giriniz:")
#ogrenciler[ogrno]={   #Bu ifadede ise ogrenciler adındaki dictionary yapısını öğrenci numarasını bağlı olarak yeni bir dictionary yapısı oluşturduk.
#    'Ad':ograd,
#    'Soyad':ogrsoyad,
#    'Telefon_No':ogrtn
#    }
#print(ogrenciler) 
#print("*"*75)
#ogrencinumarasi=input("Bulmak istediğiniz öğrencinin numarasını giriniz:") #Burda ise kullanıcıdan girdiğimiz öğrenci değerlerini ekrana yazdırmak öğrenci numarasını alıp karşılık gelen numaranın alt dictionary deki bilgisine erişip yazdırmak için.
#yazdirma=ogrenciler[ogrencinumarasi]#burda ise "yazdirma" adındaki değişkenin içine aldığımız öğrenci numarasının tüm bilgilerini aktarmış olup alt satırda belirlenen formatta yazdırdık.
#print(f"Aradığınız {ogrencinumarasi} nolu öğrencinin adı:{yazdirma['Ad']} soyadı:{yazdirma['Soyad']} ve Telefon Numarası:{yazdirma['Telefon_No']}")

#sayi=input("sayi giriniz:") # Kullanıcıdan sayı girmesini istiyoruz.Girilen sayıyı "say değişkenine atıyoruz."
#result=(int(sayi)>0) and (int(sayi)%2==0) #"result" adlı değişkenin içinde "sayi" adlı değişkenin sıfırdan büyük olmasını ve 2 ile mod alınıp ve bağlacı ile birleştirip mantıksal bir sonuç elde ederiz.
#print(result) #"result" adlı değişken mantıksal sonucunu sözel olarak ekrana yazdırırız.
