import modules.filemanager as filemanager, modules.parser as parser, modules.gui as gui


def main(WWB_path, WSM_path, WSM_folder="/Users/pvvmsktekniikka/Desktop/"):

    print(WWB_path, WSM_path, WSM_folder)

    WWB_xml_root = filemanager.read_WWB_data(WWB_path)
    frequencies = parser.parse_WWB_frequencies(WWB_xml_root)
    filemanager.write_WSM_data(WSM_path, WSM_folder, frequencies)


if __name__ == "__main__":
    # WWB_path = "/Users/pvvmsktekniikka/Desktop/New Inventory.inv"
    # WSM_path = "/Users/pvvmsktekniikka/Desktop/20220528_testi.wsm"
    # WSM_folder = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/"
    converter_gui = gui.GUI()