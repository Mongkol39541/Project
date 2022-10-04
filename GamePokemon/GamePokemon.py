from ProcessPokemon import RATEPokemon
from DataPokemon import DataPokemon
import csv

select_element = str(input("ธาตุที่ต้องการสุ่ม(Fire/Aqua/Electricity/Grass/Earth) : "))
if select_element == "Fire":
    carater, carater_evolution, carater_maga, carater_giga = DataPokemon.pokemon_fire()
elif select_element == "Aqua":
    carater, carater_evolution, carater_maga, carater_giga = DataPokemon.pokemon_aqua()
elif select_element == "Electricity":
    carater, carater_evolution, carater_maga, carater_giga = DataPokemon.pokemon_electricity()
elif select_element == "Grass":
    carater, carater_evolution, carater_maga, carater_giga = DataPokemon.pokemon_grass()
elif select_element == "Earth":
    carater, carater_evolution, carater_maga, carater_giga = DataPokemon.pokemon_earth()

number_random = int(input("ท่านต้องการสุ่มกี่ครั้ง : "))
get_pokemon, GetGrade, ListHapSSR, ListHapSP = RATEPokemon.play_rate(carater, carater_evolution, carater_maga, carater_giga, number_random)
name_file = input("ชื่อไฟล์ที่ต้องการบันทึก : ")

with open("%s.csv" % (name_file), "w", newline="", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade", "Element", "โอกาสได้รับ SSR เพิ่มขึ้น", "โอกาสได้รับ SP เพิ่มขึ้น"])
    for i in range(len(get_pokemon)):
        writer.writerow([get_pokemon[i], GetGrade[i], select_element, str(ListHapSSR[i]) + "%", str(ListHapSP[i]) + "%"])
