import requests
import time

class RickMortyExtractor:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"


    def get_data(self, endpoint, params=None):

        data = []
        url = f"{self.base_url}/{endpoint}"

        while url:
            print(url)

            try:
                response = requests.get(url, params=params, timeout=30)

                if response.status_code == 429:
                    print(response.headers)
                    retry_after = int(response.headers["Retry-After"])
                    print(f"Rate limit exceeded. Retrying after the time set in requeste header: {retry_after}")
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                curr_page_response = response.json()
                data.extend(curr_page_response["results"])
                url = curr_page_response["info"]["next"]

            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                break
            except KeyError as e:
                print(f"Missing expected field in response: {e}")
                break
            except ValueError:
                print("Invalid JSON response")
                break

        return data


    def get_characters(self, name=None, status=None, species=None, type=None, gender=None):
        params = {"name": name,
                  "status": status,
                  "species": species,
                  "type": type,
                  "gender": gender}
        return self.get_data(endpoint="character", params=params)
        

    def get_episodes(self, name=None, episode=None):

        params = {"name": name,
                  "episode": episode}

        return self.get_data("episode", params)
        

    def get_locations(self, name=None, type=None, dimension=None):

        params = {"name": name,
                  "type": type,
                  "dimension": dimension}

        return self.get_data("location", params)

api = RickMortyExtractor()
#characters = api.get_characters()
#print(len(characters))

episodes = api.get_episodes()
print(episodes)
print(len(episodes))

locations = api.get_locations(dimension="unknown")
print(len(locations))