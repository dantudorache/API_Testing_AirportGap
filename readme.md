
1. Instalarea librariilor necesare se va face in Terminal folosind urmatoarele comenzi:
    - pip install pytest
    - pip install requests
    - pip install pytest pytest-html

    Instalarea librariilor se mai poate face si din Pyton Packages
    cautand numele librariilor (pytest, requests, pytest-html ) in bara de cautare.

2. Rularea testelor se va face in Terminal folosind urmatoarele comenzi:
    - pytest tests
    - pytest tests -v
    - pytest tests/file_name -v

   Inaintea rularii unui nou test este necesara rularea comenzii: "pytest tests/test_delete_favorites_clear_all.py -v"
   in Terminal.

3. Generare raport in Terminal:
    - pytest --html=report.html

4. Accesarea raportului html:
    - click dreapta pe fisierul raport.html
    - Open in > Browser > se va alege browser-ul dorit

