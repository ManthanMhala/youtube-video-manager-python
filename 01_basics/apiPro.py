import requests

# url = f"https://randomuser.me/api/"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.text)

# for random user
def fetch_random():
    url = f'https://api.freeapi.app/api/v1/public/meals/meal/random'  
    requests.get(url)         
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    
    if data ["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        location = user_data["location"]["country"]
        dob = user_data["dob"]
        registered1 = user_data["registered"]
        picture = user_data["picture"]
        return user_name, location, dob, registered1, picture
    
    else:
        raise Exception("Failed to fetch user data")
       
def main():
    try:
        user_name, location, dob, registered1, picture = fetch_random()
        print(f"Username:{user_name} \nLocation: {location} \nDob: {dob} \nRegistered: {registered1} \nPicture: {picture}")
    except Exception as e:
        print(str(e))

# for meal
def fetch_random():
    url = f'https://api.freeapi.app/api/v1/public/meals/meal/random'  
    requests.get(url)         
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    
    if data["success"] and "data" in data:
        meal_data = data["data"]    
        meal_id = meal_data["idMeal"]
        meal_name = meal_data["strMeal"]
        instructions = meal_data["strInstructions"]

        return meal_id, meal_name, instructions

    
    else:
        raise Exception("Failed to fetch user data")
    
    
def main():
    try:
        meal_id, meal_name, instructions = fetch_random()
        print(f"meal_id: {meal_id} \nMeal_name: {meal_name}\nInstructions: {instructions}")
    except Exception as e:
        print(str(e))
        
        
if __name__=="__main__":
    main()