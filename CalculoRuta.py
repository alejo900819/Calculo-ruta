import networkx as nx

def desarrollar_sistema_inteligente():
    G = nx.Graph()

    conexiones = [
        ("Portal Norte", "Calle 100", 15, "Troncal"),
        ("Calle 100", "Calle 72", 10, "Troncal"),
        ("Calle 72", "Av. Jiménez", 12, "Troncal"),
        ("Av. Jiménez", "Portal Américas", 25, "Troncal"),
        ("Calle 72", "Patios (Suba)", 20, "Alimentador")
    ]

    for origen, destino, tiempo, tipo in conexiones:
        G.add_edge(origen, destino, weight=tiempo, tipo=tipo)

    esta_lloviendo = True 
    
    print(">>> Iniciando razonamiento lógico...")

    for u, v, data in G.edges(data=True):
        if esta_lloviendo and data['tipo'] == "Alimentador":
            data['weight'] = data['weight'] * 1.5
            print(f"Aviso: La ruta hacia {v} se ha penalizado por lluvia.")

    punto_a = "Portal Norte"
    punto_b = "Patios (Suba)"

    try:
        ruta_final = nx.shortest_path(G, source=punto_a, target=punto_b, weight='weight')
        tiempo_total = nx.shortest_path_length(G, source=punto_a, target=punto_b, weight='weight')

        print("\n" + "="*40)
        print(f"MEJOR RUTA ENCONTRADA: {' -> '.join(ruta_final)}")
        print(f"TIEMPO TOTAL ESTIMADO: {tiempo_total} minutos")
        print("="*40)
    except nx.NetworkXNoPath:
        print("No se encontró una ruta disponible.")

desarrollar_sistema_inteligente()