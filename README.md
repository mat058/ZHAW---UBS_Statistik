<div align="center">

# UBS-Aktie: Renditen und Konfidenzintervalle

**Statistik-Übung (ZHAW) mit echten Kursdaten der UBS Group AG**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![yfinance](https://img.shields.io/badge/Daten-Yahoo%20Finance-6001D2)

[Aufgabenstellung](#aufgabenstellung) · [Vorgehen](#vorgehen) · [Ergebnis](#ergebnis) · [Ausführen](#ausführen)

</div>

---

## Aufgabenstellung

Anhand der Schlusskurse der UBS-Aktie (`UBSG.SW`, SIX Swiss Exchange) aus elf Handelstagen im
März 2025 werden die Tagesrenditen untersucht und die mittlere Tagesrendite mit Konfidenzintervallen geschätzt.

## Vorgehen

| Skript | Inhalt |
|---|---|
| [`aufgabe_c.py`](aufgabe_c.py) | Kursdaten laden, Tagesrenditen, Mittelwert, Standardabweichung und Standardfehler |
| [`aufgabe_d.py`](aufgabe_d.py) | Konfidenzintervalle (80 %, 90 %, 95 %, 99 %) mit der t-Verteilung (df = n − 1) und Grafik |

Verwendete Formeln:

- Tagesrendite: $r_t = \frac{P_t - P_{t-1}}{P_{t-1}}$
- Standardfehler: $SE = \frac{s}{\sqrt{n}}$
- Konfidenzintervall: $\bar{r} \pm t_{1-\alpha/2,\,n-1} \cdot SE$

## Ergebnis

<p align="center">
  <img src="konfidenzintervalle.png" alt="Konfidenzintervalle der mittleren UBS-Tagesrendite" width="720">
</p>

Je höher das Konfidenzniveau, desto breiter das Intervall. Bei nur zehn Renditen ist die Unsicherheit
entsprechend gross.

## Ausführen

```bash
git clone https://github.com/mat058/ZHAW---UBS_Statistik.git
cd ZHAW---UBS_Statistik
pip install -r requirements.txt
python aufgabe_c.py
python aufgabe_d.py
```

Die Kursdaten werden beim Ausführen live über Yahoo Finance geladen.
