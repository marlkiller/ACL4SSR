# Surge DOMAIN-SET convert to QuantumultX/Loon
import os

# DOMAIN-SET:
# 文件中每行为一个域名或一个 IP 地址，如果某行以 . 开头则表示匹配所有子域名和该域名本身。


convert_files = ["gfw.txt"]
LOON_OUT_PATH = f'..{os.sep}Loon{os.sep}'
QX_OUT_PATH = f'..{os.sep}QuantumultX{os.sep}'


def convert_to_loon(surge_file_name):
    lines = get_surge_rules(surge_file_name)
    with open(LOON_OUT_PATH + surge_file_name, "w") as loon_rule:
        for line in lines:
            if line.startswith("."):
                line = line.replace("\n", "")
                # DOMAIN-SUFFIX,xxx.com
                loon_rule.write(f"DOMAIN-SUFFIX,{line[1:]}\n")


def get_surge_rules(surge_file_name):
    with open(surge_file_name, "r") as surge_rule:
        lines = surge_rule.readlines()
    return lines


def convert_to_qx(surge_file_name):
    lines = get_surge_rules(surge_file_name)
    with open(QX_OUT_PATH + surge_file_name, "w") as loon_rule:
        for line in lines:
            if line.startswith("."):
                line = line.replace("\n", "")
                # DOMAIN-SUFFIX,poe.com,🚀 节点选择
                loon_rule.write(f"DOMAIN-SUFFIX,{line[1:]},🚀 节点选择\n")


def convert(convert_file):
    convert_to_loon(convert_file)
    convert_to_qx(convert_file)


if __name__ == '__main__':
    for convert_file in convert_files:
        convert(convert_file)
