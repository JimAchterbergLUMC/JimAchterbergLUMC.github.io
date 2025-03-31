from scholarly import scholarly
import json

SCHOLAR_ID = "YOUR_SCHOLAR_ID"


def fetch_publications():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    publications = []
    for pub in author.get("publications", []):
        title = pub["bib"].get("title", "Unknown Title")
        year = pub["bib"].get("pub_year", "Unknown Year")
        link = pub.get("pub_url", "#")
        publications.append({"title": title, "year": year, "link": link})

    with open("publications.json", "w") as f:
        json.dump(publications, f, indent=4)


if __name__ == "__main__":
    fetch_publications()
