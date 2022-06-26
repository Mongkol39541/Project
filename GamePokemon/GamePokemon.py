from ProcessPokemon import RATEPokemon
from DataPokemon import DataPokemon
import csv

selectElement = str(input("ธาตุที่ต้องการสุ่ม(Fire/Aqua/Electricity/Grass/Earth) : "))
if selectElement == "Fire":
    Carater, CaraterEvolution, CaraterMaga, CaraterGiga = DataPokemon.PokemonFire()
if selectElement == "Aqua":
    Carater, CaraterEvolution, CaraterMaga, CaraterGiga = DataPokemon.PokemonAqua()
if selectElement == "Electricity":
    Carater, CaraterEvolution, CaraterMaga, CaraterGiga = DataPokemon.PokemonElectricity()
if selectElement == "Grass":
    Carater, CaraterEvolution, CaraterMaga, CaraterGiga = DataPokemon.PokemonGrass()
if selectElement == "Earth":
    Carater, CaraterEvolution, CaraterMaga, CaraterGiga = DataPokemon.PokemonEarth()

numberRandom = int(input("ท่านต้องการสุ่มกี่ครั้ง : "))
GetPokemon, GetGrade, ListHapSSR, ListHapSP = RATEPokemon.playRATE(Carater, CaraterEvolution, CaraterMaga, CaraterGiga, numberRandom)

with open("Day1.csv", "w", newline="", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade", "Element", "โอกาสได้รับ SSR เพิ่มขึ้น", "โอกาสได้รับ SP เพิ่มขึ้น"])
    for i in range(len(GetPokemon)):
        writer.writerow([GetPokemon[i], GetGrade[i], selectElement, str(ListHapSSR[i])+"%", str(ListHapSP[i])+"%"])