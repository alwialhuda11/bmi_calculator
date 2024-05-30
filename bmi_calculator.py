def main():
    weight = float(input("Masukkan berat badan Anda (kg): "))
    height = float(input("Masukkan tinggi badan Anda (m): "))

    bmi = calculate_bmi(weight, height)
    print(f"Body Mass Index (BMI) Anda adalah: {bmi:.2f}")

def calculate_bmi(weight, height):
    # Rumus BMI yang benar: bmi = weight / (height ** 2)
    bmi = weight / (height ** 2)
    return bmi

if __name__ == "__main__":
    main()