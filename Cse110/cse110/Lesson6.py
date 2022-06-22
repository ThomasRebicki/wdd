
dump_tem_measur = float(input("What is the temperature in F? "))
Right_way_to_measure_temperature = (dump_tem_measur - 32) * 5 / 9

print(f"The temperature in Celsius is {Right_way_to_measure_temperature:.1f} degrees.")

Right_way_to_measure_temperature = float(input("What is the temperature in C? "))
dump_tem_measur = ((Right_way_to_measure_temperature * 9) / 5) + 32

print(f"The temperature in F is {dump_tem_measur:.1f} degrees.")