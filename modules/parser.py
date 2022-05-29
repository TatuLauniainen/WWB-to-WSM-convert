import xml.etree.ElementTree as ET
import filemanager


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

        series = device.find("series").text
        if not series in frequencies.keys():
            frequencies[series] = []

        for channel in device.iter("channel"):
            frequencies[series].append(channel.find("frequency").text)

    print(frequencies)

    return


if __name__ == "__main__":
    WWB_xml_root = filemanager.read_WWB_data(
        "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220529.inv"
    )
    parse_WWB_frequencies(WWB_xml_root)
