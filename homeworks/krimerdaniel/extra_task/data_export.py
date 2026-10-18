from pathlib import Path
import pandas as pd   #azért pandas, mert ezt ismerem


file_path = Path("homeworks") / "krimerdaniel" / "extra_task"


class CsvHandler:
    def export(self, data):
        df = pd.DataFrame([data])
        df.to_csv(file_path/"exported_data.csv", index = False)

class JsonHandler:
    def export(self, data):
        df = pd.DataFrame([data])
        df.to_json(file_path/"exported_data.json", orient="records", indent=4)

class XmlHandler:
    def export(self, data):
        df = pd.DataFrame([data])
        df.to_xml(file_path/"exported_data.xml", parser='etree')


data = {"name": "Jane", "age": 25}



def export_data(handler, data):
    handler.export(data)

csv_handler=CsvHandler()
json_handler=JsonHandler()
xml_handler=XmlHandler()

export_data(csv_handler, data)
export_data(json_handler, data)
export_data(xml_handler, data)