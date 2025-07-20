sher1 = {"nomi":"Ona yurting-Oltin beshiging",
         "muallif":"Abdulla Oripov",
         "sher":"""Ona yurting – oltin beshiging, bolam,  
Unga dogʻ tushirma hech qachon, aslo!  
Uning har gaji azizdir, muqaddas,  
Dushman toʻpigʻini bosmasin, maslo.

Togʻlaring – qalqon-u, daryolaring – jon,  
Uzumdek bogʻlaring toʻkilar baraka.  
Noni – halol, suvi – musaffo, pok,  
Bu yurtda yashashning o'zi bir baxt-da!

Sen unga xizmat qil, nomus bilan sen,  
Shunda u seni yuksaltirar yuksak.  
Koʻnglingni toza tut, yurtingni asra,  
Yurakda yashasin – Vatan degan sha’n!"""}

sher2 = {"nomi":"Ona tili",
         "muallif":"Erkin Vohidov",
         "sher":"""Ona tili – ruhi, qalbi millatning,  
Ajdodlardan qolgan bebaho meros.  
Tilni asrash burchi har bir avlodning,  
U tugʻilsin yurak ichra, yurakda yonsin.

Ona tilim – bedor fikr-u soʻzlarim,  
Koʻngil qushi undan qanotlanadi.  
She’rlarim, duolarim, izhorim,  
Ona tilim orqali jonlanadi.

Qanday tilda kuylasam, tilim – ona,  
U orqali anglayman bor haqiqat.  
Uni e’zoz qilsam – men o‘zligimni,  
Yo‘qotmasman hech qachon, aslo hayot."""}

sher3 = {"nomi":"Yurak dardi",
         "muallif":"Zulfiya",
         "sher":"""Yuragimda g‘amlar kechalar yotar,  
Tunlarin yulduzga boqaman sokin.  
So‘zsiz og‘riq meni aytmayin quchar,  
Yig‘lamay o‘tkazdim bir umr, yakin.

Men aytgim keladi, ammo til ojiz,  
Dardimni kim eshitadi dunyoda?  
Yurakda yig‘laydi ovozsiz g‘amlar,  
Ko‘zda emas, ichda to‘ladi qushta.

Aytinglar, yurakni kim tushunadi?  
Ko‘ngilning iztirobi, armonini?  
Faol hayotimda jim qolgan yurak,  
She’rda aytar o‘zining bor jonini..."""}
sherlar = [sher1, sher2, sher3]
for sher in sherlar:
    print(f"She'r {sher['muallif']}ning {sher['nomi']} \n{sher['sher']} \n{'-'*50}")