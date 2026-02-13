# Konwerter WLP -> HTML W Nowej Formie EXE!

## WLP → HTML Translator

**WLP_App.exe** to aplikacja desktopowa służąca do tłumaczenia plików  
**WLP (Web Language Program)** na standardowy **HTML**.

Program posiada graficzny interfejs użytkownika (GUI) i nie wymaga używania terminala.

---

## 📌 Funkcje

- Wybór pliku `.wlp`
- Automatyczna konwersja do `.html`
- Obsługa:
  - `title="..."`
  - `wlp-pro-key="..."`
  - `background-color="..."`
  - `text-color="..."`
  - `textbox(text="...", onclick="...")`
  - `inputtext(text="...")`
  - `button(text="...", onclick="...")`
- Zapisywanie wygenerowanego pliku HTML
- Prosty i szybki interfejs

---

## 🖥 Wymagania

- System Windows 10 / 11
- Brak potrzeby instalowania Pythona (program jest skompilowany do EXE)

---

## 🚀 Jak używać

1. Uruchom `WLP_App.exe`
2. Kliknij przycisk wyboru pliku
3. Wybierz plik `.wlp`
4. Wskaż miejsce zapisu pliku `.html`
5. Gotowe ✅

---

## 📂 Przykład pliku WLP

```wlp
start-web-page;
page {
  head {
    title="Moja strona";
    background-color="black";
    text-color="white";
  }
  body {
    textbox(text="Witaj świecie!");
    button(text="Kliknij mnie");
  }
}
code-end;
```

Po konwersji powstanie poprawny plik HTML.

---

## 📜 Struktura WLP

Plik musi zaczynać się od:

```
start-web-page;
```

i kończyć:

```
code-end;
```

---

## ⚠ Uwagi

- Program może nadpisać istniejący plik, jeśli wybierzesz tę samą nazwę.
- Obsługiwane są podstawowe funkcje WLP 1.0.
- Program nie interpretuje JavaScript — jedynie przekazuje go do HTML.

---

## 🔮 Planowane funkcje (WLP 2.0)

- Obsługa `<div>`
- Obsługa obrazów
- Klasy CSS
- Lepsze bezpieczeństwo
- Tryb PRO

---

## 👨‍💻 Autor

Projekt: **Web Language Program (WLP)**  
Silnik: **WLP_App.exe**
