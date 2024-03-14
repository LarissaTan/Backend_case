# Backend_case
</br></br>
## Instruction

</br><br >
### 1. View a list of all restaurants.
< br >

```
curl -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants

```
< br >
This command will send a GET request to the '/restaurants' , and the server should return a list of all restaurants. However, due to pagination limitations, without adding a page number, the first page will be displayed by default, with a maximum of 10 data.
< br >< br >
### 2. Add a new restaurant to the list
< br >
```
curl -X POST -H "Content-Type: application/json" -H "Authorization: 2dd09e4342550f67986b5d789002a13c" -d "{ \"name\": \"Pizza Palace\", \"location\": \"New York\", \"contact\": {\"phone\": \"456-789-0123\", \"email\": \"info@pizzapalace.com\"}, \"cuisine\": \"Italian\", \"rating\": 4.8}" http://127.0.0.1:5000/restaurants

```
< br >
This command sends a POST request through '- X POST' and specifies the request body in JSON format through '- H "Content Type: application/JSON"`- The parameter'd 'is followed by the detailed information of the new restaurant to be added.
< br >< br >
### 3. Retrieve detailed information about a specific restaurant
< br >
Replace '<id>' with the actual ID of the restaurant you want to view.
< br >
```
curl -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants/1
```
< br >
This command sends a GET request to the '/restaurants/1' endpoint to obtain detailed information about the restaurant with ID 1.
< br >< br >
### 4. Update the details of an existing restaurant
< br >
Similarly, replace '<id>' with the actual ID of the restaurant you want to update.
< br >
```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: 2dd09e4342550f67986b5d789002a13c" -d "{ \"name\": \"Updated Pasta Place\", \"location\": \"Rome\", \"cuisine\": \"Italian\", \"rating\": 4.6, \"contact\": {\"phone\": \"123-456-7890\", \"email\": \"update@pastaplace.com\"}}" http://127.0.0.1:5000/restaurants/1
```
< br >
This command sends a PUT request through '- X PUT' to update the information of the specified restaurant.
< br >< br >
### 5. Delete a restaurant from the list
< br >
Replace '<id>' with the actual ID of the restaurant you want to delete.
< br >
```
curl -X DELETE -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants/1
```
< br >
This command sends a Delete request through '- X Delete' to delete the specified restaurant.

< br >< br >
### 6. Filter restaurants based on location or cuisine
< br >
```
curl -X GET "http://127.0.0.1:5000/restaurants?page=1&per_page=5location=New%20York&cuisine=Italian" -H "Authorization: 2dd09e4342550f67986b5d789002a13c"

```
< br >< br >
### 7.Paginated results when retrieving the list of restaurants
< br >
Here is an example 'curl' command that requests data on page 1, assuming 5 records are displayed on each page:
< br >
```
curl -X GET "http://127.0.0.1:5000/restaurants?page=1&per_page=5" -H "Authorization: 2dd09e4342550f67986b5d789002a13c"
```
< br >
-'page=1' indicates that the request is for the first page.< br >
-'per_page=5' indicates that you want to display 5 records per page.


