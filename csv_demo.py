import pickle


def read_csv(file_path, encoding="utf-8"):
    m = [] # m is save data list
    try:
        f = open(file_path, "r", encoding=encoding) # open file
        line = f.readline()
        while True:
            line = f.readline()
            if line == "":
                break
            lst = line.split(",")
            if "要" in lst[2]:
                continue
            lst[2] = lst[2][:lst[2].find("                    ")]
            if "￥" not in lst[4]:
                continue
            lst[4] = lst[4][lst[4].find("￥")+1:]
            if "环境" in lst[6]:
                lst[6] = lst[6].split("                                ")
                lst[6] = [["质量", lst[6][0][-3:]], ["环境", lst[6][1][-3:]], ["服务", lst[6][2][-4:-1]]]
            data = [["classify", lst[0]], ["name", lst[1]], ["comment", lst[2]], ["star", lst[3]], ["price", lst[4]], ["address", lst[5]], ["commentlist", lst[6]]]
            m.append(data)
        p = open("csv.pkl", "wb")  # save pickle
        pickle.dump(m, p)
    finally:
        f.close()
        p.close()

def read_pickle(file_path):
    try:
        p = open(file_path, "rb")
        read = pickle.load(p)
        print(read)
    finally:
        p.close()

if __name__ == "__main__":
    read_csv("111.csv")
    # read_pickle("csv.pkl")