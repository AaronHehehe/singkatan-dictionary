meme_dict = {
            "NU": "No Ulti",
            "NF": "No Flicker",
            "NP": "No purify atau No petri",
            "NR":"No Retri",
            "AFK":"seorang pemain meninggalkan permainan untuk sementara atau lama",
            "KDA":"kill death assist",
            "HP":"Health Point",
            "MP":"mana Point"
            }

word = input("Ketik singkatan ml yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata",word,"adalah",meme_dict[word])
else:
    print('kata tidak ditemukan')
