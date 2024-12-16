import math

# Bu fonksiyon iki nokta arasındaki mesafeyi hesaplar
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaları burada tanımlıyoruz (x, y) olarak
points = [(1, 2), (4, 6), (5, 1), (2, 4)]  # Noktalar listesi

# Mesafeleri saklamak için boş bir liste
mesafeler = []

# Tüm noktaları karşılaştırıyoruz
for i in range(len(points)):  # İlk noktayı seçiyoruz
    for j in range(i+1, len(points)):  # İkinci noktayı seçiyoruz, aynı nokta olmasın diye i+1
        mesafe = euclideanDistance(points[i], points[j])  # Mesafeyi hesapla
        mesafeler.append(mesafe)  # Listeye ekle
        print(f"{points[i]} ve {points[j]} arasındaki mesafe: {mesafe:.2f}")

# En kısa mesafeyi buluyoruz
en_kisa_mesafe = min(mesafeler)
print(f"\nEn kısa mesafe: {en_kisa_mesafe:.2f}")
