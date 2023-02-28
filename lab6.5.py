kaz = ('а','ә','б','в','г','ғ','д','е','ё','ж','з','и','й','к','қ','л','м','н','ң','о','ө','п','р','с','т','у','ұ','ү','ф', 'х', 'һ','ц','ч','ш','щ','ъ','ы','і','ь','э','ю','я')
lat = ('a','a','b','v','g','g','d','e','io','j','z','i','i','k','q','l','m','n','n','o','o','p','r','s','t','u','u','u','f','h','h','ts','ch','sh','shch','','y','i','','e','iu','ia')
soz = input("\n\nSoz: ")
for i in soz:
    san = 0
    for j in kaz:
        if j == i:
            print(lat[san],end="")
            break
        elif i.lower() == j:
            print(lat[san].upper(),end="")
            break
        san +=1