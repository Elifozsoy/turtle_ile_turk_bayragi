import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("@computerwith_e")      # Başlık
w.setup(width=720,height=420)   # Pencere Boyutu
w.bgcolor("DarkRed")            # Arka Plan Kırmızı Yap

# İlk daire
t.up()
t.goto(-100,-100)               # Fare imleci lokasyonu
t.color('white')                # Beyaz renk
t.begin_fill()                  # Beyaz rengi doldur
t.circle(120)                   # Çapı
t.end_fill()

# Hilal yapabilmek için ikinci daire
t.goto(-70,-80)                 # Fare imleci lokasyonu
t.color('DarkRed')                  # Kırmızı renk
t.begin_fill()                  # Kırmızı rengi doldur
t.circle(100)                   # Çapı
t.end_fill()                    # Dolguyu Bitir

# Yıldız için hazırlık
t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

# Yıldız için tekrar eden üçgen çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-130,-190)
t.color("white")
t.write("18 Mart Çanakkale Zaferi Kutlu Olsun", font=("Times New Roman", 13,"italic"))

# Ekrana tıklayınca programın kapanmasını sağlar.
w.exitonclick()
