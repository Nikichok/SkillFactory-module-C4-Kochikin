import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors

app = bottle.Bottle()

class TodoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }

tasks_db = {
    uid: TodoItem(desc, uid)
    for uid, desc in enumerate(
        start=1,
        iterable=[
            "написать код",
            "покормить морскую свинку",
            "постирать кроссовки",
            "поесть еды",
        ])
}

@enable_cors
@app.route("/api/tasks/")
# @bottle.route("/api/tasks/")
def index():
    # bottle.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    tasks = [task.to_dict() for task in tasks_db.values()]
    return {"tasks": tasks}


@enable_cors
@app.route("/api/add-task", method="POST")
# @bottle.route("/api/add-task", method="POST")
def add_task():
    # bottle.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    # desc = bottle.request.POST.description.strip()
    desc = bottle.request.json['description']
    is_completed = bottle.request.json['is_completed']
    if len(desc) > 0:
        new_uid = max(tasks_db.keys()) + 1
        t = TodoItem(desc, new_uid)
        t.is_completed = is_completed
        tasks_db[new_uid] = t
    return "Ok"


@enable_cors
@app.route("/api/delete/<uid:int>")
# @bottle.route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return "Ok"


@enable_cors
@app.route("/api/complete/<uid:int>")
# @bottle.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "Ok"


###

app.install(CorsPlugin(origins=['http://localhost:8000']))

if __name__ == "__main__":
    bottle.run(host="localhost", port=5000)