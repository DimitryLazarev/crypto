cipher = "Aef pwwvcf xvkefs vj p ahkf tw ltctpukepgfavx jrgjavaravtc xvkefs, zefsf fpxe ufaafs vc pc pukepgfa vj lpkkfo at vaj crlfsvx fbrvipufca, fcxshkafo rjvcn p jvlkuf lpaeflpavxpu wrcxavtc, pco xtcifsafo gpxd at p ufaafs. Aef wtslrup rjfo lfpcj aepa fpxe ufaafs fcxshkaj at tcf taefs ufaafs, pco gpxd pnpvc, lfpcvcn aef xvkefs vj fjjfcavpuuh p japcopso jrgjavaravtc xvkefs zvae p sruf ntifscvcn zevxe ufaafs ntfj at zevxe. Pj jrxe, va epj aef zfpdcfjjfj tw puu jrgjavaravtc xvkefsj. wupn{FpJhXshKatPunTsVaL}"

flag_task = 'wupn{FpJhXshKatPunTsVaL}'

# (a * 5 + b) % 26 = 22
# (a * 0 + b) % 26 = 15
# (a * 11 + b) % 26 = 20
# (a * 6 + b) % 26 = 13

a_key = 0
b_key = 0

for a in range(1000):
    if a_key and b_key:
        break
    for b in range(26):
        if (a * 5 + b) % 26 == 22 and (a * 0 + b) % 26 == 15 and (a * 11 + b) % 26 == 20 and (a * 6 + b) % 26 == 13:
            a_key, b_key = a, b
            break

decryption_a_key = 0
for i in range(1, 100):
    if a_key * i % 26 == 1:
        decryption_a_key = i
        break

decryption = ''

for letter in cipher.lower():
    if not letter.isalpha():
        decryption += letter
        continue
    x = ord(letter) - ord('a')
    y = decryption_a_key * (x - b_key) % 26
    y += ord('a')
    y = chr(y)
    decryption += y

print(decryption)
