import requests


def login(username, password):
	r = requests.post("http://oneconsole.us/api/v1/user/login/", data = {'username' : username, "password":password})
	elem = r.json()
	return elem


def logout(username):
	pass


def profile(token):
	r = requests.get("http://oneconsole.us/api/v1/profile/?format=json&auth="+token)
	get_json = r.json()
	elem = get_json['objects'][0]
	# title = str(elem['title'])
	# json = {"title":title}
	return elem


def addworklog(token, worklog):
	pass


def ticket(token, id):
	r = requests.get("http://oneconsole.us/api/v1/ticket/?format=json&auth="+token+"&tid="+id)
	get_json = r.json()
	elem = get_json['objects'][0]
	return elem



def notifications(token):
	r = requests.get("http://oneconsole.us/api/v1/notification/?format=json&&auth="+token)
	get_json = r.json()
	elem = get_json['objects']
	return elem


def alltickets(token):
	r = requests.get("http://oneconsole.us/api/v1/yourticket/?format=json&&auth="+token)
	get_json = r.json()
	elem = get_json['objects']
	return elem
