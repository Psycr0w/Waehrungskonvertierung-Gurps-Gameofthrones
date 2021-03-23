import PySimpleGUI as sg      
from math import floor

sg.theme('DarkBlack')    # Keep things interesting for your users

layout = [[sg.InputText(key='input')],
[sg.Output(key='output')],
[sg.Checkbox('Monde', key="moon"), sg.Checkbox('Random Loot',key="randloot")],      
[sg.Button('Convert'), sg.Exit()]]      

window = sg.Window('Converter', layout)      

def clicked():
    try:
        event, values = window.read()
        gurpsdollar = float(values['input']) * 4
        drachendiv = 23520
        mondediv = 784
        hirschendiv = 112
        sternediv = 16
        groschendiv = 8
        halbgroschendiv = 4
        penniesdiv = 2
        monde = 0
        monddolar = 0
        drachen = floor(gurpsdollar / drachendiv)
        drachendollar = drachen * drachendiv

        if window['moon'].get() == True:
            monde = floor((gurpsdollar - drachendollar) / mondediv)
            monddolar = monde * mondediv

        hirschen = floor((gurpsdollar - drachendollar - monddolar) / hirschendiv)
        hirschdollar = hirschen * hirschendiv
        sterne = floor((gurpsdollar - drachendollar - monddolar - hirschdollar) / sternediv)
        sterndollar = sterne * sternediv
        groschen = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar) / groschendiv)
        groschendollar = groschen * groschendiv
        halbgroschen = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar) / halbgroschendiv)
        halbgroschendollar = halbgroschen * halbgroschendiv
        pennies = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar) / penniesdiv)
        penniesdollar = pennies * penniesdiv
        halbpennies = gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar - penniesdollar

        d = {
            "singulare" : ["Drache", "Mond", "Hirsch", "Stern", "Groschen", "Halbgroschen", "Penny", "Halbpenny"],
            "plurale" : ["Drachen", "Monde", "Hirsche", "Sterne", "Groschen", "Halbgroschen", "Pennies", "Halbpennies"],
            "gewichte" : [0.2, 0.14, 0.02, 0.04, 0.2, 0.1, 0.005, 0.0025],
            "verhaeltnisse" : [1, 30, 7, 7, 2, 2, 2, 2],
            "values" : [drachen, monde, hirschen, sterne, groschen, halbgroschen, pennies, halbpennies]
            }

        stringer = "hithar"
        finalgewicht = 0.0

        for i in range(8):
            singular, plural, gewicht, verhaeltnis, value = (d["singulare"][i], d["plurale"][i], d["gewichte"][i], d["verhaeltnisse"][i], d["values"][i])
            if value != 0:
                if stringer == "hithar":
                    stringer = ""
                else:
                    stringer = stringer + ", "
                stringer = stringer + str(value) + " " 
                if value == 1:
                    stringer = stringer + singular
                else:
                    stringer = stringer + plural
                finalgewicht = finalgewicht + gewicht * value

        print(stringer + "\n" + str(finalgewicht) + "lb")

    except:
        print('error')



while True:                             # The Event Loop
    event, values = window.read() 
    if event == 'Convert':
        window['Convert'].click()
        window['output'].update("")
        clicked()      
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()