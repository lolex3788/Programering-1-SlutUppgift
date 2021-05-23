from _plotly_utils.basevalidators import ColorlistValidator   #|                                           
import pandas as pd                                           #| 
import plotly.express as px                                   #|          
import matplotlib.pyplot as plt                               #|              
from plotly.subplots import make_subplots                     #|                          
import plotly.graph_objects as go                             #|Använder mig av import för att importera olika datasett eller biblotek.                  


Val = int(input("Vill ni se data ifrån? Skriv \"1\" för att se data ifrån \"National_Daily_Deaths\" eller \"2\" för att se data ifrån \"National_Total_Deaths_by_Age_Group\" ")) #Användaren får välja datasett

if Val == 1:
    DailyDeaths = pd.read_csv("National_Daily_Deaths.csv", encoding = "ISO-8859-1", header = 0) #Om användaren skriver 1 så använder programmet pandas för att läser in "National_Daily_Deaths.csv" på en variabel som heter DailyDeaths.


    fig = make_subplots(rows=1, cols=2, specs=[[{"type":"scatter"},{"type":"bar"}]]) #Här använder programmet plotly.subplot för att skapas subploten med två platser bredvid varandra på samma rad.

    data = [go.Scatter()]                                                                                  #|
    fig.add_trace(go.Scatter(x=DailyDeaths["Date"], y=DailyDeaths["National_Daily_Deaths"]), row=1, col=1) #|Här skapas första graften med hjälp av plotly.graph_objects. Den sätter datumet som X-axeln och antal döda varje dag på Y-axeln.

    data = [go.Bar()]                                                                                   #|
    fig.add_trace(go.Bar(x=DailyDeaths["Date"], y=DailyDeaths["National_Daily_Deaths"]), row=1, col=2)  #|Här skapas andra grafen och här är också datumet på X-axeln och antal döda på Y-axeln.


    fig.update_layout(height=800, width=1500, title_text="National Total Deaths") #Sätter bredden till 800 och höjden till 1500 samt skriver "National Total Deaths" uppe i högra hörnet av html sidan.
    fig.update_xaxes(title_text="Datum", row=1, col=1)                      #|
    fig.update_xaxes(title_text="Datum", row=1, col=2)                      #|Skriver ut "Datum" på X-axeln.
    fig.update_yaxes(title_text="Antal döda den dagen", row=1, col=1)       #|
    fig.update_yaxes(title_text="Antal döda den dagen", row=1, col=2)       #|Skriver ut "Antal döda dem dagen" på Y-axeln.
    fig.write_html('first_figure.html', auto_open=True) #Öppnar html filen automatiskt.


if Val == 2:
    AgeGroups = pd.read_csv("National_Total_Deaths_by_Age_Group.csv", encoding = "ISO-8859-1", header = 0)  #Om användaren skriver 2 så läser programmet in "National_Total_Deaths_by_Age_Group.csv" på en variabel som heter AgeGroups.


    fig = make_subplots(rows=2, cols=2, specs=[[{"type":"surface"},{"type":"bar"}],[{"type":"bar"},{"type":"bar"}]])  #Här skapar subploten och två platser bredvid varandra på två olika rader.

    data = [go.Scatter3d()]
    fig.add_trace(go.Scatter3d(x=AgeGroups["Total_Cases"], y=AgeGroups["Age_Group"], z=AgeGroups["Total_Deaths"]), row=1,col=1) #Här skapar programmet första grafen och den är i 3D så här sätts antal smittade på X-axeln, åldern på Y-axeln och antal döda i varje grupp på Z-axeln.

    data = [go.Bar()]
    fig.add_trace(go.Bar(x=AgeGroups["Age_Group"], y=AgeGroups["Total_Cases"]), row=1, col=2)  #Här skapar programmet en 2D bar graf som visar åldern på X-axeln och hur många smittade på Y-axeln.

    data = [go.Bar()]
    fig.add_trace(go.Bar(x=AgeGroups["Age_Group"], y=AgeGroups["Total_Deaths"]), row=2, col=1)  #Här skapar programmet en till 2D bar graf fast som visar åldern på X-axeln och antal döda på Y-axeln.

    data = [go.Bar()]
    fig.add_trace(go.Bar(x=AgeGroups["Total_Cases"], y=AgeGroups["Total_Deaths"]), row=2, col=2)  #Här skapar programmer en sista 2D graf som visar Antal smittade på X-axeln och antal döda på Y-axeln.

    fig.update_layout(height=1000, width=1200, title_text="National Total Deaths by Age Group") 
    fig.update_xaxes(title_text="Ålder", row=1, col=2)  #|
    fig.update_xaxes(title_text="Ålder", row=2, col=1)  #|Skriver ut "Ålder" på X-axeln.
    fig.update_xaxes(title_text="Antal Döda", row=2, col=2) #Skriver ut "Antal Döda" på X-axeln.

    fig.update_yaxes(title_text="Antal Smittade", row=1, col=2) #Skriver ut "Antal Smittade" på Y-axeln.
    fig.update_yaxes(title_text="Antal Döda", row=2, col=1) #|
    fig.update_yaxes(title_text="Antal Döda", row=2, col=2) #|Skriver ut "Antal Döda" på Y-axeln.
    fig.write_html('first_figure.html', auto_open=True)  #Öppnar html dockumentet automatiskt.



#Källor :


#https://plotly.com/python/bar-charts/#bar-chart-with-wide-format-data

#https://plotly.com/python/plotly-express/

#https://plotly.com/python/subplots/