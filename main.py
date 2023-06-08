import modules.filemanager as filemanager, modules.parser as parser, modules.gui as gui


def main(WWB_path, WSM_path, output_folder):

    print(WWB_path, WSM_path, output_folder)

    WWB_xml_root = filemanager.read_WWB_data(WWB_path)
    frequencies = parser.parse_WWB_frequencies(WWB_xml_root)
    filemanager.write_WSM_data(WSM_path, output_folder, frequencies)


if __name__ == "__main__":
    converter_gui = gui.GUI()