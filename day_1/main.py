from calibration_document import CalibrationDocument


def main(calibration_document: CalibrationDocument) -> None:
    calibration_values = calibration_document.get_calibration_values()
    sum_calibration_values = calibration_document.sum_calibration_values(
        calibration_values)
    print(f'Result: {sum_calibration_values}')


if __name__ == '__main__':
    with open("day_1/input.txt", "r") as file:
        input_calibration_document = file.readlines()

    calibration_document = CalibrationDocument(input_calibration_document)

    main(calibration_document)
