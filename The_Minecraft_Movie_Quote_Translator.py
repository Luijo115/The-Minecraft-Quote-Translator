import flet as ft

Memes = {"Steve": {
        "Ingles": "I Am Steve",
        "Español": "Soy Steve",
        "Frances": "Je suis Steve",
        "Italiano": "Io sono Steve",
        "Aleman": "Ich bin Steve"
    },
        "Crafting": {
        "Ingles": "THIS is a Crafting Table",
        "Español": "ESTA es una mesa de trabajo",
        "Frances": "CECI est une table d'artisanat",
        "Italiano": "QUESTO è un tavolo da lavoro",
        "Aleman": "DAS ist ein Basteltisch"
    },
        "Chicken": {
        "Ingles": "Chicken Jockey",
        "Español": "Jinete de gallina",
        "Frances": "Poulet cavalier",
        "Italiano": "Cavaliere di pollo",
        "Aleman": "Hühnerreiter"
    },
        "Nether": {
        "Ingles": "The nether",
        "Español": "Al nether",
        "Frances": "Le nether",
        "Italiano": "Il nether",
        "Aleman": "Der Nether"
    },
        "Flint": {
        "Ingles": "Flint and steel",
        "Español": "Acero y pedernal",
        "Frances": "Silex et acier",
        "Italiano": "Pietra focaia e acciaio",
        "Aleman": "Feuerstein und Stahl"
    },
        "asachild": {
        "Ingles": "As a child I yearned for the mines",
        "Español": "De niño anhelaba las minas",
        "Frances": "Enfant, je rêvais des mines",
        "Italiano": "Da bambino desideravo le miniere",
        "Aleman": "Als Kind sehnte ich mich nach den Minen"
    }}
def main(page: ft.Page):
    page.title = "Minecraft Movie Quote Translator"

    #para poner los botones bonitos
    button_style = ft.ButtonStyle(
    shape=ft.RoundedRectangleBorder(radius=2),
    bgcolor=ft.colors.GREY_700,
    color=ft.colors.WHITE70,
    padding=10,
    text_style=ft.TextStyle(font_family="Monocraft",size=14,weight=ft.FontWeight.W_500))

   #imagenes y textos
    stv = ft.Image(src="Stevemovie.png", width=300,height=300)
    stvtext = ft.Text("I Am Steve",size=28, font_family="Monocraft",width=250)
    craft = ft.Image(src="Craftingmovie.png", width=250,height=250)
    crafttext = ft.Text("THIS is a Crafting Table", size=28, font_family="Monocraft",width=250)
    chijo = ft.Image(src="chickenjockey.jpg", width=270,height=270)
    chijotext = ft.Text("Chicken Jockey", size=28, font_family="Monocraft",width=250)
    nether = ft.Image(src="Nether.webp", width=300,height=300)
    nethertext = ft.Text("The Nether", size=28, font_family="Monocraft",width=250)
    flint = ft.Image(src="flint.jpeg", width=300,height=300)
    flinttext = ft.Text("Flint and steel", size=28, font_family="Monocraft",width=250)
    asachild = ft.Image(src="asachild.jpeg", width=300,height=300)
    asachildtext = ft.Text("As a child I yearned for the mines", size=25, font_family="Monocraft",width=250)
  
    
    #funciones
    def cambiar(e):
        stvtext.value = Memes["Steve"][e.control.text]
        crafttext.value = Memes["Crafting"][e.control.text]
        chijotext.value = Memes["Chicken"][e.control.text]
        nethertext.value = Memes["Nether"][e.control.text]
        flinttext.value = Memes["Flint"][e.control.text]
        asachildtext.value = Memes["asachild"][e.control.text]
        page.update()
    #botones
    boin=ft.FilledButton(text="Ingles", width=100, height=30,style=button_style, on_click=cambiar)
    boes=ft.FilledButton(text="Español", width=100, height=30,style=button_style, on_click=cambiar)
    boit=ft.FilledButton(text="Italiano", width=100, height=30,style=button_style, on_click=cambiar)
    bofra=ft.FilledButton(text="Frances", width=100, height=30,style=button_style, on_click=cambiar)
    boal=ft.FilledButton(text="Aleman", width=100, height=30,style=button_style, on_click=cambiar)

    imafila = ft.Row(
        controls=[
            ft.Column([stv, stvtext]),
            ft.Column([craft, crafttext]),
            ft.Column([chijo, chijotext]),
            ft.Column([nether, nethertext]),
            ft.Column([flint, flinttext]),
            ft.Column([asachild, asachildtext]),
        ],
        scroll="always",
        wrap=False,  
    )

    botofila = ft.Row(
        controls=[boin, boes, boit, bofra, boal],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(ft.Column(controls=[imafila,botofila,],scroll="auto",))
    
ft.app(target=main, assets_dir="assets")
