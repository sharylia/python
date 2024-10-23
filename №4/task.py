import random
import requests
import json
from typing import Dict, List, Any

class RickAndMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def get_random_character(self) -> Dict[str, Any]:
        response = requests.get(f"{self.BASE_URL}/character")
        data = json.loads(response.text)
        total_characters = data['info']['count']
        
        random_id = random.randint(1, total_characters)
        
        character_response = requests.get(f"{self.BASE_URL}/character/{random_id}")
        return json.loads(character_response.text)

    def search_characters(self, name: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.BASE_URL}/character", params={"name": name})
        return json.loads(response.text).get("results", [])

    def get_all_locations(self) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.BASE_URL}/location")
        return json.loads(response.text).get("results", [])

    def search_episodes(self, name: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.BASE_URL}/episode", params={"name": name})
        return json.loads(response.text).get("results", [])

    def analyze_character_status(self) -> Dict[str, int]:
        response = requests.get(f"{self.BASE_URL}/character")
        characters = json.loads(response.text).get("results", [])
        
        status_count = {}
        for character in characters:
            status = character.get("status")
            if status:
                status_count[status] = status_count.get(status, 0) + 1
                
        return status_count

if __name__ == "__main__":
    client = RickAndMortyClient()

    random_character = client.get_random_character()
    print(f"Случайный персонаж: {random_character.get('name', 'Неизвестно')}")

    characters = client.search_characters("Rick")
    print(f"Персонажи с именем 'Rick': {[char.get('name', 'Неизвестно') for char in characters]}")

    locations = client.get_all_locations()
    print(f"Все локации: {[location.get('name', 'Неизвестно') for location in locations]}")

    episodes = client.search_episodes("Pilot")
    print(f"Эпизоды с названием 'Pilot': {[episode.get('name', 'Неизвестно') for episode in episodes]}")

    status_analysis = client.analyze_character_status()
    print(f"Анализ статусов персонажей: {status_analysis}")
