#kullanacağımız grafikleri import ettik.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('Housing.csv')#csv dosyamızı okuyoruz.

#ödev kontrolü daha rahat olsun diye her sorunun çıktısını ayrı ayrı veren bir sistem hazırladım.

a=int(input("Ödevin kacinci sorusunun ciktisini gormek istersiniz? "))

if a==1: 
    #regresyon kullanarak çizilecek grafiğin x ve y eksenlerini belirleyip türünün regresyon olduğunu belirtiyoruz.
    sns.jointplot(x="area",y="price", data=df, kind="reg")   
    plt.title("Area ve Price ilişkisi", pad=1)
    sns.jointplot(x="bedrooms",y="price", data=df, kind="reg")
    plt.title("Bedrooms ve Price ilişkisi", pad=1)
    sns.jointplot(x="stories",y="price", data=df, kind="reg")
    plt.title("Stories ve Price ilişkisi", pad=1)


elif a==2:
    plt.figure(figsize=(12,4)) #grafiğin eni ve boyunu belirliyoruz
    plt.subplot(1,2,1) #yan yana iki grafik yapacağımız için bunun ayarlamasını yapıyoruz. Girdiğimiz değerlerin anlamı sırasıyla şu şekilde
                       #(1 satırdan oluşacak, satırda 2 grafik olacak, bu grafik o iki grafikten 1.si)
    sns.barplot(x="bedrooms",y="price", data=df) #grafik ayarlamaları
    plt.title("bedroom sayisina göre ortalama ev fiyatlari")
    plt.subplot(1,2,2)
    sns.barplot(x="furnishingstatus",y="price", data=df)
    plt.title("furnishingstatus durumuna göre ortalama ev fiyatlari")
    plt.tight_layout()


elif a==3:
    #bu satırda str değerleri olan değişkenler elenmiş bir dict oluşturup bunu dataframe tipine çeviriyoruz.
    newdf=pd.DataFrame({"price":df['price'],"area":df['area'],"bedrooms":df['bedrooms'],"bathrooms":df['bathrooms'],"stories":df["stories"],"parking":df['parking']})
    #yeni df'teki değerlerin korelasyonunu hesaplıyoruz
    corrmatrix = newdf.corr()
    #heatmap türündeki grafik için ayarlamalar
    plt.figure(figsize=(10,8))
    sns.heatmap(corrmatrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})    
    plt.title('Korelasyon Matrisi')

else:
    print("1,2,3 değerlerinden birini giriniz")
#grafikleri ekrana veren fonksiyon
plt.show()

#KULLANILAN FONKSİYONLAR BAZI DEĞERLERİ ÜSLÜ SAYI OLARAK İFADE EDİYOR. GRAFİKTE BUNA DİKKAT EDİNİZ