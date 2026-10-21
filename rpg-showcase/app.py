from flask import Flask, render_template

from models.product import DigitalProduct, PhysicalProduct

app = Flask(__name__)

# CUSTOMIZE HERE: choose a theme and introduce your showcase.
SHOWCASE_NAME = "MineShop — Mercado do Vilarejo"
SHOWCASE_DESCRIPTION = "Troque suas Esmeraldas por equipamentos, blocos e poções com os mestres aldeões."
AUTHOR_NAME = "Mestre Aldeão"

CATEGORIAS = [
    {
        "id": "armas",
        "nome": "Armas & Ferramentas",
        "itens": [
            {
                "id": 1,
                "nome": "Espada de Ferro",
                "preco": 8,
                "stack": 1,
                "dano": "+6 Ataque",
                "imagem": "placeholder.svg",  # Sprite futuro: iron_sword.png
                "descricao": "Lâmina confiável forjada na bigorna do vilarejo para combate corpo a corpo.",
                "lore": "Encantamento sugerido: Afiação III · Reparação",
                "classe": "fisico",
                "entrega": "Ferreiro de Armas (Armorer)",
            },
            {
                "id": 2,
                "nome": "Picareta de Diamante",
                "preco": 24,
                "stack": 1,
                "durabilidade": "1561 usos",
                "imagem": "placeholder.svg",  # Sprite futuro: diamond_pickaxe.png
                "descricao": "Ferramenta de alta resistência capaz de extrair Obsidiana e minérios raros.",
                "lore": "Encantamento sugerido: Eficiência IV · Fortuna III",
                "classe": "fisico",
                "entrega": "Mestre Ferramenteiro (Toolsmith)",
            },
        ],
    },
    {
        "id": "blocos",
        "nome": "Blocos & Recursos",
        "itens": [
            {
                "id": 3,
                "nome": "Fardo de Feno",
                "preco": 2,
                "stack": 64,
                "tipo": "Construção/Alimento",
                "imagem": "placeholder.svg",  # Sprite futuro: hay_block.png
                "descricao": "Amortece 80% do dano de queda e serve para alimentar cavalos e lhamas.",
                "lore": "Compactado com 9 trigos colhidos nas fazendas da vila.",
                "classe": "fisico",
                "entrega": "Fazendeiro da Vila (Farmer)",
            },
            {
                "id": 4,
                "nome": "Tronco de Carvalho",
                "preco": 4,
                "stack": 64,
                "tipo": "Madeira",
                "imagem": "placeholder.svg",  # Sprite futuro: oak_log.png
                "descricao": "Bloco básico e versátil para tábuas, bancadas de trabalho e estruturas.",
                "lore": "4 Tábuas de Carvalho por tronco refinado.",
                "classe": "fisico",
                "entrega": "Lenhador do Vilarejo",
            },
        ],
    },
    {
        "id": "alquimia",
        "nome": "Poções & Consumíveis",
        "itens": [
            {
                "id": 5,
                "nome": "Poção de Agilidade II",
                "preco": 12,
                "stack": 1,
                "duracao": "1:30 min",
                "imagem": "placeholder.svg",  # Sprite futuro: speed_potion.png
                "descricao": "Aumenta a velocidade de movimento em +40% para explorar biomas rapidamente.",
                "lore": "Destilada com Fungo do Nether, Açúcar e Pó de Pedra Luminosa.",
                "classe": "digital",
                "entrega": "Efeito Alquímico Instantâneo",
            },
            {
                "id": 6,
                "nome": "Maçã Dourada",
                "preco": 16,
                "stack": 64,
                "efeito": "Regeneração II",
                "imagem": "placeholder.svg",  # Sprite futuro: golden_apple.png
                "descricao": "Fruta mística revestida com 8 barras de ouro puro que restaura corações.",
                "lore": "Concede Regeneração II (5s) e Absorção I (2:00 min).",
                "classe": "digital",
                "entrega": "Bênção Mística no Inventário",
            },
        ],
    },
]


def _build_products(categorias):
    built_products = []
    for categoria in categorias:
        for item in categoria["itens"]:
            if "dano" in item:
                stat_label, stat_value = "Dano", item["dano"]
            elif "durabilidade" in item:
                stat_label, stat_value = "Durabilidade", item["durabilidade"]
            elif "tipo" in item:
                stat_label, stat_value = "Tipo", item["tipo"]
            elif "duracao" in item:
                stat_label, stat_value = "Duração", item["duracao"]
            else:
                stat_label, stat_value = "Efeito", item.get("efeito", "Especial")

            common_kwargs = dict(
                item_id=item["id"],
                name=item["nome"],
                description=item["descricao"],
                price=float(item["preco"]),
                image=item["imagem"],
                category_id=categoria["id"],
                category_name=categoria["nome"],
                stack=item["stack"],
                stat_label=stat_label,
                stat_value=stat_value,
                lore=item["lore"],
            )

            if item.get("classe") == "digital":
                built_products.append(
                    DigitalProduct(
                        file_format=item["entrega"],
                        **common_kwargs,
                    )
                )
            else:
                built_products.append(
                    PhysicalProduct(
                        pickup_location=item["entrega"],
                        **common_kwargs,
                    )
                )
    return built_products


products = _build_products(CATEGORIAS)


@app.route("/")
def index():
    return render_template(
        "index.html",
        showcase_name=SHOWCASE_NAME,
        showcase_description=SHOWCASE_DESCRIPTION,
        author_name=AUTHOR_NAME,
        products=products,
        categories=CATEGORIAS,
    )
