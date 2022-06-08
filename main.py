import modules.filemanager as filemanager, modules.parser as parser


def main(WWB_path, WSM_path, WSM_folder):

    WWB_xml_root = filemanager.read_WWB_data(WWB_path)
    frequencies = parser.parse_WWB_frequencies(WWB_xml_root)
    filemanager.write_WSM_data(WSM_path, WSM_folder, frequencies)


if __name__ == "__main__":
    WWB_path = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220608.inv"
    WSM_path = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/20220608.wsm"
    WSM_folder = "/Users/pvvmsktekniikka/Documents/VSCode/WWB-to-WSM-convert/dev_data/"
    main(WWB_path, WSM_path, WSM_folder)
