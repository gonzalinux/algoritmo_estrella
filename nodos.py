from NodosMetro import NodosMetro


class Nodo:
    def __init__(self):
        nodos = dict()
        nodos["Kifissia"] = NodosMetro("Kifissia", 536, 99, [1])
        nodos["KAT"] = NodosMetro("KAT", 502, 133, [1])
        nodos["Maroussi"] = NodosMetro("Maroussi", 469, 167, [1])
        nodos["Neratziotissa"] = NodosMetro("Neratziotissa", 432, 202, [1])
        nodos["Irini"] = NodosMetro("Irini", 403, 204, [1])
        nodos["Iraklio"] = NodosMetro("Iraklio", 331, 212, [1])
        nodos["Nea Ionia"] = NodosMetro("Nea Ionia", 313, 232, [1])
        nodos["Pefkakia"] = NodosMetro("Pefkakia", 294, 249, [1])
        nodos["Perissos"] = NodosMetro("Perissos", 275, 269, [1])
        nodos["Ano Pahssia"] = NodosMetro("Ano Pahssia", 256, 288, [1])
        nodos["Aghios Eleftherios"] = NodosMetro("Aghios Eleftherios", 236, 308, [1])
        nodos["Kato Patissia"] = NodosMetro("Kato Patissa", 215, 330, [1])
        nodos["Aghios Nikolaos"] = NodosMetro("Aghios Nikolaos", 193, 351, [1])
        nodos["Attiki"] = NodosMetro("Attiki", 176, 370, [1, 2])
        nodos["Victoria"] = NodosMetro("Victoria", 213, 420, [1])
        nodos["Omonia"] = NodosMetro("Omonia", 214, 451, [1, 2])
        nodos["Monastiraki"] = NodosMetro("Monastiraki", 212, 485, [1, 3])
        nodos["Thissio"] = NodosMetro("Thissio", 211, 522, [1])
        nodos["Petralona"] = NodosMetro("Petralona", 203, 546, [1])
        nodos["Tavros"] = NodosMetro("Tavros", 181, 569, [1])
        nodos["Kallithea"] = NodosMetro("Kallithea", 158, 593, [1])
        nodos["Moschato"] = NodosMetro("Moschato", 136, 613, [1])
        nodos["Faliro"] = NodosMetro("Falira", 112, 638, [1])
        nodos["Piraeus"] = NodosMetro("Piraeus", 22, 648, [1])



        nodos["Aghios Antonios"] = NodosMetro("Aghios Antonios", 113, 305, [2])
        nodos["Sepolia"] = NodosMetro("Sepolia", 144, 338, [2])
        nodos["Larissa Station"] = NodosMetro("Larissa Station", 176, 402, [2])
        nodos["Metaxourghio"] = NodosMetro("Metaxourghio", 176, 432, [2])
        nodos["Panepistimio"] = NodosMetro("Panepistimio", 232, 467, [2])
        nodos["Akropoli"] = NodosMetro("Akropoli", 253, 524, [2])
        nodos["Sygrou-Fix"] = NodosMetro("Sygrou-Fix", 253, 554, [2])
        nodos["Neos Kosmos"] = NodosMetro("Neos Kosmos", 253, 584, [2])
        nodos["Aghios Ioannis"] = NodosMetro("Aghios Ioannis", 253, 614, [2])
        nodos["Dafni"] = NodosMetro("Dafni", 253, 644, [2])
        nodos["Aghios Dimitrios"] = NodosMetro("Aghios Dimitrios", 253, 674, [2])
        nodos["Syntagma"] = NodosMetro("Syntagma", 250, 485, [3, 2])
        nodos["Evangelismos"] = NodosMetro("Evangelismos", 316, 485, [3])



        nodos["Airport"] = NodosMetro("Airport", 648, 503, [3])
        nodos["Koropi"] = NodosMetro("Koropi", 587, 478, [3])
        nodos["Paiania-Kantza"] = NodosMetro("Paiania-Kantza", 588, 370, [3])
        nodos["Pallini"] = NodosMetro("Pallini", 588, 325, [3])
        nodos["Doukissis Planketias"] = NodosMetro("Doukissis Plakentias", 541, 305, [3])
        nodos["Halandri"] = NodosMetro("Halandri", 510, 332, [3])
        nodos["Aghia Paraskevi"] = NodosMetro("Aghia Paraskevi", 492, 350, [3])
        nodos["Nomismatokopio"] = NodosMetro("Nomismatokopio", 475, 367, [3])
        nodos["Holargos"] = NodosMetro("Holargos", 457, 385, [3])
        nodos["Ethniki Amyna"] = NodosMetro("Ethniki Amyna", 439, 402, [3])
        nodos["Katehaki"] = NodosMetro("Katehaki", 422, 421, [3])
        nodos["Panormou"] = NodosMetro("Panormou", 405, 438, [3])
        nodos["Ambelokipi"] = NodosMetro("Ambelokipi", 387, 455, [3])
        nodos["Megaro Moussikis"] = NodosMetro("Megaro Moussikis", 369, 475, [3])


        nodos["Kerameikos"] = NodosMetro("Kerameikos", 128, 476, [3])
        nodos["Eleonas"] = NodosMetro("Eleonas", 92, 443, [3])
        nodos["Egaleo"] = NodosMetro("Egaleo", 53, 400, [3])

        nodos.get("Airport").adyacentes.append([nodos.get("Koropi"), 5050])
        nodos.get("Koropi").adyacentes.append([nodos.get("Airport"), 5050])
        nodos.get("Koropi").adyacentes.append([nodos.get("Paiania-Kantza"), 8170])
        nodos.get("Paiania-Kantza").adyacentes.append([nodos.get("Koropi"), 8170])
        nodos.get("Paiania-Kantza").adyacentes.append([nodos.get("Pallini"), 2470])
        nodos.get("Pallini").adyacentes.append([nodos.get("Paiania-Kantza"), 2470])
        nodos.get("Pallini").adyacentes.append([nodos.get("Doukissis Planketias"), 3750])
        nodos.get("Doukissis Planketias").adyacentes.append([nodos.get("Pallini"), 3750])
        nodos.get("Doukissis Planketias").adyacentes.append([nodos.get("Halandri"), 1090])
        nodos.get("Halandri").adyacentes.append([nodos.get("Doukissis Planketias"), 1090])
        nodos.get("Halandri").adyacentes.append([nodos.get("Aghia Paraskevi"), 900])
        nodos.get("Aghia Paraskevi").adyacentes.append([nodos.get("Halandri"), 900])
        nodos.get("Aghia Paraskevi").adyacentes.append([nodos.get("Nomismatokopio"), 1060])
        nodos.get("Nomismatokopio").adyacentes.append([nodos.get("Aghia Paraskevi"), 1060])
        nodos.get("Nomismatokopio").adyacentes.append([nodos.get("Holargos"), 1110])
        nodos.get("Holargos").adyacentes.append([nodos.get("Nomismatokopio"), 1110])
        nodos.get("Holargos").adyacentes.append([nodos.get("Ethniki Amyna"), 910])
        nodos.get("Ethniki Amyna").adyacentes.append([nodos.get("Holargos"), 910])
        nodos.get("Ethniki Amyna").adyacentes.append([nodos.get("Katehaki"), 1140])
        nodos.get("Katehaki").adyacentes.append([nodos.get("Ethniki Amyna"), 1140])
        nodos.get("Katehaki").adyacentes.append([nodos.get("Panormou"), 1110])
        nodos.get("Panormou").adyacentes.append([nodos.get("Katehaki"), 1110])
        nodos.get("Panormou").adyacentes.append([nodos.get("Ambelokipi"), 860])
        nodos.get("Ambelokipi").adyacentes.append([nodos.get("Panormou"), 860])
        nodos.get("Ambelokipi").adyacentes.append([nodos.get("Megaro Moussikis"), 1000])
        nodos.get("Megaro Moussikis").adyacentes.append([nodos.get("Ambelokipi"), 1000])
        nodos.get("Megaro Moussikis").adyacentes.append([nodos.get("Evangelismos"), 600])
        nodos.get("Evangelismos").adyacentes.append([nodos.get("Megaro Moussikis"), 600])
        nodos.get("Evangelismos").adyacentes.append([nodos.get("Syntagma"), 980])
        nodos.get("Kerameikos").adyacentes.append([nodos.get("Monastiraki"), 1270])
        nodos.get("Kerameikos").adyacentes.append([nodos.get("Eleonas"), 1840])
        nodos.get("Eleonas").adyacentes.append([nodos.get("Kerameikos"), 1840])
        nodos.get("Eleonas").adyacentes.append([nodos.get("Egaleo"), 1160])
        nodos.get("Egaleo").adyacentes.append([nodos.get("Eleonas"), 1160])
        nodos.get("Aghios Antonios").adyacentes.append([nodos.get("Sepolia"), 1320])
        nodos.get("Sepolia").adyacentes.append([nodos.get("Aghios Antonios"), 1320])
        nodos.get("Sepolia").adyacentes.append([nodos.get("Attiki"), 810])
        nodos.get("Attiki").adyacentes.append([nodos.get("Sepolia"), 810])
        nodos.get("Attiki").adyacentes.append([nodos.get("Larissa Station"), 840])
        nodos.get("Larissa Station").adyacentes.append([nodos.get("Attiki"), 840])
        nodos.get("Larissa Station").adyacentes.append([nodos.get("Metaxourghio"), 710])
        nodos.get("Metaxourghio").adyacentes.append([nodos.get("Larissa Station"), 710])
        nodos.get("Metaxourghio").adyacentes.append([nodos.get("Omonia"), 700])
        nodos.get("Omonia").adyacentes.append([nodos.get("Metaxourghio"), 700])
        nodos.get("Omonia").adyacentes.append([nodos.get("Victoria"), 1000])
        nodos.get("Omonia").adyacentes.append([nodos.get("Panepistimio"), 570])
        nodos.get("Omonia").adyacentes.append([nodos.get("Monastiraki"), 970])
        nodos.get("Panepistimio").adyacentes.append([nodos.get("Omonia"), 570])
        nodos.get("Panepistimio").adyacentes.append([nodos.get("Syntagma"), 670])
        nodos.get("Syntagma").adyacentes.append([nodos.get("Panepistimio"), 670])
        nodos.get("Syntagma").adyacentes.append([nodos.get("Akropoli"), 850])
        nodos.get("Syntagma").adyacentes.append([nodos.get("Evangelismos"), 980])
        nodos.get("Syntagma").adyacentes.append([nodos.get("Monastiraki"), 890])
        nodos.get("Akropoli").adyacentes.append([nodos.get("Syntagma"), 850])
        nodos.get("Akropoli").adyacentes.append([nodos.get("Sygrou-Fix"), 500])
        nodos.get("Sygrou-Fix").adyacentes.append([nodos.get("Akropoli"), 560])
        nodos.get("Sygrou-Fix").adyacentes.append([nodos.get("Neos Kosmos"), 760])
        nodos.get("Neos Kosmos").adyacentes.append([nodos.get("Sygrou-Fix"), 760])
        nodos.get("Neos Kosmos").adyacentes.append([nodos.get("Aghios Ioannis"), 560])
        nodos.get("Aghios Ioannis").adyacentes.append([nodos.get("Neos Kosmos"), 560])
        nodos.get("Aghios Ioannis").adyacentes.append([nodos.get("Dafni"), 860])
        nodos.get("Dafni").adyacentes.append([nodos.get("Aghios Ioannis"), 860])
        nodos.get("Dafni").adyacentes.append([nodos.get("Aghios Dimitrios"), 1020])
        nodos.get("Aghios Dimitrios").adyacentes.append([nodos.get("Dafni"), 1020])

        nodos.get("Kifissia").adyacentes.append([nodos.get("KAT"), 940])
        nodos.get("KAT").adyacentes.append([nodos.get("Kifissia"), 940])
        nodos.get("KAT").adyacentes.append([nodos.get("Maroussi"), 1090])
        nodos.get("Maroussi").adyacentes.append([nodos.get("KAT"), 1090])
        nodos.get("Maroussi").adyacentes.append([nodos.get("Neratziotissa"), 1610])
        nodos.get("Neratziotissa").adyacentes.append([nodos.get("Maroussi"), 1610])
        nodos.get("Neratziotissa").adyacentes.append([nodos.get("Irini"), 1090])
        nodos.get("Irini").adyacentes.append([nodos.get("Neratziotissa"), 1090])
        nodos.get("Irini").adyacentes.append([nodos.get("Iraklio"), 1500])
        nodos.get("Iraklio").adyacentes.append([nodos.get("Irini"), 1500])
        nodos.get("Iraklio").adyacentes.append([nodos.get("Nea Ionia"), 1070])
        nodos.get("Nea Ionia").adyacentes.append([nodos.get("Iraklio"), 1070])
        nodos.get("Nea Ionia").adyacentes.append([nodos.get("Pefkakia"), 655])
        nodos.get("Pefkakia").adyacentes.append([nodos.get("Nea Ionia"), 655])
        nodos.get("Pefkakia").adyacentes.append([nodos.get("Perissos"), 655])
        nodos.get("Perissos").adyacentes.append([nodos.get("Pefkakia"), 655])
        nodos.get("Perissos").adyacentes.append([nodos.get("Ano Pahssia"), 1940])
        nodos.get("Ano Pahssia").adyacentes.append([nodos.get("Perissos"), 1940])
        nodos.get("Ano Pahssia").adyacentes.append([nodos.get("Aghios Eleftherios"), 540])
        nodos.get("Aghios Eleftherios").adyacentes.append([nodos.get("Ano Pahssia"), 540])
        nodos.get("Aghios Eleftherios").adyacentes.append([nodos.get("Kato Patissia"), 980])
        nodos.get("Kato Patissia").adyacentes.append([nodos.get("Aghios Eleftherios"), 980])
        nodos.get("Kato Patissia").adyacentes.append([nodos.get("Aghios Nikolaos"), 530])
        nodos.get("Aghios Nikolaos").adyacentes.append([nodos.get("Kato Patissia"), 530])
        nodos.get("Aghios Nikolaos").adyacentes.append([nodos.get("Attiki"), 940])
        nodos.get("Attiki").adyacentes.append([nodos.get("Aghios Nikolaos"), 940])
        nodos.get("Attiki").adyacentes.append([nodos.get("Sepolia"), 810])
        nodos.get("Attiki").adyacentes.append([nodos.get("Victoria"), 1020])
        nodos.get("Attiki").adyacentes.append([nodos.get("Larissa Station"), 710])
        nodos.get("Victoria").adyacentes.append([nodos.get("Attiki"), 1020])
        nodos.get("Victoria").adyacentes.append([nodos.get("Omonia"), 1000])
        nodos.get("Monastiraki").adyacentes.append([nodos.get("Omonia"), 940])
        nodos.get("Monastiraki").adyacentes.append([nodos.get("Kerameikos"), ])
        nodos.get("Monastiraki").adyacentes.append([nodos.get("Syntagma"), ])
        nodos.get("Monastiraki").adyacentes.append([nodos.get("Thissio"), 1430])
        nodos.get("Thissio").adyacentes.append([nodos.get("Petralona"), 1350])
        nodos.get("Thissio").adyacentes.append([nodos.get("Monastiraki"), 1350])
        nodos.get("Petralona").adyacentes.append([nodos.get("Thissio"), 1350])
        nodos.get("Petralona").adyacentes.append([nodos.get("Tavros"), 855])
        nodos.get("Tavros").adyacentes.append([nodos.get("Petralona"), 855])
        nodos.get("Tavros").adyacentes.append([nodos.get("Kallithea"), 580])
        nodos.get("Kallithea").adyacentes.append([nodos.get("Tavros"), 580])
        nodos.get("Kallithea").adyacentes.append([nodos.get("Moschato"), 1680])
        nodos.get("Moschato").adyacentes.append([nodos.get("Kallithea"), 1680])
        nodos.get("Moschato").adyacentes.append([nodos.get("Faliro"), 1760])
        nodos.get("Faliro").adyacentes.append([nodos.get("Moschato"), 1760])
        nodos.get("Faliro").adyacentes.append([nodos.get("Piraeus"), 1950])
        nodos.get("Piraeus").adyacentes.append([nodos.get("Faliro"), 1950])








































        self.nodos=nodos
