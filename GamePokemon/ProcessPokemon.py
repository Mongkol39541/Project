from random import randrange

class RATEPokemon:
    def playRATE(Carater, CaraterEvolution, CaraterMaga, CaraterGiga, numberRandom):
        RandomCarater = []
        for r in range(1,66):
            if int(len(Carater)) == 0:
                break
            if r > int(len(Carater)):
                r = r%int(len(Carater))
            RandomCarater.append(Carater[r-1])
        for sr in range(1,21):
            if int(len(CaraterEvolution)) == 0:
                break
            if sr > int(len(CaraterEvolution)):
                sr = sr%int(len(CaraterEvolution))
            RandomCarater.append(CaraterEvolution[sr-1])
        for ssr in range(1,11):
            if int(len(CaraterMaga)) == 0:
                break
            if ssr > int(len(CaraterMaga)):
                ssr = ssr%int(len(CaraterMaga))
            RandomCarater.append(CaraterMaga[ssr-1])
        for sp in range(1,6):
            if int(len(CaraterGiga)) == 0:
                break
            if sp > int(len(CaraterGiga)):
                sp = sp%int(len(CaraterGiga))
            RandomCarater.append(CaraterGiga[sp-1])
        GetPokemon, GetGrade, HapSSR, HapSP = RandomPokemon.playRandom(RandomCarater, CaraterMaga, CaraterGiga, numberRandom)
        return GetPokemon, GetGrade, HapSSR, HapSP

class RandomPokemon:
    def playRandom(RandomCarater, CaraterMaga, CaraterGiga, numberRandom):
        GetPokemon = []
        GetGrade = []
        HapSSR = 0
        HapSP = 0
        ListHapSSR = []
        ListHapSP = []
        for rd in range(numberRandom):
            GetCarater = randrange(len(RandomCarater))
            if int(GetCarater) < 65 :
                Grade = "R"
            if 65 <= int(GetCarater) < 85:
                Grade = "SR"
            if 85 <= int(GetCarater) < 95:
                Grade = "SSR"
            if int(GetCarater) >= 95:
                Grade = "SP"
            GetPokemon.append(RandomCarater[GetCarater])
            GetGrade.append(Grade)
            for addMaga in range(2):
                if int(len(CaraterMaga)) == 0:
                    break
                RandomCarater.append(CaraterMaga[randrange(len(CaraterMaga))])
                HapSSR = HapSSR+1
            for addGiga in range(1):
                if int(len(CaraterGiga)) == 0:
                    break
                RandomCarater.append(CaraterGiga[randrange(len(CaraterGiga))])
                HapSP = HapSP+1
            if Grade == "SSR":
                for removeSSR in range(len(RandomCarater)-100):
                    RandomCarater.pop(100)
                HapSSR = 0
                HapSP = 0
            if Grade == "SP":
                for removeSP in range(len(RandomCarater)-100):
                    RandomCarater.pop(100)
                HapSSR = 0
                HapSP = 0
            ListHapSSR.append(HapSSR)
            ListHapSP.append(HapSP)
        return GetPokemon, GetGrade, ListHapSSR, ListHapSP