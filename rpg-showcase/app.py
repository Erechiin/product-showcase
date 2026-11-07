from flask import Flask, render_template

from models.product import DigitalProduct, PhysicalProduct

app = Flask(__name__)

# CUSTOMIZE HERE: choose a theme and introduce your showcase.
SHOWCASE_NAME = "MineShop — Mercado do Vilarejo"
SHOWCASE_DESCRIPTION = "Explore o comércio do Overworld e do Nether! Visite a oficina de cada Villager e troque suas Esmeraldas e Barras de Ouro."
AUTHOR_NAME = "Mestre Aldeão"

VILLAGERS = {
    "armeiro": {
        "id": "armeiro",
        "nome": "Ferreiro Gorak",
        "profissao": "Mestre Armeiro & Ferramenteiro",
        "nivel": "Nível 5 · Mestre (Esmeralda)",
        "bloco_trabalho": "Bigorna & Alto-Forno",
        "dimensao": "overworld",
        "dimensao_nome": "Overworld",
        "moeda_nome": "Esmeraldas",
        "moeda_curta": "Esm.",
        "moeda_icone": "/static/images/Emerald_JE3_BE3.png",
        "icone": "⚒️",
        "avatar": "/static/images/ferreiro.png",
        "flip_avatar": True,
        "tema": "theme-armeiro",
        "frase": "Forjo lâminas, machados e picaretas desde que a primeira mina foi aberta abaixo da vila. Se precisa quebrar Obsidiana ou enfrentar hordas à noite, veio à forja certa!",
        "especialidade": "Armas corpo a corpo, picaretas de mineração e armaduras pesadas",
    },
    "alquimista": {
        "id": "alquimista",
        "nome": "Clérigo Eldrin",
        "profissao": "Mestre Alquimista & Encantador",
        "nivel": "Nível 5 · Mestre (Esmeralda)",
        "bloco_trabalho": "Suporte de Poções & Mesa de Encantamentos",
        "dimensao": "overworld",
        "dimensao_nome": "Overworld",
        "moeda_nome": "Esmeraldas",
        "moeda_curta": "Esm.",
        "moeda_icone": "/static/images/Emerald_JE3_BE3.png",
        "icone": "🧪",
        "avatar": "/static/images/Savanna_Cleric.png",
        "flip_avatar": True,
        "tema": "theme-alquimista",
        "frase": "No alto da torre da vila, destilo poções raras e preparo frutas douradas encantadas para garantir velocidade, regeneração e magia aos viajantes.",
        "especialidade": "Poções alquímicas, maçãs douradas e artefatos místicos",
    },
    "nether_trader": {
        "id": "nether_trader",
        "nome": "Mercador Ignis (Piglin)",
        "profissao": "Mestre de Trocas do Bastião (Piglin)",
        "nivel": "Nível 5 · Mestre do Ouro (Piglin)",
        "bloco_trabalho": "Baú do Bastião & Âncora de Renascimento",
        "dimensao": "nether",
        "dimensao_nome": "Nether",
        "moeda_nome": "Barras de Ouro",
        "moeda_curta": "Ouro",
        "moeda_icone": "/static/images/Gold_Ingot_JE4_BE2.png",
        "icone": "🔥",
        "avatar": "/static/images/piglincard.png",
        "flip_avatar": True,
        "tema": "theme-ignis",
        "frase": "Esmeraldas não têm valor aqui no Nether! Traga suas Barras de Ouro brilhantes e eu troco por Pérolas do Fim, Obsidiana Chorona e Netherita pura!",
        "especialidade": "Bartering por Barras de Ouro: Pérolas do Fim, Obsidiana Chorona e Netherita",
    },
}

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
                "imagem": "Iron_Sword_JE2_BE2.png",
                "descricao": "Lâmina confiável forjada na bigorna do vilarejo para combate corpo a corpo.",
                "lore": "Encantamento sugerido: Afiação III · Reparação",
                "classe": "fisico",
                "entrega": "Forja do Ferreiro Gorak (Armorer)",
                "villager_id": "armeiro",
                "dimensao": "overworld",
            },
            {
                "id": 2,
                "nome": "Picareta de Diamante",
                "preco": 24,
                "stack": 1,
                "durabilidade": "1561 usos",
                "imagem": "Diamond_Pickaxe_JE3_BE3.png",
                "descricao": "Ferramenta de alta resistência capaz de extrair Obsidiana e minérios raros.",
                "lore": "Encantamento sugerido: Eficiência IV · Fortuna III",
                "classe": "fisico",
                "entrega": "Forja do Ferreiro Gorak (Toolsmith)",
                "villager_id": "armeiro",
                "dimensao": "overworld",
            },
            {
                "id": 7,
                "nome": "Machado de Diamante",
                "preco": 20,
                "stack": 1,
                "dano": "+9 Ataque / Corte Rápido",
                "imagem": "machadodiamante.png",
                "descricao": "Corta troncos instantaneamente e quebra escudos inimigos com golpes pesados.",
                "lore": "Encantamento sugerido: Eficiência V · Toque Suave",
                "classe": "fisico",
                "entrega": "Forja do Ferreiro Gorak (Weaponsmith)",
                "villager_id": "armeiro",
                "dimensao": "overworld",
            },
            {
                "id": 8,
                "nome": "Peitoral de Ferro",
                "preco": 18,
                "stack": 1,
                "durabilidade": "240 usos (+6 Armadura)",
                "imagem": "peitoralferro.png",
                "descricao": "Armadura peitoral reforçada no alto-forno para proteger contra flechas e explosões.",
                "lore": "Encantamento sugerido: Proteção IV · Inquebrável III",
                "classe": "fisico",
                "entrega": "Forja do Ferreiro Gorak (Armorer)",
                "villager_id": "armeiro",
                "dimensao": "overworld",
            },
        ],
    },
    {
        "id": "blocos",
        "nome": "Relíquias & Recursos",
        "itens": [
            {
                "id": 12,
                "nome": "Pérola do Fim (Ender Pearl)",
                "preco": 14,
                "stack": 16,
                "tipo": "Teleporte Dimensional",
                "imagem": "Ender_Pearl_JE3_BE2.png",
                "descricao": "Item favorito nas trocas com Piglins! Permite se teleportar instantaneamente ao lançá-la.",
                "lore": "Essencial para fabricar Olhos do Fim e encontrar o Portal do End.",
                "classe": "fisico",
                "entrega": "Bartering com Mercador Ignis (Piglin)",
                "villager_id": "nether_trader",
                "dimensao": "nether",
            },
            {
                "id": 13,
                "nome": "Obsidiana Chorona",
                "preco": 10,
                "stack": 64,
                "tipo": "Bloco Raro do Bastião",
                "imagem": "Crying_Obsidian_JE1_BE1.png",
                "descricao": "Obsidiana ancestral que emana partículas roxas luminosas, exclusiva de trocas com Piglins.",
                "lore": "Usada para construir Âncoras de Renascimento no Nether.",
                "classe": "fisico",
                "entrega": "Bastião do Mercador Ignis (Piglin)",
                "villager_id": "nether_trader",
                "dimensao": "nether",
            },
            {
                "id": 14,
                "nome": "Barra de Netherita",
                "preco": 36,
                "stack": 64,
                "tipo": "Metal Lendário (Imune à Lava)",
                "imagem": "Netherite_Ingot_JE1_BE2.png",
                "descricao": "Fundida com 4 Fragmentos de Netherita e 4 Barras de Ouro nos tesouros do Bastião.",
                "lore": "Melhora qualquer equipamento de Diamante na Bancada de Ferraria.",
                "classe": "fisico",
                "entrega": "Cofre Real do Mercador Ignis (Piglin)",
                "villager_id": "nether_trader",
                "dimensao": "nether",
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
                "imagem": "Potion_of_Swiftness_JE3.png",
                "descricao": "Aumenta a velocidade de movimento em +40% para explorar biomas rapidamente.",
                "lore": "Destilada com Fungo do Nether, Açúcar e Pó de Pedra Luminosa.",
                "classe": "digital",
                "entrega": "Torre do Clérigo Eldrin (Efeito Alquímico)",
                "villager_id": "alquimista",
                "dimensao": "overworld",
            },
            {
                "id": 6,
                "nome": "Maçã Dourada",
                "preco": 16,
                "stack": 64,
                "efeito": "Regeneração II",
                "imagem": "Golden_Apple_JE2_BE2.png",
                "descricao": "Fruta mística revestida com 8 barras de ouro puro que restaura corações.",
                "lore": "Concede Regeneração II (5s) e Absorção I (2:00 min).",
                "classe": "digital",
                "entrega": "Altar do Clérigo Eldrin (Bênção Mística)",
                "villager_id": "alquimista",
                "dimensao": "overworld",
            },
            {
                "id": 11,
                "nome": "Frasco de Experiência",
                "preco": 10,
                "stack": 64,
                "efeito": "+XP de Encantamento",
                "imagem": "Bottle_o'_Enchanting_JE1_BE1.png",
                "descricao": "Frasco cintilante que libera orbes de XP ao ser lançado no chão.",
                "lore": "Perfeito para reparar itens com Reparação ou encantar equipamentos.",
                "classe": "digital",
                "entrega": "Torre do Clérigo Eldrin (Orbes de XP)",
                "villager_id": "alquimista",
                "dimensao": "overworld",
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

            v_id = item.get("villager_id", "armeiro")
            villager_info = VILLAGERS.get(v_id, VILLAGERS["armeiro"])

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
                villager_id=v_id,
                villager_name=villager_info["nome"],
                villager_role=villager_info["profissao"],
                dimension=item.get("dimensao", villager_info["dimensao"]),
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
        villagers=VILLAGERS,
    )
