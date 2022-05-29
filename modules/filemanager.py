from datetime import datetime
import xml.etree.ElementTree as ET


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


def write_WSM_data(WSM_path, WSM_data):
    """

    Write data to WSM file

    Parameters:
    WSM_path (str): path to WSM file
    WSM_data (str): data writable to WSM file

    """

    now = datetime.datetime.now()
    date = now.strftime("%Y%m%d-%H%M")

    frequencies = [
        "536125",
        "577875",
    ]  # Later these frequencies will be read from the WWB inventory report

    with open(
        f"{date}_frequencies.csv", "w"
    ) as file:  # Find a good folder to save this file to
        file.write(
            "name;type;frequency;tolerance;minfrequency;maxfrequency;priority;squelchlevel\n"
        )
        i = 1
        for frequency in frequencies:
            file.write(
                f"Frequency {str(i).zfill(3)};2;{frequency};0;{frequency};{frequency};2;5\n"
            )
            i += 1
    return


if __name__ == "__main__":
    # frequencies = ["536125", "577875"]
    # write_WSM_data(frequencies)
    read_WWB_data(
        "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220528.inv"
    )
