def main():
    value_translations = {}
    file_path = "upwork/txtB.txt"
    with open(file_path, "r") as file:
        for line in file:
            setting_values = str(line.strip()).split(",")
            setting_values = list(filter(lambda x: x is not None and x != '', setting_values))
            for values in setting_values:
                value = values.split("/")
                value_translations[int(value[0])] = int(value[1])

    file_path = "upwork/txtA.txt"
    with open(file_path, "r") as file:
        for line in file:
            adding_up = 0
            data = line
            for value in data.split(","):
                # print(value_translations.get(value, value))
                adding_up += int(value_translations.get(int(value), int(value)))
            result = f'{data} A{adding_up} / B{adding_up + 5}'
            print(str(result).replace("\n", ""))














if __name__ == "__main__":
    main()