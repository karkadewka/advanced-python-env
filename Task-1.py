import string
import re
def main(text,new_text):
    try:
        with open(text, "r" , encoding="UTF-8") as f:
            text=f.read().lower()
            lines=text.splitlines()
        total_lines = len(lines)
        words=re.findall(r'\w+',text)
        number_words=len(words)
        frequency_words={}

        for word in words:
            if word in frequency_words:
                frequency_words[word]+=1
            else:
                frequency_words[word]=1
        with open (new_text,"w", encoding="UTF-8") as o:
            o.write(f"number of words: {number_words}\nnumber of lines: {total_lines}\n")
            o.write(f"frequency of words:\n")
            for key,value in frequency_words.items():
                o.write(f"{key}:{value}\n")
    except FileNotFoundError:
        print("FILE NOT FOUND")

if __name__ == "__main__":
    main("text.txt", "analysis.txt")

