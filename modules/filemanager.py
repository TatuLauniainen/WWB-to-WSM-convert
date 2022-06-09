from datetime import datetime
import xml.etree.ElementTree as ET
import modules.parser as parser, modules.devicemap as devicemap


def read_WWB_data(WWB_path):
    """

    Read data from WWB file

    Parameters:
    WWB_path (str): path to WWB inventory file

    Returns:
    WWB_xml_root (Element): data read from WWB inventory file

    """

    tree = ET.parse(WWB_path)
    WWB_xml_root = tree.getroot()
    return WWB_xml_root


def write_WSM_data(WSM_path, wsm_folder, frequencies):
    """

    Write data to WSM file

    Parameters:
    WSM_path (str): path to WSM file
    frequencies (Dict): data writable to WSM file

    """

    tree = ET.parse(WSM_path)
    WSM_xml_root = tree.getroot()

    for device in WSM_xml_root.iter("Device"):
        type = device.get("Type")
        print(type)
        try:
            WWB_type = devicemap.map_WSM_to_WWB(type)
        except KeyError:
            continue

        for receiver in device.iter("Receiver"):
            if not len(frequencies[WWB_type]):
                frequency = 0
            else:
                frequency = frequencies[WWB_type].pop(0)
            receiver.find("CurrentFrequency").text = frequency

    now = datetime.now()
    date = now.strftime("%Y%m%d-%H%M")

    tree.write(wsm_folder + str(date) + ".wsm")

    return


if __name__ == "__main__":
    # frequencies = ["536125", "577875"]
    # write_WSM_data(frequencies)
    WWB_xml_root = read_WWB_data(
        "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220529.inv"
    )
    frequencies = parser.parse_WWB_frequencies(WWB_xml_root)
    wsm_path = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220529.wsm"
    wsm_folder = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/"
    write_WSM_data(wsm_path, wsm_folder, frequencies)
