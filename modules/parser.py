import xml.etree.ElementTree as ET
import modules.filemanager as filemanager
from pprint import PrettyPrinter

pp = PrettyPrinter()

ignore_devices = {"AXT600"}


def parse_WWB_frequencies(WWB_xml_root):
    """

    Find channel frequencies from Wireless Workbench inventory file and store thrm in a dict

    Parameters:
    WWB_xml_root (Element): data exported from WWB

    Returns:
    frequencies (dict): channel frequencies for all devices

    """

    frequencies = {}
    for device in WWB_xml_root.iter("device"):

        model = device.find("model").text
        if model in ignore_devices:
            print(model + " ignored")
            continue

        series = device.find("series").text
        if not series in frequencies.keys():
            frequencies[series] = []

        for channel in device.iter("channel"):
            print(channel.find("frequency"))
            frequencies[series].append(channel.find("frequency").text)

    pp.pprint(frequencies)

    return frequencies


if __name__ == "__main__":
    WWB_xml_root = filemanager.read_WWB_data(
        "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220607.inv"
    )
    parse_WWB_frequencies(WWB_xml_root)
