import json

class JsonWrapper():
    def __init__(self):
        pass


    def tojson(self, dict):
        try:
            obj = json.dumps(dict)
            return obj
        except json.JSONDecodeError as e:
            print("couldn't parse, " + str(e))
            return None

    def fromjson(self, obj):
        try:
            obj = json.loads(obj)
            return obj
        except json.JSONDecodeError as e:
            print("couldn't parse, " + str(e))
            return None

if __name__ == '__main__':
    print("json")
