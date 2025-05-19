from Tufinho.scraper.scraper import baixar_pagina

def main():
    html = baixar_pagina
    if html:
        print(f"HTML baixado com {len(html)} caracteres.")


if __name__ == "__main__":
    main()