"""
Usage:  `python timms_gen_url.py <mm> <dd>`
Does:   Prints to clipboard the respective video urls.
"""

import sys

VIDEO_LABELS = ["001", "002"]

def generate_url(mm, dd, label):
    mm  = str(mm)
    dd  = str(dd)
    return \
        "https://timms-ms09.uni-tuebingen.de/UT_2024/" \
        + mm + "/" + dd + "/UT_2024" + mm + dd + "_" \
        + label + "_sose24stochastik_0001.854x480_cb950.mp4"

def generate_urls(mm, dd):
    v_001   = generate_url(mm, dd, VIDEO_LABELS[0])
    v_002   = generate_url(mm, dd, VIDEO_LABELS[1])
    return v_001, v_002

def main():
    mm, dd      = sys.argv[1], sys.argv[2]
    url1, url2  = generate_urls(mm, dd)
    print(url1)
    print(url2)

if __name__ == "__main__":
    main()

