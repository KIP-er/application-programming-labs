import argparse
import re
def main():
    parser=argparse.ArgumentParser(description='Описание программы')
    parser.add_argument('filename', help='Имя файла для чтения')
    args = parser.parse_args()
    pattern=r'^(Город:)\s(Москва|г. Москва)$'
    with open(args.filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
        records = [lines[i:i+7] for i in range(0,len(lines), 7) if len(lines[i:i+7])==7]
    found=[]
    for record in records:
        city=record[6]
        if re.search(pattern, city):
            found.append(record[1:7])
    print(len(found))
main()