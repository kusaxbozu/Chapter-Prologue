# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
#define background
image background war a = "b_war.png"
image background room c = "c_room.png"
image background black = "black_screen.png"
image was_background = "b_maf.png"
image pds_background = "b_eth.png"
image gni_background = "b_kz.png"
image background black2 = "black_screen2.png"

#define images
image kyoxi: 
    "a_kz2.png"
    zoom 0.65
image kyoxi2: 
    "a_kz1.png"
    zoom 0.65
image mafurei:
    "a_maf1.png"
    zoom 0.90
image mafurei2:
    "a_maf2.png"
    zoom 0.90
image ethan: 
    "a_eth1.png"
    zoom 0.65
image ethan2:
    "a_eth2.png"
    zoom 0.65

#define character
define M = Character("M")
define K = Character("K")
define E = Character("E")
define Unknown = Character("???")


# The game starts here.


label start:
    with fade
    "      "

label bgm:
    play music "audio/theme1.mp3" fadein 1.0 volume 0.75

label background0:
    "Dua Kubu."
    "Apa yang terlintas di pikiran kalian ketika mendengar kata kubu?"
    "..."
    "Ya, itu pemikiran yang bagus."
    "Namun, bagi kami, kami yang ada disini, kubu adalah pihak menang atau kalah."
    "...Ya, kami berperang untuk mengalahkan satu sama lain."
    "...Ya, kami berperang untuk hidup."

label background: 
    scene background war a 
    with fade
    "Kami berperang untuk hidup."
    "Alkisah dari pada paham menuju pedang. Kisah ini merupakan kisah dari perselisihan yang disebut dengan konflik Miseria. "
    "Sesuai namanya saja, Miseria, keputusasaan... Perselisihan ini adalah sumber dari pada malapetaka dunia yang tak lain Bumi." 
    "Katanya Bumi ini diciptakan untuk damai, tapi lagi-lagi, hanya karena paham berubah menjadi acungan pedang."
    " Mungkin kalian akan bertanya; 'Kenapa perang itu bisa terjadi?' --- selain dengan selisih paham yang terjadi... "
    "Oh, tentu saja karena mereka yang punya tujuan, terkadang malah menyakiti satu sama lainnya."


label sprites1:
    scene background black 
    with fade
    "...."
    "..."
    ".."

label sprites2:
    scene background room c 
    with fade

    "...."

    show kyoxi
    "K" "Namamu?"

    menu: 
        "....":
            jump choices1_a
    label choices1_a:
    "???" "...."


label sprites3:
    scene background room c
    show kyoxi2
    "K" "Ya, kamu pasti tidak punya nama."
    "K" "Toh, mereka yang tidak punya nama biasanya menengahi, bukan mengadili."
    "K" "Tapi dengan sebab apa kamu bertahan?"

    show ethan at left
    "E" "Kamu yakin 'K'? Kami hanya menengahi dan bukan mengadili?"

    "K" "..."
    
   

label sprites4:
    scene background room c
    show mafurei2
    "M" "Saya rasa sudah cukup basa-basinya. Masih banyak hal yang kita harus perbincangkan dibandingkan berdebat terus menerus. "
    "M" "Duduklah, ???, perbincangan ini akan sangat panjang. "
    "M" "Saya harap kamu tidak akan bosan mendengarkan ini. "
    with dissolve



label choices2:
    with dissolve
    menu:
        "Diam di tempat":
            jump choices2_a
        "Duduk":
            jump choices2_b
    
label choices2_a:
    scene background room c
    show mafurei
    "M" "..."
    "M" "Kenapa tidak duduk?"

    show ethan2 at left
    "E" "Pft-- Hahaha!"
    "E" "Ayolah, memangnya ada orang yang dipanggil secara tiba-tiba mau menengahi dua kubu yang sedang berselisih?"
    "E" "Aku saja ke sini karena terpaksa lho, M."


    show kyoxi at right
    "K" "...Kalau begitu biar saja dia berdiri sampai pembicaraan ini berakhir."
    "K" "Dan E, jaga sikapmu. Jangan sampai kami memutuskan menendangmu keluar dari sini."

    "E" "Alright, alright, huhu, galaknya~."
    jump choices3_common

label choices2_b:
    scene background room c
    show kyoxi2
    "K" "...Kamu yakin bahwa kebanyakan mereka yang tidak punya nama itu barbarian, M?"

    show mafurei at right
    "M" "Kebanyakan, jangan sampai kamu salah pemaknaan dari kebanyakan."
    "M" "Lagi pula ??? sendiri berbeda dari kebanyakan mereka. Semata-mata saya tidak akan mengundangnya hanya untuk basa basi kan?"
    
    show ethan2 at left
    "E" "(whistle)  Whoo, ada apa ini~? "
    jump choices3_common

label choices3_common:
    scene background room c
    show mafurei2
    "M" "Baiklah, kita mulai saja rapatnya."

label background1:
    scene background war a
    with fade
    "Konflik Miseria- konflik besarnya terjadi selama 3 tahun, sementara konflik dinginnya masih berlangsung sampai sekarang."
    "Perselisihan ini timbul karena (...) yang masih dirahasiakan oleh ketiga kubu- kubu 1, penengah, dan kubu 2. 
    Namun rumor mengatakan; konflik ini berhubungan dengan sebuah ramalan yang turun di tanah ini-"
    "Bahwa kebenaran tersembunyi sebenarnya dapat diketahui bila salah satu dapat menggapai kedamaian."
    "Lihat, bahkan hanya dengan ramalan, mereka dapat berperang.. Tidakkah kamu bertanya apa maksud dari ramalan itu?"
    "Namun, lagi, ramalan itu ditutup-tutupi dengan fakta lapangan bahwa konflik pembunuhan dan pengkhianat perjanjian diantara kubu 1 dan kubu 2 terjadi."
    "Dengan jumlah korban hampir 100.000 jiwa- mereka yang kuat akan bertahan, 
    sementara mereka yang lemah akan dilahap habis oleh ketidaksanggupan."
    "Tentunya, perdamaian yang semata-mata hanya perjanjian di atas kertas itu tidak membuahkan hasil. 
    Sehingga konflik diantara ketiganya- keduanya, masih terus berlanjut."

label background2:
    scene was_background
    with fade
    "Kubu 1 : WAS (Wisteria Art School), oleh tumpah darahnya, Tanah Kehormatan Hera."

label background3:
    scene gni_background
    with fade
    "Kubu 2 : GNIEC ( Gniozie Nationality Impregnable of Independent Enormity Acumen Campaign - military - Achelon), 
    Oleh tumpah darahnya, Republik Federal Gniozie."

label background4:
    scene pds_background
    with fade
    "Kubu 3 : Paradise and Showtime, oleh tumpah darahnya, Pulau Suci - Kincir"

label background5:
    scene background black
    with dissolve

label choices4:
    scene background black
    with fade
    "Sejujurnya aku jadi sedikit ingin bertanya kepada kalian."
    "Dengan penjelasan sejauh ini, menurut kalian siapa yang salah, dan siapa yang benar?"
    "..."
    "Yah, benar, kalian bisa menduga bahwa semuanya salah. Tapi pula bisa menduga semuanya benar. 
    Pula kalian bisa tidak memilih."
    "Tapi, bila kalian tidak memilih- apakah kalian ingin tahu dari sudut pandang mereka?"
    
    menu: 
        "Ya":
            jump choices4_common
        "Ya?":
            jump choices4_common

label choices4_common:
    "Haha, maaf, kalian tidak akan bisa memilih."
    "Hidup memang pilihan. Tapi ada masa dimana kalian tidak bisa memilih. Contohnya ya... Seperti yang tadi saja."
    "Sekarang, coba melangkah ke depan. Pilih lah pilihan kalian sebaik mungkin. Setiap pilihan kalian akan menentukan nasib kalian."
    "Pilih lah, kalian ingin bertahan- atau kalian ingin mengikuti 100.000 jiwa yang melayang?"
    "Ini kisah dari pada sebuah hal yang dinamakan tujuan, pula kebengisan manusia."

label sprites5:
    scene background black2
    with fade
    


    return 
