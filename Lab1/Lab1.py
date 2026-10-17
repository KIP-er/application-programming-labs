import argparse
import re


def read_records(filename: str) -> list[list[str]]:
    """
    Чтение файла и разделение анкет на записи по 7 строк.

    Args:
        filename: Имя файла для чтения.

    Returns:
        Список анкет, каждая из которых содержит 7 строк.
    """
    with open(filename, 'r', encoding='utf-8') as file_input:
        lines = [line.strip() for line in file_input if line.strip()]
        records = [
            lines[i:i + 7]
            for i in range(0, len(lines), 7)
            if len(lines[i:i + 7]) == 7
        ]
    return records


def find_moscow(records: list[list[str]]) -> list[list[str]]:
    """
    Поиск анкет, в которых указан город Москва.

    Args:
        records: Список всех анкет.

    Returns:
        Список анкет жителей Москвы.
    """
    pattern=r'^(Город:)\s(Москва|г\. Москва)$'

    found = []
    for record in records:
        city = record[6]
        if re.search(pattern, city):
            found.append(record[1:7])
    return found


def save_records(found: list[list[str]]) -> None:
    """
    Запись найденных анкет в файл Moskva_ankets.txt.

    Args:
        found: Список найденных анкет.

    Returns:
        None.
    """
    with open('Moskva_ankets.txt', 'w', encoding='utf-8') as file_output:
        for i, anket in enumerate(found):
            file_output.write(f'{i + 1})\n')
            for line in anket:
                file_output.write(f'{line}\n')
            if i < len(found) - 1:
                file_output.write('\n')


def main() -> None:
    """
    Основная функция программы.

    Returns:
        None.
    """
    parser = argparse.ArgumentParser(
        description='Поиск анкет жителей Москвы'
    )
    parser.add_argument('filename', help='Имя файла для чтения')
    args = parser.parse_args()

    try:
        records = read_records(args.filename)
        found = find_moscow(records)
        print(len(found))
        save_records(found)
    except OSError as exc:
        print(f'Ошибка при работе с файлом: {exc}')


if __name__ == '__main__':
    main()