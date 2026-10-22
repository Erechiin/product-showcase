from flask import Flask, render_template

from models.product import DigitalProduct, PhysicalProduct

app = Flask(__name__)

# CUSTOMIZE HERE: choose a theme and introduce your showcase.
SHOWCASE_NAME = "MineShop — Mercado do Vilarejo"
SHOWCASE_DESCRIPTION = "Explore o comércio do Overworld e do Nether! Visite a oficina de cada Villager e troque suas Esmeraldas."
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
        "icone": "⚒️",
        "tema": "theme-armeiro",
        "frase": "Forjo lâminas, machados e picaretas desde que a primeira mina foi aberta abaixo da vila. Se precisa quebrar Obsidiana ou enfrentar hordas à noite, veio à forja certa!",
        "especialidade": "Armas corpo a corpo, picaretas de mineração e armaduras pesadas",
    },
    "fazendeiro": {
        "id": "fazendeiro",
        "nome": "Aldeão Tobias",
        "profissao": "Mestre Fazendeiro & Carpinteiro",
        "nivel": "Nível 5 · Mestre (Esmeralda)",
        "bloco_trabalho": "Compostador & Bancada de Madeira",
        "dimensao": "overworld",
        "dimensao_nome": "Overworld",
        "icone": "🌾",
        "tema": "theme-fazendeiro",
        "frase": "Cuido das plantações de trigo e das florestas de carvalho ao redor do vilarejo. Meus blocos levantam qualquer construção e meus pães mantêm você de pé!",
        "especialidade": "Blocos de construção, madeiras nobres, fardos e alimentos da fazenda",
    },
    "alquimista": {
        "id": "alquimista",
        "nome": "Clérigo Eldrin",
        "profissao": "Mestre Alquimista & Encantador",
        "nivel": "Nível 5 · Mestre (Esmeralda)",
        "bloco_trabalho": "Suporte de Poções & Mesa de Encantamentos",
        "dimensao": "overworld",
        "dimensao_nome": "Overworld",
        "icone": "🧪",
        "tema": "theme-alquimista",
        "frase": "No alto da torre da vila, destilo poções raras e preparo frutas douradas encantadas para garantir velocidade, regeneração e magia aos viajantes.",
        "especialidade": "Poções alquímicas, maçãs douradas e artefatos místicos",
    },
    "nether_trader": {
        "id": "nether_trader",
        "nome": "Mercador Ignis",
        "profissao": "Forjador do Bastião Rubro",
        "nivel": "Nível 5 · Ancião do Nether",
        "bloco_trabalho": "Bigorna de Netherita & Âncora de Renascimento",
        "dimensao": "nether",
        "dimensao_nome": "Nether",
        "icone": "🔥",
        "tema": "theme-nether",
        "frase": "Direto das fortalezas e bastiões além do portal de Obsidiana! Trago equipamentos de Netherita, blocos luminosos e elixires contra o fogo do Nether.",
        "especialidade": "Equipamentos de Netherita, blocos dimensionais e poções de resistência ao fogo",
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
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite do Machado de Diamante
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
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite do Peitoral de Ferro
                "descricao": "Armadura peitoral reforçada no alto-forno para proteger contra flechas e explosões.",
                "lore": "Encantamento sugerido: Proteção IV · Inquebrável III",
                "classe": "fisico",
                "entrega": "Forja do Ferreiro Gorak (Armorer)",
                "villager_id": "armeiro",
                "dimensao": "overworld",
            },
            {
                "id": 12,
                "nome": "Espada de Netherita",
                "preco": 48,
                "stack": 1,
                "dano": "+8 Ataque (Imune à Lava)",
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite da Espada de Netherita
                "descricao": "Forjada com Detritos Ancestrais nas profundezas do Nether. Não queima na lava!",
                "lore": "Relíquia do Bastião · Afiação V · Aspecto Flamejante II",
                "classe": "fisico",
                "entrega": "Bastião do Mercador Ignis (Nether)",
                "villager_id": "nether_trader",
                "dimensao": "nether",
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
                "imagem": "Hay_Bale_(UD)_JE3_BE3.png",
                "descricao": "Amortece 80% do dano de queda e serve para alimentar cavalos e lhamas.",
                "lore": "Compactado com 9 trigos colhidos nas fazendas ensolaradas da vila.",
                "classe": "fisico",
                "entrega": "Celeiro do Aldeão Tobias (Farmer)",
                "villager_id": "fazendeiro",
                "dimensao": "overworld",
            },
            {
                "id": 4,
                "nome": "Tronco de Carvalho",
                "preco": 4,
                "stack": 64,
                "tipo": "Madeira",
                "imagem": "Oak_Log_(UD)_JE8_BE3.png",
                "descricao": "Bloco básico e versátil para tábuas, bancadas de trabalho e estruturas.",
                "lore": "Rende 4 Tábuas de Carvalho por tronco refinado.",
                "classe": "fisico",
                "entrega": "Serraria do Aldeão Tobias",
                "villager_id": "fazendeiro",
                "dimensao": "overworld",
            },
            {
                "id": 9,
                "nome": "Estante de Livros",
                "preco": 9,
                "stack": 64,
                "tipo": "Encantamento / Decoração",
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite da Estante de Livros
                "descricao": "Aumenta o nível de poder da Mesa de Encantamentos e decora sua base.",
                "lore": "Feita com 6 Tábuas de Carvalho e 3 Livros encadernados.",
                "classe": "fisico",
                "entrega": "Carpintaria do Aldeão Tobias",
                "villager_id": "fazendeiro",
                "dimensao": "overworld",
            },
            {
                "id": 10,
                "nome": "Pão Fresco da Vila",
                "preco": 3,
                "stack": 64,
                "tipo": "Alimento (+5 Fome)",
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite do Pão
                "descricao": "Assado todas as manhãs com trigo selecionado das plantações da vila.",
                "lore": "Restaura 2.5 coxas de fome e 6 pontos de saturação.",
                "classe": "fisico",
                "entrega": "Padaria do Aldeão Tobias (Farmer)",
                "villager_id": "fazendeiro",
                "dimensao": "overworld",
            },
            {
                "id": 13,
                "nome": "Pedra Luminosa (Glowstone)",
                "preco": 6,
                "stack": 64,
                "tipo": "Iluminação Nível 15 (Nether)",
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite da Glowstone
                "descricao": "Cristal brilhante colhido no teto do Nether. Ilumina até debaixo d'água.",
                "lore": "Fonte para recarregar Âncoras de Renascimento.",
                "classe": "fisico",
                "entrega": "Caravana do Mercador Ignis (Nether)",
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
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite do Bottle o' Enchanting
                "descricao": "Frasco cintilante que libera orbes de XP ao ser lançado no chão.",
                "lore": "Perfeito para reparar itens com Reparação ou encantar equipamentos.",
                "classe": "digital",
                "entrega": "Torre do Clérigo Eldrin (Orbes de XP)",
                "villager_id": "alquimista",
                "dimensao": "overworld",
            },
            {
                "id": 14,
                "nome": "Poção de Resistência ao Fogo",
                "preco": 15,
                "stack": 1,
                "duracao": "8:00 min (Imune a Fogo/Lava)",
                "imagem": "placeholder.svg",  # Trocar depois pelo sprite da Poção de Resistência ao Fogo
                "descricao": "Indispensável para explorar fortalezas do Nether e nadar em mares de lava.",
                "lore": "Destilada com Creme de Magma e Redstone no Bastião.",
                "classe": "digital",
                "entrega": "Alquimia do Mercador Ignis (Nether)",
                "villager_id": "nether_trader",
                "dimensao": "nether",
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
