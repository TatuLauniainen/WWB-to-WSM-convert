import modules.filemanager as filemanager, modules.parser as parser, modules.gui as gui, modules.paths as paths


def main(WWB_path, WSM_path, WSM_folder=paths.WSM_FOLDER_PATH):

    print(WWB_path, WSM_path, WSM_folder)

    WWB_xml_root = filemanager.read_WWB_data(WWB_path)
    frequencies = parser.parse_WWB_frequencies(WWB_xml_root)
    filemanager.write_WSM_data(WSM_path, WSM_folder, frequencies)


if __name__ == "__main__":
    converter_gui = gui.GUI()