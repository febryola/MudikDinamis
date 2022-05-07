from collections import deque
# from collections import defaultdict

# Membuat class graph
class Graph:
    # Membuat fungsi __init__
    def __init__(self, adjajency_list):
        self.adjajency_list = adjajency_list
 
    # Membuat fungsi get_tetangga untuk mendapatkan tetangga simpul yang berdekatan
    def get_tetangga(self, v):
        return self.adjajency_list[v]
 
    # Membuat fungsi heuristik yang akan membuat semua simpul menjadi equal
    def heuristik(self, n):
        H = {
            'V1': 1,
            'V2': 1,
            'V3': 1,
            'V4': 1,
            'V5': 1,
            'V6': 1,
            'V7': 1
        }
        return H[n]

    # Membuat fungsi algoritma A star sebagai algoritma utama
    def algoritma_A_Star(self, start, stop):
        # Menginisialisasi semua variabel yang dibutuhkan

        # variabel nodes adalah list yang berisi semua simpul
        nodes = {}
        nodes[start] = start     
        
        # variabel awal adalah simpul awal
        # variabel akhir adalah list simpul yang telah dikunjungi
        awal = set([start])
        akhir = set([])
 
        # variabel value merepresentasikan cost dari simpul awal ke simpul lain 
        value = {}
        value[start] = 0
 
        # melakukan looping untuk mencari simpul yang telah dikunjungi
        while len(awal) > 0:
            val = None
 
            # untuk menemukan value terkecil dari fungsi f() -
            for i in awal:
                if val == None or value[i] + self.heuristik(i) < value[val] + self.heuristik(val):
                    val = i;
 
            # jika simpul yang dicari tidak ada di list akhir
            if val == None:
                print('Path does not exist!')
                return None
 
            # jika current simpulnya adalah stop maka ulang kembali dari simpul awal
            if val == stop:
                reconst_path = []
 

                while nodes[val] != val:
                    reconst_path.append(val)
                    val = nodes[val]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('\033[32mRute yang ditempuh\033[0m: {}'.format(reconst_path))
                for i in reconst_path:
                    if i == 'V1':
                        i = "\033[34mPadang\033[0m"
                    elif i == 'V2':
                        i = "\033[33mPariaman\033[0m"
                    elif i == 'V3':
                        i = "\033[35mPesisir Selatan\033[0m"
                    elif i == 'V4':
                        i = "\033[32mSolok\033[0m"
                    elif i == 'V5':
                        i = "\033[36mTanah Datar\033[0m"
                    elif i == 'V6':
                        i = "\033[31mAgam\033[0m"
                    elif i == 'V7':
                        i = "\033[34mBukittinggi\033[0m"
                    print(i)
                print("\n\033[31mCost yang dibutuhkan\033[0m: {}".format(value[stop]))
                
                return reconst_path
 
            # untuk semua current node yang tersisa maka lakukan proses berikut
            for (m, weight) in self.get_tetangga(val):
              # jika simpul yang dicari tidak ada di list akhir maupun list awal
                # tambahkan simpul yang dicari ke list awal
                if m not in awal and m not in akhir:
                    awal.add(m)
                    nodes[m] = val
                    value[m] = value[val] + weight

                else:
                    if value[m] > value[val] + weight:
                        value[m] = value[val] + weight
                        nodes[m] = val
                        
                        if m in akhir:
                            akhir.remove(m)
                            awal.add(m)
            
            # hapus val dari list awal dan tambahkan ke list akhir
            # karena semua simpul telah dikunjungi
            awal.remove(val)
            akhir.add(val)
            
        print('Path does not exist!')
        return None

# Driver program
adjajency_list = {
    'V1': [('V2', 49), ('V3', 73)],
    'V2': [('V4', 107), ('V5', 75), ('V6', 65)], 
    'V3': [('V4', 194), ('V5', 174), ('V6', 194)],
    'V4': [('V7', 73)],
    'V5': [('V7', 45)],
    'V6': [('V7', 43)]
}
graph1 = Graph(adjajency_list)
graph1.algoritma_A_Star('V1', 'V7')
