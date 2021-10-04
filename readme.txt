1. Clone the project
2. setup a pyhton environment
3. start the project using --> python manage.py runserver


routes --> 
main requirement:
--> GET 'ministry/:name' for details of single ministry and all the fundings associated with it
[Note: for ministry pass name of the ministry as the param, not the id. For example: "http://localhost:8000/ministry/Ministry of Indigenous Affairs"]

other routes[had to implement as I had to insert some data manually, so I created the route and inserted through api]:
--> GET 'fundings/' for list of all fundings
--> GET 'funding/:id' for details of single funding
--> PUT 'funding/:id' with updated body for update a funding
--> DELETE 'funding/:id' for delete a funding

--> GET 'ministry/' for list of all ministry
--> PUT 'ministry/:name' and updated req body to update a ministry info
--> DELETE 'ministry/:name' to delete a ministry
