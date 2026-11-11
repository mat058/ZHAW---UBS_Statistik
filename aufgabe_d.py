# Schritt 1: Libraries importieren

import yfinance as yf
import numpy as np
from scipy import stats

# Schritt 2: Daten laden (gleich wie Aufgabe c)

daten = yf.download("UBSG.SW", start="2025-03-10", end="2025-03-25")
schlusskurse = daten["Close"]["UBSG.SW"]
schlusskurse = schlusskurse.head(11)

# Schritt 3: Renditen, Mittelwert, SE berechnen

renditen = schlusskurse.pct_change().dropna()
n = len(renditen)
mittelwert = renditen.mean()
standardabweichung = renditen.std(ddof=1)
standardfehler = standardabweichung / np.sqrt(n)

print(f"Mittelwert: {mittelwert:.6f}")
print(f"Standardfehler: {standardfehler:.6f}")
print(f"Freiheitsgrade (df): {n - 1}")

# Schritt 4: Konfidenzintervalle berechnen

konfidenzniveaus = [0.80, 0.90, 0.95, 0.99]
df = n - 1  # Freiheitsgrade = 9

print("\n=== Konfidenzintervalle ===")
print(f"{'Niveau':<12} {'t-Wert':<10} {'Untergrenze':<16} {'Obergrenze':<16} {'Breite':<12}")
print("-" * 66)

for niveau in konfidenzniveaus:

    t_wert = stats.t.ppf((1 + niveau) / 2, df)

    # Unter- und Obergrenze berechnen
    untergrenze = mittelwert - t_wert * standardfehler
    obergrenze = mittelwert + t_wert * standardfehler
    breite = obergrenze - untergrenze

    print(f"{niveau*100:>5.0f}%      {t_wert:<10.4f} {untergrenze:<16.6f} {obergrenze:<16.6f} {breite:<12.6f}")

    # Schritt 5: Grafische Darstellung der Konfidenzintervalle

import matplotlib.pyplot as plt

# Daten für den Plot vorbereiten
farben = ['#2ecc71', '#3498db', '#e67e22', '#e74c3c']
labels = []
t_werte = []
untergrenzen = []
obergrenzen = []

for niveau in konfidenzniveaus:
    t_wert = stats.t.ppf((1 + niveau) / 2, df)
    untergrenze = mittelwert - t_wert * standardfehler
    obergrenze = mittelwert + t_wert * standardfehler
    labels.append(f"{niveau*100:.0f}%")
    t_werte.append(t_wert)
    untergrenzen.append(untergrenze)
    obergrenzen.append(obergrenze)

# Plot erstellen
fig, ax = plt.subplots(figsize=(10, 5))

for i in range(len(konfidenzniveaus)):
    # Horizontaler Balken für jedes Konfidenzintervall
    ax.barh(i, obergrenzen[i] - untergrenzen[i],
            left=untergrenzen[i], height=0.5,
            color=farben[i], alpha=0.7,
            label=f"{labels[i]} (t = {t_werte[i]:.3f})")

# Mittelwert als vertikale Linie
ax.axvline(x=mittelwert, color='black', linestyle='--', linewidth=1.5, label=f'Mittelwert = {mittelwert:.4f}')

# Achsen beschriften
ax.set_yticks(range(len(konfidenzniveaus)))
ax.set_yticklabels(labels, fontsize=12)
ax.set_xlabel('Tagesrendite', fontsize=12)
ax.set_title('Konfidenzintervalle für die mittlere UBS-Tagesrendite', fontsize=14)
ax.legend(loc='lower right', fontsize=10)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('konfidenzintervalle.png', dpi=150)
plt.show()

print("\nGrafik wurde als 'konfidenzintervalle.png' gespeichert.")