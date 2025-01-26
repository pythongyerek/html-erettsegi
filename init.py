import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def html_content():
    # Betöltjük a HTML fájlt teszteléshez
    with open("troli.html", encoding="utf-8") as file:
        content = file.read()
    return content

def test_title_exists(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title
    assert title is not None, "Hiányzik a <title> elem a dokumentumból!"
    assert title.string == "Trolibuszok", "A cím nem megfelelő!"

def test_header_exists(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    header = soup.find("h1")
    assert header is not None, "Hiányzik a főcím (<h1>) a dokumentumból!"
    assert header.text.strip() == "Érettségi Web Feladat", "A főcím szövege hibás!"

def test_table_structure(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")
    assert table is not None, "Hiányzik a táblázat a HTML dokumentumból!"

    # Ellenőrizzük, hogy van-e fejléc (thead)
    thead = table.find("thead")
    assert thead is not None, "A táblázatnak nincs fejléc része!"

    # Ellenőrizzük, hogy van-e legalább egy sor (tr) az adatok között
    tbody = table.find("tbody")
    assert tbody is not None, "A táblázatnak nincs tartalmi része!"
    rows = tbody.find_all("tr")
    assert len(rows) > 0, "A táblázat nem tartalmaz adatokat!"

def test_css_styles(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    styles = soup.find_all("link", {"rel": "stylesheet"})
    assert len(styles) > 0, "Nincs CSS fájl a dokumentumhoz linkelve!"
    css_links = [style["href"] for style in styles]
    assert "styles.css" in css_links, "A styles.css fájl nincs linkelve!"
