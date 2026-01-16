import json
def avg_grade(text,new_text):
    try:
        with open(text, "r", encoding="utf-8") as f:
            file = json.load(f)
        new_file=[]
        for i in file:
            grade=i.get('grade')
            if grade:
                avg_g=sum(grade)/len(grade)
            else:
                avg_g=0
            i["AVG"]=round(avg_g)
            new_file.append(i)

        with open(new_text, "w", encoding="utf-8") as o:
            json.dump(new_file,o,indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print("file not exist")

if __name__ == "__main__":
    avg_grade("student.json", "read.json")