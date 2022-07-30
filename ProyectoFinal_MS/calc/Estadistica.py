import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import seaborn as sbn

class Estadistica:
    """
    Clase estadistica que se encarga de realizar diferentes
    calculos estadisticos sobre el proyecto de ventas
    """
    def __init__(self):
        self.df = pd.read_csv('static/file/CardioGoodFitness_Fuente_datos.csv')
        # self.recombrarDistritos()
        # self.recombrarPaises()
        #Transformación del tipo de dato de Fecha
        #self.df['Date'] = pd.to_datetime(self.df['Date'])
        #Extración unicamente del mes
        #Mejora en la presentación de la información
        self.df['fitness'] = self.df['Fitness'].map({1: 'muy mal',
                                       2: 'un poco mal',
                                       3: 'regular',
                                       4: 'bien',
                                       5: 'muy bien'})
        self.df['income'] = self.df['Income']

    def datos(self):
        """
        funcion que retorna el dataframe con los datos
        """
        return self.df