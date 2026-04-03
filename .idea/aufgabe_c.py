#Schritt 1: Libraries importieren

import yfinance as yf
import pandas as pd
import numpy as np

#Schritt 2: UBS-Kursdaten herunterladen

daten = yf.download("UBSG.SW", start="2025-03-10", end="2025-03-25")

# Nur die Schlusskurse extrahieren
schlusskurse = daten["Close"]["UBSG.SW"]

# Die ersten 11 Handelstage nehmen
schlusskurse = schlusskurse.head(11)

print("=== Schlusskurse der UBS-Aktie ===")
print(schlusskurse)
print(f"\nAnzahl Kurse: {len(schlusskurse)}")

# Schritt 3: Tagesrenditen berechnen

renditen = schlusskurse.pct_change().dropna()

print("\n=== Tagesrenditen der UBS-Aktie ===")
print(renditen)
print(f"\nAnzahl Renditen: {len(renditen)}")

# Schritt 4: Mittelwert der Tagesrenditen

mittelwert = renditen.mean()

print("\n=== Mittelwert der Tagesrenditen ===")
print(f"Mittelwert: {mittelwert:.6f}")
print(f"In Prozent: {mittelwert * 100:.4f}%")

# Schritt 5: Standardabweichung berechnen

standardabweichung = renditen.std(ddof=1)

print("\n=== Standardabweichung der Tagesrenditen ===")
print(f"Standardabweichung: {standardabweichung:.6f}")
print(f"In Prozent: {standardabweichung * 100:.4f}%")

# Schritt 6: Standardfehler berechnen

n = len(renditen)
standardfehler = standardabweichung / np.sqrt(n)

print("\n=== Standardfehler des Stichprobenmittelwerts ===")
print(f"Anzahl Beobachtungen (n): {n}")
print(f"Standardabweichung (s):   {standardabweichung:.6f}")
print(f"Standardfehler (SE):      {standardfehler:.6f}")
print(f"In Prozent:               {standardfehler * 100:.4f}%")