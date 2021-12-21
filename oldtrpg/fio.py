import csv
import json

class f_deal():
    def __init__(self,file_path=None,dir_path=None,encode="UTF-8_sig"):
        self.file_path = file_path
        self.dir_path = dir_path
        self.encode = encode

    def is_dir(self):
        # if not os.path.exists(self.dir_path):
        #    os.mkdir(self.dir_path)
        return self.dir_path

    def fread(self,index=False,rtype="dict"):
        """parameters\n
        - index: contain index, boolean\n
        - rtype: return data type optional -> list or dict\n
        returns: object included list,
        """
        with open(self.file_path,"r",encoding=self.encode) as f:
            if "csv" in self.file_path:
                if rtype.lower() == "list":
                    if not index: next(csv.reader(f))
                    datas = [i for i in csv.reader(f)]
                    for i in datas:
                        for k, v in enumerate(i):
                            try: i[k] = int(v)
                            except: i[k] = v
                elif rtype.lower() == "dict":
                    datas = [i for i in csv.DictReader(f)]
                    for i in datas:
                        for k, v in i.items():
                            try: i[k] = int(v)
                            except: i[k] = v
                else: raise ValueError("rtype is wrong")
            elif "json" in self.file_path: datas = json.load(f)
            else: datas = f.read()
        return datas

    def fwrite(self,wtype="dict",header=None,values=None,mode="w",space=False):
        """parameters\n
        - wtype: write type, list or dim or dict
        -- dim is list in list, sample [[],...,[]]
        - header: index\n
        - values: elements, list or dict\n
        - mode: w(write) or a(append)\n
        returns: boolean, Success -- True, Failed -- False
        """
        complete = False
        with open(self.file_path,mode,newline="",encoding=self.encode) as f:
            if space == True: pass
            if "csv" in self.file_path:
                w = csv.writer(f)
                if wtype.lower() == "list": w.writerow(values)
                elif wtype.lower() == "dim": w.writerows(values)
                elif wtype.lower() == "dict":
                    w = csv.DictWriter(f,header)
                    w.writeheader()
                    try:
                        for i in range(len(values)): w.writerow(values[i])
                    except KeyError: w.writerow(values)
                else: raise ValueError("wtype is wrong")
            elif "json" in self.file_path:
                json.dump(values,f,indent=4)
            else: f.write(values)
            complete = True
        return complete
