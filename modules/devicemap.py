"""
Map to convert from WWB device name to WSM device name
"""


def map_WWB_to_WSM(WWB_device):
    WWB_to_WSM = {"EW 500 G3": "EM500G3",
                  "EW 300 IEM G3": "SR-IEMG4"}
    return WWB_to_WSM[WWB_device]


def map_WSM_to_WWB(WSM_device):
    WSM_to_WWB = {"EM500G3": "EW 500 G3",
                  "SR-IEMG4": "EW 300 IEM G3"}
    return WSM_to_WWB[WSM_device]
