import csv
import json
import xml.etree.ElementTree as ET


class CsvHandler:
    def export(self, data):
        with open("data.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)

class JsonHandler:
    def export(self, data):
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

class XmlHandler:
    def export(self, data):
        root = ET.Element("data")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        ET.ElementTree(root).write(
            "data.xml", encoding="utf-8", xml_declaration=True
        )


data = {"name": "Jane", "age": 25}


def export_data(handler, data):
    handler.export(data)

csv_handler=CsvHandler()
json_handler=JsonHandler()
xml_handler=XmlHandler()

export_data(csv_handler, data)
export_data(json_handler, data)
export_data(xml_handler, data)