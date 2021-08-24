
import os,wx, wx.media,sys

import platform

from datetime import datetime

from wx import *

import subprocess

import pathlib

def verConfig(Object):

    os.system("java -jar "+os.path.join(os.path.dirname(__file__), "Config.jar"));

def ponerArgumento(texto,index,tipo):

    global array

    args=""

    if((int)(index)<len(array)):

        args=texto

        valor=array[(int)(index)]

        if tipo == "1":

            if(valor!="0"):

                args+=" "+valor

            else:

                args=""
                
        elif tipo == "2":

            args+=" \""+valor+"\""

        elif tipo == "3":

            if((int)(valor)==0):

                args=""

        elif tipo == "4":

                args=valor

    return args

def setEndTime(Object):

    calcularTiempo()

    calcularTiempo()

def setStartTime(Object):

    global time1

    if tiempo!="":

        time1=tiempo
    
    calcularTiempo()

if not sys.warnoptions:

    import warnings

    warnings.simplefilter("ignore")

app = App()

raiz = Frame(None, title="Jayant Player And Converter", size=(1000,600))

panel = Panel(raiz)

l1 = StaticText(panel, -1, "")

l3 = StaticText(panel, -1, "") 

raiz.timer = wx.Timer(raiz)

video=""

tiempo=""

tiempo2=""

nowm=""

nows=""

current = StaticText(panel,label="--:--")

time1="";

time2="";

numtime1=0

numtime2=0

separador=""

array=""

rutaActual=os.getcwd()

def limpiarCadena(cadena):

    texto=cadena

    texto=texto.replace("  ", " ")

    texto=texto.replace(" ", "-")

    return texto

def enSegundos(tiempo):

    minutos=tiempo[0:2]

    segundos=tiempo[3:5]

    segundos=(int)(segundos[0:1]+segundos[1:2])
 
    minutos=(int)(minutos[0:1]+minutos[1:2])*60
    
    return minutos+segundos

def calcularTiempo():
    
    global time1  
    
    global time2

    if time1!="" and time2!="" and tiempo!="" and tiempo2!="":
    
        if tiempo2!="":
    
            time2=tiempo
    
        if time1!=tiempo2 and time1==time2:
            
            time2=tiempo2
    
        if numtime1>=numtime2:
        
            time1="00:00"
    
        if numtime2<numtime1:
        
            time2=tiempo2

    if time1=="":

        time1="00:00"

    if time2=="":

        time2=time2=tiempo2
    
    l1.SetLabel(time1);

    l3.SetLabel(time2);

def convertir(Object):
	
    now = datetime.now()

    date_time = now.strftime("%m/%d/%Y-%H:%M:%S")

    date_time=date_time.replace("/","-")

    date_time=date_time.replace(":","_")

    nombre_nuevo=date_time+".gif"

    if time1!="" and time2!="":
        
        global array

        archivoSalida=video[0:video.rfind(separador)+1]+nombre_nuevo

        proc=subprocess.Popen("java -jar "+os.path.join(os.path.dirname(__file__), "ReadFile.jar")+" -i "+str(pathlib.Path().absolute())+separador+"Config.txt -n 28",shell=True, stdout=subprocess.PIPE )
    
        output=proc.communicate()[0]
    
        proc.kill()

        salida=bytes.decode(output)

        salida=salida.replace(" ","")

        salida=salida.replace("\r","")
    
        salida=salida.replace("\t","")

        array=salida.split('=')

        if(len(array)==29):

            dato=""
         
            if ponerArgumento("","3","1")!="" and ponerArgumento("","1","1")!="":
                
                dato=ponerArgumento("-ss","1","1")+" "+ponerArgumento("-t","3","1")

            else:

                dato="-ss "+str(enSegundos(time1))+ " -t "+str(enSegundos(time2)-enSegundos(time1))   

            calidad=""

            marcaDeAgua=""

            if ponerArgumento("","11","4")!="":

                marcaDeAgua=ponerArgumento("-watermark","11","2")+" "+ponerArgumento("-pos-watermark","13","1")+" "+ponerArgumento("--color-watermark","15","2")+" "+ponerArgumento("-text-watermark","17","2")+" "+ponerArgumento("-font-size-text-watermark","19","1")

            if ponerArgumento("-good","21","3")=="-good":

                calidad=ponerArgumento("-good","21","3")
            
            else:

                calidad=ponerArgumento("-bad","23","3")
            
            comando="java -jar "+os.path.join(os.path.dirname(__file__), "jffmpeg.jar")+" -i \""+video+"\" "+dato+" "+ponerArgumento("-r","5","1")+" "+ponerArgumento("-fps","7","1")+" "+ponerArgumento("-s","9","4")+" "+marcaDeAgua+" "+calidad

            os.system(comando.replace("  "," "))
    
            videoSalida=video[0:-4]+"-output"+video[video.rfind("."):len(video)]
         
            comando="python "+os.path.join(os.path.dirname(__file__), "vdo2gif.py")+" \""+videoSalida+"\" \""+archivoSalida+"\" "+ponerArgumento("-f","7","1")+" "+ponerArgumento("-s","25","1")+" "+ponerArgumento("-r","27","1")
                        
            os.system(comando.replace("  "," "))

            os.remove(videoSalida)

            if separador=="\\":

                os.system("C:\\Windows\\explorer.exe " + "\"" + archivoSalida )

            else:

                os.system("xdg-open " + archivoSalida)

def ontimer(e):

    if raiz.video.GetState() == 1 or raiz.video.GetState() == 2:

        currenttime = raiz.video.Tell()/1000

        slider.SetValue(currenttime)

        nmin = int(currenttime//60)

        nsec = int(currenttime%60)

        if nmin < 10:
            nowm = str("0"+str(nmin))

        else:
            nowm = str(nmin)

        if nsec < 10:
            nows = str("0"+str(nsec))

        else:
            nows = str(nsec)
            
        global tiempo
        
        global tiempo2
        
        global numtime1
        
        global numtime2

        numtime1=nowm+nows

        tiempo=nowm+":"+nows
        
        current.SetLabel(tiempo)
        
        totaltime = raiz.video.Length()/1000
        
        slider.SetMax(totaltime)
        
        minute = int(totaltime//60)
        
        sec = int(totaltime%60)
        
        if minute < 10:
            tmin = str("0"+str(minute))
        
        else:
            tmin = str(minute)
        
        if sec < 10:
            tsec = str("0"+str(sec))
        
        else:
            tsec = str(sec)
             
        if tiempo2=="":
            
            numtime2=tmin+tsec;
            
            tiempo2=tmin+":"+tsec;
                
        total.SetLabel(tmin+":"+tsec)
                
raiz.Bind(EVT_TIMER,ontimer)

raiz.timer.Start(0)

def play_video(event):

    if raiz.video.GetState() == 2:

        raiz.video.Pause()
        
        play.SetBitmap(Bitmap(rutaActual+"play.png"))

    else:

        raiz.video.Play()
        
        raiz.video.SetVolume(float("0." + str(volume.GetValue())))
        
        play.SetBitmap(Bitmap(rutaActual+"pause.png"))
        
def stop_play(event):
    
    raiz.video.Stop()
    
    slider.SetValue(0)
    
    current.SetLabel("--:--")
    
    total.SetLabel("--:--")
    
    play.SetBitmap(Bitmap(rutaActual+"play.png"))

def open_file(event):
    
    global video

    file = FileDialog(panel,"Open",wildcard="*mp4")
    
    if file.ShowModal() == ID_OK:
        
        video=file.GetPath()

        raiz.video.Load(file.GetPath())

def quit_win(event):
    
    raiz.Close()

def sound_ctrl(event):
    
    if raiz.video.GetVolume() > 0.0:
    
        raiz.video.SetVolume(0)
    
        volume.SetValue(0)
    
        sound.SetBitmap(Bitmap(rutaActual+"mute.jpg"))
    
    else:
    
        raiz.video.SetVolume(0.3)
    
        volume.SetValue(3)
    
        sound.SetBitmap(Bitmap(rutaActual+"volume.jpg"))

def volume_ctrl(event):
    
    if raiz.video.GetVolume() > 0.0:
    
        sound.SetBitmap(Bitmap(rutaActual+"volume.jpg"))
    
    else:
    
        sound.SetBitmap(Bitmap(rutaActual+"mute.jpg"))
    
    if volume.GetValue() < 10:
    
        raiz.video.SetVolume(float("0."+str(volume.GetValue())))
    
    else:
    
        raiz.video.SetVolume(1.0)

def move_time(event):
    
    raiz.video.Seek(slider.GetValue()*1000)

def forward(event):
    
    raiz.video.Seek(raiz.video.Tell()+10000)

def backward(event):
    
    raiz.video.Seek(raiz.video.Tell()-10000)

l1.SetLabel("00:00");

l3.SetLabel("00:00");

separador="/"

if platform.system()=="Windows":
    
    file=video[video.rfind("\\")+1:video.rfind(".")]

    file=limpiarCadena(file)

separador="\\"

rutaActual=os.path.join(os.path.dirname(__file__), "icon"+separador)

menubar = MenuBar()

media = Menu()

tools = Menu()

config = Menu()

menubar.Append(media,"Media")

menubar.Append(config,"Config")

menubar.Append(tools,"Convert")

open = media.Append(1,"Open File...\tCtrl+O")

media.Bind(EVT_MENU,open_file,open)

quit = media.Append(ID_EXIT,"Quit\tCtrl+Q")

media.Bind(EVT_MENU,quit_win,quit)

openfolder = tools.Append(ID_ANY,"Set Start time")

tools.Bind(EVT_MENU,setStartTime,openfolder)

Opendisk = tools.Append(ID_ANY,"Set End time")

tools.Bind(EVT_MENU,setEndTime,Opendisk)

convert = tools.Append(ID_ANY,"Convert")

tools.Bind(EVT_MENU,convertir,convert)

configuracion = config.Append(ID_ANY,"Config")

config.Bind(EVT_MENU,verConfig,configuracion)

mainbox = BoxSizer(VERTICAL)

raiz.video = wx.media.MediaCtrl(panel,1,szBackend=wx.media.MEDIABACKEND_WMP10)

raiz.Bind(wx.media.EVT_MEDIA_LOADED,play_video)

mainbox.Add(raiz.video,7,ALL|EXPAND)

slide = BoxSizer(HORIZONTAL)

slide.Add(current,0,ALL)

slider = Slider(panel,minValue=0,value=0,maxValue=100,style=SL_HORIZONTAL)

slider.Bind(EVT_SLIDER,move_time,slider)

slide.Add(slider,1,EXPAND|ALL,border=2)

total = StaticText(panel,label="--:--")

slide.Add(total,0,ALL)

mainbox.Add(slide,0,EXPAND|ALL,border=10)

footer = BoxSizer(HORIZONTAL)

play = BitmapButton(panel,-1,Bitmap(rutaActual+"play.png"))

play.Bind(EVT_BUTTON,play_video,play)

footer.Add(play,0,ALL)

spback = BitmapButton(panel,-1,Bitmap(rutaActual+"swipeback.png"))

spback.Bind(EVT_BUTTON,backward,spback)

stop = BitmapButton(panel,-1,Bitmap(rutaActual+"stop.png"))

stop.Bind(EVT_BUTTON,stop_play,stop)

spfor = BitmapButton(panel,-1,Bitmap(rutaActual+"swipefor.png"))

spfor.Bind(EVT_BUTTON,forward,spfor)

footer.AddMany([(spback,0,ALL),(stop,0,ALL),(spfor,0,ALL)])

sound = BitmapButton(panel,-1,Bitmap(rutaActual+"volume.jpg"))

sound.Bind(EVT_BUTTON,sound_ctrl,sound)

footer.Add(sound,0,ALL)

volume = Slider(panel,minValue=0,value=3,maxValue=10,style=SL_HORIZONTAL)

volume.Bind(EVT_SLIDER,volume_ctrl,volume)

footer.Add(volume,0,ALL)

l0 = StaticText(panel, -1, "        ")

l2 = StaticText(panel, -1, "                    ")

footer.Add(l0,0,ALL)

footer.Add(l1,0,ALL)

footer.Add(l2,0,ALL)

footer.Add(l3,0,ALL)

mainbox.Add(footer,0,border=10)

panel.SetSizer(mainbox)

raiz.SetMenuBar(menubar)

raiz.Show()

app.MainLoop()