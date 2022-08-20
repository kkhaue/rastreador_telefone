from tkinter import *
import phonenumbers

from phonenumbers import carrier
from phonenumbers import geocoder
from PIL import Image, ImageTk
from phonenumbers import timezone

from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

# Janela
root=Tk ()
root.title('Rastrear com Khaue o BRABO')
root.geometry('365x584')
root.resizable(False,False)
root.configure(bg='white')


def timezonefinder():
    pass


def tracker():
    enter_numero = entry.get()
    numbers=phonenumbers.parse(enter_numero)
    local=geocoder.description_for_number(numbers,'br')
    cidade.config(text=local)

    operadora = carrier.name_for_number(numbers,'br')
    sim.config(text=operadora)

    pais = timezone.time_zones_for_number(numbers)
    zone.config(text=pais)

    geolocal = Nominatim(user_agent='geoapiExercises')
    localizacao=geolocal.geocode(local)

    lng=localizacao.longitude
    lat=localizacao.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    obj = timezonefinder()
    result = obj.timezone_at(lng=localizacao.longitude,lat=localizacao.latitude)

    home=pytz.timezone(result)
    local_time = datetime.now(home)
    current_time =localizacao_time.strftime("%I:%M:%p")
    clock.config(text=current_time)


# Logo sistema
logo=PhotoImage(file='lupa_telefone.png')
Label(root,image=logo,bg='white').place(x=160,y=20)

# icon forms
icon = Image.open('lupa_telefone.png')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)
# Label
Cabecalho = Label(root,text='Rastreamento De Tefone',fg='green',font=('roboto',15,'bold'),bg='white')
Cabecalho.place(x=60,y=100)


entry_Cabecalho = PhotoImage(file='2161472-200.png')
Label(root,image=entry_Cabecalho,bg='white').place(x=80,y=140)

entry=StringVar()
enter_numero=Entry(root,textvariable=entry,width=20,bd=0,font=('roboto',10),justify='center')
enter_numero.place(x=92.5,y=232.5)

Pesquisar_image = PhotoImage(file='Free-Search-Button-PNG-Image.png')
Pesquisar=Button(image=Pesquisar_image,borderwidth=0,cursor='hand2',bd=0,font=0,bg='white',command=tracker)
Pesquisar.place(x=96.5,y=300)

cidade = Label(root,text='●Cidade:',bg='white',fg='black',font=('roboto',10,'bold'))
cidade.place(x=20,y=400)

sim = Label(root,text='●Operadora:',bg='white',fg='black',font=('roboto',10,'bold'))
sim.place(x=200,y=400)

zone = Label(root,text='●Pais:',bg='white',fg='black',font=('roboto',10,'bold'))
zone.place(x=20,y=440)

clock = Label(root,text='●Horário:',bg='white',fg='black',font=('roboto',10,'bold'))
clock.place(x=200,y=440)

longitude = Label(root,text='●Longi:',bg='white',fg='black',font=('roboto',10,'bold'))
longitude.place(x=200,y=480)

latitude = Label(root,text='●Lati:',bg='white',fg='black',font=('roboto',10,'bold'))
latitude.place(x=20,y=480)

root.mainloop()
