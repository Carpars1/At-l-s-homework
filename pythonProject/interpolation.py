while True:
    try:
        # İlk noktayı alıyoruz (x1, y1)
        x1 = float(input("x1 değerini girin: "))
        y1 = float(input("y1 değerini girin: "))

        # İkinci noktayı alıyoruz (x2, y2)
        x2 = float(input("x2 değerini girin: "))
        y2 = float(input("y2 değerini girin: "))

        # Interpolasyon yapılacak x değerini alıyoruz
        x = float(input("Interpolasyon yapılacak x değerini girin: "))

        # Lineer interpolasyon formülü ile y değerini hesaplıyoruz
        yinter1 = y1 + (y2 - y1) * ((x - x1) / (x2 - x1))

        # Sonucu virgülden sonra 4 hane olacak şekilde yazdırıyoruz
        print("Interpolasyon sonucu y değeri: {:.4f}".format(yinter1))
        print("________________________________________________________________________________________")
        x_1 = x1
        y_1 = float(input("y_1 değerini girin: "))

        # İkinci noktayı alıyoruz (x2, y2)
        x_2 = x2
        y_2 = float(input("y_2 değerini girin: "))



        # Lineer interpolasyon formülü ile y değerini hesaplıyoruz
        yinter2 = y_1 + (y_2 - y_1) * ((x - x_1) / (x_2 - x_1))
        print("Interpolasyon sonucu y değeri: {:.4f}".format(yinter2))
        print("..............................................................................")
        xu_1 = x1
        yu_1 = float(input("yu_1 değerini girin: "))

        # İkinci noktayı alıyoruz (x2, y2)
        xu_2 = x2
        yu_2 = float(input("yu_2 değerini girin: "))



        # Lineer interpolasyon formülü ile y değerini hesaplıyoruz
        yinteru2 = yu_1 + (yu_2 - yu_1) * ((x - xu_1) / (xu_2 - xu_1))
        print("Interpolasyon sonucu y değeri: {:.4f}".format(yinteru2))
        print("..............................................................................")


    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
    except ZeroDivisionError:
        print("x1 ve x2 değerleri aynı olamaz, çünkü bu durumda interpolasyon yapılamaz.")
