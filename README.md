# wejsciowka3MN

# README

## Opis Zadań i Wyników

### Zadanie 1: Metoda Newtona

**Cel:** Znalezienie miejsca zerowego funkcji \( f(x) = cos(exp(x / 5))) w przedziale \((32, 34)\) z wykorzystaniem metody Newtona.

- **Parametry wejściowe:**

  - Punkt początkowy: \( x0 = 33 \)
  - Dokładność: \( epsilon = 0.026 )
  - Maksymalna liczba iteracji: 10

- **Rezultat:**
  - Iteracja 1: \( x = 32.818 \), \( f(x) = 0.465 \)
  - Iteracja 2: \( x = 32.815 \), \( f(x) = -0.041 \)
  - **Miejsce zerowe:** \( x = 32.815 \)

---

### Zadanie 2: Obliczanie Pierwiastków Wielomianu

**Cel:** Wyznaczenie miejsc zerowych wielomianu:
\[
f(x) = x^4 - 19x^3 + 126x^2 - 344x + 320
\]

- **Metoda:** Obliczenie pierwiastków za pomocą biblioteki NumPy (`np.roots`) i posortowanie wyników.

- **Rezultat:** Pierwiastki wielomianu:
  \[
  [0.125, 0.2, 0.25, 0.5]
  \]

---

### Zadanie 3: Metoda Bisekcji

**Cel:** Znalezienie miejsca zerowego funkcji:
\[
f(x) = sin(x - 1) + exp(-(x - 3)^2)
\]
w przedziale \((10, 14)\) z dokładnością \( epsilon = 0.087 \) i maksymalnie 10 iteracjami.

- **Rezultat:**
  - Funkcja nie zmienia znaku w podanym przedziale (\( f(a) cdot f(b) > 0 \)).
  - **Odpowiedź:** \( None \)

---

## Podsumowanie

1. **Metoda Newtona** wykazała szybkie zbieganie do miejsca zerowego \( x = 32.815 \).
2. **Pierwiastki wielomianu** zostały poprawnie obliczone i posortowane.
3. **Metoda bisekcji** nie mogła zostać zastosowana z powodu braku zmiany znaku funkcji w podanym przedziale.
