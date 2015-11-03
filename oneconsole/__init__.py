import requests

# login function
def login(username, password):
	r = requests.post("http://oneconsole.us/api/v1/user/login/",
					data = {'username' : username, "password":password})
	json = r.json()
	try:
		elem = {"token" :  json['token']}
		return elem
	except:
		return "Invalid Credentials, Please try again!"

#logout function
def logout(username):
	pass

# get profile details
def profile(token):
	r = requests.get("http://oneconsole.us/api/v1/profile/?format=json&auth="+token)
	try:
		get_json = r.json()
		elem = get_json['objects'][0]
		return elem
	except:
		return "Invalid Token"

# add worklog
def addworklog(token, worklog):
	pass


def ticket(token, id):
	r = requests.get("http://oneconsole.us/api/v1/ticket/?format=json&auth="+token+"&tid="+id)
	try:
		get_json = r.json()
		elem = get_json['objects'][0]
		return elem
	except:
		return "Invalid Token Or Ticket ID"


# crete ticket
def CreateTicket(token, summary=None, description=None , impact=None, email=None, phone=None):
	if summary and description and impact and email and phone:
		try:
			r = requests.post("http://oneconsole.us/api/v1/createrequest/?format=json&&auth="+token,
						data = {'summary' : summary, "desc":description, "impact":impact, "email": email,
						"phone" : phone})
		except:
			return "Something went wrong, please refer our documentation http://dev.oneconsole.us"
		status_code = r.status_code
		if status_code == 200:
			elem = "Ticket Created , Your TicketID is " + str(r.text)
			return elem
		else:
			return "Invalid Token"
	else:
		return "All Fields are Mandatoy, please refer our documentation http://dev.oneconsole.us"



# get notification
def notifications(token):
	r = requests.get("http://oneconsole.us/api/v1/notification/?format=json&&auth="+token)
	try:
		get_json = r.json()
		elem = get_json['objects']
		return elem
	except:
		return "Invalid Token"


# all tickets
def alltickets(token):
	r = requests.get("http://oneconsole.us/api/v1/yourticket/?format=json&&auth="+token)
	try:
		get_json = r.json()
		elem = get_json['objects']
		return elem
	except:
		return "Invalid Token"
