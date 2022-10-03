class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    _next = None

    def __init__(self,no_rekening,nama,saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self._next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEMpty(self):
        return self._size == 0
    
    def insert_tail(self, nomor_r,nam,sal):
        baru = NodeTabungan(nomor_r,nam,sal)
        if self.isEMpty()==True:
            self._head = baru
            self._tail = baru
        else:
            baru._next = self._head
            self._head = baru
        self._size += 1
    
    def insert_head(self, nomor_r,nam,sal):
        baru = NodeTabungan(nomor_r,nam,sal)
        if self._tail == None:
            self._head = baru
            self._tail = baru
        else:
            self._tail._next = baru
            self._tail = baru
        self._size += 1
    
    def delete(self,x):
        if self._head == None:
            return
        location = 0
        current_loc = self._head
        while current_loc._next and location < x:
            j = current_loc
            current_loc = current_loc._next
            location +=1
        if location == 0:
            hapus = self._head
            self._head = self._head._next
            del hapus
        else:
            j._next = current_loc._next
        self._size += 1
        
    def filter(self,x):
        counter = 0
        prev = None
        helper = self._head
        while helper != None:
            if helper.saldo == x:
                if helper == self._head:
                    self._head = self._head._next
                    helper = self._head
                else:
                    helper = helper._next
        print("Rekening yang berhasil dihapus sebanyak:",counter,"buah")

    def update(self,i):
        helper = self._head
        if i <=100:
            while helper != None:
                helper.saldo = int( helper.saldo + ((helper.saldo/100)*i))
                helper = helper._next
            print("Semua saldo rekening berhasil ditambahkan sebanyak",i,'%')
        else:
            print('maaf besaran persen harus diantara 0-100')
        
    def print(self):
        helper = self._head
        while helper != None:
            print('Norek:', helper.no_rekening)
            print('Nama:',helper.nama)
            print('Saldo:',helper.saldo)
            helper = helper._next
        print()


