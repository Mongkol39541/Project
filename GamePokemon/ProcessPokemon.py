import numpy as np

class RATEPokemon:
    def play_rate(carater, carater_evolution, carater_maga, carater_giga, number_random):
        random_carater = []
        for loop_r in range(1, 66):
            if len(carater) == 0:
                break
            if loop_r > len(carater):
                loop_r = loop_r % len(carater)
            random_carater.append(carater[int(loop_r - 1)])
        for loop_sr in range(1, 21):
            if len(carater_evolution) == 0:
                break
            if loop_sr > len(carater_evolution):
                loop_sr = loop_sr % len(carater_evolution)
            random_carater.append(carater_evolution[int(loop_sr - 1)])
        for loop_ssr in range(1, 11):
            if len(carater_maga) == 0:
                break
            if loop_ssr > len(carater_maga):
                loop_ssr = loop_ssr % len(carater_maga)
            random_carater.append(carater_maga[int(loop_ssr - 1)])
        for loop_sp in range(1, 6):
            if len(carater_giga) == 0:
                break
            if loop_sp > len(carater_giga):
                loop_sp = loop_sp % len(carater_giga)
            random_carater.append(carater_giga[int(loop_sp-1)])
        get_pokemon, get_grade, hap_ssr, hap_sp = RandomPokemon.play_random(random_carater, carater_maga, carater_giga, number_random)
        return get_pokemon, get_grade, hap_ssr, hap_sp

class RandomPokemon:
    def play_random(random_carater, carater_maga, carater_giga, number_random):
        get_pokemon = []
        get_grade = []
        hap_ssr = 0
        hap_sp = 0
        listhap_ssr = []
        listhap_sp = []
        for _ in range(number_random):
            get_carater = np.random.randint(len(random_carater))
            if get_carater < 65 :
                grade = "R"
            if 65 <= get_carater < 85:
                grade = "SR"
            if 85 <= get_carater < 95:
                grade = "SSR"
            if get_carater >= 95:
                grade = "SP"
            get_pokemon.append(random_carater[get_carater])
            get_grade.append(grade)
            for _ in range(2):
                if len(carater_maga) == 0:
                    break
                random_carater.append(carater_maga[np.random.randint(len(carater_maga))])
                hap_ssr = hap_ssr + 1
            for _ in range(1):
                if len(carater_giga) == 0:
                    break
                random_carater.append(carater_giga[np.random.randint(len(carater_giga))])
                hap_sp = hap_sp + 1
            if grade == "SSR":
                for _ in range(len(random_carater)-100):
                    random_carater.pop(100)
                hap_ssr = 0
                hap_sp = 0
            if grade == "SP":
                for _ in range(len(random_carater)-100):
                    random_carater.pop(100)
                hap_ssr = 0
                hap_sp = 0
            listhap_ssr.append(hap_ssr)
            listhap_sp.append(hap_sp)
        return get_pokemon, get_grade, listhap_ssr, listhap_sp
