dataGudang = [
    {'kodeSku' : '1001',
    'nama' : 'Gunting',
    'harga' : 25000,
    'qty' : 12},

    {'kodeSku' : '1002',
    'nama' : 'Pisau',
    'harga' : 55000,
    'qty' : 8},

    {'kodeSku' : '1003',
    'nama' : 'Spidol',
    'harga' : 18000,
    'qty' : 50},

    {'kodeSku' : '1004',
    'nama' : 'Lem',
    'harga' : 5000,
    'qty' : 9},

    {'kodeSku' : '1005',
    'nama' : 'Kipas',
    'harga' : 75000,
    'qty' : 5},
    ]


def menu():
    print("========= Data Stok Gudang ===========")
    print("Daftar Menu : ")
    print("1. Melihat Daftar Barang")
    print("2. Menambahkan Barang")
    print("3. Mengedit Barang")
    print("4. Menghapus Barang")
    print("5. Keluar")
    pilih = input("Silahkan Masukkan Angka : ")
    return pilih

def pilihMenu(p):
    if p=="1":
        lihatData()
    elif p=="2":
        tambahData()
    elif p =="3":
        editData()
    elif p=="4":
        hapusData()
    elif p=="5":
        keluarProgram()
    else:
        print("Silahkan masukkan angka yang sesuai")
        balikMenu()


def lihatData():
    list_kosong=[]
    for i in range(len(dataGudang)):
        for key,value in dataGudang[i].items(): 
            if key == "kodeSku":
                list_kosong.append([
                        dataGudang[i]["kodeSku"],
                        dataGudang[i]["nama"], 
                        dataGudang[i]["harga"],
                        dataGudang[i]["qty"],
                        ]) 
    list_kosong.sort()
    print("="*140)
    print()
    print(f"{'_'*53} LIST DAFTAR BARANG {'_'*67}")
    print(f"{'_'*140}")
    print(f"{' '*10} Nomor |{' '*4}  SKU     |{' '*5} Nama       |      QTY     |  Harga")
    print(f"{'-'*140}")
    for i in range(len(list_kosong)):
        print(f"{' '* 5}    {i+1}. \t\t{list_kosong[i][0]}\t       {list_kosong[i][1]}\t\t {list_kosong[i][3]}\t    {list_kosong[i][2]}")
    print(f"{'-'*140}")
    list_kosong=[]

def tambahData(kodeSku,nama,harga,qty):
    dataGudang.append({
        'kodeSku' : kodeSku,
        'nama' : nama,
        'harga' : harga,
        'qty' : qty,
    })
    print("Data Berhasil ditambahkan!!!")

def sku_checker(sku):
    indx = -1
    for i in range(len(dataGudang)):
        for key,value in dataGudang[i].items():
            if dataGudang[i]['kodeSku'] == sku:
                indx = i
                break
        if i == indx:
            break
    return indx

def editSku(index, kodeSkuBaru):
    skuLama = dataGudang[index]['kodeSku']
    dataGudang[index]['kodeSku'] = kodeSkuBaru
    print(f'''
    {80*"="}
    {20*"="} Kode SKU Berhasil Diperbaharui ! {26*"="}
    {80*"="}
    {10*" "}      SKU Sebelumnya \t= {skuLama}
    {10*" "}      SKU Baru \t\t= {kodeSkuBaru}
    {80*"="}
    ''')
    
def editNama(index, namaBaru):
    namaLama = dataGudang[index]['nama']
    dataGudang[index]['nama'] = namaBaru
    print(f'''
    {80*"="}
    {20*"="} Nama Berhasil Diperbaharui ! {30*"="}
    {80*"="}
    {10*" "}      Nama Sebelumnya \t= {namaLama}
    {10*" "}      Nama Baru \t\t= {namaBaru}
    {80*"="}
    ''')

def editQty(index, qtyBaru):
    qtyLama = dataGudang[index]['qty']
    dataGudang[index]['qty'] = qtyBaru
    print(f'''
    {80*"="}
    {20*"="} Qty Berhasil Diperbaharui ! {31*"="}
    {80*"="}
    {10*" "}      Qty Sebelumnya \t= {qtyLama}
    {10*" "}      Qty Baru \t\t= {qtyBaru}
    {80*"="}
    ''')

def editHarga(index, hargaBaru):
    hargaLama = dataGudang[index]['harga']
    dataGudang[index]['harga'] = hargaBaru
    print(f'''
    {80*"="}
    {20*"="} Harga Berhasil Diperbaharui ! {29*"="}
    {80*"="}
    {10*" "}      Harga Sebelumnya \t= {hargaLama}
    {10*" "}      Harga Baru \t\t= {hargaBaru}
    {80*"="}
''')

def hapusData(index):
    del dataGudang[index]
    print("Data Berhasil dihapus!")

def editData(index, qty_baru):
    qty_lama = dataGudang[index]['qty']
    dataGudang[index]['qty'] = qty_baru

def keluarProgram():
    exit()

def balikMenu():
    return menu()


def main():
    while True:
        pilihMenu = menu()
        while pilihMenu not in [ '1' , '2' , '3' ,'4' ,'5']:
            print("Masukkan angka menu yang sesuai")
            return main()
        if pilihMenu == '1':
            lihatData()
        elif pilihMenu == '2':
            inputSku = input("Masukkan kode SKU : ")
            sku = sku_checker(inputSku)
            sku_numeric  = inputSku.isnumeric()
            while sku != -1 or (len(inputSku) > 4) or sku_numeric == False:
                if sku != -1 :
                    print("SKU sudah terdaftar, silahkan masukkan kode SKU dengan angka lain")
                elif len(inputSku)>4 or sku_numeric == False:
                    print("Input harus numerik dan tidak lebih dari 4 angka!")
                inputSku = input("Masukkan kode SKU : ")
                sku = sku_checker(inputSku)
                sku_numeric  = inputSku.isnumeric()
            inputNama = input("Masukkan Nama Barang : ")
            inputQty = input("Masukkan Qty Barang : ")
            inputHarga = input("Masukkan Harga : ")
            tambahData(inputSku, inputNama,inputHarga,inputQty)
        elif pilihMenu == '3':
            input_sku = input("Masukkan kode SKU : ")
            sku = sku_checker(input_sku)
            if sku == -1:
                print("SKU tidak ditemukan")
            else:
                inputSkuBaru = input("Masukkan SKU Baru : ")
                editSku(sku, inputSkuBaru)
                inputNamaBaru = input("Masukkan Nama baru : ")
                editNama(sku, inputNamaBaru)
                inputQtyBaru = input("Masukkan Qty Baru : ")
                editQty(sku, inputQtyBaru)
                inputHargaBaru = input("Masukkan Harga Baru : ")
                editHarga(sku, inputHargaBaru)
        elif pilihMenu == '4':
            input_sku = input("Masukkan kode SKU yang Akan Dihapus : ")
            sku = sku_checker(input_sku)
            if sku == -1:
                print("SKU tidak ditemukan!")
            else:
                hapusData(sku)                
        else:
            keluarProgram()
        

main()