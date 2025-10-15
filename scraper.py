import pandas as pd

df = pd.DataFrame({
    "Marca": ["Citroen", "Fiat", "Ford"],
    "Modello": ["C3", "Punto", "Fiesta"],
    "Allestimento": ["Base", "Base", "Base"],
    "Anno": [2008, 2009, 2007],
    "0-100 km/h": [12.5, 11.8, 13.2],
    "Consumo_misto": [5.8, 6.2, 6.0],
    "Coppia_Nm": [95, 100, 90]
})
df.to_excel("auto_analisi.xlsx", index=False)
print("Excel auto_analisi.xlsx creato correttamente.")
