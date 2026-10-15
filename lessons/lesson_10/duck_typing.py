class CsvHandler:
    def export(self, data):
        pass

class JsonHandler:
    def export(self, data):
        pass

class XmlHandler:
    def export(self, data):
        pass


data = {"name": "Jane", "age": 25}


def export_data(handler, data):
    handler.export(data)

csv_handler=CsvHandler()
json_handler=JsonHandler()
xml_handler=XmlHandler()

export_data(csv_handler, data)
export_data(json_handler, data)
export_data(xml_handler, data)