
# 191307001 Mehmet Arda YÜKSEL - Vize Proje -2021

def konum_Bulucu(x,okunan_Labirent_Guncel):
    '''
        DOCSTRING:Bu fonksiyon, parametrelerinde belirtilen karakter ve list of list için ;
                  matrix'de karakteri arar ve matrix[x][y] gibi (x,y) konumunu bir dictionary yapısına kaydeder.
        Parametreler: x:Konumu aranan karakter , okunan_Labirent_Guncel:Aramanın yapılacağı List of List.
    '''

    Satir = -1

    for eleman in okunan_Labirent_Guncel:
        Satir = Satir + 1
        if eleman.find(x) != -1:
            Sutun = eleman.find(x)
            break

    konumlar[x]["satir"]=Satir
    konumlar[x]["sutun"]=Sutun


def matrix_create(x,y,w):
    '''
        DOCSTRING:Bu fonksiyon, belirtilen satır ve sutun sayısında list of list(matrix) oluşturur ve döndürür.
        Parametreler: x:satır sayısı, y:sütun sayısı  w:default karakter.
    '''

    list_of_list=[]
    for row in range(x):
      inner_list=[]
      for col in range(y):
            inner_list.append(w)
      list_of_list.append(inner_list)
    return (list_of_list)


def yolu_bul(x,y,labirent_Matrix,labirent_Matrix_Cozum,Ending):

    '''
        DOCSTRING:Bu fonksiyon, belirtilen başlangıç ve varış noktası için labirent matrixinde duvarları, sınırları ve
                  geçtiği yolları göz önünde bulundurarak başlangıçtan bitişe doğru bir yol bulur.
        Parametreler: Başlangıç konumu:(x,y) , labirent_Matrix:labirent matrixi,
                      labirent_Matrix_Cozum: Çözüm yolunu net bir şekilde kaydeden matrix, Ending: Bitiş noktası.
    '''

    if labirent_Matrix[x][y]==Ending:
        print(f"Bulundu {x},{y}")
        labirent_Matrix_Cozum[x][y] = 1
        return True
    elif labirent_Matrix[x][y]=="W":
        print(f"Duvar : {x},{y}")
        return False
    elif labirent_Matrix[x][y]=="V":
        print(f"Ziyaret edildi:{x},{y}")
        return False

    print(f"Ziyaret ediliyor : {x},{y}")
    labirent_Matrix[x][y]="V"

    if((y<matrixSutunSayisi-1 and yolu_bul(x,y+1,labirent_Matrix,labirent_Matrix_Cozum,Ending))
        or(x<matrixSatirSayisi-1 and yolu_bul(x+1,y,labirent_Matrix,labirent_Matrix_Cozum,Ending))
        or(y>0 and yolu_bul(x,y-1,labirent_Matrix,labirent_Matrix_Cozum,Ending))
        or(x>0 and yolu_bul(x-1,y,labirent_Matrix,labirent_Matrix_Cozum,Ending))):
        labirent_Matrix_Cozum[x][y] = 1
        return True
    return False


if __name__ == '__main__':

    # 1.KISIM:
    print("****KISIM 1****")
    # İlgili text dosyası oluşturulup Labirentin içine yazılması.
    girdi_file=open("girdi.txt","w",encoding="utf-8")
    girdi_file.write("WPPWWW\n"
               "WWPWPS\n"
               "WWPWPW\n"
               "PPPPPW\n"
               "FWPWWW\n"
               "WPPPPW")
    girdi_file.close()


    # Girdi.text dosyasından labirent bilgilerinin okunup kaydedilmesi.
    girdi_file=open("girdi.txt","r",encoding="utf-8")

    okunan_Labirent=girdi_file.readlines()
    girdi_file.close()
    okunan_Labirent_Guncel=[]
    print(f"Okunan Labirent listesi: {okunan_Labirent}")


    # Labirentin ham bilgilerinin tutulduğu "okunan_Labirent" adlı listenin satır ve sütun sayılarını tespit etme.
    matrixSatirSayisi=len(okunan_Labirent)
    matrixSutunSayisi=len(okunan_Labirent[len(okunan_Labirent)-1])

    # Bulunan satır ve sütun sayılarına göre;
    # labirent_Matrix ve çözümünün tutulacağı labirent_Matrix_Cozum 'ün oluşturulup tanımlanması.
    labirent_Matrix = matrix_create(matrixSatirSayisi, matrixSutunSayisi, "")
    labirent_Matrix_Cozum = matrix_create(matrixSatirSayisi, matrixSutunSayisi, 0)

    # Labirent bilgilerinin tutulduğu listenin "\n" lerden temizlenmesi.
    for item in okunan_Labirent:
        okunan_Labirent_Guncel.append(item.rstrip())

    # Labirent matrixinde başlangıç ve bitiş gibi belli noktaların satır ve sütun bilgilerinin tutulması için
    # Bir Dictionary yapısının oluşturulması.
    konumlar={ "F":{"satir":0,"sutun":0 },"S":{"satir":0,"sutun":0} }

    # Başlangıç ve bitiş noktalarının konum_Bulucu fonksiyonu aracılığıyla konumlarının bulunması.
    # Konumları "konumlar" adlı dictionary yapısına kaydetme işlemi fonksiyonun içinde gerçekleşmektedir.
    konum_Bulucu("F",okunan_Labirent_Guncel)
    konum_Bulucu("S",okunan_Labirent_Guncel)
    print(f"Güncellenmiş Okunan Labirent listesi: {okunan_Labirent_Guncel}")

    # Nihai "labirent_Matrix"in her [x][y] konumuna "W","S","F","P" gibi labirent özelliklerini belirten karakterlerin
    # teker teker yerleştirilmesi.
    y=0
    for x in range(len(okunan_Labirent_Guncel)):
        y=0
        for i in okunan_Labirent_Guncel[x]:
            labirent_Matrix[x][y]=i
            y=y+1

    print(f"Nihai Labirent Matrixi : {labirent_Matrix}")

    # Labirentin çözülmesi.
    yolu_bul(konumlar["S"]["satir"],konumlar["S"]["sutun"],labirent_Matrix,labirent_Matrix_Cozum,"F")

    # Çözümü "1" ler ve "0" lar halinde içinde yer alan çözüm matrix'ine sonradan "S" ve "F" bilgilerinin yerleştirilmesi.
    labirent_Matrix_Cozum[konumlar["S"]["satir"]][konumlar["S"]["sutun"]] = "S"
    labirent_Matrix_Cozum[konumlar["F"]["satir"]][konumlar["F"]["sutun"]] = "F"

    # Labirent matrix'in çözümünün listeler halinde konsol ekranına yazdırılması (kontrol amaçlı).
    print("----Çözüm----")
    for i in labirent_Matrix_Cozum:
      print(i)

    # Bulunan yolların istenilen formatta tekrar bir çözüm.txt adlı bir dosyaya yazılıp kaydedilmesi.
    girdi_file2=open("cozum.txt","w",encoding="utf-8")

    for i in labirent_Matrix_Cozum:
        for t in range(len(i)):
            girdi_file2.write(f"{str(i[t])} ")
        girdi_file2.write("\n")
    girdi_file2.close()




    # 2.KISIM:
    print("\n")
    print("\n")
    print("****KISIM 2****")

    # İlgili text dosyası oluşturulup Labirentin içine yazılması.
    guclu_girdi_file = open("guclu_girdi.txt", "w", encoding="utf-8")
    guclu_girdi_file.write("WPPWWW\n"
                     "WWPWPS\n"
                     "WWPWPW\n"
                     "PPHPPW\n"
                     "FWPWWW\n"
                     "WPPPPW")
    guclu_girdi_file.close()

    # Girdi.text dosyasından labirent bilgilerinin okunup kaydedilmesi.
    guclu_girdi_file = open("guclu_girdi.txt", "r", encoding="utf-8")

    okunan_Guclu_Labirent = guclu_girdi_file.readlines()
    guclu_girdi_file.close()
    okunan_Guclu_Labirent_Guncel = []
    print(f"Okunan Labirent listesi: {okunan_Guclu_Labirent}")

    # Labirentin ham bilgilerinin tutulduğu "okunan_Guclu_Labirent" adlı listenin satır ve sütun sayılarını tespit etme.
    matrixSatirSayisi = len(okunan_Guclu_Labirent)
    matrixSutunSayisi = len(okunan_Guclu_Labirent[len(okunan_Guclu_Labirent) - 1])

    # Bulunan satır ve sütun sayılarına göre;
    # guclu_labirent_Matrix ve çözümünün tutulacağı guclu_labirent_Matrix_Cozum 'ün oluşturulup tanımlanması.
    guclu_labirent_Matrix = matrix_create(matrixSatirSayisi, matrixSutunSayisi, "")
    guclu_labirent_Matrix_Cozum = matrix_create(matrixSatirSayisi, matrixSutunSayisi, 0)

    # Labirent bilgilerinin tutulduğu listenin "\n" lerden temizlenmesi.
    for item in okunan_Guclu_Labirent:
        okunan_Guclu_Labirent_Guncel.append(item.rstrip())

    # Labirent matrixinde başlangıç ve bitiş gibi belli noktaların satır ve sütun bilgilerinin tutulması için
    # Bir Dictionary yapısının oluşturulması.
    konumlar = {"F": {"satir": 0, "sutun": 0}, "S": {"satir": 0, "sutun": 0}, "H": {"satir": 0, "sutun": 0}}

    # Başlangıç ve bitiş noktalarının "konum_Bulucu" fonksiyonu aracılığıyla konumlarının bulunması.
    # Konumları "konumlar" adlı dictionary yapısına kaydetme işlemi fonksiyonun içinde gerçekleşmektedir.
    konum_Bulucu("F",okunan_Guclu_Labirent_Guncel)
    konum_Bulucu("S",okunan_Guclu_Labirent_Guncel)
    konum_Bulucu("H",okunan_Guclu_Labirent_Guncel)
    print(f"Güncellenmiş Okunan Labirent listesi: {okunan_Guclu_Labirent_Guncel}")


    # Nihai "labirent_Matrix"in her [x][y] konumuna "W","S","F" gibi labirent özelliklerini belirten karakterlerin
    # teker teker yerleştirilmesi.
    y = 0
    for x in range(len(okunan_Guclu_Labirent_Guncel)):
        y = 0
        for i in okunan_Guclu_Labirent_Guncel[x]:
            guclu_labirent_Matrix[x][y] = i
            y = y + 1

    print(f"Nihai Labirent Matrixi : {guclu_labirent_Matrix}")

    # Labirentin çözülmesi.
    yolu_bul(konumlar["S"]["satir"], konumlar["S"]["sutun"],guclu_labirent_Matrix,guclu_labirent_Matrix_Cozum,"H")
    yolu_bul(konumlar["H"]["satir"], konumlar["H"]["sutun"],guclu_labirent_Matrix,guclu_labirent_Matrix_Cozum,"F")

    # Çözümü "1"ler ve "0"lar halinde içinde yer alan çözüm matrix'ine, sonradan "S","F" ve "H" bilgilerinin yerleştirilmesi.
    guclu_labirent_Matrix_Cozum[konumlar["S"]["satir"]][konumlar["S"]["sutun"]] = "S"
    guclu_labirent_Matrix_Cozum[konumlar["F"]["satir"]][konumlar["F"]["sutun"]] = "F"
    guclu_labirent_Matrix_Cozum[konumlar["H"]["satir"]][konumlar["H"]["sutun"]] = "H"

    # Labirent matrix'in çözümünün listeler halinde konsol ekranına yazdırılması (kontrol amaçlı).
    print("----Çözüm----")
    for i in guclu_labirent_Matrix_Cozum:
        print(i)

    # Bulunan yolların istenilen formatta tekrar bir guclu_çözüm.txt adlı bir dosyaya yazılıp kaydedilmesi.
    guclu_girdi_file2 = open("guclu_cozum.txt", "w", encoding="utf-8")

    for i in guclu_labirent_Matrix_Cozum:
        for t in range(len(i)):
            guclu_girdi_file2.write(f"{str(i[t])} ")
        guclu_girdi_file2.write("\n")
    guclu_girdi_file2.close()
