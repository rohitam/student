# student
apis demo:

1)	marks/sturec(POST to add student)
	Request:
	{
		"name": "JOJO",
		"last_name": "JO",
		"first_name": "88",
		"email": "email@mail.com"
	}

	Response:
	{
		"data": {
			"name": "JOJO",
			"email": "email@mail.com",
			"id": 15,
			"first_name": "88",
			"last_name": "JO"
		},
		"response": "Student record added"
	}

2)	marks/total(Get request)	
	Response:
	[
    {
        "stu_id": 1,
        "total": 429
    }
	]
3)	marks/avg
	Response:
	{
		"maths": 93,
		"physics": 92,
		"chemistry": 88,
		"biology": 86,
		"english": 61
	}

4) marks/<stu_id>/addmarks(post to add/edit marks)
	Request:
	{
		"maths": 100,
		"physics": 77,
		"chemistry": 88,
		"biology": 89,
		"english": 58
	}

	Response:
	{
		"data": {
			"stu_id": 14,
			"maths": 100,
			"physics": 77,
			"chemistry": 88,
			"biology": 89,
			"english": 58
		},
		"response": "Hello, world. This is marks apps, marks added"
	}
