# https://www.acmicpc.net/problem/28691

n = input()

match n.upper():
    case "M":
        print("MatKor")
    case "W":
        print("WiCys")
    case "C":
        print("CyKor")
    case "A":
        print("AlKor")
    case "$":
        print("$clear")