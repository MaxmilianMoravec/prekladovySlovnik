from tkinter import * #importuji tkinter


preklad =open ("databaze/preklad.txt","r",encoding ="utf8")
pre = preklad.read().splitlines()

nezname =open ("databaze/nezname.txt","r",encoding ="utf8")
nez = nezname.read().splitlines()


window = Tk()#pro jednodušší zápis vezmu proměnou a přiřadím jí funkci
window.geometry("1400x500")#nastavím velikost okna
window.title("Slovník")#nastavím popiek okna
window.configure(bg="#e0fcff")
hledanyViraz = StringVar(window)#vytvořim proměnou hledanyViraz, abych jí mohl volat metodou .get, a tak s ní pracovat v entry i label
prekladCara = Frame(master=window, width=5,height=1500, bg="#0d8dbb")

def hledatFun():#vytvořím funkci hledatFun, spustí se při zmáčknutí tlačítka hledat
    if hledanyViraz.get() == "":
        zadanyVstupLabel.config(text="Žádný text k překladu.", font=("Calibri,15,Bold"),fg="#c24f3d")
    else:
        if (hledanyViraz.get() in nez) == True:
            search=nez.index(hledanyViraz.get())
        else:
            search=len(pre)-1

        zadanyVstupLabel.config(text="Hledaný výraz: " +hledanyViraz.get(), font=("Calibri,15,Bold"),fg="#33a7cc")#vypíše text a hledaný výraz
        prekladCara.pack(fill=Y, side=BOTTOM,padx=(50,20))
        neznameSlovo.config(text="Neznámé slovo")
        vyznamSlovo.config(text="Význam")
        nS.config(text=hledanyViraz.get(), font=("Calibri",20),fg="#33a7cc")
        vS.config(text=pre[search],font=("Calibri",20),fg="#33a7cc")
def smazatFun():
    vyhledavaciPole.delete(0, END)
    zadanyVstupLabel.config(text="")
    prekladCara.pack_forget()
    neznameSlovo.config(text="")
    vyznamSlovo.config(text="")
    nS.config(text="")
    vS.config(text="")
def closeFun():
    window.destroy()

textKvyhlPoli = Label(window, text='Zadejte text k překladu:',bg="#e0fcff")#vytvořím text k vyhledávacímu poli
textKvyhlPoli.place(x=40, y=12)#

vyhledavaciPole = Entry(window, textvariable=hledanyViraz, fg="#004047")
vyhledavaciPole.place(x=180, y=12)#

hledatButt = Button(window, text="Hledat", command=hledatFun, bg="#007783", fg="#00272b")#vytvoří tlačítko, co volá funkci hledatFun
hledatButt.place(x=320, y=9)#zobrazí tlačítko

smazatButt = Button(window, text="Smazat", command=smazatFun)#vytvoří tlačítko, co volá funkci hledatFun
smazatButt.place(x=380, y=9)#zobrazí tlačítko

zavritButt = Button(window, text="Zavřít", command=closeFun,bg="#d96a67")#vytvoří tlačítko, co volá funkci hledatFun
zavritButt.place(x=440, y=9)#zobrazí tlačítko

oddelovaciCara = Frame(master=window, width=700, height=1, bg="#007783")
oddelovaciCara.pack(fill=X, pady=(50,20))

zadanyVstupLabel = Label(window, font="Calibri,10",anchor="e", justify="right",bg="#e0fcff")#vytvoří texttové prázdné pole, to se při vyhledání zobrazí
zadanyVstupLabel.place(x=20, y=70)#řekne, kde se má vytvořit

neznameSlovo = Label(window, font="Calibri,10",anchor="e", justify="right",bg="#e0fcff")#vytvoří texttové prázdné pole, to se při vyhledání zobrazí
neznameSlovo.place(anchor=E,relx=0.2, y=110)#řekne, kde se má vytvořit

vyznamSlovo = Label(window, font="Calibri,10", justify="left",bg="#e0fcff")#vytvoří texttové prázdné pole, to se při vyhledání zobrazí
vyznamSlovo.place(anchor=E,relx=0.65, y=110)#řekne, kde se má vytvořit


##########################
nS = Label(window,anchor="e", justify="right",bg="#e0fcff")#vytvoří texttové prázdné pole, to se při vyhledání zobrazí
nS.place(anchor=W,relx=0.1,y=160)#řekne, kde se má vytvořit


vS = Label(window,anchor="e", justify="right",bg="#e0fcff")#vytvoří texttové prázdné pole, to se při vyhledání zobrazí
vS.place(anchor=W,relx=0.6, y=160)#řekne, kde se má vytvořit

window.mainloop()#smička, aby se okno nezavřelo