import msvcrt

filename = "kunci.txt"
try:
    array_kunci = []
    banyak_soal = 0
    skor_total = 0

    skor_user_total = 0

    with open(filename) as openfileobject:
        first_line = True
        for line in openfileobject:
            if first_line:
                first_line = False
                continue
            banyak_soal += 1
            splitted_line = line.split()

            nomor = splitted_line[0]
            jawaban = splitted_line[1].split(',')
            skor_benar = splitted_line[2]
            skor_salah = splitted_line[3]
            temp_array = [nomor, jawaban, skor_benar, skor_salah]

            array_kunci.append(temp_array)
            skor_total += int(splitted_line[2])

    check_not_ended = True
    current_number = 1
    print("Input jawaban tiap nomor dengan menekan (1/2/3/4):")
    while check_not_ended:
        # Receive keyboard input
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            try:
                # Detected user answer in number
                user_choice = str(int(key_stroke))
                # Check answer
                curr_answer = array_kunci[current_number-1]
                print("Jawaban No ({}):".format(curr_answer[0]), end=" ")
                if(user_choice in curr_answer[1]):
                    print("{} (BENAR) -> Skor +{}".format(
                        user_choice, curr_answer[2]))
                    skor_user_total += int(curr_answer[2])
                else:
                    print("{} (SALAH) -> Skor {} <Jawaban Benar {}>".format(
                        user_choice, curr_answer[3], curr_answer[1]))
                    skor_user_total += int(curr_answer[3])

                if(current_number == banyak_soal):
                    check_not_ended = False
                current_number += 1
            except ValueError:
                print()
                print("Input harus berupa angka")
                print("Meminta input ulang untuk soal No." + str(current_number))

    print()
    print("Skor Peserta: {}".format(skor_user_total))
    print("Skor Max Soal: {}".format(skor_total))
    print()
    print("Nilai Akhir Peserta: {}%".format(
        round((skor_user_total/skor_total)*100), 2))
except IOError:
    print(filename + " tidak ditemukan")

test = input('Tekan ENTER untuk EXIT')
